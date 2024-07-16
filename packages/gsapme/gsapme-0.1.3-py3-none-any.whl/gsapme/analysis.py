# analysis.py
import numpy as np
from itertools import combinations
import scipy.special
from gsapme.simulation import jointSim, condSim
from gsapme.models import ishigami_mod, borehole_function
from gsapme.covariance import generate_cov_matrix


def compute_variance_np(model, jointSim, Nv, covMat, pert=False):
    X_v = jointSim(Nv, covMat)  # Generate samples using the joint simulation function

    # Sequential execution of the model on generated samples
    Y = model(X_v)

    # Compute the variance of the model output, using ddof=1 for sample variance
    vy = np.var(Y, ddof=1)
    return vy, X_v


def conditional_elements_estimation_np(model, condSim, jointSim, No, Ni, d, vy, covMat):
    # Generate conditional samples
    condX = jointSim(No, covMat)

    # Initialize indices and combination weights
    indices = [None] * (d + 1)
    comb_weights = np.zeros(d)

    # Use NumPy to create combinations and store indices for each interaction level
    for j in range(1, d + 1):
        indices[j] = np.array(list(combinations(range(d), j))).T
        comb_weights[j-1] = 1 / scipy.special.comb(d - 1, j - 1)

    # Initialize storage for variance explained results, mirroring the structure of indices
    VEs = [None] * len(indices)

    # Estimate variance explained for each subset of variables
    for level in range(1, len(indices)):
        current_level_indices = indices[level]
        current_level_VEs = []  # Initialize an empty list to store VEs for the current level
        for subset in current_level_indices.T:
            VE = estim_VE_MC(condX, condSim, model, list(subset), Ni, vy, covMat)
            current_level_VEs.append(VE)
        VEs[level] = np.array(current_level_VEs)  # Store the VEs for the current level

    # Set the last element of VEs to 1, representing the total variance explained for the full model
    VEs[-1] = 1

    # Convert combination weights to a NumPy array for consistency
    comb_weights_array = np.array(comb_weights)

    # Return the estimated VEs, indices, and combination weights
    return VEs, indices, comb_weights_array


def estim_VE_MC(condX, condSim, model, subset, Ni, vy, covMat):
    condX = np.asarray(condX)
    No, d = condX.shape

    # Adjust subset indices to match the R function logic
    complement_subset = np.setdiff1d(np.arange(d), subset)

    varVec = np.zeros(No)
    for i in range(No):
        # Extract conditional values for each sample, ensuring xjc matches the expected shape
        xjc = condX[i, complement_subset]  # Direct indexing without further adjustment

        # Perform conditional simulation
        # Ensure the condSim function is designed to accept these parameters correctly
        X_ = condSim(Ni, subset, complement_subset, xjc, covMat)  # Adjusted order to match the function definition

        # Apply the model function
        Y_ = model(X_)
        varVec[i] = np.var(Y_, ddof=1)  # ddof=1 for sample variance

    return np.mean(varVec) / vy


def calculate_shapley_effects(d, indices, VEs, comb_weights):
    Shaps = np.zeros(d)
    for var_j in range(d):
        for ord in range(d):
            if VEs[ord] is None or VEs[ord + 1] is None:
                continue

            idx_j = np.where(indices[ord + 1] == var_j)[1]
            idx_woj = np.where(np.all(indices[ord] != var_j, axis=0))[0]

            # Handling different types in VEs
            if isinstance(VEs[ord + 1], (np.ndarray, list)):
                effect_incl_j = np.sum([VEs[ord + 1][i] for i in idx_j])
            else:  # If it's an integer
                effect_incl_j = VEs[ord + 1]

            if isinstance(VEs[ord], (np.ndarray, list)):
                effect_excl_j = np.sum([VEs[ord][i] for i in idx_woj])
            else:  # If it's an integer
                effect_excl_j = VEs[ord]

            # Ensure both are numbers before subtraction
            if isinstance(effect_incl_j, (int, float)) and isinstance(effect_excl_j, (int, float)):
                total_incremental = effect_incl_j - effect_excl_j
            else:
                total_incremental = 0  # Default to 0 if types are not compatible

            Shaps[var_j] += comb_weights[ord] * total_incremental

    Shaps /= d
    return Shaps


