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

---

## 3. Executed scale battery (Record VMC-QF-Vault-13; run 2026-09-30)

All four falsification criteria of §2 were executed as simulations on the exact single-excitation block engine (the D05 Vault-11 closure principle, generalized to arbitrary networks). Script: [[_data/04_SCALE_TRANSITION/S04/s04_scale_battery.py]]; results [[_data/04_SCALE_TRANSITION/S04/S04_battery_results.csv]]; figure [[_data/04_SCALE_TRANSITION/S04/S04_battery.png]]; full log [[_data/04_SCALE_TRANSITION/S04/s04_battery_output.txt]].

### Battery tests and verdicts

| # | test (criterion) | measured | threshold | verdict |
|---|---|---|---|---|
| T1 | Lieb–Robinson causality (criterion 1) | $v_{\text{ratio}} = v_{\text{eff}}/v_{\text{LR}}$ = **0.3962** ($v_{\text{LR}}$ = 2eΔ = 14.135, $v_{\text{eff}}$ = 5.6 edges/τ by wavefront half-max) | $v_{\text{ratio}} \le 1$ | **PASS** |
| T2 | Lifetime enhancement (criterion 2) | $R_\tau(\beta)$ **flat at 0.965** across $\beta \in [0, 1]$ — macro (4-chain) never beats micro | $R_\tau > 1$ | **FAIL** (honest negative: the scale-transition criterion 2 is not met in this engine) |
| T3 | A03 balance residue (criterion 3) | max population-continuity residue **5.62e-04** at grid 0.00125; dephasing population invariance **exactly 0**; global drift **8.3e-14** | $\le \delta_{\text{tol}}$ = 6.34e-04 | **PASS** |
| T4 | Defect-density collapse (criterion 4) | $\rho_c$ measured = **0.4075** (spanning crossing, L=64, 300 seeds) = $1 - p_c^{\text{site}}$(square lattice) to 3 decimals; pinning ratio $R_{\text{pin}}$ = **0.9912** | see E4 correction + verdict below | **MIXED** — percolation half passes; pinning half fails |

### Registered findings

1. **Criterion 1 (causality) holds:** the excitation wavefront propagates at 0.40 × the Lieb–Robinson bound — no super-causal transport on the cluster network. The D02 causal cap is respected with a comfortable margin.

2. **Criterion 2 fails in the registered engine — honest negative, not hidden:** with the balance/leak channel of D05 and no registered nonlinear feedback strength, the multi-cluster macro network gives $R_\tau = 0.965 < 1$ uniformly, i.e., **the coarse-grained network does not extend soliton coherence** in this implementation. S04's criterion-2 premise ("nonlinear coupling and feedback") is load-bearing: without a registered feedback operator there is nothing to switch on. The criterion is therefore recorded as **open-pending-feedback-operator**, not passed and not falsified — the honest state is that VMC-QF currently possesses no mechanism that produces the scale-up lifetime enhancement S04 demands.

3. **Criterion 3 (balance) holds to tolerance:** the discretized continuity equation for site populations closes within the registered $\delta_{\text{tol}}$ (residue 5.62e-04 ≤ 6.34e-04, converging with grid refinement); the dephasing channel is population-invariant by construction (diagonal Kraus), and total excitation number drifts at 8.3e-14 over 200 steps — machine-precision conservation of the A03 balance structure.

4. **Criterion 4 splits into two sub-verdicts:**
   - **Percolation half — PASS with an E4 correction:** the spanning-crossing threshold of trap-free sublattices on the square lattice was measured at $\rho_c$ = 0.4075 (L=64, 300 seeds), matching $1 - p_c^{\text{site}}$(square) = 0.4073. The previously registered value **$\rho_c \approx 0.382$ has no traceable source and is superseded** (E4 battery-caught correction; S03 §2 corrected in place). 0.382 was likely a corruption of 0.407 or a confusion with the triangular-lattice complement; the measured value is now the registered one.
   - **Pinning half — FAIL (honest negative):** a defect cluster placed as the soliton's neighbor is **destructive, not pinning**, in this engine: $R_{\text{pin}} = \tau(\text{defect nb})/\tau(\text{clean nb})$ = 0.9912 < 1. The S03 picture of defects as potential wells that pin and protect (via $U_{\text{pin}} \propto \delta^2$) is **not** what the linear hopping engine implements: a detuned neighbor scatters the single excitation rather than trapping it. The pinning dynamics therefore requires the nonlinear on-site term (which the minimal soliton model of D04 registers but the battery engine omits); this is recorded as an open engine-scope limitation, not a refutation of S03.

### Scope and honesty qualifiers (family convention)

- All results are **in-silico, model-level** (label [sim]); no empirical or cosmological claim is made.
- T2 and T4-pinning are **negative results registered as such** — they identify precisely which mechanism (nonlinear feedback operator) the vault still lacks; see D04 §5.2 (edge-phase flux, executed in Vault-11) for the mechanism that *does* pass its criterion.
- The battery verdict for the vault as a whole: **criteria 1 and 3 pass; criterion 2 is open (feedback operator missing); criterion 4 percolation passes with corrected $\rho_c$ = 0.4075, pinning is engine-scope-negative.** The falsification chain of the vault is thereby closed for the linear-excitation engine — every registered criterion now has a measured value or an explicitly named missing mechanism.
