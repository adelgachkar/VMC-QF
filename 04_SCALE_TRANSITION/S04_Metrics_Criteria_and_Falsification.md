---
id: S04
title: Metrics, Criteria, and Falsification
vault: VMC-QF_Vault
layer: 04_SCALE_TRANSITION
status: audited
language: en
tags:
  - metrics
  - falsification
  - validation
cross_references:
  - "[A03_Balance_Principle](../00_CORE_AXIOMS/A03_Balance_Principle.md)"
  - "[D02_Causal_Bounds_and_Lieb_Robinson](../03_DYNAMICS_SOLITON/D02_Causal_Bounds_and_Lieb_Robinson.md)"
  - "[D05_Cluster_Simulation_and_Validation](../03_DYNAMICS_SOLITON/D05_Cluster_Simulation_and_Validation.md)"
  - "[S01_Scale_Bridge_Definitions](S01_Scale_Bridge_Definitions.md)"
  - "[S02_Effective_Dynamics_and_Causality](S02_Effective_Dynamics_and_Causality.md)"
---

# S04: Metrics, Criteria, and Falsification

## 1. Measurement indices and scalability (Quantitative Scaling Metrics)
For numerical evaluation of the micro→meso/macro transition, the following indices are fixed with explicit operational conventions:

1. **Coherence-lifetime enhancement ratio ($R_\tau$):**
   $$R_\tau = \frac{\tau_{\text{life}}^{\text{macro}}}{\tau_{\text{life}}^{\text{micro}}}$$
   At each level, $\tau_{\text{life}}$ is the measured duration for which $|\chi_{\text{eff}}(t)|\ge\varepsilon_{\text{cut}}=10^{-3}$ holds; $|\chi_{\text{eff}}|$ is the edge-coherence average defined in [S01_Scale_Bridge_Definitions](S01_Scale_Bridge_Definitions.md). Using the ring-average coherence instead of the effective amplitude must be explicitly registered. A successful scale transition requires $R_\tau>1$.

2. **Causal-propagation ratio ($v_{\text{ratio}}$):**
   $$v_{\text{ratio}} = \frac{v_{\text{eff}}}{v_{\text{LR}}}$$
   Using an identical distance and time-step convention in numerator and denominator, preservation of the causality principle of [D02_Causal_Bounds_and_Lieb_Robinson](../03_DYNAMICS_SOLITON/D02_Causal_Bounds_and_Lieb_Robinson.md) requires $0<v_{\text{ratio}}\le1$.

3. **Conditional-charge stability index ($S_Q$):**
   $$S_Q(\tau) = Q_{\text{eff}}(\tau) \cdot \Theta\left(|\chi_{\text{eff}}(\tau)| - \varepsilon_{\text{cut}}\right), \qquad \Theta(0)=1$$
   Here $|\chi_{\text{eff}}|$ is the same edge-based coherence average used in the $\tau_{\text{life}}$ protocol; the Heaviside step convention at zero is explicitly $\Theta(0)=1$.

### Operational definition of balance quantities and the tolerance bound
- **Effective flux $J_{\text{eff}}$:** the net flux through cluster/region boundary edges, computed from the edge flux and the edge-orientation convention of [A03_Balance_Principle](../00_CORE_AXIOMS/A03_Balance_Principle.md). In boundary sums, the sign of incoming and outgoing flux must follow the boundary orientation.
- **Effective leak rate $\gamma_{\text{eff}}$:** the coarse-grained average of the per-node cadence-leak rate relative to that node's balance:
  $$\gamma_{\text{eff}} = \frac{1}{N_{\text{cluster}}} \sum_{i \in \text{cluster}} \frac{L_i^{\text{cad}}}{B_i}$$
  where $L_i^{\text{cad}}$ is the cadence leak defined in [A04_Cadence_Phase_Leak](../00_CORE_AXIOMS/A04_Cadence_Phase_Leak.md) and $B_i$ is the nonzero normalizing local balance; numerator and denominator must be reported in the same time/cadence convention.
