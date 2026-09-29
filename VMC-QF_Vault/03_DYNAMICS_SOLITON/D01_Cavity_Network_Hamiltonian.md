---
id: D01
title: Graph-Native Dynamics Generator for Microcavity Networks
vault: VMC-QF_Vault
layer: 03_DYNAMICS_SOLITON
tags:
  - dynamics
  - generator
  - unitary
  - cptp
  - memory
  - balance
  - gauge
  - lindblad
status: revised-draft
created: 2026-09-28
language: en
cross_references:
  - "[[A01_Manifold_Free_Substrate]]"
  - "[[A02_Microcavity_Quantization]]"
  - "[[A03_Balance_Principle]]"
  - "[[A04_Cadence_Phase_Leak]]"
  - "[[G01_Five_Around_One_Deficit]]"
  - "[[D02_Causal_Bounds_and_Lieb_Robinson]]"
  - "[[D03_Topological_Soliton_Formation]]"
---

# D01: Graph-Native Dynamics Generator for Microcavity Networks

---

### 1. Purpose and structural philosophy
This document lays the mathematical framework of the microcavity-network dynamics on the irregular substrate hypergraph $\mathcal{G} = (\mathcal{V}, \mathcal{E}, \mathcal{W})$ ([[A01_Manifold_Free_Substrate]]).

To prevent premature locking to continuum geometry or invalid phenomenological fits:
1. No continuous coordinates are imposed as a presupposition of space; all interactions are inherently **graph-local**.
2. Time is defined dually: a **discrete cadence step** ($\Delta\tau_i$) aligned with the quantization axioms ([[A02_Microcavity_Quantization]], [[A04_Cadence_Phase_Leak]]) and an **effective continuous time** ($\tau$) for collective coarse scales.
3. The evolution generator is built so that in the closed limit it is a Hermitian Hamiltonian with Heisenberg exchange, and in the open limit a completely positive trace-preserving (CPTP) map in explicit consistency with the balance law ([[A03_Balance_Principle]]).

---

### 2. Network Hilbert space and physical dimensions
Per axiom [[A02_Microcavity_Quantization]], every cavity $i \in \mathcal{V}$ carries a finite Hilbert space $\mathcal{H}_i$ of dimension $d_i < \infty$.
The total network state space is the tensor product of local spaces:
$$
\mathcal{H} = \bigotimes_{i \in \mathcal{V}} \mathcal{H}_i, \quad \dim(\mathcal{H}) = \prod_{i \in \mathcal{V}} d_i < \infty
$$

- **Time variable ($\tau$):** the effective evolution variable carrying the physical dimension of time ($\text{s}$).
- **Evolution generator ($\hat{G}$):** a Hermitian operator with the dimension of angular frequency ($\text{rad/s}$), so that the physical-energy Hamiltonian is $\hat{H} = \hbar \hat{G}$.
- **System state:** described by a density matrix $\rho \in \mathcal{S}(\mathcal{H})$ with $\rho \ge 0$ and $\mathrm{Tr}(\rho) = 1$.

---

### 3. Graph locality principle (Graph Locality Decomposition)
Dynamics on the substrate occur exclusively through the nodes and edges present in $\mathcal{E}$. The total generator $\mathcal{L}$ or energy generator $\hat{G}$ decomposes into three local levels:

$$
\hat{G} = \sum_{i \in \mathcal{V}} \hat{G}_i + \sum_{(i,j) \in \mathcal{E}} \hat{G}_{ij}
$$

1. **Single-node local generators ($\hat{G}_i$):** containing the cavity resonance frequency and intra-cavity self-interaction / nonlinear effects:
   $$
   \hat{G}_i = \omega_{0,i} \hat{n}_i + \chi_i \hat{n}_i (\hat{n}_i - \mathbb{I})
   $$
   where $\hat{n}_i$ is the local excitation-number operator ($\mathrm{spec}(\hat{n}_i) = \{0, 1, \dots, d_i - 1\}$).
2. **Edge exchange generators ($\hat{G}_{ij}$):** describing coupling and hopping of excitations along allowed edges:
   $$
   \hat{G}_{ij} = \kappa_{ij} \hat{a}_i^\dagger \hat{a}_j + \kappa_{ij}^* \hat{a}_j^\dagger \hat{a}_i + \lambda_{ij} \hat{n}_i \hat{n}_j
   $$
   where $\kappa_{ij} = |\kappa_{ij}| e^{i \chi_{ij}}$ is the complex edge coupling and $\lambda_{ij}$ the cross-polarization/density interaction.

---

### 4. The three dynamical regimes

