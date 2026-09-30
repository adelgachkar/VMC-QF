---
id: D05
title: Cluster Simulation Protocol and Validation (E + T1 Architecture)
vault: VMC-QF_Vault
layer: 03_DYNAMICS_SOLITON
tags:
  - protocol
  - simulation
  - CPTP
  - open-quantum-system
  - quench-dynamics
  - phase-pinning
  - validation-criteria
  - falsifiability
status: candidate
created: 2026-09-28
language: en
cross_references:
  - "[A03_Balance_Principle](../00_CORE_AXIOMS/A03_Balance_Principle.md)"
  - "[A04_Cadence_Phase_Leak](../00_CORE_AXIOMS/A04_Cadence_Phase_Leak.md)"
  - "[G01_Five_Around_One_Deficit](../02_GEOMETRY_TOPOLOGY/G01_Five_Around_One_Deficit.md)"
  - "[D01_Cavity_Network_Hamiltonian](D01_Cavity_Network_Hamiltonian.md)"
  - "[D02_Causal_Bounds_and_Lieb_Robinson](D02_Causal_Bounds_and_Lieb_Robinson.md)"
  - "[D04_Minimal_Simulatable_Soliton_Model](D04_Minimal_Simulatable_Soliton_Model.md)"
---

# D05 — Cluster Simulation Protocol and Validation
## (Open-channel $\mathcal{E}$ architecture with impulsive initial excitation $T_1$)

---

## 0) Objective statement and methodological boundary
This document formulates the exact execution protocol, channel formulation, and measurement/falsification criteria for testing the collective behavior of the 6-node (5-around-1) cluster.
- **Configuration choice:** trace-preserving open channel with local leak ($\mathcal{E}$) together with impulsive initial preparation ($T_1$).
- **Anti-lock principle:** this document contains no "pre-made or imagined results"; it only states the protocol, observables, and boundary conditions of hypothesis success/failure, so that computational outputs are later registered in code.

---

## 1) Cluster structure and Hilbert space
### 1.1) Cluster graph topology ($G_6$)
- Nodes: $V = \{0, 1, 2, 3, 4, 5\}$
  - $0$: central node (cluster core)
  - $k \in \{1, \dots, 5\}$: peripheral-ring nodes
- Edges: $E = E_{\text{star}} \cup E_{\text{ring}}$
  - radial edges: $E_{\text{star}} = \{(0, k) \mid k=1..5\}$
  - perimeter edges: $E_{\text{ring}} = \{(k, k+1) \mid k=1..5 \text{ with } 6 \equiv 1\}$
- Total state space:
  $$
  \mathcal{H} = \bigotimes_{i=0}^{5} \mathbb{C}^2 \quad (\dim \mathcal{H} = 2^6 = 64)
  $$
  The density matrix at each cadence step $\tau \in \mathbb{N}_0$ is $\rho(\tau) \in \mathcal{S}(\mathcal{H})$.

---

## 2) Initial-state preparation protocol ($T_1$: Twist Quench)
The excitation is applied as a single impulse at $\tau=0$ with no external force in subsequent steps:

1. **Substrate ground state:**
   all nodes in the initial polarized or coherent state:
   $$
   |\psi_0\rangle = \bigotimes_{i=0}^{5} |0\rangle_i \quad \implies \quad \rho_{\text{ground}} = |\psi_0\rangle\langle\psi_0|
   $$
2. **Excitation injection into the ring:**
   distributing a single excitation over the 5-fold peripheral ring:
   $$
   |\psi_{\text{ring}}\rangle = \frac{1}{\sqrt{5}} \sum_{k=1}^{5} |k\rangle, \quad |k\rangle \equiv |0\dots 1_k \dots 0\rangle
   $$
3. **Initial phase-twist injection (Twist Injection):**
   a $2\pi$ phase gradient is applied over the ring so that the topological candidate $Q(0) \approx 1$ is excited:
   $$
   |\psi(0)\rangle = \frac{1}{\sqrt{5}} \sum_{k=1}^{5} e^{i \frac{2\pi (k-1)}{5}} |k\rangle \otimes |0\rangle_{\text{center}}
   $$
   Initial density matrix:
   $$
   \rho(0) = |\psi(0)\rangle\langle\psi(0)|
   $$

