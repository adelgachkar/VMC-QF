---
id: A04
title: Cadence, Phase-Leak, and Memory in Discrete Microcavities
vault: VMC-QF_Vault
layer: 00_CORE_AXIOMS
tags:
  - foundational
  - cadence
  - phase_leak
  - memory_kernel
  - bottleneck
  - reconstruction
status: revised-draft
created: 2026-09-28
language: en
cross_references:
  - "[[A01_Manifold_Free_Substrate]]"
  - "[[A02_Microcavity_Quantization]]"
  - "[[A03_Balance_Principle]]"
  - "[[G01_Five_Around_One_Deficit]]"
  - "[[D01_Cavity_Network_Hamiltonian]]"
  - "[[D02_Causal_Bounds_and_Lieb_Robinson]]"
---

# A04 — Cadence, Phase-Leak, and Memory in Discrete Microcavities

---

### 1. Purpose and place in VMC-QF
Document [[A03_Balance_Principle]] defined the general framework of conservation and the accounting of phase/balance exchange, but did not specify the mechanism of the following phenomena:
1. Why is the network's local response accompanied by **time delay and memory**?
2. Why do **bottleneck** and redistribution phenomena occur in high-flux regimes?
3. What is the mechanism of coherence **reconstruction** after passing through a bottleneck?

This document introduces the complementary cadence-behavior axiom and fixes the mathematical form of the memory terms ($\mathcal{M}_i$) and the effective leak ($\mathcal{L}_i$) in the balance equation of A03:

> **Axiom 4 (cadence and phase leak):**
> The exchange of phase and balance in the microcavity substrate is inherently a cadence-based, delayed process; therefore, part of the local balance over short time intervals is stored in a "reactive/trapped" form and does not directly participate in edge flux. The release of this part is governed by a causal memory kernel, and under super-thermal driving, part of it exits the separable description as an effective cadence leak.

---

### 2. Local and network cadence definition
Per [[A02_Microcavity_Quantization]], every cavity $v_i$ has a characteristic bandwidth $\Delta\omega_i$ and quality factor $Q_i$:

1. **Local cadence time ($\tau_{c,i}$):**
   The minimal time scale required for establishing a stable phase response in the cavity:
   $$
   \tau_{c,i} \sim \frac{1}{\Delta\omega_i} = \frac{Q_i}{\omega_i}
   $$
2. **Fundamental network cadence step:**
   At the fundamental discrete level ($\tau \in \mathbb{N}_0$), one time-step unit corresponds to the shortest network cadence:
   $$
   \Delta\tau_{\min} = \min_{i \in V} \tau_{c,i}
   $$
3. **Regional cadence time:**
   For a subset of cavities $\Omega \subset V$:
   $$
   \tau_c(\Omega) \equiv \max_{i \in \Omega} \tau_{c,i}
   $$

---

### 3. Balance decomposition: transferable versus reactive residue
Following section 6 of A03, the local balance $\mathcal{B}_i$ decomposes:
$$
\mathcal{B}_i = \mathcal{B}_i^{\text{tr}} + \mathcal{B}_i^{\text{res}}
$$
- **Transferable balance ($\mathcal{B}_i^{\text{tr}}$):** the excitation component that participates in edge flux in real time:
  $$
  \mathcal{J}_{i \to j} \approx \mathcal{F}_{ij}\left(\mathcal{B}_i^{\text{tr}}, \mathcal{B}_j^{\text{tr}}, \kappa_{ij}, \chi_{ij}\right)
  $$
- **Trapped/reactive-residue balance ($\mathcal{B}_i^{\text{res}}$):** the component locked in reactive modes whose release requires elapsed cadence time.

---

### 4. Memory kernel and non-Markovian return (Memory Kernel)
The gradual conversion of trapped balance $\mathcal{B}_i^{\text{res}}$ into transferable balance is modeled through the memory term $\mathcal{M}_i$:

#### 4.1) Fundamental discrete (cadence) formulation
At the cadence-step scale $\tau \in \mathbb{N}_0$:
$$
\mathcal{M}_i(\tau) = \sum_{\tau'=0}^{\tau} K_i(\tau - \tau') \, \Xi_i(\tau')
$$

#### 4.2) Effective continuum limit
At time scales larger than the cadence:
$$
\mathcal{M}_i(\tau) = \int_{-\infty}^{\tau} K_i(\tau - \tau') \, \Xi_i(\tau') \, d\tau'
$$
where:
- $K_i(\Delta\tau)$ is the cavity's causal response kernel:
  $$
  K_i(\Delta\tau) = 0 \quad (\forall \Delta\tau < 0)
  $$
- $\Xi_i$ is the local driving signal (the net-flux gradient function or the time derivative of excitation).
- **Standard first-order form (exponential relaxation):**
  $$
  K_i(\Delta\tau) \propto \exp\left(-\frac{\Delta\tau}{\tau_{c,i}}\right)
  $$

---

### 5. Cadence phase leak versus environmental decay
The leak term $\mathcal{L}_i$ in the balance equation is the sum of two independent contributions:
$$
\mathcal{L}_i(\tau) = \mathcal{L}_i^{\text{cad}}(\tau) + \mathcal{L}_i^{\text{env}}(\tau)
$$
1. **Real environmental decay ($\mathcal{L}_i^{\text{env}}$):** the escape of energy/phase into a thermal bath or an open external environment.
2. **Effective cadence leak ($\mathcal{L}_i^{\text{cad}}$):**
   Even in a network with globally unitary evolution, the analytical elimination of high-frequency degrees of freedom (coarse-graining) at the cadence scale produces an apparent decay of the transferable balance:
   $$
   \mathcal{L}_i^{\text{cad}} = \gamma_{c,i} \, \mathcal{B}_i^{\text{res}}
   $$
   where the effective cadence discharge rate scales with the cavity bandwidth: $\gamma_{c,i} \sim 1/\tau_{c,i} \sim \Delta\omega_i$.

---

### 6. Bottleneck dynamics and reconstruction

#### 6.1) Edge boundary capacity and the bottleneck condition
For every regional boundary $\partial\Omega$, a maximum acceptance and transport capacity is defined:
$$
\mathcal{C}_{\partial\Omega} = \sum_{e_{ij} \in \partial\Omega} c_{ij}
$$
where the edge capacity $c_{ij}$ is bounded by the coupling budget and bandwidth:
$$
c_{ij} \le |\kappa_{ij}| \cdot \min(\Delta\omega_i, \Delta\omega_j)
$$
- **Bottleneck occurrence:** if the injection flux rate entering the region exceeds the boundary capacity:
  $$
  \dot{\mathcal{B}}_{\Omega}^{\text{in}} > \mathcal{C}_{\partial\Omega}
  $$
  supercritical phase accumulation at the boundary, activation of the cadence leak $\mathcal{L}^{\text{cad}}$, and flux saturation $\sigma_i \to 0$ take place.

#### 6.2) Reconstruction mechanism
Reconstruction occurs when, after passing through a bottleneck, the balance stored in memory ($\mathcal{M}_i$) re-synchronizes with the flow along peripheral loop paths. In this state, the coherence factor or effective balance rises again without any violation of the conservation laws of A03.

---

### 7. Mapping phase debt to reactive residue
The phase debt $\Pi_i$ defined in [[A02_Microcavity_Quantization]] directly represents the cavity's reactive load:
$$
\mathcal{B}_i^{\text{res}} = g_i(\Pi_i)
$$
with compatibility conditions:
$$
g_i(0) = 0, \qquad \frac{d g_i}{d\Pi_i} > 0
$$
Near saturation ($\Pi_i \to 1$), the major share of the balance is locked in reactive form and the direct transfer flux $\mathcal{J}_{i \to j}$ drops sharply.

---

### 8. Empirical and theoretical falsification criteria
This document is falsified if any of the following holds:
1. **Instantaneous response in all regimes:** a proof that the network under fast pulse driving has no phase residue or cadence delay ($K_i(\Delta\tau) = \delta(\Delta\tau)$).
2. **No bottleneck threshold:** unlimited flux through a single edge without saturation or cadence leak.
3. **Coarse-graining inconsistency with the effective leak:** an analytical proof that coarse-graining in a closed quantum network can never produce a local decay-like term $\mathcal{L}^{\text{cad}}$.

---

### 9. Open variables
- Determining the exact analytic form of $K_i$ from the modal structure of the D01 Hamiltonian.
- An explicit operational definition of the observable measuring reconstruction (such as comparing the purity factor $\operatorname{Tr}(\rho^2)$ with the phaseor coherence index).