#### Regime 1: discrete cadence-step evolution (Cadence-Step Map)
At the most fundamental level, for each cadence step $\Delta\tau$:
$$
\rho(\tau + \Delta\tau) = \Phi_{\Delta\tau}[\rho(\tau)]
$$
To preserve causal structure and locality, $\Phi_{\Delta\tau}$ is obtained from products of local maps (Trotter–Suzuki decomposition on the graph):
$$
\Phi_{\Delta\tau} = \left( \prod_{i \in \mathcal{V}} \Phi^{(i)}_{\Delta\tau} \right)^{1/2} \left( \prod_{(i,j) \in \mathcal{E}} \Phi^{(ij)}_{\Delta\tau} \right) \left( \prod_{i \in \mathcal{V}} \Phi^{(i)}_{\Delta\tau} \right)^{1/2} + \mathcal{O}(\Delta\tau^3)
$$
This map is completely positive and trace-preserving (CPTP) and guarantees that no value singularity occurs in Hilbert space.

#### Regime 2: continuous Markovian limit (Lindblad Limit)
Under linear-loss approximation, when the cadence time is much smaller than the system evolution time ($\Delta\tau \ll \tau_{\text{evol}}$), the density-matrix evolution obeys the standard Lindblad master equation:
$$
\frac{d\rho}{d\tau} = -i [\hat{G}, \rho] + \sum_{i \in \mathcal{V}} \gamma_{c,i} \mathcal{D}[\hat{L}_i]\rho + \sum_{(i,j) \in \mathcal{E}} \gamma_{ij} \mathcal{D}[\hat{L}_{ij}]\rho
$$
where the decoherence superoperator is $\mathcal{D}[\hat{L}]\rho = \hat{L}\rho\hat{L}^\dagger - \frac{1}{2}\{\hat{L}^\dagger\hat{L}, \rho\}$ and the collapse operators are:
- **Local cadence leak ([[A04_Cadence_Phase_Leak]]):** $\hat{L}_i = \hat{a}_i$ or $\hat{L}_{i,\phi} = \hat{n}_i$ (dephasing).
- **Edge decay:** $\hat{L}_{ij} = \hat{a}_i - \hat{a}_j$.

#### Regime 3: non-Markovian memory limit
Per the memory axiom of [[A04_Cadence_Phase_Leak]], if the decoherence rate is comparable to the cavity bandwidth, the network's historical memory activates:
$$
\frac{d\rho}{d\tau} = -i [\hat{G}, \rho] + \int_{0}^{\tau} \mathcal{K}(\tau - \tau') [\rho(\tau')] \, d\tau'
$$
- The memory superoperator $\mathcal{K}(t)$ is analytic, causal ($\mathcal{K}(t < 0) = 0$), and residue-reproducing:
  $$
  \mathcal{K}(t) = \sum_{k} \Gamma_k e^{-t / \tau_{M,k}} \cos(\Omega_k t + \theta_k) \mathcal{D}[\hat{L}_k]
  $$
  where the memory time is linked to the quality parameter: $\tau_{M,i} \sim Q_i / \omega_{0,i}$.

---

### 5. Mathematical link with the balance axiom: explicit flux derivation (Closure to A03)

For compatibility with the conservation law and local energy/charge balance ([[A03_Balance_Principle]]):
$$
\mathcal{B}_i(\tau) \equiv \mathrm{Tr}\big(\rho(\tau) \hat{B}_i\big)
$$
the time derivative of this observable in the Heisenberg picture decomposes as:
$$
\frac{d\mathcal{B}_i}{d\tau} = \mathrm{Tr}\left( \rho(\tau) \cdot i [\hat{G}, \hat{B}_i] \right) + \mathrm{Tr}\left( \mathcal{L}_{\text{diss}}[\rho(\tau)] \hat{B}_i \right)
$$
Substituting the edge decomposition $\hat{G} = \sum_k \hat{G}_k + \sum_{(k,l)} \hat{G}_{kl}$, the Heisenberg terms form exactly the edge fluxes:
$$
i [\hat{G}, \hat{B}_i] = \sum_{j \in \mathcal{N}(i)} \hat{\mathcal{J}}_{j \to i}
$$
where the **edge flux operator** is uniquely and antisymmetrically defined:
$$
\hat{\mathcal{J}}_{j \to i} \equiv i [\hat{G}_{ij}, \hat{B}_i] = -\hat{\mathcal{J}}_{i \to j}
$$
and the contributions of structural losses and environmental leaks are recovered as sink and source terms:
$$
\mathcal{L}_i^{\text{loss}} = -\mathrm{Tr}\big( \mathcal{L}_{\text{diss}}[\rho] \hat{B}_i \big) \ge 0, \quad \mathcal{S}_i^{\text{gain}} = \mathrm{Tr}\big( \mathcal{L}_{\text{pump}}[\rho] \hat{B}_i \big)
$$
Thus the network continuity equation on the graph is obtained without any continuous spatial derivative:
$$
\frac{d\mathcal{B}_i}{d\tau} = \sum_{j \in \mathcal{N}(i)} \mathcal{J}_{j \to i}(\tau) + \mathcal{S}_i(\tau) - \mathcal{L}_i(\tau) + \mathcal{M}_i(\tau)
$$

