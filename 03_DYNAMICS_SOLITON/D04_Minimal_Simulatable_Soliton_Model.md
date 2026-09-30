---
id: D04
title: Minimal Simulatable Soliton Model (Cadence + Phase + Balance)
vault: VMC-QF_Vault
layer: 03_DYNAMICS_SOLITON
tags:
  - minimal-model
  - CPTP
  - unitary-circuit
  - cadence
  - balance
  - phase-winding
  - trapping
  - defect-pinning
  - lieb-robinson
status: audited
created: 2026-09-27
audited: 2026-09-28
language: en
cross_references:
  - "[[A02_Microcavity_Quantization]]"
  - "[[A03_Balance_Principle]]"
  - "[[A04_Cadence_Phase_Leak]]"
  - "[[G01_Five_Around_One_Deficit]]"
  - "[[D01_Cavity_Network_Hamiltonian]]"
  - "[[D02_Causal_Bounds_and_Lieb_Robinson]]"
  - "[[D03_Topological_Soliton_Formation]]"
---

# D04: Minimal Simulatable Soliton Model
## (Cadence + Phase-Leak + Local Balance on a 5-around-1 Cluster)

---

## 0. Purpose and the anti-lock principle (Anti-Lock Principle)
The purpose of D04 is to formulate the simplest algebraic-graphical structure that simultaneously reproduces three fundamental features:
1. **Discrete cadence timing ($\tau \in \mathbb{N}$)** without assuming continuous time.
2. **Phase winding and loop holonomy ($\Phi_\ell, Q_\Omega$)** as emergent topological variables.
3. **Local balance and coherence flux ($\mathcal{B}_i, \mathcal{J}_{i \to j}$)** with operational, simulation-computable definitions.

No manifold, background metric, or continuous field is assumed; the substrate consists only of a finite graph, a finite-dimensional Hilbert space, and local quantum maps.

---

## 1. Laboratory substrate: the 6-node 5-around-1 cluster

### 1.1. Graph topology ($\mathcal{G} = (\mathcal{V}, \mathcal{E})$)
- **Node set:** $\mathcal{V} = \{0, 1, 2, 3, 4, 5\}$
  - central node: $0$
  - peripheral-ring nodes: $k \in \{1, 2, 3, 4, 5\}$
- **Star edges:** $\mathcal{E}_{\text{star}} = \{(0 \leftrightarrow k) \mid k=1,\dots,5\}$
- **Ring edges:** $\mathcal{E}_{\text{ring}} = \{(k \leftrightarrow k+1) \mid k=1,\dots,5 \text{ with } 6 \equiv 1\}$

### 1.2. Local Hilbert space
For every node $i \in \mathcal{V}$, a qubit degree of freedom ($d_i = 2$) with computational basis $\{|0\rangle, |1\rangle\}$ is adopted:
$$
\mathcal{H} = \bigotimes_{i=0}^5 \mathbb{C}^2, \quad \dim(\mathcal{H}) = 2^6 = 64
$$

---

## 2. Cadence dynamics: the discrete-step evolution map (Discrete-Step Generator)
At each cadence tick $\tau \mapsto \tau + 1$, the total cluster density matrix $\hat{\rho}(\tau)$ evolves under the layered CPTP channel:

$$
\hat{\rho}(\tau+1) = \mathcal{E}_{\text{leak}} \circ \mathcal{E}_{\text{ring}} \circ \mathcal{E}_{\text{star}} \big( \hat{\rho}(\tau) \big)
$$

### 2.1. Edge-coupling sub-steps ($\mathcal{E}_{\text{star}}, \mathcal{E}_{\text{ring}}$)
On each edge $e = (i, j)$, an exchange two-qubit gate with interaction angle $\theta_{ij} = \kappa_{ij} \Delta \tau$ is applied:
$$
U_{ij}(\theta_{ij}, \phi_{ij}) = \exp\left( -i \theta_{ij} \left( e^{i \phi_{ij}} \sigma_i^+ \sigma_j^- + e^{-i \phi_{ij}} \sigma_i^- \sigma_j^+ \right) \right)
$$

### 2.2. Local leak and dephasing sub-step ($\mathcal{E}_{\text{leak}}$ — axiom A04)
On each node $i \in \mathcal{V}$, a single-qubit dephasing channel is applied:
$$
\mathcal{D}_{\gamma_i}(\rho_i) = (1 - \gamma_i)\rho_i + \gamma_i Z_i \rho_i Z_i
$$

---

## 3. Phase variables and loop holonomy

### 3.1. Complex edge correlation
For each edge $(i, j) \in \mathcal{E}$, the local link phase is extracted from the expectation value:
$$
\chi_{ij}(\tau) \equiv \mathrm{Tr}\left( \hat{\rho}(\tau) \sigma_i^+ \sigma_j^- \right) = |\chi_{ij}(\tau)| e^{i \phi_{ij}(\tau)}
$$

