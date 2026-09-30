---
id: A03
title: Balance Principle for Phase and Reactive Exchange
vault: VMC-QF_Vault
layer: 00_CORE_AXIOMS
tags:
  - foundational
  - balance_principle
  - phase_flow
  - reactive_energy
  - network_dynamics
status: revised-draft
created: 2026-09-28
language: en
cross_references:
  - "[A01_Manifold_Free_Substrate](A01_Manifold_Free_Substrate.md)"
  - "[A02_Microcavity_Quantization](A02_Microcavity_Quantization.md)"
  - "[A04_Cadence_Phase_Leak](A04_Cadence_Phase_Leak.md)"
  - "[G01_Five_Around_One_Deficit](../02_GEOMETRY_TOPOLOGY/G01_Five_Around_One_Deficit.md)"
  - "[D01_Cavity_Network_Hamiltonian](../03_DYNAMICS_SOLITON/D01_Cavity_Network_Hamiltonian.md)"
---

# A03 — Balance Principle for Phase and Reactive Exchange

---

### 1. Role of the document in the VMC-QF structure
Following axioms [A01_Manifold_Free_Substrate](A01_Manifold_Free_Substrate.md) and [A02_Microcavity_Quantization](A02_Microcavity_Quantization.md):
- The substrate network is a discrete collection of microcavities.
- Every microcavity has a finite capacity for excitation, phase storage, and reactive-energy accumulation.

This document establishes the accounting law governing inter-cavity exchanges:

> **Axiom 3 (balance principle):**
> Any change in the phase asset, reactive energy, or local balance quantity of a cavity must be exactly accounted for through interaction and flux on adjacent edges, internal component conversions, cadence leaks, or effective source/sink terms. In a closed system, no local balance appears or vanishes without a structural exchange.

---

### 2. Representation independence and the local balance quantity
The balance principle does not depend on a particular representation and is expressed as an observable or an effective local functional:

$$
\mathcal{B}_i \equiv \mathcal{B}_i[\rho_i] = \operatorname{Tr}\left(\rho_i \hat{B}_i\right)
$$

where:
- $\rho_i$ is the reduced density matrix of cavity $v_i$.
- $\hat{B}_i$ is a Hermitian operator or effective balance index (such as the number operator $\hat{n}_i$, the phase debt $\Pi_i$, or a combined phase-coherence operator).

---

### 3. Fundamental formulation and the continuum balance limit

#### 3.1) Discrete difference form (fundamental cadence scale)
At the fundamental level with a discrete cadence counter $\tau \in \mathbb{N}_0$:
$$
\Delta \mathcal{B}_i(\tau) \equiv \mathcal{B}_i(\tau + 1) - \mathcal{B}_i(\tau) = \sum_{j \in \mathcal{N}(i)} \mathcal{J}_{j \to i}(\tau) + \mathcal{S}_i(\tau) - \mathcal{L}_i(\tau) + \mathcal{M}_i(\tau)
$$

#### 3.2) Effective continuous-time approximation
At time scales larger than the base cadence ($\tau \gg 1$):
$$
\frac{d\mathcal{B}_i}{d\tau} = \sum_{j \in \mathcal{N}(i)} \left( \mathcal{J}_{j \to i} - \mathcal{J}_{i \to j} \right) + \mathcal{S}_i - \mathcal{L}_i + \mathcal{M}_i
$$
- $\mathcal{J}_{j \to i}$: the balance-transfer flux from node $j$ to node $i$ along edge $e_{ij}$.
- $\mathcal{S}_i$: local injection or source term.
- $\mathcal{L}_i$: decay or effective cadence leak to environmental degrees of freedom (leakage, per [A04_Cadence_Phase_Leak](A04_Cadence_Phase_Leak.md)).
- $\mathcal{M}_i$: the memory and non-instantaneous return contribution from the cavity's delayed response.

---

### 4. Edge flux and the reciprocity constraint
The flux exchanged on structural edge $e_{ij}$ is a function of the local states and the edge linkage:
$$
\mathcal{J}_{i \to j} = \mathcal{F}_{ij}(\rho_i, \rho_j, \kappa_{ij}, \chi_{ij})
$$
where $\kappa_{ij}$ is the structural coupling and $\chi_{ij}$ the edge phase/delay variables.

- **Unitary/reversible exchange condition (antisymmetric flux):**
  In the absence of decay or on-edge storage:
  $$
  \mathcal{J}_{i \to j} = -\mathcal{J}_{j \to i}
  $$
- **Correction due to edge delay or decay:**
  In the presence of an environment or edge transition capacity:
  $$
  \mathcal{J}_{i \to j} + \mathcal{J}_{j \to i} = \mathcal{R}_{ij}
  $$
  where $\mathcal{R}_{ij}$ describes the intermediate decay or accumulation of the edge.

