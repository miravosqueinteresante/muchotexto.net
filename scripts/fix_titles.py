#!/usr/bin/env python3
"""Fix missing accents in article frontmatter safely."""
import pathlib, glob

articles_dir = 'C:/Users/pc/Desktop/Proyectos/muchotexto.net/_posts'
files = sorted(glob.glob(f'{articles_dir}/*.md'))

# Only safe replacements that won't corrupt other words
replacements = [
    ('mas ', 'm\u00e1s '),
    (' mas', ' m\u00e1s'),
    ('esta ', 'est\u00e1 '),
    (' esta', ' est\u00e1'),
    ('asi ', 'as\u00ed '),
    ('despues', 'despu\u00e9s'),
    ('cientifica', 'cient\u00edfica'),
    ('politica', 'pol\u00edtica'),
    ('fisica', 'f\u00edsica'),
    ('automatica', 'autom\u00e1tica'),
    ('practica', 'pr\u00e1ctica'),
    ('economica', 'econ\u00f3mica'),
    ('publica ', 'p\u00fablica '),
    ('publica,', 'p\u00fablica,'),
    ('publica.', 'p\u00fablica.'),
    ('publica?', 'p\u00fablica?'),
    ('numeros', 'n\u00fameros'),
    ('proximo', 'pr\u00f3ximo'),
    ('informatica', 'inform\u00e1tica'),
    ('educacion', 'educaci\u00f3n'),
    ('formando', 'formando'),
    ('necesita', 'necesita'),  # same with/without
]

# Separate replacements for 'ano' -> 'año' that MUST avoid 'anotacion'
def safe_replace(text):
    """Replace 'ano' with 'a\u00f1o' but not when part of 'anotacion'."""
    # Use word boundary approach
    result = []
    words = text.split(' ')
    for w in words:
        clean = w.strip(',.;:!?')
        # Replace 'ano' only if it's the whole word or at word boundary
        if clean == 'ano' or clean == 'Ano':
            w = w.replace('ano', 'a\u00f1o')
        elif clean == 'ano,' or clean == 'ano.' or clean == 'ano;' or clean == 'ano:':
            w = w.replace('ano', 'a\u00f1o')
        result.append(w)
    return ' '.join(result)

count = 0
for f in files:
    t = pathlib.Path(f).read_text(encoding='utf-8')
    original = t
    
    lines = t.split('\n')
    new_lines = []
    fm_count = 0
    
    for line in lines:
        if line.strip() == '---':
            fm_count += 1
            new_lines.append(line)
            continue
        
        if fm_count < 2 and (line.startswith('title:') or line.startswith('description:')):
            modified = line
            for old, new in replacements:
                modified = modified.replace(old, new)
            modified = safe_replace(modified)
            if modified != line:
                print(f'  [{pathlib.Path(f).name}] {line.strip()[:50]} -> {modified.strip()[:50]}')
            new_lines.append(modified)
        else:
            new_lines.append(line)
    
    result = '\n'.join(new_lines)
    if result != original:
        pathlib.Path(f).write_text(result, encoding='utf-8')
        count += 1

print(f'\nFiles updated: {count}')
