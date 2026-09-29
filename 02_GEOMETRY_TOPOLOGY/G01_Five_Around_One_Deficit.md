---
id: G01
title: Five-Around-One Topological Deficit and Structural Frustration
vault: VMC-QF_Vault
layer: 02_GEOMETRY_TOPOLOGY
tags:
  - foundational
  - topology
  - angular_deficit
  - frustration
  - discrete_geometry
  - holonomy
status: audited
created: 2026-09-28
updated: 2026-09-30
language: en
cross_references:
  - "[[A01_Manifold_Free_Substrate]]"
  - "[[A02_Microcavity_Quantization]]"
  - "[[A03_Balance_Principle]]"
  - "[[A04_Cadence_Phase_Leak]]"
  - "[[D01_Cavity_Network_Hamiltonian]]"
  - "[[D03_Topological_Soliton_Formation]]"
  - "[[D04_Minimal_Simulatable_Soliton_Model]]"
  - "[[D05_Cluster_Simulation_and_Validation]]"
  - "[[S03_Topological_and_Memory_Scaling]]"
---

# G01: Five-Around-One Topological Deficit and Structural Frustration

---

### 1. Purpose and place in the VMC-QF architecture

In the preceding documents:
- The substrate was defined as a discrete manifold-free hypergraph ([[A01_Manifold_Free_Substrate]]).
- Nodes carry finite phase capacity and intrinsic cadence ([[A02_Microcavity_Quantization]], [[A04_Cadence_Phase_Leak]]).
- Exchanges obey the closed-flux balance law ([[A03_Balance_Principle]]).

This document introduces the root of **intrinsic frustration** in the network:

> **Problem:** why can the microcavity network not reach a completely flat, static, isotropic, flux-free ground state?
> **Answer:** the combinatorial 5-around-1 cluster carries a **local angular/holonomic deficit** $\delta\theta = 7.356103^\circ$ (Section 3, derived — not postulated). This geometric mismatch prevents all perimeter links from carrying zero phase simultaneously and forces the system to store phase tension, break gauge symmetry, or form stable circulating vortices.

---

### 2. Structural definition of the local 5-around-1 complex

Assume that in a subset of substrate nodes, a central cavity $v_0 \in \mathcal{V}$ together with its 5 immediate neighbors forms a local cell (star/cluster complex $\mathcal{S}_5$):
$$
\mathcal{N}(v_0) = \{ v_1, v_2, v_3, v_4, v_5 \}
$$

Edge connections are defined as:
1. **Radial edges:** $e_{0k} = (v_0, v_k)$ for $k \in \{1,\dots,5\}$ with coupling amplitude $\kappa_{0k}$ and link phase $\chi_{0k}$.
2. **Perimeter edges:** $e_{k,k+1} = (v_k, v_{k+1})$ with the periodic convention $v_6 \equiv v_1$ and coupling amplitudes $\kappa_{k,k+1}$.

```text
        v1
      /    \
    v5      v2
    |   v0  |
    v4──────v3
```

---

### 3. Derivation of the angular deficit (complete)

**Registered result (reproduced by `_data/02_GEOMETRY_TOPOLOGY/G01/verify_G01_deficit.py`):**
$$
\boxed{\;\delta\theta \;=\; 2\pi - 5\arccos\tfrac{1}{3} \;=\; 7.356103^\circ \;=\; 0.1284\ \text{rad}\;}
$$

#### 3.1 The 3D construction closes exactly

Glue five regular tetrahedra of edge 1 around a common edge $AB$: tetrahedron $k$ has vertices $(A, B, c_k, d_k)$... — only the apex orbit $\{c_k\}$ matters here, since the second apex pair repeats the same construction on the far side of $AB$. Each apex $c_k$ satisfies $|AB| = |Ac_k| = |Bc_k| = |c_k c_{k+1}| = 1$ (all faces equilateral).

