#!/usr/bin/env python3
"""Find truncated editorial titles and fix them."""
import pathlib, glob

posts = sorted(glob.glob('C:/Users/pc/Desktop/Proyectos/muchotexto.net/_posts/2026-07-0*-editorial*.md'), reverse=True)

for f in posts[:5]:
    t = pathlib.Path(f).read_text(encoding='utf-8')
    lines = t.split('\n')
    title_line = ''
    for i, l in enumerate(lines):
        if l.startswith('title: '):
            title_line = l
            title = l[7:].strip().strip('"')
            break
    
    name = pathlib.Path(f).name
    print(f'{name}  |  {len(title)} chars')
    if len(title) > 70:
        print(f'  LONG: {title}')
