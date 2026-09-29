---
id: S04
title: Metrics, Criteria, and Falsification
vault: VMC-QF_Vault
layer: 04_SCALE_TRANSITION
status: candidate
language: en
tags:
  - metrics
  - falsification
  - validation
cross_references:
  - "[[A03_Balance_Principle]]"
  - "[[D02_Causal_Bounds_and_Lieb_Robinson]]"
  - "[[D05_Cluster_Simulation_and_Validation]]"
  - "[[S01_Scale_Bridge_Definitions]]"
  - "[[S02_Effective_Dynamics_and_Causality]]"
---

# S04: Metrics, Criteria, and Falsification

## 1. Measurement indices and scalability (Quantitative Scaling Metrics)
For numerical evaluation of the micro→meso/macro transition, the following indices are fixed with explicit operational conventions:

1. **Coherence-lifetime enhancement ratio ($R_\tau$):**
   $$R_\tau = \frac{\tau_{\text{life}}^{\text{macro}}}{\tau_{\text{life}}^{\text{micro}}}$$
   At each level, $\tau_{\text{life}}$ is the measured duration for which $|\chi_{\text{eff}}(t)|\ge\varepsilon_{\text{cut}}=10^{-3}$ holds; $|\chi_{\text{eff}}|$ is the edge-coherence average defined in [[S01_Scale_Bridge_Definitions]]. Using the ring-average coherence instead of the effective amplitude must be explicitly registered. A successful scale transition requires $R_\tau>1$.

2. **Causal-propagation ratio ($v_{\text{ratio}}$):**
   $$v_{\text{ratio}} = \frac{v_{\text{eff}}}{v_{\text{LR}}}$$
   Using an identical distance and time-step convention in numerator and denominator, preservation of the causality principle of [[D02_Causal_Bounds_and_Lieb_Robinson]] requires $0<v_{\text{ratio}}\le1$.

3. **Conditional-charge stability index ($S_Q$):**
   $$S_Q(\tau) = Q_{\text{eff}}(\tau) \cdot \Theta\left(|\chi_{\text{eff}}(\tau)| - \varepsilon_{\text{cut}}\right), \qquad \Theta(0)=1$$
   Here $|\chi_{\text{eff}}|$ is the same edge-based coherence average used in the $\tau_{\text{life}}$ protocol; the Heaviside step convention at zero is explicitly $\Theta(0)=1$.

### Operational definition of balance quantities and the tolerance bound
- **Effective flux $J_{\text{eff}}$:** the net flux through cluster/region boundary edges, computed from the edge flux and the edge-orientation convention of [[A03_Balance_Principle]]. In boundary sums, the sign of incoming and outgoing flux must follow the boundary orientation.
- **Effective leak rate $\gamma_{\text{eff}}$:** the coarse-grained average of the per-node cadence-leak rate relative to that node's balance:
  $$\gamma_{\text{eff}} = \frac{1}{N_{\text{cluster}}} \sum_{i \in \text{cluster}} \frac{L_i^{\text{cad}}}{B_i}$$
  where $L_i^{\text{cad}}$ is the cadence leak defined in [[A04_Cadence_Phase_Leak]] and $B_i$ is the nonzero normalizing local balance; numerator and denominator must be reported in the same time/cadence convention.
- **Tolerance threshold $\delta_{\text{tol}}$:** the allowed residue of steady-state imbalance:
  $$\delta_{\text{tol}} = \eta \cdot \left\langle |\Phi_{\partial\Omega}| \right\rangle, \qquad \eta\ll1$$
  where $\langle|\Phi_{\partial\Omega}|\rangle$ is the mean absolute boundary flux over the steady measurement window and $\eta$ is a small, reported tolerance coefficient. Compared quantities must share the same normalization.

---

## 2. Scale falsification criteria (Falsification Criteria)
The scale-transition hypothesis is declared falsified under any of the following conditions:

- **Falsification criterion 1 (Lieb–Robinson causality violation):** the effective propagation speed of excitation or phase current in the multi-cluster network exceeds the causal speed cap ($v_{\text{eff}}>v_{\text{LR}}$).
- **Falsification criterion 2 (no lifetime enhancement at the coarse scale):** a multi-cluster network equipped with nonlinear coupling and feedback shows no lifetime improvement of the soliton coherence over the single cluster ($R_\tau\le1$).
- **Falsification criterion 3 (balance-principle violation at the mesoscopic scale):** the effective boundary fluxes cannot satisfy the flux balance of [[A03_Balance_Principle]] within the steady tolerance:
  $$\left|\sum_{\text{boundary}} J_{\text{eff}} - \sum_{\text{cluster}} \gamma_{\text{eff}}\right| > \delta_{\text{tol}}$$
  Operationally, the leak term must be applied with the same balance/flux normalization, and $J_{\text{eff}}$ is the net boundary flux.
- **Falsification criterion 4 (collapse from defect density):** as the density of geometric defects of [[G01_Five_Around_One_Deficit]] grows, the soliton, instead of pinning stably, immediately undergoes destructive scattering and $S_Q\to0$.


## D05 simulation data
Raw values and protocol comparisons are registered in these files:
- [[_data/03_DYNAMICS_SOLITON/D05/D05_S01_trajectory.csv]]
- [[_data/03_DYNAMICS_SOLITON/D05/D05_S02_trajectory.csv]]
- [[_data/03_DYNAMICS_SOLITON/D05/D05_S03_gamma_sweep.csv]]
- [[_data/03_DYNAMICS_SOLITON/D05/D05_key_times_comparison.csv]]
- [[_data/03_DYNAMICS_SOLITON/D05/D05_scenario_summary.csv]]

## Simulation record (VMC-QF-Vault-10)
**D05 simulation outcome.** Using $\varepsilon_{cut}=10^{-3}$ and lifetime as the first crossing of the coherence threshold, $\gamma=0.03$ yields $\tau_1=46.052$, $\tau_2=115.129$, $R\tau=2.50>2$. Initial charges are respectively 0 and 1; S-02 remains charged beyond $\tau=20$ (indeed to $\tau=100$). **Status:** these outcomes are candidate-model results, conditional on a phenomenological topology-dependent leakage factor; they do not establish an empirical claim. See [[D05_Cluster_Simulation_and_Validation]] and its linked CSVs.

## CSV data files

- [[_data/03_DYNAMICS_SOLITON/D05/D05_S01_trajectory.csv]]
- [[_data/03_DYNAMICS_SOLITON/D05/D05_S02_trajectory.csv]]
- [[_data/03_DYNAMICS_SOLITON/D05/D05_S03_gamma_sweep.csv]]
- [[_data/03_DYNAMICS_SOLITON/D05/D05_key_times_comparison.csv]]
- [[_data/03_DYNAMICS_SOLITON/D05/D05_scenario_summary.csv]]
