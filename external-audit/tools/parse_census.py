#!/usr/bin/env python3
import sys, re, collections
f = sys.argv[1]
axioms = collections.Counter()
bad = []
carriers = collections.defaultdict(list)
for line in open(f):
    line = line.strip()
    m = re.match(r"'([^']+)' depends on axioms: \[(.*)\]", line)
    if m:
        deps = tuple(sorted(d.strip() for d in m.group(2).split(',')))
        axioms[deps] += 1
        carriers[deps].append(m.group(1))
        for d in deps:
            if d not in ('propext', 'Quot.sound'):
                bad.append((m.group(1), d))
    elif "does not depend on any axioms" in line:
        axioms[('NONE',)] += 1
    elif line:
        bad.append(('UNPARSED', line[:100]))
total = sum(axioms.values())
print(f"total census lines: {total}")
for k, v in axioms.most_common():
    print(f"  {v:4d}  {k}")
print(f"VIOLATIONS (non-propext/Quot.sound axioms, or unparsed lines): {len(bad)}")
for b in bad[:15]:
    print("  ", b)
# name the Quot.sound carriers if few
qs = [k for k in carriers if 'Quot.sound' in k]
for k in qs:
    print(f"Quot.sound carriers ({k}): {len(carriers[k])}")
    for n in carriers[k][:40]:
        print("   ", n)
