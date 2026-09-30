---
id: S01
title: Scale Bridge Definitions
vault: VMC-QF_Vault
layer: 04_SCALE_TRANSITION
status: candidate
language: en
tags:
  - scale_bridge
  - coarse_graining
  - order_parameter
cross_references:
  - "[A01_Manifold_Free_Substrate](../00_CORE_AXIOMS/A01_Manifold_Free_Substrate.md)"
  - "[A03_Balance_Principle](../00_CORE_AXIOMS/A03_Balance_Principle.md)"
  - "[G01_Five_Around_One_Deficit](../02_GEOMETRY_TOPOLOGY/G01_Five_Around_One_Deficit.md)"
  - "[D01_Cavity_Network_Hamiltonian](../03_DYNAMICS_SOLITON/D01_Cavity_Network_Hamiltonian.md)"
  - "[D05_Cluster_Simulation_and_Validation](../03_DYNAMICS_SOLITON/D05_Cluster_Simulation_and_Validation.md)"
---

# S01: Scale Bridge Definitions

## 1. Purpose and scope
This document establishes the coarse-graining bridge between the microcopic node-edge description of [D01_Cavity_Network_Hamiltonian](../03_DYNAMICS_SOLITON/D01_Cavity_Network_Hamiltonian.md), the minimal simulatable soliton model of [D04_Minimal_Simulatable_Soliton_Model](../03_DYNAMICS_SOLITON/D04_Minimal_Simulatable_Soliton_Model.md), and the mesoscopic/macroscopic description of a multi-cluster network. The goal is to preserve the causal constraints of [A01_Manifold_Free_Substrate](../00_CORE_AXIOMS/A01_Manifold_Free_Substrate.md) and the topological invariants of [G01_Five_Around_One_Deficit](../02_GEOMETRY_TOPOLOGY/G01_Five_Around_One_Deficit.md) throughout the spatio-temporal averaging process.

## 2. Mapping microscopic variables to mesoscopic ones
- **Effective population density ($n_{\text{eff}}$):** the average population of core and ring nodes in each cluster:
  $$n_{\text{eff}}(X, t) = \frac{1}{N_{\text{cluster}}} \sum_{i \in \text{cluster}} \langle n_i(t) \rangle$$
- **Effective ring coherence ($\chi_{\text{eff}}$):** the average edge-coherence amplitude along the closed loop $C$:
  $$|\chi_{\text{eff}}| = \frac{1}{N_{\text{ring}}} \sum_{k \in \text{ring}} |\chi_{k, k+1}(t)|$$
  In this document, $\chi_{ij}$ refers to the complex edge coherence (with magnitude $|\chi_{ij}|$ and phase $\theta_{ij}=\arg(\chi_{ij})$); in contrast, $\chi_i$ in [D01_Cavity_Network_Hamiltonian](../03_DYNAMICS_SOLITON/D01_Cavity_Network_Hamiltonian.md) is the site/node Kerr nonlinear coefficient in the term $\hat{G}_i$. These two quantities differ in meaning and role. $|\chi_{\text{eff}}|$ is only the mean coherence amplitude of the ring edges and must not be confused with $|\chi_{ij}|$ at the level of a single edge, or with the site Kerr coefficient $\chi_i$.
- **Conditional topological charge ($Q_{\text{eff}}$):** in evaluating the protocol of [D05_Cluster_Simulation_and_Validation](../03_DYNAMICS_SOLITON/D05_Cluster_Simulation_and_Validation.md), phase and topological charge are valid only when the coherence on all ring edges stays above the critical threshold. The charge is defined as the discrete graph winding number on the oriented loop $C$:
  $$Q_{\text{eff}}(C) = \frac{1}{2\pi} \sum_{(i \to j) \in C} \Delta \theta_{ij} \pmod{2\pi} \quad \text{subject to} \quad \min_{(i \to j) \in C} |\chi_{ij}| \ge \varepsilon_{\text{cut}}$$
  Here $\Delta\theta_{ij}$ is the edge phase-coherence difference in the discrete loop traversal (with consistent unwrapping of neighboring phases). If the minimum-magnitude condition fails, the loop winding is deemed invalid/decayed; the threshold used in [D05_Cluster_Simulation_and_Validation](../03_DYNAMICS_SOLITON/D05_Cluster_Simulation_and_Validation.md) is $\varepsilon_{\text{cut}} \approx 10^{-3}$.

## 3. Gauge fixing at the large scale
To prevent divergence of the relative phase caused by cadence leakage, flux and loss must be consistent in the balance accounting. Per [A04_Cadence_Phase_Leak](../00_CORE_AXIOMS/A04_Cadence_Phase_Leak.md), the local cadence leak enters the balance as $\mathcal{L}_i^{\text{cad}}$ (and, under proportional modeling, $\mathcal{L}_i^{\text{cad}}=\gamma_{c,i}\mathcal{B}_i^{\text{res}}$); the symbol $\gamma$ alone is not used in this document as the A04-defined quantity. The gauge-fixing condition is imposed on the basis of the compatibility of equilibrium currents ([A03_Balance_Principle](../00_CORE_AXIOMS/A03_Balance_Principle.md)) at cluster boundaries.


### Reproducible D05 data
- [D05_S01_trajectory.csv](../_data/03_DYNAMICS_SOLITON/D05/D05_S01_trajectory.csv)
- [D05_S02_trajectory.csv](../_data/03_DYNAMICS_SOLITON/D05/D05_S02_trajectory.csv)
- [D05_S03_gamma_sweep.csv](../_data/03_DYNAMICS_SOLITON/D05/D05_S03_gamma_sweep.csv)
- [D05_key_times_comparison.csv](../_data/03_DYNAMICS_SOLITON/D05/D05_key_times_comparison.csv)
- [D05_scenario_summary.csv](../_data/03_DYNAMICS_SOLITON/D05/D05_scenario_summary.csv)

## Simulation record (VMC-QF-Vault-10)
**D05 simulation consistency record.** The operational order parameter is the mean absolute ring-edge coherence $C$, with $\varepsilon_{cut}=10^{-3}$; $Q$ is the oriented, wrapped phase winding on the peripheral five-cycle, valid only when the cutoff is met. In the supplied candidate run, S-01 has $Q(0)=0$; S-02 has $Q(0)=1$ and holds $Q=1$ through $\tau=100$ at $\gamma=0.03$. CSV records are linked in [D05_Cluster_Simulation_and_Validation](../03_DYNAMICS_SOLITON/D05_Cluster_Simulation_and_Validation.md). Numeric results are model outputs, not experimental confirmation.