- **Tolerance threshold $\delta_{\text{tol}}$:** the allowed residue of steady-state imbalance:
  $$\delta_{\text{tol}} = \eta \cdot \left\langle |\Phi_{\partial\Omega}| \right\rangle, \qquad \eta\ll1$$
  where $\langle|\Phi_{\partial\Omega}|\rangle$ is the mean absolute boundary flux over the steady measurement window and $\eta$ is a small, reported tolerance coefficient. Compared quantities must share the same normalization.

---

## 2. Scale falsification criteria (Falsification Criteria)
The scale-transition hypothesis is declared falsified under any of the following conditions:

- **Falsification criterion 1 (Lieb–Robinson causality violation):** the effective propagation speed of excitation or phase current in the multi-cluster network exceeds the causal speed cap ($v_{\text{eff}}>v_{\text{LR}}$).
- **Falsification criterion 2 (no lifetime enhancement at the coarse scale):** a multi-cluster network equipped with nonlinear coupling and feedback shows no lifetime improvement of the soliton coherence over the single cluster ($R_\tau\le1$).
- **Falsification criterion 3 (balance-principle violation at the mesoscopic scale):** the effective boundary fluxes cannot satisfy the flux balance of [A03_Balance_Principle](../00_CORE_AXIOMS/A03_Balance_Principle.md) within the steady tolerance:
  $$\left|\sum_{\text{boundary}} J_{\text{eff}} - \sum_{\text{cluster}} \gamma_{\text{eff}}\right| > \delta_{\text{tol}}$$
  Operationally, the leak term must be applied with the same balance/flux normalization, and $J_{\text{eff}}$ is the net boundary flux.
- **Falsification criterion 4 (collapse from defect density):** as the density of geometric defects of [G01_Five_Around_One_Deficit](../02_GEOMETRY_TOPOLOGY/G01_Five_Around_One_Deficit.md) grows, the soliton, instead of pinning stably, immediately undergoes destructive scattering and $S_Q\to0$.


## D05 simulation data
Raw values and protocol comparisons are registered in these files:
- [D05_S01_trajectory.csv](../_data/03_DYNAMICS_SOLITON/D05/D05_S01_trajectory.csv)
- [D05_S02_trajectory.csv](../_data/03_DYNAMICS_SOLITON/D05/D05_S02_trajectory.csv)
- [D05_S03_gamma_sweep.csv](../_data/03_DYNAMICS_SOLITON/D05/D05_S03_gamma_sweep.csv)
- [D05_key_times_comparison.csv](../_data/03_DYNAMICS_SOLITON/D05/D05_key_times_comparison.csv)
- [D05_scenario_summary.csv](../_data/03_DYNAMICS_SOLITON/D05/D05_scenario_summary.csv)

## Simulation record (VMC-QF-Vault-10)
**D05 simulation outcome.** Using $\varepsilon_{cut}=10^{-3}$ and lifetime as the first crossing of the coherence threshold, $\gamma=0.03$ yields $\tau_1=46.052$, $\tau_2=115.129$, $R\tau=2.50>2$. Initial charges are respectively 0 and 1; S-02 remains charged beyond $\tau=20$ (indeed to $\tau=100$). **Status:** these outcomes are candidate-model results, conditional on a phenomenological topology-dependent leakage factor; they do not establish an empirical claim. See [D05_Cluster_Simulation_and_Validation](../03_DYNAMICS_SOLITON/D05_Cluster_Simulation_and_Validation.md) and its linked CSVs.

## CSV data files

- [D05_S01_trajectory.csv](../_data/03_DYNAMICS_SOLITON/D05/D05_S01_trajectory.csv)
- [D05_S02_trajectory.csv](../_data/03_DYNAMICS_SOLITON/D05/D05_S02_trajectory.csv)
- [D05_S03_gamma_sweep.csv](../_data/03_DYNAMICS_SOLITON/D05/D05_S03_gamma_sweep.csv)
- [D05_key_times_comparison.csv](../_data/03_DYNAMICS_SOLITON/D05/D05_key_times_comparison.csv)
- [D05_scenario_summary.csv](../_data/03_DYNAMICS_SOLITON/D05/D05_scenario_summary.csv)

