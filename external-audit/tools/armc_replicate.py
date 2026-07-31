#!/usr/bin/env python3
"""Independent replication of Arm C: per-round ceremony/1k and theorem/1k
densities for Circle Three (letters C3-R*) , Circle Four (C4-R*), Circle Two
(ROUND*.md ... actually circle-two repo ROUND1-3? no: Circle Two rounds are
ROUND1.md? we test), plus correlation stats. Tries both term-set variants:
full TERMS v1, and TERMS v1 minus charge/norm (per the control's correction).
"""
import re, os, glob, sys, math, itertools, collections

CEREMONY_FULL = ["seat","crossing","pin","gate","instrument","norm","charge",
                 "seal","door","ferry","admissib","bitten","crate","adjudicat"]
def cere_re(terms):
    return re.compile(r"\b(?:" + "|".join(terms) + r")\w*", re.I)

THEOREM_WORD = re.compile(r"\btheorem\b", re.I)

def measure(files, cre):
    words = cer = thm = 0
    for f in files:
        t = open(f, encoding='utf-8', errors='replace').read()
        words += len(t.split())
        cer += len(cre.findall(t))
        thm += len(THEOREM_WORD.findall(t))
    if not words: return None
    return (round(1000*cer/words,1), round(1000*thm/words,1), words)

def pearson(xs, ys):
    n = len(xs)
    mx, my = sum(xs)/n, sum(ys)/n
    cov = sum((x-mx)*(y-my) for x,y in zip(xs,ys))
    vx = sum((x-mx)**2 for x in xs); vy = sum((y-my)**2 for y in ys)
    r = cov/math.sqrt(vx*vy)
    t = r*math.sqrt((n-2)/(1-r*r))
    return r, t

def run(label, groups, terms):
    cre = cere_re(terms)
    xs, ys = [], []
    print(f"--- {label} (terms: {'full' if len(terms)==14 else 'minus charge/norm'}) ---")
    for g, files in groups:
        m = measure(files, cre)
        if m:
            print(f"  {g:9s} {m[0]:6.1f} / {m[1]:4.1f}   ({m[2]} words, {len(files)} files)")
            xs.append(m[0]); ys.append(m[1])
    if len(xs) > 2:
        r, t = pearson(xs, ys)
        kern = [x for x,y in zip(xs,ys) if y > 0]
        none = [x for x,y in zip(xs,ys) if y == 0]
        print(f"  n={len(xs)} r={r:.3f} t={t:.2f}", end="")
        if kern and none:
            print(f"  kernel-mean={sum(kern)/len(kern):.1f} none-mean={sum(none)/len(none):.1f} ratio={ (sum(none)/len(none))/(sum(kern)/len(kern)):.2f}x")
        else:
            print()
    return xs, ys

def c3_groups(base):
    L = sorted(glob.glob(base+'/letters/C3-*.md'))
    g = collections.defaultdict(list)
    for f in L:
        m = re.match(r'C3-(R\d+|POSTSEAL)-', os.path.basename(f))
        if m: g[m.group(1)].append(f)
    order = [f'R{i}' for i in range(1,12)] + ['POSTSEAL']
    return [(k, g[k]) for k in order if k in g]

def c4_groups(base):
    L = sorted(glob.glob(base+'/letters/C4-*.md'))
    g = collections.defaultdict(list)
    for f in L:
        m = re.match(r'C4-(R\d+)-', os.path.basename(f))
        if m: g[m.group(1)].append(f)
    order = [f'R{i}' for i in range(0,9)]
    return [(k, g[k]) for k in order if k in g]

c2 = '/workspace/the-workshop-circle-two'
c4 = '/workspace/the-workshop-circle-four'
minus = [t for t in CEREMONY_FULL if t not in ('charge','norm')]

for terms in (CEREMONY_FULL, minus):
    x3, y3 = run("Circle Three", c3_groups(c2), terms)
    x4, y4 = run("Circle Four", c4_groups(c4), terms)
    xs, ys = x3+x4, y3+y4
    r, t = pearson(xs, ys)
    kern = [x for x,y in zip(xs,ys) if y>0]; none=[x for x,y in zip(xs,ys) if y==0]
    print(f"POOLED n={len(xs)} r={r:.3f} t={t:.2f} kernel={sum(kern)/len(kern):.1f} none={sum(none)/len(none):.1f} ratio={(sum(none)/len(none))/(sum(kern)/len(kern)):.2f}x")
    print("="*70)
