"""Pre-processor for BASIC code listings

Suitable for most vintage 70s-80s dialects of BASIC,
including Applesoft, TRS-80, and Commodore

Features:
* Automatic numbering
* Upper-case conversion
* Ignore empty lines and #comments
* Concatenate lines with :line
* Symbolic labels with @name
* Aliases with `NAME
* Conditionally-excluded blocks
* Dependency graph; viewer at http://viz-js.com/

Created by Sean Gugler 2022-08-06
last revised 2022-09-16
"""
import sys
import re
import argparse
from pathlib import Path

patVar = re.compile(r'`\w+')
patLabel = re.compile(r'@+\w+')

def usage():
    parser = argparse.ArgumentParser(description = __doc__.split('\n')[0])  # extract first line of """ header
    parser.add_argument('basic', help="Input file")
    parser.add_argument('-c', '--case', action='store_true', help="Convert all lines to uppercase")
    parser.add_argument('-d', '--deps', action='store_true', help="Generate dependency graph in Graphviz DOT format")
    return parser.parse_args()

def main(infile):
    file = Path(infile)
    lines = file.read_text().split('\n')

    numbered,var,labels = pass1(lines)
    fixup,deps = pass2(numbered,var,labels)

    file.with_suffix('.txt').write_text('\n'.join(fixup)+'\n')
    if args.deps:
        file.with_suffix('.dep').write_text('\n'.join(fmt_dot(deps))+'\n')
    return 0

def round_up(n,m):
    return ((n//m)+1)*m

def pass1(raw):
    """Auto-number, and apply all pre-processing directives."""
    out = []
    var = {}
    label = {}
    disable = {}
    n = 0
    skip = False
    src = map(str.upper, raw) if args.case else raw
    for line in src:
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
            here = line
            if line[1] != '@':
                n = round_up(n,100)
            if line in label:
                raise Exception("Duplicate label " + line)
            label[line] = str(n)
        elif line.startswith('`'):
            name, value = line.split('=')
            var[name] = value
        elif line.startswith(':'):
            out[-1] += line
        else:
            if line.startswith("'"):
                line = f'REM {line[1:]}'
            out.append(f'{n} {line}')
            n += 10
    return out,var,label

def pass2(bas,var,label):
    """Fixup labels, create dependency graph"""
    dep = []
    here = 'TOP'
    def line_num(match):
        jump = match.group(0)
        dep.append(map(lambda s: s.lstrip('@'), (here, jump)))
        return label[jump]

    fixed = []
    section = {v:k for k,v in label.items()}
    for line in bas:
        n = line.split(' ',1)[0]
        here = section.get(n, here)
        line = patVar.sub (lambda m: var[m.group(0)], line)
        line = patLabel.sub (line_num, line)
        fixed.append(line)
    return fixed, dep

def fmt_dot(deps):
    """Format dependencies in DOT syntax"""
    yield 'strict digraph {'
    yield '\trankdir="LR"'
    yield '\tranksep=2'
    for a,b in deps:
        yield f'\t{a} -> {b}'
    yield '}'

if __name__ == "__main__":
    args = usage()
    sys.exit(main(args.basic))
