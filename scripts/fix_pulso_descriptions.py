#!/usr/bin/env python3
import os, re, glob

base = os.path.join(os.path.dirname(__file__), '..', '_posts')
files = glob.glob(os.path.join(base, '*-pulso-paraguay.md'))

count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    lines = content.split('\n')

    if len(lines) < 16:
        continue

    tema_line = None
    first_content = None
    for i, line in enumerate(lines):
        if 'TEMA #' in line and 'DEL DÍA' in line:
            tema_line = line
            if i + 2 < len(lines):
                first_content = lines[i + 2].strip()
            break

    if not tema_line or not first_content:
        continue

    m = re.search(r'TEMA\s*#?\d+\s*DEL\s*D[IÍ]A:\s*(.+)', tema_line)
    if not m:
        continue
    topic = m.group(1).strip()
    topic = re.sub(r'^[^\wáéíóúñÁÉÍÓÚÑ]+', '', topic).strip()

    sentence = first_content.strip()
    sentence = re.sub(r'^[^\wáéíóúñÁÉÍÓÚÑ]+', '', sentence).strip()
    if not sentence.endswith('.'):
        sentence += '.'

    title_match = re.search(r'\u2014\s*(\d{1,2}\s+de\s+\w+\s+de\s+\d{4})', content)
    if title_match:
        date_fmt = title_match.group(1)
    else:
        date_fmt = ''

    desc = f'{topic}: {sentence} Pulso Paraguay \u2014 {date_fmt}.'

    lines[3] = f'description: \"{desc}\"\n'
    new_content = '\n'.join(lines)

    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(new_content)

    count += 1
    print(f'Fixed: {os.path.basename(f)}')

print(f'\nTotal: {count}')
