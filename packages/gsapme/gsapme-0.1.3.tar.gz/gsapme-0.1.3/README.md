# Overview

## What does this package do?
This package is designed to support various methods for statistical analysis. In particular, we hope to offer tools for computing Shapley effects and Proportional Marginal Effects (PMEs) for a variety of models.

## Current features
The *gsapme* package is a work in progress. We currently support the following features:

### Simulation
1. Computation of conditional multivariate normal distributions (`conditional_mvn`)
2. Conditional simulations from a multivariate normal distribution (`cond_sim`)

### Example Models
1. Ishigami function (`ishigami_mod`)
2. Borehole function (`borehole_function`)

### Analysis
1. Computation of Shapley effects for a given model (`calculate_shapley_effects_np`)
2. Computation of Proportional Marginal Effects (PMEs) for a given model (`calculatePME`)