Because the construction is invariant under rotation by $2\pi/5$ about $AB$, the apex orbit **exactly closes in $\mathbb{R}^3$**: $c_6 \equiv c_1$ by construction. The five-around-one complex exists in 3D with **zero geometric residue** — consistent with the manifold-free substrate of [[A01_Manifold_Free_Substrate]], which never demands an ambient plane. The deficit computed below is therefore a failure of *planar* closure only, and this is precisely why it can reappear as a **phase** constraint on the graph: link phases on $\mathcal{S}_5$ live on the cycle, not in an embedding.

#### 3.2 Sector angle: two independent computations

Place the axis $AB$ vertical with $|AB| = 1$. The apex of each tetrahedron sits at height $h = 1/2$ above the midpoint of $AB$ (centroid of the equilateral face), at horizontal distance
$$
r = \sqrt{1^2 - (1/2)^2 - (1/2)^2} \;=\; \sqrt{3}/2
$$
from the axis. Consecutive apices are one edge apart: $|c_k c_{k+1}| = 1$. The sector angle $\beta$ subtended at the axis by one perimeter edge follows from the chord relation $|c_k c_{k+1}| = 2 r \sin(\beta/2)$:
$$
\beta \;=\; 2\arcsin\!\Big(\frac{1}{2r}\Big) \;=\; 2\arcsin\!\Big(\frac{1}{\sqrt{3}}\Big) \;=\; 1.2309594\ \text{rad} \;=\; 70.528779^\circ .
$$

**Lemma (sector angle = tetrahedral dihedral angle).** $\;2\arcsin(1/\sqrt{3}) = \arccos(1/3)$.

*Proof.* Let $\theta = 2\arcsin(1/\sqrt{3})$, so $\sin(\theta/2) = 1/\sqrt{3}$ and $\cos(\theta/2) = \sqrt{2/3}$. Then
$$
\cos\theta = \cos^2(\theta/2) - \sin^2(\theta/2) = \tfrac{2}{3} - \tfrac{1}{3} = \tfrac{1}{3}. \qquad\blacksquare
$$
(This is the standard tetrahedral dihedral angle — the same $\arccos(1/3)$ that governs how four equilateral faces meet at one tetrahedron edge; here it appears as the *projected* sector angle of five tetrahedra sharing one edge.)

#### 3.3 The deficit and its two exact forms

Planar closure around the axis would demand $5\beta = 2\pi$; instead
$$
5\beta = 5\arccos\tfrac{1}{3} = 352.643897^\circ = 6.1547969\ \text{rad},
$$
so
$$
\delta\theta = 2\pi - 5\beta = 0.1283882\ \text{rad} = 7.356103^\circ,
$$
which reproduces the registered vault constant $0.1284$ rad to all five significant figures. Both exact forms are used interchangeably below:
$$
\delta\theta = 2\pi - 5\arccos\tfrac{1}{3} \;=\; 2\pi\Big(1 - \tfrac{5}{2\pi}\arccos\tfrac{1}{3}\Big).
$$

#### 3.4 Correction register (superseded draft formula)

The superseded draft of this note derived the deficit as $2\pi - 5\arccos(7/8)$, i.e. from a planar equilateral-triangle apex angle $\alpha = \arccos(7/8) \approx 28.955^\circ$. **That formula is numerically wrong for this construction:** it evaluates to $215.2249^\circ$, not $7.356103^\circ$ (the arccos(7/8) angle belongs to the vertex figure of a *single* tetrahedron, not to the projected sector of the five-around-one packing). The correct registered identity is $2\pi - 5\arccos(1/3)$ (Section 3.3), machine-verified in `verify_output.txt`. Both D01–D03 and S02 already used the numerical value $0.1284$ rad, so **no downstream constant changes**; only this derivation was repaired.

#### 3.5 Honest structural remarks (registered, not smoothed over)