---

### 6. Phase gauge symmetry and loop invariance (Gauge Structure)

#### 6.1) Local $U(1)$ gauge transformations
Under a local phase transformation with angle $\alpha_i \in [0, 2\pi)$ on each node:
$$
|\psi_i\rangle \to e^{i \alpha_i \hat{n}_i} |\psi_i\rangle \implies \hat{a}_i \to \hat{a}_i e^{-i \alpha_i}
$$
for the generator $\hat{G}_{ij}$ to remain invariant, the edge link phases must transform as:
$$
\chi_{ij} \to \chi_{ij} + (\alpha_i - \alpha_j)
$$

#### 6.2) Gauge-invariant loop phase
For any closed path $\mathcal{C} = (v_1, v_2, \dots, v_n, v_1)$, the sum of edge phases is a gauge invariant:
$$
\Phi_{\mathcal{C}} = \sum_{(i \to j) \in \mathcal{C}} \chi_{ij} \pmod{2\pi}
$$
This loop phase acts as a local pseudo-magnetic flux (Plaquette Flux) on the graph.

---

### 7. Bridge G01 → D01: the 5-around-1 frustration potential

Per [[G01_Five_Around_One_Deficit]], the 5-around-1 cluster carries a rigid angular deficit $\delta\theta = 7.356^{\circ}$ ($0.1284\ \text{rad}$). This geometric mismatch enters the edge generator as a preferred phase-tension potential $\Phi^\star$:

$$
\Phi^\star = \delta\theta = 2\pi - 5 \alpha_{\text{eff}} \approx 0.1284\ \text{rad}
$$

The frustration energy stored in the 5-fold perimeter loop $\mathcal{C}_5$:
$$
\hat{G}_{\text{frust}} = -K_5 \cos\left( \sum_{k=1}^5 \chi_{k,k+1} - \Phi^\star \right)
$$
- The minimum of this interaction does **not** occur at $\Phi_{\text{loop}} = 0$; the system is forced in its ground state to maintain a permanent phase rotation with nonzero angular rate.
- This tension is the definite grounding for the emergence of **spontaneous chiral currents** and the nucleation of topological solitons in [[D02_Causal_Bounds_and_Lieb_Robinson]] and [[D03_Topological_Soliton_Formation]].

---

### 8. Nonlinear saturation and dynamic bounds (Dynamic Stability)
To prevent phase and energy divergence under continuous driving:
1. **Hilbert-dimension bound:** per node $d_i < \infty$; hence $\langle \hat{n}_i \rangle \le d_i - 1$.
2. **Hopping saturation (Kerr-type de-tuning):** as the excitation content inside a cavity grows, the nonlinear frequency mismatch ($\chi_i \hat{n}_i^2$) strongly suppresses edge hopping (self-trapping):
   $$
   |\kappa_{ij}^{\text{eff}}| = \frac{|\kappa_{ij}|}{\sqrt{1 + \left( \frac{\chi_i n_i - \chi_j n_j}{|\kappa_{ij}|} \right)^2}}
   $$
   This guarantees that node capacities ([[A02_Microcavity_Quantization]]) are never violated.

---

### 9. Precise falsification criteria
This dynamics-generator structure is falsified if:
1. **Graph-locality failure:** it is proven that balance exchange between two cavities $i$ and $j$ without a direct edge $e_{ij} \notin \mathcal{E}$ occurs faster than step-by-step Lindblad propagation along the shortest graph path (a violation of the graph Lieb–Robinson bound).
2. **Violation of operator balance conservation:** it is proven that the edge-flux operator relation $\hat{\mathcal{J}}_{j \to i} = i[\hat{G}_{ij}, \hat{B}_i]$ fails to remain closed at the density-matrix level and yields a divergent observable.
3. **Frustration ineffectiveness:** numerical simulation of the 5-around-1 cluster shows that the loop phase converges to $\Phi_{\text{loop}} \to 0$ for all initial conditions, leaving no chirality or persistent current.
