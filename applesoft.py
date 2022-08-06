"""Convert a quick-n-dirty text file into an Applesoft BASIC listing

Features:
Automatic numbering
Ignore empty lines and #comments
Concatenate lines with :line
Symbolic labels with @name
"""
import sys
import re
from pathlib import Path

patLabel = re.compile(r'@\w+')

def main(infile):
    file = Path(infile)
    lines = file.read_text().split('\n')
    caps,labels = pass1(lines)
    fixup = pass2(caps,labels)
    file.with_suffix('.txt').write_text('\n'.join(fixup))
    return 0

def pass1(raw):
    """Convert to BASIC syntax
    Concatenate lines, skip comments, mark labels
    """
    out = []
    label = {}
    for line in map(str.upper, raw):
        if not line or line.startswith('#'):
            continue
        elif line.startswith('@'):
            label[line] = str(len(out))
        elif line.startswith(':'):
            out[-1] += line
        else:
            if line.startswith("'"):
                line = f'REM {line[1:]}'
            out.append(line)
    return out,label

def pass2(bas,label):
    """Fixup labels"""
    for n,line in enumerate(bas):
        fix = patLabel.sub (lambda m: label[m.group(0)], line)
        yield f'{n} {fix}'

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