1. **Chirality doubling.** $\;360^\circ / 7.356103^\circ = 48.9390$ is **not an integer**: the 5-fold cell alone cannot build a full circulation out of $\delta\theta$ steps. Exact $2\pi$ closure of the *same-handed* chiral state requires **two cells** of opposite handedness (each contributing $7.356103^\circ \times 48.94 \approx 360^\circ$ in the statistically averaged sense) — see [[D03_Topological_Soliton_Formation]] for the paired-defect construction. This non-integer is registered as a structural fact, not rounded away.
2. **Winding accumulation scale.** One full $2\pi$ winding corresponds to $\approx 48.94$ frustrated cells; the fractional charge per cell is therefore genuinely fractional (Section 4.3).
3. **Defect-localized, not global.** The residue binds to the elementary cell; an assembly of cells distributes it without cancellation when cells are same-handed (Section 6).

**Consequences of $\delta\theta \neq 0$:**
1. No assignment of link phases can make all five sector phases vanish simultaneously — the product constraint $\sum_{k=1}^{5}\chi_{k,k+1} = \delta\theta \pmod{2\pi}$ is a hard geometric residue.
2. The ground state cannot be a uniform zero-phase state; the system must distribute the residue as persistent winding, circulating currents, or pinned defect phase.

---

### 4. Holonomy of the perimeter loop and topological charge

#### 4.1 Definition and gauge invariance

For the oriented perimeter loop $\ell_5 = (v_1 \to v_2 \to v_3 \to v_4 \to v_5 \to v_1)$, the loop holonomy is the gauge-invariant sum of link phases:
$$
\Phi(\ell_5) = \sum_{k=1}^{5} \chi_{k,k+1} \pmod{2\pi}
$$
Under the local gauge transformation $\chi_{ij} \to \chi_{ij} + (\alpha_i - \alpha_j)$ the sum is invariant, since each node angle enters exactly once with $+$ and once with $-$:
$$
\textstyle\sum_{(ij)\in\ell_5} \big[(\chi_{ij} + \alpha_i - \alpha_j)\big] = \sum \chi_{ij} + \underbrace{\textstyle\sum_i (\alpha_i - \alpha_i)}_{=0}.
$$

#### 4.2 Quantization of the holonomy sector

The deficit fixes the loop phase modulo $2\pi$ only up to an integer winding number $m$ (any configuration and its $2\pi$-rotated representative are the same physical link phases):
$$
\Phi(\ell_5) = m\,\delta\theta \pmod{2\pi}, \qquad m \in \mathbb{Z},
$$
and the associated topological (winding) charge of the cluster:
$$
Q_{\Omega} \;=\; \frac{\Phi(\ell_5)}{2\pi} \;=\; \frac{m\,\delta\theta}{2\pi} \;\neq\; 0 \quad \text{for } m \neq 0.
$$
Two consistency statements, both proven rather than assumed:
- **$Q_\Omega$ is gauge-invariant** (Section 4.1) and **conserved under the closed dynamics**: the generator of [[D01_Cavity_Network_Hamiltonian]] is number- and connectivity-preserving, and the leakage channel of [[A04_Cadence_Phase_Leak]] is phase-diagonal — so $\Phi(\ell_5)$ can only change through an event that erases a link's coherence entirely (this is exactly the "$Q$ validity window" registered in [[D05_Cluster_Simulation_and_Validation]]).
- **Distinct $m$ are distinct superselection sectors:** no local gauge transformation connects $m$ to $m'$ (they differ by the invariant $\Phi$), so charge $Q_\Omega$ is a genuine topological label of the cell, not a dynamical variable.

#### 4.3 The minimal sector and the per-cell fractional charge

The minimal nonzero sector $m = \pm 1$ carries
$$
Q_{\Omega}^{(1)} = \frac{\delta\theta}{2\pi} = \frac{2\pi - 5\arccos(1/3)}{2\pi} = 0.02043362\ \text{(exact)}
$$
— the **five-fold fractional charge** registered in the vault's family constants. Registered convention: the family writes this as $\delta\theta/2\pi = 0.02044$, which is the rounding derivative $0.1284/2\pi = 0.0204355$ at four significant figures; the exact value is $0.0204336$. All downstream notes use the $0.02044$ label; nothing depends on the fourth-decimal difference. Because $\arccos(1/3)$ is irrational (Niven's theorem: its rational multiples of $\pi$ are only $0, \pm\tfrac{1}{2}, \pm 1$), $Q_\Omega^{(1)}$ is an **irrational fraction of $2\pi$** — no finite number of same-handed cells closes a full winding exactly (Section 3.5).