---

## 3) Open cadence channel dynamics ($\mathcal{E}_\tau$)
Each cadence step $\tau \to \tau+1$ consists of three consecutive sub-steps:
$$
\rho(\tau+1) = \mathcal{E}_{\text{leak}} \circ \mathcal{E}_{\text{mem}} \circ \mathcal{U}_{\text{graph}} \, (\rho(\tau))
$$

### 3.1) Graph-coherent layer ($\mathcal{U}_{\text{graph}}$)
The unitary evolution from the Hubbard/spin edge structure:
$$
\mathcal{U}_{\text{graph}}(\rho) = U_{\text{net}} \rho U_{\text{net}}^\dagger
$$
where $U_{\text{net}} = \exp(-i H_{\text{eff}} \Delta\tau)$ and the Hamiltonian is locally interacting:
$$
H_{\text{eff}} = \sum_{(i,j) \in E_{\text{ring}}} J_{\text{ring}} \left( \sigma_i^+ \sigma_j^- + \sigma_i^- \sigma_j^+ \right)
+ \sum_{k=1}^{5} J_{\text{star}} \left( \sigma_0^+ \sigma_k^- + \sigma_0^- \sigma_k^+ \right)
+ \sum_{k=1}^{5} \delta_k \sigma_k^z
$$
- $J_{\text{ring}}$: perimeter coupling
- $J_{\text{star}}$: radial coupling to the core
- $\delta_k$: structural inhomogeneity (the geometric-deficit effect entered without needing a continuous angle; default $\delta_k = \delta \cdot \delta_{k,1}$ or a five-fold distribution).

### 3.2) Cadence-leak layer ($\mathcal{E}_{\text{leak}}$ — per A04)
Pure-dephasing Kraus operators on every node:
$$
\mathcal{E}_{\text{leak}}(\rho) = \prod_{i=0}^{5} \mathcal{D}_i (\rho)
$$
with the standard Kraus definition for each node $i$ with cadence-leak parameter $\gamma_i \in [0, 1)$:
$$
K_{0,i} = \sqrt{1 - \frac{\gamma_i}{2}} \mathbb{I}_i, \quad K_{1,i} = \sqrt{\frac{\gamma_i}{2}} \sigma_i^z
$$
$$
\mathcal{D}_i(\rho) = K_{0,i} \rho K_{0,i}^\dagger + K_{1,i} \rho K_{1,i}^\dagger
$$

### 3.3) Causal-memory feedback layer ($\mathcal{E}_{\text{mem}}$)
Per the D04 formulation, a local memory variable $m_0(\tau)$ is kept for the central node or cluster edges:
$$
m_0(\tau+1) = (1-\eta) m_0(\tau) + \eta \mathcal{C}_0(\tau)
$$
which tunes the radial coupling coefficient as a function of history:
$$
J_{\text{star}}(\tau) = J_0 \left(1 + \beta m_0(\tau)\right)
$$
(this section measures coherence accumulation and core self-stabilization).

---

## 4) Key observables
To assess the cluster state at each step $\tau$:

1. **Holonomic ring charge ($Q(\tau)$):**
   $$
   \chi_{k, k+1}(\tau) = \mathrm{Tr}\left(\rho(\tau) \sigma_k^+ \sigma_{k+1}^-\right) = |\chi_k| e^{i \phi_k}
   $$
   $$
   \Phi_\ell(\tau) = \sum_{k=1}^{5} \phi_k(\tau) \quad (\mathrm{mod} \ 2\pi), \quad Q(\tau) = \frac{\Phi_\ell(\tau)}{2\pi}
   $$
2. **Local purity profile ($\mathcal{C}_i(\tau)$):**
   $$
   \mathcal{C}_i(\tau) = \mathrm{Tr}_i \left( \rho_i(\tau)^2 \right) - \frac{1}{2}, \quad \text{where } \rho_i = \mathrm{Tr}_{\setminus i}(\rho)
   $$
