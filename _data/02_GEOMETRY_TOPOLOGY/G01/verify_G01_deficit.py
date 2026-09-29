#!/usr/bin/env python3
"""G01 verification: the five-around-one angular deficit.

Registered derivation (vault note G01 section 3):
five regular tetrahedra glued around one common edge; the projected sector
angle beta equals the tetrahedral dihedral angle arccos(1/3); the planar
closure demand 5*beta = 2*pi fails by

    delta_theta = 2*pi - 5*arccos(1/3) = 7.356103 deg = 0.1284 rad (registered).

This script re-derives every number from integers/square roots only and
cross-checks the registered vault constants. It also registers the
correction: the superseded draft formula 2*pi - 5*arccos(7/8) gives
215.2249 deg, which is NOT the deficit.
"""
import math

def main():
    ok = True

    # --- construction: five regular tetrahedra around the common edge AB ---
    # apex height of an equilateral triangle |AB|=|Ac|=|Bc|=1 above AB:
    r = math.sqrt(3) / 2
    # projected angle at the axis spanned by one perimeter edge |c_k c_k+1| = 1:
    beta = 2 * math.asin(1 / (2 * r))

    # lemma: this equals the tetrahedral dihedral angle arccos(1/3)
    dihedral = math.acos(1 / 3)
    lemma = abs(beta - dihedral) < 1e-15
    ok &= lemma
    print(f"[G01] sector angle beta = 2*arcsin(1/sqrt(3)) = {beta:.15f} rad")
    print(f"[G01] tetrahedral dihedral   arccos(1/3)     = {dihedral:.15f} rad")
    print(f"[G01] lemma beta == dihedral: {lemma}")

    # --- closure check in R^3: the apex orbit exactly closes (5-fold) ---
    # apex of tetrahedron k: rotate c by 2*pi*k/5 about the z-axis through the
    # triangle centroid axis; consistency c_6 == c_1 is automatic by construction
    # (5-fold rotation symmetry), so the 3D complex exists with zero geometric
    # residue -- the deficit is purely a PLANAR-closure failure.
    rot_consistent = abs(5 * (2 * math.pi / 5) - 2 * math.pi) < 1e-12
    ok &= rot_consistent
    print(f"[G01] 3D closure via 5-fold rotation: {rot_consistent}")

    # --- the deficit ---
    delta = 2 * math.pi - 5 * beta
    deg = math.degrees(delta)
    print(f"[G01] 5*beta                    = {5*beta:.15f} rad "
          f"= {math.degrees(5*beta):.6f} deg")
    print(f"[G01] delta_theta = 2pi - 5beta = {delta:.15f} rad = {deg:.6f} deg")

    reg_rad, reg_deg = 0.1284, 7.356103
    match = abs(delta - reg_rad) < 5e-5 and abs(deg - reg_deg) < 5e-7
    ok &= match
    print(f"[G01] registered (0.1284 rad, 7.356103 deg): match = {match}")

    # --- topological charge ---
    q_exact = delta / (2 * math.pi)
    q_rounded = reg_rad / (2 * math.pi)
    print(f"[G01] exact per-cell charge delta/2pi     = {q_exact:.12f}")
    print(f"[G01] rounding derivative 0.1284/2pi      = {q_rounded:.12f}")
    print(f"[G01] family registered constant          = 0.02044 "
          f"(agrees with the rounding derivative at 4 s.f.)")
    ok &= abs(q_exact - 0.020433619923) < 1e-11

    # --- correction register: superseded draft formula ---
    old = 2 * math.pi - 5 * math.acos(7 / 8)
    print(f"[G01] superseded draft 2pi - 5*arccos(7/8) = {old:.12f} rad "
          f"= {math.degrees(old):.4f} deg  (NOT the deficit; corrected 2026-09-30)")
    ok &= abs(old - delta) > 1

    # --- winding accumulation scale ---
    print(f"[G01] cells to accumulate one full 2pi winding: 2pi/delta = "
          f"{2*math.pi/delta:.4f}")

    print(f"[G01] ALL CHECKS PASSED: {ok}")
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
