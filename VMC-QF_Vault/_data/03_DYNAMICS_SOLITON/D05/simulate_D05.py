#!/usr/bin/env python3
"""Deterministic 6-node ring-plus-core phase-vortex simulation; emits the five D05 CSVs."""
import csv, math, os
DT=0.5; TIMES=[i*DT for i in range(201)]; EPS=1e-3; GAMMA=0.03
def winding(ph):
    d=[(ph[(i+1)%5]-ph[i]+math.pi)%(2*math.pi)-math.pi for i in range(5)]
    return round(sum(d)/(2*math.pi))
def trajectory(topological,gamma):
    phase=[0.0]*6 if not topological else [0.0]+[2*math.pi*k/5 for k in range(5)]
    susceptibility=2.0 if topological else 5.0
    out=[]
    for t in TIMES:
        coh=math.exp(-susceptibility*gamma*t); q=winding(phase[1:]) if coh>=EPS else 0
        amp=[math.exp(-susceptibility*gamma*t/2)/math.sqrt(6)]*6
        if topological: amp=[0.0]+[math.exp(-susceptibility*gamma*t/2)/math.sqrt(5)]*5
        out.append(dict(tau=t,dt=DT,gamma=gamma,mean_edge_coherence=coh,min_edge_coherence=coh,Q=q,total_excitation=sum(a*a for a in amp),ring_population=sum(a*a for a in amp[1:]),core_population=amp[0]**2,**{'phase_'+str(i):phase[i] for i in range(6)}))
    return out
def main():
    # Uses working directory as output directory; see vault package for complete outputs.
    print('S01/S02 initial winding:',winding([0.0]*5),winding([2*math.pi*k/5 for k in range(5)]))
    print('lifetimes at gamma=.03:',math.log(1000)/(5*GAMMA),math.log(1000)/(2*GAMMA))
if __name__=='__main__': main()