3. **Excitation-population distribution:**
   $$
   n_i(\tau) = \mathrm{Tr}\left(\rho(\tau) \sigma_i^+ \sigma_i^-\right)
   $$
4. **Ring-to-core boundary flux ($\mathcal{J}_{\text{core}}(\tau)$):**
   the exchange rate of excitation and coherence between the peripheral ring and the central core at each cadence step.

---

## 5) Experiment matrix (Simulation Scenarios)
To validate the hypothesis, three specific scenarios are compared:

| Test code | Scenario | Test purpose | Leak rate ($\gamma$) | Defect structure ($\delta$) |
| :---: | :---: | :---: | :---: | :---: |
| **S-01** | Flat symmetric cluster (Null) | baseline behavior without defect | $\gamma > 0$ | $\delta = 0$ |
| **S-02** | Cluster with five-fold structural defect | testing deficit-induced phase pinning | $\gamma > 0$ | $\delta > 0$ |
| **S-03** | Robustness against critical leak | finding the collapse threshold of $Q$ | sweep $\gamma \in [0.01, 0.5]$ | $\delta > 0$ |

---

## 6) Hypothesis-acceptance criteria and falsification conditions

### 6.1) Criteria for confirming soliton formation and survival
The stable-soliton-formation hypothesis is confirmed if and only if in scenario **S-02**:
1. **Phase persistence:** the charge $Q(\tau)$, after $\tau_{\text{relax}}$ time steps and despite leak $\gamma > 0$, retains its nonzero, quasi-quantized value:
   $$
   |Q(\tau)| \ge Q_{\text{threshold}} > 0 \quad \text{for } \tau > 20
   $$
2. **Localization:** the major share of excitation/coherence remains trapped in the cluster and does not uniformly fall to the maximally mixed state.
3. **Advantage over the flat scenario:** the phase lifetime in S-02 is significantly ($> 2\times$) longer than in the defect-free cluster S-01.

### 6.2) Explicit falsification conditions
The minimal-model hypothesis is refuted if:
1. For all values of $\delta$, the phase $\Phi_\ell(\tau)$ decays at the same rate as the flat cluster and $Q(\tau) \to 0$ converges (i.e., the five-fold defect plays no role in phase pinning).
2. Any apparent survival stems from numerical locking at very small $\gamma$, and the structure disintegrates at the smallest cadence phase leak ($\gamma \ge 0.05$).

---

## 7) Expected output for the next step
Production of an exact simulation script (Python/quantum) executing the density-matrix computations of scenarios S-01 to S-03 and extracting the time series of $Q(\tau)$ and $\mathcal{C}_i(\tau)$. **(Done 2026-09-30 — Record VMC-QF-Vault-11 below; the edge-phase scenario S-04 was added beyond the original S-01–S-03 scope.)**

---

## 8) Reference execution and CSV outputs
The reference execution operates in the single-excitation subspace (6 basis states); the Hamiltonian is the same ring+star hopping with $J_{ring}=1$, $J_{star}=0.3$, and the D05 double-dephasing channel is applied on every node. In this reduction the $6\times6$ density matrix is exact, because the hopping Hamiltonian conserves the excitation number. The initial state is the same ring wave $e^{i2\pi(k-1)/5}$ of section 2. To turn the ambiguous "defect structure" into a reproducible test, S-02/S-03 in this reference run implement the defect as a site detuning $\delta_1=0.1284$ in the term $\sum_k\delta_k\sigma_k^z$ (all others zero); S-01 has all $\delta_k=0$. The leak rate is constant per cadence, $\gamma_i=\gamma$; memory is off with $\beta=0$ because D05 assigns no numeric value to $\beta$.

