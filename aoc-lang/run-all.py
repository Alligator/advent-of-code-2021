import subprocess
import glob
import re
import sys

pat = re.compile(r'part[12] took (.*)')

for f in sorted(glob.glob('*.aoc')):
    cmd = f'aoc21 -b {f}'
    if '-t' in sys.argv:
        cmd = f'aoc21 -b -t {f}'
    p = subprocess.run(cmd, shell=True, capture_output=True)
    m = pat.findall(p.stdout.decode('utf-8'))
    if m:
        p1 = m[0]
        p2 = m[1]
        print(f'{f}\t{p1}\t{p2}')
