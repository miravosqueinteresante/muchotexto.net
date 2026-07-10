#!/usr/bin/env python3
"""Fix accents on ia-en-paraguay.markdown - safe replacement only in body text."""
import pathlib

filepath = 'C:/Users/pc/Desktop/Proyectos/muchotexto.net/ia-en-paraguay.markdown'
t = pathlib.Path(filepath).read_text(encoding='utf-8')

# First undo all corruptions in slugs from previous failed attempts
t = t.replace('anotacion-datos', 'anotacion-datos')  # ensure clean
t = t.replace('añotacion', 'anotacion')
t = t.replace('qué-es', 'que-es')
t = t.replace('país', 'pais')

# Now apply ONLY safe replacements (body text only, not in URLs or Liquid)
replacements = [
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
    ('anotando datos', 'anotando datos'),
    ('cientifica', 'científica'),
    ('etica', 'ética'),
    ('ultimo pais', 'último país'),
    ('economia del futuro', 'economía del futuro'),
    ('infraestructura:', 'infraestructura:'),
    ('electricidad de la que', 'electricidad de la que'),  # already correct
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
    ('interesante', 'interesante'),
    ('electrico', 'eléctrico'),
    ('comercio', 'comercio'),
    ('integral', 'integral'),
    ('anuncio', 'anuncio'),
    ('noticias', 'noticias'),
]

for old, new in replacements:
    if old in t:
        t = t.replace(old, new)

pathlib.Path(filepath).write_text(t, encoding='utf-8')

# Verify no slug corruptions
bad_slugs = ['añotacion', 'qué-es', 'país-', 'último-aliado-tecnológico']
for slug in bad_slugs:
    if slug in t:
        print(f'WARNING: Corruption found: {slug}')

print('Done')