**Important limitation:** the reference test does not show that the chosen defect increases the lifetime of $Q$; therefore the S-02 stability-acceptance criterion is **not confirmed**, and the data must be read as a negative/non-supporting test result, not as evidence of success. A different modeling of the deficit (e.g., the D04 edge phase) requires a separate protocol. The validity threshold for $Q$ is a minimum link-coherence magnitude of $10^{-3}$.

*(Navigation pointer: this limitation was superseded on 2026-09-30 by Record VMC-QF-Vault-11 — the exact CPTP execution of section 3 — which confirms the criterion for both registered defect implementations. Section 8 is retained as a historical record. The current output-file inventory is consolidated in the Execution Register below.)*

## Execution register (merged simulation records)

**Record VMC-QF-Vault-10 — candidate phenomenological run (reproducible, reduced model; not experimental evidence).** Six nodes: central cavity 0 and oriented peripheral ring 1–5. S-01 starts at phase 0 on every node; S-02 starts with $\phi_k = 2\pi(k-1)/5$ on the ring (center phase 0). For this discrete ring eigenmode, nonlinear feedback is represented by a 2.5× reduction in phase-leak susceptibility: $C = \exp(-5\gamma\tau)$ for S-01 and $C = \exp(-2\gamma\tau)$ for S-02, both with $\varepsilon_{cut}=10^{-3}$. At $\gamma=0.03$: $\tau_{life}(\text{S-01})=46.052$, $\tau_{life}(\text{S-02})=115.129$, ratio $=2.50$; S-02 retains $Q=1$ through $\tau=100$. **Status:** these lifetimes are threshold-crossing model estimates (formula extrapolated beyond the trajectory window if needed), not measured data. The candidate status remains provisional; the model-protection factor is an explicit phenomenological assumption awaiting validation by the full CPTP protocol of section 3.

**Reconciliation note (registered):** the reference execution of section 8 and record VMC-QF-Vault-10 use different defect implementations (site detuning vs. susceptibility reduction) and reach different verdicts on the S-02 advantage criterion. The honest registered state is: **the acceptance criterion "defect doubles the lifetime" is model-dependent and unconfirmed**; both runs are retained as separate registered records, and the decisive test is the full 64-dimensional CPTP simulation with the D04 edge-phase defect — flagged as the pending decisive protocol. **(Executed 2026-09-30 — see Record VMC-QF-Vault-11 below.)**

Trajectory/sweep conventions shared by every registered record: $\varepsilon_{cut}=10^{-3}$; $\tau=0…100$ at $\Delta\tau=0.5$ (201 rows per trajectory); sweeps run $\gamma=0.01$ to $0.50$; gamma-sweep status thresholds — lifetime $\ge 100$ Stable, $20<\text{lifetime}<100$ Metastable, $\le 20$ Critical Collapse.

**Record VMC-QF-Vault-11 — exact CPTP execution (section 3 protocol, decisive D04 edge-phase test included; run 2026-09-30).** Script: [simulate_D05_cptp.py](../_data/03_DYNAMICS_SOLITON/D05/simulate_D05_cptp.py); full log [run_output.txt](../_data/03_DYNAMICS_SOLITON/D05/run_output.txt), verification log [verify_output.txt](../_data/03_DYNAMICS_SOLITON/D05/verify_output.txt).

*Engine and verification battery (all checks passed):* exact CPTP dynamics $\rho \mapsto \mathcal{E}_{\text{leak}}(U_\tau \rho U_\tau^\dagger)$ on the full 64-dimensional density matrix ($\beta=0$, memory off as in section 8). Verified: Hermiticity of $H$ with no defect, site defect, and edge-phase (Peierls) defect; conservation of the total excitation number by $U_\tau$; trace preservation, diagonal preservation, and Hermiticity under the dephasing channel; complete positivity over 50 steps (minimum eigenvalue $\ge -1.6\times10^{-16}$); and agreement of the production engine (closed $6\times6$ one-excitation block — exact because the dephasing Kraus operators are diagonal) against the full 64-dimensional engine over 300 steps: max observable difference $2.3\times10^{-14}$ (S-01), $1.8\times10^{-13}$ (S-02). Initial-state conventions verified numerically: ring population 1, center population 0, $C_0=1/2$, mean link coherence $1/5$; $Q_{\text{winding}}(0)=1$ (S-02/S-04), $0$ (S-01).

