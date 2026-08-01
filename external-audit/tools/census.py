#!/usr/bin/env python3
"""Independent axiom-census builder: strips comments, finds every theorem
(with namespace context), appends `#print axioms` for each into a copy."""
import re, sys

src_path, out_path = sys.argv[1], sys.argv[2]
src = open(src_path).read()

def strip_comments(s):
    out = []; i = 0; depth = 0
    while i < len(s):
        if s.startswith('/-', i): depth += 1; i += 2; continue
        if depth and s.startswith('-/', i): depth -= 1; i += 2; continue
        if depth: i += 1; continue
        if s.startswith('--', i):
            j = s.find('\n', i); i = len(s) if j < 0 else j; continue
        out.append(s[i]); i += 1
    return ''.join(out)

code = strip_comments(src)
names = []; stack = []
thm_re = re.compile(r"\s*(?:private\s+)?(?:theorem|lemma)\s+([\w.']+)")
ns_re = re.compile(r"\s*namespace\s+([\w.]+)")
end_re = re.compile(r"\s*end\s+([\w.]+)\s*$")
for line in code.split('\n'):
    m = ns_re.match(line)
    if m: stack.append(m.group(1)); continue
    m = end_re.match(line)
    if m and stack and stack[-1] == m.group(1): stack.pop(); continue
    m = thm_re.match(line)
    if m: names.append('.'.join(stack + [m.group(1)]))

print(f"{len(names)} theorems found in {src_path}")
with open(out_path, 'w') as fh:
    fh.write(src + '\n')
    for n in names:
        fh.write(f'#print axioms {n}\n')