### 3.2. Loop holonomy and cluster topological charge
For the 5-fold peripheral loop $\ell = (1 \to 2 \to 3 \to 4 \to 5 \to 1)$:
$$
\Phi_\ell(\tau) = \left[ \sum_{k=1}^5 \phi_{k, k+1}(\tau) \right] \pmod{2\pi}
$$
Cluster charge:
$$
Q(\tau) = \frac{\Phi_\ell(\tau)}{2\pi}
$$

### 3.3. Twist-injection protocol (Twist Injection - T1)
At the initial step $\tau = 0$, a phase twist is imprinted on the ring edges by applying the gate $R_z(2\pi / 5)$ on the peripheral nodes so that $\Phi_\ell(0) \approx 2\pi$ ($Q(0) \approx 1$).

---

## 4. Local balance accounting and coherence flux (A03)

### 4.1. Local purity/coherence balance
For each node $i$:
$$
\mathcal{B}_i(\tau) \equiv \mathcal{C}_i(\tau) = \mathrm{Tr}\left( \hat{\rho}_i^2(\tau) \right) - \frac{1}{2} \in [0, 0.5]
$$
where $\hat{\rho}_i = \mathrm{Tr}_{\mathcal{V} \setminus \{i\}}(\hat{\rho})$.

### 4.2. Edge coherence flux
The purity flux during execution of the edge gate $(i \to j)$:
$$
\mathcal{J}_{i \to j}(\tau) \equiv \mathcal{C}_j^{(\text{after } U_{ij})} - \mathcal{C}_j^{(\text{before } U_{ij})}
$$
Balance conservation is checked and logged at each step according to equation A03.

---

## 5. One-step causal memory and the G01 frustration

### 5.1. Local memory kernel
The phase-memory variable of each node with update coefficient $\eta \in [0, 1]$:
$$
m_i(\tau+1) = (1 - \eta) m_i(\tau) + \eta \, \mathcal{C}_i(\tau)
$$
The effective link phase in the next step is self-tuned: $\phi_{ij}(\tau+1) \leftarrow \phi_{ij} + \beta (m_i - m_j)$.

### 5.2. Applying the G01 angular deficit
The 5-around-1 geometric frustration is applied as an intrinsic phase on edge $(5 \leftrightarrow 1)$:
$$
\phi_{5, 1}^{(0)} = \delta\theta \approx 7.356^{\circ} \approx 0.1284 \ \text{rad}
$$

> **Execution pointer (2026-09-30 — Record VMC-QF-Vault-11, [[D05_Cluster_Simulation_and_Validation]]):** this edge-phase implementation was executed exactly in the 64-dimensional CPTP simulation as the hermitian Peierls flux $e^{+i\delta\theta}$ on the oriented hop $5 \to 1$ (and $e^{-i\delta\theta}$ on $1 \to 5$), alongside the scalar site-detuning realization of the same $\delta\theta$. Both satisfy the criterion-4 separation $\tau_{\text{life}}(\text{twist}) > 2\,\tau_{\text{life}}(\text{baseline})$ at $\gamma = 0.1$: ratio **2.083** (this edge-phase channel) vs **2.042** (site detuning); this channel additionally holds the $Q$ validity window to $\tau = 25.0$ vs $10.0$ (site). The γ-dependence of both ratios is mapped in Record VMC-QF-Vault-12 ($\times 2$ survives to $\gamma \approx 0.3$). Implementation: `simulate_D05_cptp.py` (defect = `edge-phase`).

---

## 6. The four validation and soliton-falsification criteria

| Index | Formulation | Soliton formation/persistence condition |
| :--- | :--- | :--- |
| **1. Loop phase locking** | $\mathrm{Var}_{\Delta \tau}[\Phi_\ell(\tau)]$ | $\le \varepsilon_\Phi \ll 1$ (holonomy stability) |
| **2. Coherence concentration** | $\sum_{k=1}^5 \mathcal{C}_k(\tau) / \mathcal{C}_0(\tau)$ | $\ge \Lambda_{\text{trap}} > 1$ (ring trapping) |
| **3. Boundary charge leak** | $\sum_{k=1}^5 \|\mathcal{J}_{k \to 0}(\tau)\|$ | $\le \varepsilon_J \ll \kappa_{\text{ring}}$ (flux isolation) |
| **4. Survival under leak** | lifetime $\tau_{\text{life}}$ with $\gamma > 0$ | $\tau_{\text{life}}(\text{with twist}) \gg \tau_{\text{life}}(\text{baseline})$ |

---

## 7. Definitive simulation configuration for D05
- **Selected branch:** $\mathbf{E} + \mathbf{T1}$ (CPTP evolution + initial phase-twist injection)
- **Base parameters:**
  - ring coupling: $\kappa_{\text{ring}} = 1.0$
  - star coupling: $\kappa_{\text{star}} = 0.3$
  - dephasing leak rate: $\gamma = 0.05$
  - memory weight: $\eta = 0.2$
