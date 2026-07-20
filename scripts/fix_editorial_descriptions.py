#!/usr/bin/env python3
import os, re, glob

base = os.path.join(os.path.dirname(__file__), '..', '_posts')
files = glob.glob(os.path.join(base, '*-editorial*.md'))

count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    lines = content.split('\n')

    if len(lines) < 10:
        continue

    body_start = 0
    for i, line in enumerate(lines):
        if line.strip() == '---':
            body_start = i + 1
            if body_start < len(lines) and lines[body_start].strip() == '---':
                body_start += 1
                break

    body = '\n'.join(lines[body_start:]).strip()
    if not body:
        continue

    plain = re.sub(r"[#*_\[\]()`>|\~\"]", "", body)
    plain = re.sub(r"\s+", " ", plain).strip()

    sentences = re.split(r'(?<=[.!?])\s+', plain)
    result = ""
    for s in sentences:
        candidate = (result + " " + s).strip() if result else s
        if len(candidate) <= 160:
            result = candidate
        else:
            if not result:
                result = s
            break

    lines[3] = f'description: \"{result}\"\n'
    new_content = '\n'.join(lines)

    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(new_content)

    count += 1
    print(f'Fixed: {os.path.basename(f)}')

print(f'\nTotal: {count}')