---

### 5. Regional balance theorem and network conservation
For any subset of cavities $\Omega \subset V$:
$$
\frac{d}{d\tau} \sum_{i \in \Omega} \mathcal{B}_i = \Phi_{\partial\Omega} + \sum_{i \in \Omega} \left( \mathcal{S}_i - \mathcal{L}_i + \mathcal{M}_i \right)
$$
where $\Phi_{\partial\Omega} = \sum_{i \in \Omega, j \notin \Omega} \mathcal{J}_{j \to i}$ is the net boundary flux.
For a closed system ($\Phi_{\partial\Omega} = 0$) and the ideal case ($\mathcal{S}_i = \mathcal{L}_i = \mathcal{M}_i = 0$), total conservation is guaranteed:
$$
\sum_{i \in V} \mathcal{B}_i = \text{const}
$$

---

### 6. Multi-component structure: separating internal and reactive contributions
To avoid conflating stable excitations with transient phases, the local balance is decomposed:
$$
\mathcal{B}_i = \mathcal{B}_i^{\text{int}} + \lambda_i \mathcal{B}_i^{\text{react}}
$$
- $\mathcal{B}_i^{\text{int}}$: the resident/internal contribution (such as the excitation population $n_i$).
- $\mathcal{B}_i^{\text{react}}$: the temporary reactive contribution from mismatch or phase debt ($\Pi_i$).
- $\lambda_i$: a dimensional conversion coefficient depending on scale and cavity parameters.

---

### 7. Capacity control, saturation, and flux redistribution
By the finite-dimension axiom of [A02_Microcavity_Quantization](A02_Microcavity_Quantization.md), every cavity has a saturation capacity $\mathcal{B}_{i,\max}(d_i)$. To control super-thermal accumulation, the effective flux is scaled by a local saturation factor $\sigma_i$:
$$
\mathcal{J}_{i \to j}^{\text{eff}} = \mathcal{J}_{i \to j} \cdot \sigma_i(\mathcal{B}_i)
$$
where:
$$
\sigma_i(\mathcal{B}_i) \to 1 \quad (\mathcal{B}_i \ll \mathcal{B}_{i,\max}), \qquad \sigma_i(\mathcal{B}_i) \to 0 \quad (\mathcal{B}_i \to \mathcal{B}_{i,\max})
$$
This nonlinearity causes automatic flux redistribution toward peripheral edges, or discharge through the cadence leak $\mathcal{L}_i$.

---

### 8. Effect of the angular deficit and the 5-around-1 linkage ([G01_Five_Around_One_Deficit](../02_GEOMETRY_TOPOLOGY/G01_Five_Around_One_Deficit.md))
In the presence of structural asymmetry or a local angular deficit $\delta\theta_i$:
$$
\mathcal{J}_{ij} = \mathcal{J}_{ij}^{(0)} + \Delta\mathcal{J}_{ij}(\delta\theta_i)
$$
This linkage deficit can produce anisotropy in flux redistribution, local circulating flux, and the grounding of trapped or metastable modes (detailed derivation is delegated to the evolution functions in D01).

---

### 9. Loop circulation and phase invariant (Loop Circulation)
On a closed path $\mathcal{C}$ in the network, phaseor circulation is characterized by the following gauge invariant:
$$
\Phi_{\mathcal{C}} = \arg\left( \prod_{e_{ij} \in \mathcal{C}} \kappa_{ij} \right)
$$
The stability of such loop circulation indicates local phase vortices; however, assigning properties such as topological charge or angular momentum requires conservation laws proven in the dynamical model.

---

### 10. Link with the memory effect and leak in [A04_Cadence_Phase_Leak](A04_Cadence_Phase_Leak.md)
Decay and memory terms are closed explicitly through cadence relations:
$$
\mathcal{L}_i = \mathcal{L}_i^{\text{phase}} + \mathcal{L}_i^{\text{react}}
$$
$$
\mathcal{M}_i(\tau) = \int_{-\infty}^{\tau} K_i(\tau - \tau') \mathcal{X}_i(\tau') \, d\tau'
$$
where $K_i$ is the causal kernel introduced in A02/A04 and $\mathcal{X}_i$ is the history of balance fluctuations.

---

### 11. Falsification criteria
1. **Conservation violation in a closed network:** a proof of an unresponsive change in the total balance in the absence of environmental degrees of freedom.
2. **Absence of saturation:** a proof that a finite-dimensional microcavity can absorb unbounded flux without redistribution or leakage.
3. **No continuum-limit convergence:** the inability of the discrete formulation to reproduce the standard continuity equation at coarse-grained scales.