---

## 3. Executed scale battery (Record VMC-QF-Vault-13; run 2026-09-30)

All four falsification criteria of §2 were executed as simulations on the exact single-excitation block engine (the D05 Vault-11 closure principle, generalized to arbitrary networks). Script: [s04_scale_battery.py](../_data/04_SCALE_TRANSITION/S04/s04_scale_battery.py); results [S04_battery_results.csv](../_data/04_SCALE_TRANSITION/S04/S04_battery_results.csv); figure [S04_battery.png](../_data/04_SCALE_TRANSITION/S04/S04_battery.png); full log [s04_battery_output.txt](../_data/04_SCALE_TRANSITION/S04/s04_battery_output.txt).

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

## 4. Record VMC-QF-Vault-14 — criterion 2 closed with the registered feedback operator (run 2026-09-30)

The "open-pending-feedback-operator" state of Record Vault-13 (row T2) is resolved: the D01 §8 saturation term (Kerr-type hopping de-tuning, mean-field closure $C_i := n_i(\tau)$ — the same operational closure as the Vault-13 memory layer) is implemented verbatim as $J_{ij}(\tau) = J_{ij}/\sqrt{1+\big(\chi(n_i-n_j)/J_{ij}\big)^2}$, with $\chi = 0$ reproducing the linear battery engine bit-for-bit (V0 regression deviation **0.00e+00**). Script: [feedback_operator_battery.py](../_data/04_SCALE_TRANSITION/S04/feedback_operator_battery.py); outputs [V14_feedback_scan.csv](../_data/04_SCALE_TRANSITION/S04/V14_feedback_scan.csv), [V14_dt_crosscheck.csv](../_data/04_SCALE_TRANSITION/S04/V14_dt_crosscheck.csv), [V14_pin_probe.csv](../_data/04_SCALE_TRANSITION/S04/V14_pin_probe.csv); figure [V14_feedback_scan.png](../_data/04_SCALE_TRANSITION/S04/V14_feedback_scan.png); full log [v14_output.txt](../_data/04_SCALE_TRANSITION/S04/v14_output.txt).

### Verdicts

| # | test | measured | threshold | verdict |
|---|---|---|---|---|
| V0 | $\chi=0$ regression vs the linear battery engine | max deviation **0.00e+00** | = 0 | **PASS** (regression anchor) |
| V1 | mean-field H hermiticity (mixed defect + feedback + pin) | **0.00e+00** | = 0 | **PASS** |
| T2 | $R_\tau(\chi)$, battery geometry, site defect | $R_\tau$ = 0.965 ($\chi\le 0.1$) → **2.064** ($\chi=0.35{--}0.5$) → 1.71 ($\chi=5$); decomposition at $\chi^*$: macro ×1.000, micro ×0.468 | $R_\tau > 1$ | **PASS-CONDITIONAL** ($\chi \ge \chi^* = 0.2$) — but the gain at $\chi^*$ is **denominator-driven** (micro degraded, macro unchanged) |
| T2 | $\chi_{\rm gen}$ (genuine macro gain > 5%) | **2.0** (macro $\tau$ 26.81 → 29.32) | macro $\tau$ above its $\chi=0$ value | **PASS-CONDITIONAL** ($\chi \ge 2.0$) |
| T2b | fine $\chi$ grid on the micro collapse | $\chi_{\rm collapse}$ = **0.14** (dt=0.5); at dt=0.1 the collapse is already present at $\chi=0.10$ — onset location is dt-sensitive | locates the instability edge | **measured with a convention qualifier** |
| T2c | collapse depth, dt refinement (χ=0.2) | \|Δτ\|/τ = **0.0008** | < 0.05 | **PASS** (depth dt-converged) |
| T2d | full T2 grid at dt = 0.1 | $R_\tau(\chi=0)$ = **2.058** (FLIP from 0.965); $R_\tau > 1$ present in **both** dt conventions; $\chi_{\rm gen}$ = **2.0 in both** | criterion-2 inequality present in both dt conventions | **existence dt-robust; $\chi^*$ location is convention-dependent** |
| T4 | S03 pin well (3 placements + gauge control) | $R_{\rm pin}$ = 0.9912 (no well) / 0.9915 (uniform, gauge-trivial control) / 0.9912–0.9914 (local) | > 1 (pinning) | **FAIL in all placements** — the registered well $U_{\rm pin} = 2.47\times10^{-3}\,J$ is too shallow in this engine ($U_{\rm pin}/J \sim 8\times10^{-3}$) |