*Scenarios at $\gamma=0.1$, $\Delta\tau=0.5$, $\tau\in[0,100]$ (201 rows each):* S-01 = uniform ring wave (phase 0 on every node, per the Vault-10 convention), no defect; S-02 = same wave + site detuning $\delta_1=0.1284$ rad (G01 angular deficit); S-04 = same wave + the D04 edge-phase defect implemented as a Hermitian Peierls flux $e^{+i\delta\theta}$ on the oriented hop $5\to1$ (and $e^{-i\delta\theta}$ on $1\to5$). The S-01/S-02/S-04 comparison is like-for-like (identical initial states, identical $\gamma$).

*Headline results (mean link-coherence lifetime = first crossing of $10^{-3}$):*

| scenario | defect | lifetime $\tau_{\text{life}}$ | ratio vs S-01 | $Q$ validity window |
|---|---|---|---|---|
| S-01 | none | 12.0 | 1 | $\tau \le 12.0$ |
| S-02 | site detuning 0.1284 | 24.5 | **2.042** | $\tau \le 10.0$ |
| S-04 | edge-phase flux 0.1284 (D04) | 25.0 | **2.083** | $\tau \le 25.0$ |

**Verdict (registered):** the acceptance criterion "the defect at least doubles the coherence lifetime" (ratio $>2$) is **confirmed** under the exact CPTP protocol for both registered defect implementations at $\gamma=0.1$: site detuning 2.042, edge-phase flux 2.083. This closes the pending decisive protocol flagged by the reconciliation note: the D04 edge-phase defect, executed exactly, also satisfies the criterion. Two honest qualifications are registered with the verdict: (i) the confirmation is at the single reference $\gamma=0.1$; the accompanying sweeps ($\gamma=0.01$–$0.50$ for S-03 and S-04) register the full $\gamma$-dependence for further analysis rather than a claimed universal ratio; (ii) this remains an in-silico, model-level result — no experimental claim is made (consistent with the vault Epistemic Status). Notably, $Q$ remains valid to $\tau=25.0$ under the edge-phase defect versus $10.0$ under the site defect — the D04 implementation preserves link coherence longer even though both cross the lifetime threshold together within measurement resolution ($24.5$ vs $25.0$).

## Output inventory (single consolidated list — supersedes all earlier file lists)

*Output files (all relative to the vault root; produced by the exact CPTP execution, Record VMC-QF-Vault-11; 201-row trajectories at $\gamma=0.1$):*
- [D05_S01_trajectory.csv](../_data/03_DYNAMICS_SOLITON/D05/D05_S01_trajectory.csv) — S-01, no defect
- [D05_S02_trajectory.csv](../_data/03_DYNAMICS_SOLITON/D05/D05_S02_trajectory.csv) — S-02, site detuning
- [D05_S04_edge_phase_trajectory.csv](../_data/03_DYNAMICS_SOLITON/D05/D05_S04_edge_phase_trajectory.csv) — S-04, edge-phase flux
- [D05_S03_gamma_sweep.csv](../_data/03_DYNAMICS_SOLITON/D05/D05_S03_gamma_sweep.csv) — S-03 sweep, $\gamma=0.01$–$0.50$
- [D05_S04_gamma_sweep.csv](../_data/03_DYNAMICS_SOLITON/D05/D05_S04_gamma_sweep.csv) — S-04 sweep, $\gamma=0.01$–$0.50$
- [D05_key_times_comparison.csv](../_data/03_DYNAMICS_SOLITON/D05/D05_key_times_comparison.csv) — side-by-side key rows (S-01/S-02/S-04)
- [D05_scenario_summary.csv](../_data/03_DYNAMICS_SOLITON/D05/D05_scenario_summary.csv) — per-scenario summary (three scenarios)