def identify_zero_players_np(indices, VEs, tol=None):
    """
    Identifies inputs with zero or negligible total Sobol indices (zero players) using a numpy-centric approach.

    Parameters:
    - indices: A list of numpy arrays, where each array represents a set of input indices for each order of interaction.
    - VEs: A list where each element is a numpy array representing variance explained (VEs) for each set of inputs.
           Elements of VEs are converted to numpy arrays if not already.
    - tol: A tolerance level below which variance contributions are considered negligible. If None, exact zeros are considered.

    Returns:
    - A numpy array of input indices considered as zero players, adjusted for 0-based indexing.
    """
    # Convert the first element of VEs to a numpy array if it's not already one
    VEs_1 = np.asarray(VEs[1])

    # Perform the comparison with tol
    if tol is not None:
        idx_z = np.where(VEs_1 <= tol)[0]
    else:
        idx_z = np.where(VEs_1 == 0)[0]

    return idx_z


def find_zero_coalitions_np(VEs, tol=0.1):
    """
    Identifies coalitions of inputs with zero or negligible variance contributions.

    Parameters:
    - VEs: A list of numpy arrays where each array represents variance explained (VEs)
           for each set of inputs at different interaction orders. The first element can be None.
    - tol: A tolerance level below which variance contributions are considered negligible.
           If tol is None, exact zeros are considered.

    Returns:
    - A numpy array of indices representing the orders of coalitions with zero or negligible
      variance contributions, adjusted for Python's 0-based indexing.
    """
    Z_coal_order = []

    # Iterate over each set of variance effects, starting from the first element
    for i, ve in enumerate(VEs):
        if ve is not None:  # Skip None elements
            # Check if any variance contributions meet the specified criteria
            if tol is None:
                zero_criteria_met = np.any(ve == 0)
            else:
                zero_criteria_met = np.any(ve <= tol)

            # If the criteria are met, append the index (adjusted for 0-based indexing in Python)
            if zero_criteria_met:
                Z_coal_order.append(i)

    return np.array(Z_coal_order, dtype=int)



def recur_PV(indices, VEs):
    """
    Recursively calculates the partial variances (Ps) for each order of input interaction.
    """
    d = len(indices) - 1
    Ps = [None] * (d + 1)  # Adjust for Python indexing

    # Ps[0] will remain None because there are no "zeroth-order" interactions
    # Assign first order effects directly from VEs
    Ps[1] = np.array(VEs[1])
    for ord in range(2, d + 1):
        Ws = np.array(VEs[ord]) if isinstance(VEs[ord], np.ndarray) else np.array([VEs[ord]])
        current_indices = indices[ord]

        if current_indices.size==0: # Check if current_indices is empty
            Ps[ord] = np.array([])  # Assign an empty array if current_indices is empty
            continue # Skip to the next iteration if current_indices is empty

        previous_indices = indices[ord - 1]
        results =  np.zeros(Ws.size)  # Initialize the results array

        for i in range(current_indices.shape[1]): # Now safe to use shape[1] because we checked size
            S = set(current_indices[:, i])
            idx_Spi = []

            for j in range(previous_indices.shape[1]):
                prev_set = set(previous_indices[:, j])
                if prev_set.issubset(S) and len(prev_set) + 1 == len(S):
                    idx_Spi.append(j)

            if idx_Spi:
                denom = sum(1 / Ps[ord -1][j] for j in idx_Spi if Ps[ord - 1][j] != 0)
                results[i] = Ws[i] / denom if denom > 0 else 0

    # Remove None values and ensure all elements are numpy arrays
        Ps[ord] = results

    return Ps




