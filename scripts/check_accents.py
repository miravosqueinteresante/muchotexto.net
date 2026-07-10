#!/usr/bin/env python3
"""Check article frontmatter for missing accents."""
import pathlib, glob, re

files = glob.glob('C:/Users/pc/Desktop/Proyectos/muchotexto.net/_posts/2026-07-0*.md')
files += glob.glob('C:/Users/pc/Desktop/Proyectos/muchotexto.net/_posts/2026-06-*.md')
files += glob.glob('C:/Users/pc/Desktop/Proyectos/muchotexto.net/_posts/2026-05-*.md')

for f in sorted(files):
    t = pathlib.Path(f).read_text(encoding='utf-8')
    if 'categories: articulos' not in t: continue
    lines = t.split('\n')
    title = ''
    desc = ''
    for l in lines:
        if l.startswith('title: '):
            title = l[7:].strip().strip('"')
        if l.startswith('description: '):
            desc = l[13:].strip().strip('"')
    
    # Check title
    title_needs = []
    desc_needs = []
    for pattern, replacement in [
        ('mas ', 'más '),
        ('mas$', 'más'),
        ('ano', 'año'),
        ('informatica', 'informática'),
        ('educacio', 'educación'),
        ('necesita', 'necesita'),
        ('esta ', 'está '),
        ('esta$', 'está'),
        ('formando', 'formando'),
        ('asi ', 'así '),
        ('despues', 'después'),
        ('cientifica', 'científica'),
        ('tecnologia', 'tecnología'),
        ('politica', 'política'),
        ('fisica', 'física'),
        ('sistematica', 'sistemática'),
    ]:
        if pattern[:-1] in title.lower() or pattern[:-1] in desc.lower():
            pass
    
    # Just check for common missing accent patterns
    print(f'{pathlib.Path(f).name[:40]:40s}')
    print(f'  Title: {title[:60]}')
    if desc:
        print(f'  Desc:  {desc[:60]}')