### Registered findings

1. **Criterion 2 verdict — PASS-CONDITIONAL, honestly decomposed:** with the D01 §8 operator switched on, $R_\tau > 1$ is achieved in both dt conventions (existence dt-robust). But the honest decomposition shows the gain near threshold is **denominator-driven**: at $\chi^*$ = 0.2 the micro lifetime collapses (27.78 → 13.00, an instability edge at $\chi_{\rm collapse}$ = 0.14) while the macro network is unchanged. **Genuine macro protection** (numerator up) requires $\chi \ge \chi_{\rm gen}$ = **2.0** — and that threshold is **dt-robust** (identical at dt = 0.5 and dt = 0.1). The load-bearing number of criterion 2 is therefore $\chi_{\rm gen} = 2.0$ (in units of $J$), not $\chi^*$.

2. **E4 qualifier on the Vault-13 row (battery-caught, 2026-09-30):** the T2d crosscheck exposed that the registered $R_\tau(\beta=0) = 0.965$ is an **engine-convention artifact**: the macro numerator is dt-robust (26.81 vs 26.74, 0.3%) but the micro denominator was **beat-revival-inflated ×2.14** by the coarse piecewise-constant dephasing (27.78 @ dt=0.5 vs 12.99 @ dt=0.1). The dt-converged baseline is $R_\tau(\beta=0) \approx$ **2.06**. The Vault-13 row 0.965 remains on record with this qualifier (history is not erased); all cross-dt comparisons of $\tau_{\rm micro}$ in this vault must carry the same convention label.

3. **The micro instability is real and located:** $\chi_{\rm collapse}$ = 0.14 (fine grid, dt=0.5) — beyond it the single-cell ring loses ring coherence abruptly (depth dt-converged to 0.08% at χ=0.2). The macro 4-chain does **not** show the corresponding instability in the same window — this asymmetry (single-cell fragile, chain robust) is the physical content behind criterion 2's scale statement.

4. **S03 pin-well claim — falsified in-engine at the registered strength:** all three local placements of the verbatim $U_{\rm pin} = \hbar\kappa_{\max}(1-\cos\delta) = 2.47\times10^{-3}\,J$ leave $R_{\rm pin} \approx 0.991$ (the uniform placement reproduces it exactly — the gauge-triviality control works). Pinning at this well depth is absent; converting scattering into pinning would need a well depth ≫ the hop scale or a genuinely trapped mode — recorded as an engine-scope negative, consistent with the Vault-13 T4 half-verdict.

## 5. Record VMC-QF-Vault-15 — the joint (γ, χ) stability map of R_τ (run 2026-09-30)

Criterion 2 generalized from the single-axis scan of Vault-14 to the **two-parameter plane**: $R_\tau(\gamma, \chi) = \tau_{\rm macro}/\tau_{\rm micro}$ over $\gamma \in [0.01, 0.50]$ (10 values) × $\chi \in [0, 5]$ (11 values, primary grid), plus a dt=0.1 replica on the coarse-χ grid — **both reconstruction contracts**, per the T2d lesson that the χ=0 baseline flips between them. Engine imported **verbatim** from the registered Vault-14 module (no re-implementation): V0 regression reproduces the anchors 27.78 / 26.81 exactly. Script: [feedback_gamma_chi_sweep.py](../_data/04_SCALE_TRANSITION/S04/feedback_gamma_chi_sweep.py); outputs [V15_gamma_chi_map.csv](../_data/04_SCALE_TRANSITION/S04/V15_gamma_chi_map.csv), [V15_dt01_replica.csv](../_data/04_SCALE_TRANSITION/S04/V15_dt01_replica.csv), [V15_boundary_curves.csv](../_data/04_SCALE_TRANSITION/S04/V15_boundary_curves.csv); figure [V15_gamma_chi_map.png](../_data/04_SCALE_TRANSITION/S04/V15_gamma_chi_map.png); register [V15_register.json](../_data/04_SCALE_TRANSITION/S04/V15_register.json); full log [v15_output.txt](../_data/04_SCALE_TRANSITION/S04/v15_output.txt).

