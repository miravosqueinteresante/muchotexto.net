#!/usr/bin/env python3
"""Fix accents in all _posts/ markdown files - safe replacement only in body text."""

import pathlib
import re

POSTS_DIR = pathlib.Path('C:/Users/pc/Desktop/Proyectos/muchotexto.net/_posts')

# Replacements: (wrong, correct) - only body text, not URLs/slugs
REPLACEMENTS = [
    ('Guia Completa 2026', 'Guía Completa 2026'),
    ('Guia completa', 'Guía completa'),
    ('esta en el mapa', 'está en el mapa'),
    ('tecnologia ajena', 'tecnología ajena'),
    ('partidas mas', 'partidas más'),
    ('tablero tecnologico', 'tablero tecnológico'),
    ('America Latina', 'América Latina'),
    ('economia digital', 'economía digital'),
    ('analisis en profundidad', 'análisis en profundidad'),
    ('investigacion de', 'investigación de'),
    ('Infraestructura y energia', 'Infraestructura y energía'),
    ('ventaja mas obvia', 'ventaja más obvia'),
    ('veces mas electricidad', 'veces más electricidad'),
    ('mas barata', 'más barata'),
    ('Sudamerica', 'Sudamérica'),
    ('combinacion es', 'combinación es'),
    ('energia renovable', 'energía renovable'),
    ('ultimo', 'último'),
    ('Taiwan', 'Taiwán'),
    ('diplomatico', 'diplomático'),
    ('petroleo', 'petróleo'),
    ('mas alla', 'más allá'),
    ('detras de cada', 'detrás de cada'),
    ('cientifica', 'científica'),
    ('etica', 'ética'),
    ('ultimo pais', 'último país'),
    ('economia del futuro', 'economía del futuro'),
    ('energia que alimenta', 'energía que alimenta'),
    ('geopolitica', 'geopolítica'),
    ('regulacion', 'regulación'),
    ('Itaipu', 'Itaipú'),
    ('Yacyreta', 'Yacyretá'),
    ('Acaray', 'Acaray'),
    ('hidroelectrica', 'hidroeléctrica'),
    ('mineria de criptoactivos', 'minería de criptoactivos'),
    ('maximo de 5', 'máximo de 5'),
    ('apertura electrica', 'apertura eléctrica'),
    ('red de transmision', 'red de transmisión'),
    ('proximamente:', 'próximamente:'),
    ('tecnologia aplicada', 'tecnología aplicada'),
    ('cultura, filosofia', 'cultura, filosofía'),
    ('filosofia y futuro', 'filosofía y futuro'),
    ('identidad digital', 'identidad digital'),
    ('reflexion filosofica', 'reflexión filosófica'),
    ('electrico', 'eléctrico'),
    ('comercio', 'comercio'),
    ('integral', 'integral'),
    ('anuncio', 'anuncio'),
    ('noticias', 'noticias'),
    ('Paso Pe', 'Paso Pe'),
    ('PasoPe', 'Paso Pe'),
    ('PASOPE', 'Paso Pe'),
    ('Mburuvicha Roga', 'Mburuvicha Róga'),
    ('Santiago Pena', 'Santiago Peña'),
    ('Santiago Pena Palacios', 'Santiago Peña Palacios'),
    ('Peter Thiel', 'Peter Thiel'),  # already correct but ensure
    ('Palantir Technologies', 'Palantir Technologies'),
    ('Founders Fund', 'Founders Fund'),
    ('Mburuvicha Roga', 'Mburuvicha Róga'),
    ('Yguazu', 'Yguazú'),
    ('Yguazu Digital', 'Yguazú Digital'),
    ('ITAIPU', 'Itaipú'),
    ('YACYRETA', 'Yacyretá'),
    ('ACARAY', 'Acaray'),
    ('HIDROELECTRICA', 'Hidroeléctrica'),
    ('MINERIA', 'Minería'),
    ('MAXIMO', 'Máximo'),
    ('APERTURA ELECTRICA', 'Apertura Eléctrica'),
    ('TRANSMISION', 'Transmisión'),
    ('PROXIMAMENTE', 'Próximamente'),
    ('TECNOLOGIA', 'Tecnología'),
    ('FILOSOFIA', 'Filosofía'),
    ('ETICA', 'Ética'),
    ('ULTIMO', 'Último'),
    ('MAQUINA', 'Máquina'),
    ('INTEGRAL', 'Integral'),
    ('ELECTRICO', 'Eléctrico'),
    ('COMERCIO', 'Comercio'),
    ('INTEGRAL', 'Integral'),
    ('ANUNCIO', 'Anuncio'),
    ('NOTICIAS', 'Noticias'),
]

def strip_accents(text):
    """Remove accents from text (used for URL matching, never for display)."""
    replacements = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u', 'ñ': 'n',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U', 'Ü': 'U', 'Ñ': 'N',
    }
    result = text
    for accented, plain in replacements.items():
        result = result.replace(accented, plain)
    return result

def safe_pattern(text):
    """Case-insensitive AND accent-insensitive regex pattern."""
    normalized = strip_accents(text)
    return re.compile(re.escape(normalized), re.IGNORECASE)

def fix_file(filepath):
    """Fix accents in a single markdown file (body text only, not front matter/URLs)."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return 0, 0

    content = content.lstrip('\ufeff')
    
    # Split front matter and body
    fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return 0, 0
    
    front_matter = fm_match.group(0)
    body = content[len(front_matter):]
    
    changes = 0
    for wrong, correct in REPLACEMENTS:
        # Case-insensitive, accent-insensitive replacement in body only
        pattern = safe_pattern(wrong)
        matches = list(pattern.finditer(body))
        if matches:
            # Replace with correct version
            for m in matches:
                start, end = m.span()
                body = body[:start] + correct + body[end:]
                changes += 1
    
    if changes > 0:
        new_content = front_matter + body
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
    
    return changes, 0

def main():
    posts = list(POSTS_DIR.glob('*.md'))
    print(f'Procesando {len(posts)} archivos en _posts/...')
    
    total_changes = 0
    files_changed = 0
    
    for filepath in posts:
        changes, _ = fix_file(filepath)
        if changes > 0:
            files_changed += 1
            total_changes += changes
            print(f'  OK {filepath.name}: {changes} correcciones')
    
    print(f'\nTotal: {files_changed} archivos modificados, {total_changes} correcciones aplicadas')
    return files_changed, total_changes

if __name__ == '__main__':
    main()