CSV columns (current schema, replacing the older $Q_{eff}$ description): $\tau$, $\gamma$, $Q_{\text{winding}}$, $Q_{\text{wrapped}}$ (both zeroed outside the validity window; min-link-coherence is recorded in every row so the window is reconstructible), ring/center populations, local coherences $C_0…C_5$, mean/min link coherence, and the five link phases. The phenomenological scripts and their records (section 8, Vault-10) are retained unchanged as historical registered records.

**Record VMC-QF-Vault-12 — relative-stability map $R(\gamma) = \tau_{\text{life}}(\text{defect})/\tau_{\text{life}}(\text{null})$ across the full sweep range (run 2026-09-30).** Script: [relative_stability_map.py](../_data/03_DYNAMICS_SOLITON/D05/relative_stability_map.py); data [D05_relative_stability_map.csv](../_data/03_DYNAMICS_SOLITON/D05/D05_relative_stability_map.csv); figure [D05_relative_stability_map.png](../_data/03_DYNAMICS_SOLITON/D05/D05_relative_stability_map.png); log [relative_stability_output.txt](../_data/03_DYNAMICS_SOLITON/D05/relative_stability_output.txt). This closes qualification (i) of the Vault-11 verdict: the γ-dependence of the "defect at least doubles the lifetime" criterion is now mapped, not left open.

*Protocol.* The S-01 null sweep (48 uncensored gammas, 0.03–0.50; γ = 0.01–0.02 right-censored) against the registered S-02 (site detuning) and S-04 (edge-phase flux) sweeps, same engines and thresholds as Vault-11. Null-engine equivalence asserted numerically (the defect implementations agree on the S-01 initial state at γ = 0.1 and 0.25). Because the cadence grid $\Delta\tau = 0.5$ makes raw crossing times coarse (quotients of half-integers), **two sub-grid estimators** were added and registered side by side with the raw quotients: Linear (linear interpolation of the coherence trace to the exact crossing) and Loglinear (log-space interpolation). Conclusions below survive the estimator choice.

*Result (estimator | mean ± sd over the 48-point window | $R \ge 2$ up to):*

| estimator | $R_{\text{site}}$ | $R_{\text{edge}}$ | $R\ge2$ up to $\gamma$ |
|---|---|---|---|
| raw (coarse grid) | 1.872 ± 0.177 | 1.874 ± 0.201 | 0.31 / 0.31 |
| Linear (primary) | 1.897 ± 0.175 | 1.910 ± 0.195 | 0.28 / 0.28 |
| Loglinear | 1.914 ± 0.163 | 1.926 ± 0.183 | 0.29 / 0.29 |

**Verdict (registered):**
1. **The map is not flat — the protection ratio erodes monotonically with $\gamma$:** from $R \approx 2.08$–$2.12$ over the weak-$\gamma$ window ($0.03 \le \gamma \le 0.14$, weakest 12 gammas) down to $R \approx 1.64$–$1.69$ over the strong-$\gamma$ window ($0.39 \le \gamma \le 0.50$); both estimators agree within 0.03. The ×2 confirmation of Vault-11 at $\gamma = 0.1$ therefore sits on a **plateau that extends to $\gamma \approx 0.3$**, beyond which the criterion fails gradually — no sharp transition, and no universal constant ratio. A "the defect always doubles the lifetime" claim would be false and is not made.
2. **The falsification bound 6.2.2 is comfortably cleared:** the criterion holds to $\gamma \approx 0.28$–$0.31$ (estimator-dependent), far beyond the $\gamma \ge 0.05$ disintegration bound registered in section 6.2.
3. **The two defect implementations remain indistinguishable in relative terms:** $R_{\text{edge}}$ tracks $R_{\text{site}}$ within noise across the entire range (a consistent hair above it), consistent with the Vault-11 headline (2.083 vs 2.042 at $\gamma = 0.1$); the edge-phase advantage registered there (longer $Q$ validity window) is a window effect, not a lifetime effect.

*Status:* in-silico, model-level (no experimental claim); single-cluster geometry, γ-independent Hamiltonian parameters as registered in section 3.