### Boundary curves (both dt contracts)

| γ | χ* (dt=0.5) | χ_gen (dt=0.5) | χ_collapse (dt=0.5) | χ* (dt=0.1) | χ_gen (dt=0.1) |
|---|---|---|---|---|---|
| 0.01 | — (censored) | — (censored) | — | — (censored) | — (censored) |
| 0.02 | 0.0 | 1.5 | — | 0.0 | 2.0 |
| 0.05 | 0.2 | 2.0 | 0.2 | 0.0 | 2.0 |
| 0.08 | 0.0 | 1.5 | — | 0.0 | 5.0 |
| 0.10 | — | 3.0 | — | — | 5.0 |
| 0.15–0.50 | — | 0.5–3.0 (non-monotone) | — | — | 1.0–5.0 (non-monotone) |

### Verdicts

| # | test | measured | threshold | verdict |
|---|---|---|---|---|
| V0 | regression vs Vault-14 anchors (γ=0.05, χ=0) | τ_micro = 27.78, τ_macro = 26.81 | ±2% | **PASS** (engine identity) |
| B1 | χ_gen at the reference point (γ=0.05, dt=0.5) | **2.0** | = 2.0 (Vault-14) | **reproduces Vault-14** |
| B2 | monotonicity of χ_gen(γ) | non-monotone: 1.5→2.0→1.5→3.0→1.5→2.0→0.5→1.5→1.0 | non-decreasing | **NON-MONOTONE — registered as a measured shape, no trend forced** |
| B3 | boundary dt-robustness (χ*, χ_gen on shared grid points) | 13 agree / **7 disagree** across contracts | agreement = robust | **boundaries are convention-sensitive — every curve is reported under BOTH dt contracts; no single-protocol claim** |
| B4 | baseline R_τ(χ=0) > 1 window | dt=0.5: γ ∈ {0.02, 0.08}; dt=0.1: γ ∈ {0.02, 0.05, 0.08} | recorded | **R_τ=1 baseline crossing sits between γ=0.02 and 0.05 in both contracts; the dt-flip region γ ∈ [0.05, 0.10] is now MAPPED** (T2d lesson quantified) |

### Registered findings

1. **The R_τ > 1 region is a narrow low-γ pocket, not a plateau.** Above γ ≈ 0.10 the map is uniformly flat at R_τ ≈ 0.97–1.00 across the entire χ axis — feedback cannot buy macro advantage once dephasing exceeds the beat-revival scale; below γ ≈ 0.02 the micro lifetime is so long that the ratio saturates on transport, not protection. The criterion-2 advantage lives in the band **γ ≈ 0.02–0.10**.
2. **χ_gen is the only load-bearing boundary, and it is dt-robust at the reference point** (2.0 in both contracts at γ=0.05) but wanders between 0.5 and 5.0 at other γ — its γ-shape is NON-monotone and contract-sensitive, so the honest registered content is the reference-point value plus the full CSV map, not a fitted curve.
3. **The dt-flip region of the baseline (Vault-14 T2d's 0.965 vs 2.058) is mapped:** the flip is confined to γ ∈ [0.05, 0.10]; outside it the two contracts agree on the sign of R_τ − 1. This converts the earlier convention qualifier into a concrete region of validity.
4. **Cross-engine honesty note:** Vault-12 maps τ_defect/τ_void on the D05 engine — a different quantity from this vault's cluster ratio; the two maps are NOT numerically comparable and this record makes no cross-engine ratio claim.