def calculate_pme_zero_players(d, indices, VEs, tolerance, idx_z, Z_coal_order):

    Z_cardMax = max(Z_coal_order) - 1  # Adjust for 0-based indexing

    if tolerance is None:
        Z_coal_cardMax = indices[Z_cardMax + 1][:, np.where(VEs[Z_cardMax + 1] == 0)[0]]
    else:
        Z_coal_cardMax = indices[Z_cardMax + 1][:, np.where(VEs[Z_cardMax + 1] <= tolerance)[0]]


    z_zeroPV = np.array([np.all(np.isin(Z_coal_cardMax, z).sum(axis=0) == Z_cardMax + 1) for z in idx_z])

    PV = np.zeros(d)

    if Z_cardMax == d:
        return PV
    else:
        PS_i = np.zeros(d)
        PS_N = np.zeros(d)

        for idx_Zcoal in range(Z_coal_cardMax.shape[1]):
            Z_coal = Z_coal_cardMax[:, idx_Zcoal]

            indices_ = [np.zeros((d - Z_cardMax - 1, 0))] * (d - Z_cardMax)
            VEs_ = [np.zeros(0)] * (d - Z_cardMax)

            for i in range(1, d - Z_cardMax):
                checkmat = np.isin(indices[i], Z_coal).reshape(i, -1)
                idx_ind_null = np.where(np.sum(checkmat, axis=0) == 0)[0]
                ind_tmp = indices[i][:, idx_ind_null]
                indices_[i] = np.vstack((ind_tmp, np.tile(Z_coal, (ind_tmp.shape[1], 1)).T))

            for i in range(1, len(indices_)):
                if Z_cardMax + i >= len(indices):
                    continue
                idx_get = []
                for x in indices_[i].T:
                    matches = np.where(np.all(np.isin(indices[Z_cardMax + i], x).reshape(Z_cardMax + i, -1), axis=0))[0]
                    if matches.size > 0:
                        idx_get.append(matches[0])
                if idx_get:
                    idx_get = np.array(idx_get)
                    if idx_get.max() < len(VEs[Z_cardMax + i]):
                        VEs_[i] = VEs[Z_cardMax + i][idx_get]

            # Calculate partial variance contributions
            PS = recur_PV(indices_, VEs_)

            idx_var = indices_[1][0, :]
            try:
                PS_i[idx_var] += 1 / PS[-2][::-1]
            except:
                PS_i[idx_var] += 1 / PS[-1][::-1]

            PS_N = np.add(PS_N, 1 / PS[-1])

        PV = PS_i / PS_N if np.any(PS_N) else PV

    return PV


def calculatePME(d, indices, VEs, tol):
    # Assuming identify_zero_players and find_zero_coalitions are defined elsewhere
    idx_z = identify_zero_players_np(indices, VEs, tol)
    Z_coal_order = find_zero_coalitions_np(VEs, tol)

    # Check if idx_z contains any elements
    if any(idx_z):
        # Assuming calculate_pme_zero_players is defined as per previous discussions
        return calculate_pme_zero_players(d, indices, VEs, tol, idx_z, Z_coal_order)
    else:
        # Assuming recur_PV is defined and adapted from your recur.PV
        PS = recur_PV(indices, VEs)

        # Adaptation of R's matrix(rev(PS[[d]] / PS[[d - 1]]), ncol = 1)
        # Assuming PS is a list of arrays where each array corresponds to an order of interaction
        # and you want to reverse the division result of the last two orders' variances
        last_order_ratio = PS[-1] / PS[-2]
        return last_order_ratio[::-1].reshape(-1, 1)  # Reverse and reshape for column vector



if __name__=="__main__":
    #cov_mat = generate_cov_matrix(4, structure='diagonal')
    Nv = 100  # Number of samples for variance estimation
    No = 20  # Number of samples for conditional expectation
    Ni = 200 # Number of inner loop samples for Monte Carlo estimation
    tol = 0.2  # Tolerance for identifying zero players
    pert = False  # Whether to perturb the jointSim function

    covMat = generate_cov_matrix(8, structure='diagonal')

    # Compute the variance
    vy, X_v = compute_variance_np(borehole_function, jointSim, Nv, covMat=covMat, pert=False)
    d = X_v.shape[1]

    VEs, indices, comb_weights = conditional_elements_estimation_np(
        model=borehole_function,
        condSim=condSim,
        jointSim=jointSim,
        No=No,
        Ni=Ni,
        d=d,
        vy=vy,
        covMat=covMat
    )



    print(calculate_shapley_effects(d, indices, VEs, comb_weights))
    
    print(calculatePME(d, indices, VEs, tol))