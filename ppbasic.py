"""Pre-processor for BASIC code listings

Suitable for most vintage 70s-80s dialects of BASIC,
including Applesoft, TRS-80, and Commodore

Features:
* Automatic numbering
* Ignore empty lines and #comments
* Concatenate lines with :line
* Symbolic labels with @name
* Conditionally-excluded blocks

Created by Sean Gugler 2022-08-06
last revised 2022-08-22
"""
import sys
import re
from pathlib import Path

patLabel = re.compile(r'@+\w+')

def main(infile):
    file = Path(infile)
    lines = file.read_text().split('\n')
    caps,labels = pass1(lines)
    fixup = pass2(caps,labels)
    file.with_suffix('.txt').write_text('\n'.join(fixup)+'\n')
    return 0

def round_up(n,m):
    return ((n//m)+1)*m

def pass1(raw):
    """Convert to BASIC syntax
    Concatenate lines, skip comments, mark labels, make uppercase
    """
    out = []
    label = {}
    disable = {}
    n = 0
    skip = False
    for line in map(str.upper, raw):
        if not line or line.startswith('#'):
            continue
        elif line.startswith('!'):
            disable[line[1:]] = True
        elif line.startswith('{'):
            skip = disable.get(line[1:])
        elif line.startswith('}'):
            skip = False
        elif skip:
            continue
        elif line.startswith('@'):
            if line[1] != '@':
                n = round_up(n,100)
            label[line] = str(n)
        elif line.startswith(':'):
            out[-1] += line
        else:
            if line.startswith("'"):
                line = f'REM {line[1:]}'
            out.append(f'{n} {line}')
            n += 10
    return out,label

def pass2(bas,label):
    """Fixup labels"""
    for n,line in enumerate(bas):
        yield patLabel.sub (lambda m: label[m.group(0)], line)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
