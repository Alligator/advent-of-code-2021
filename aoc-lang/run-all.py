import subprocess
import glob
import re
import sys

pat = re.compile(r'part[12] took (.*)')

for f in sorted(glob.glob('*.aoc'), key=lambda x: int(re.findall('\d+', x)[0])):
    cmd = f'aoc21 -b {f}'
    if '-t' in sys.argv:
        cmd = f'aoc21 -b -t {f}'
    p = subprocess.run(cmd, shell=True, capture_output=True)
    m = pat.findall(p.stdout.decode('utf-8'))
    if m:
        p1 = m[0]
        p2 = '.'
        if len(m) > 1:
            p2 = m[1]
        print(f'{f}\t{p1}\t{p2}')
    if p.returncode != 0:
        print('error! stdout:')
        print(p.stdout.decode('utf-8'))
        print('error! stderr:')
        print(p.stderr.decode('utf-8'))