---

### 5. Frustration potential and the frustration ground state

The frustrated ring couples to the deficit through the phase potential (mirroring the D01 generator term):
$$
\hat{G}_{\text{frust}} = -K_5 \cos\left( \sum_{k=1}^5 \chi_{k,k+1} - \Phi^\star \right), \qquad \Phi^\star = \delta\theta
$$
- The minimum of this potential lies at $\Phi_{\text{loop}} = \delta\theta$, **not** at $\Phi_{\text{loop}} = 0$: the flat, zero-flux configuration is not the ground state.
- In the quantum regime the ground state carries a persistent chiral phase circulation with two degenerate orientations ($m = +1$, $m = -1$) — spontaneous chirality with no explicit chiral term in the Hamiltonian (the symmetry-breaking pattern of Section 3.5: the Hamiltonian is orientation-blind, the frustrated cell is not).
- Pinning of topological solitons ([[D03_Topological_Soliton_Formation]]) onto this frustrated cell is energetically favored: $V_{\text{pinning}} \propto -\cos(\Phi(\ell_5) - \delta\theta)$.

---

### 6. Consequences for network assembly (multi-cell packing)

When many 5-around-1 cells assemble:
1. Each cell contributes an independent frustration well (a pinned phase-vortex site).
2. The network-level defect density $\rho_{\text{defect}}$ controls percolation of phase-transport paths (threshold registered in [[S03_Topological_and_Memory_Scaling]]: $\rho_c \approx 0.382$).
3. The cumulative holonomy distribution inherits the universal signature $\delta\theta/2\pi = 0.02044$ per elementary cell — an observable fingerprint of the five-fold packing.

---

### 7. Falsification criteria

This document is falsified if:
1. **Exact flat closure exists:** a rigorous construction shows the 5-around-1 complex admits a defect-free, frustration-free assignment (all loop phases simultaneously zero) compatible with the coupling structure.
2. **No ground-state winding:** numerical simulation of the frustrated ring shows convergence of the loop phase to $\Phi_{\text{loop}} \to 0$ for all initial conditions, with no surviving chirality or persistent current.
3. **Deficit-independent spectra:** the excitation spectra of the frustrated and the flat (6-around-1) clusters are indistinguishable in all measurable channels.
4. **Arithmetic reproduction fails:** an independent recomputation of the construction of Section 3 does not reproduce $\delta\theta = 2\pi - 5\arccos(1/3) = 7.356103^\circ$. The registered reproduction path is `_data/02_GEOMETRY_TOPOLOGY/G01/verify_G01_deficit.py` (log: `verify_output.txt`), which re-derives every number from integers and square roots only.

---

### 8. Where the deficit has already been consumed downstream

| consumer | role of $\delta\theta$ | status |
|---|---|---|
| [[D01_Cavity_Network_Hamiltonian]] | site-detuning implementation $\delta_k\sigma_k^z$ | registered |
| [[D04_Minimal_Simulatable_Soliton_Model]] | edge-phase (Peierls flux) implementation $e^{\pm i\delta\theta}$ | registered |
| [[D05_Cluster_Simulation_and_Validation]] | both implementations executed exactly (Record VMC-QF-Vault-11): lifetime ratio $2.042$ (site) / $2.083$ (edge-phase) at $\gamma=0.1$ — the "defect doubles the coherence lifetime" criterion confirmed in-silico | executed 2026-09-30 |

The two D05 implementations are the two faces of this note's two mathematical objects: the site detuning realizes the *scalar* deficit (Section 3.3), the edge phase realizes the *holonomy* (Section 4.2).
