#!/usr/bin/env python3
"""
Observatorio Intel — Dashboard editorial para muchotexto.net.
Genera _planning/estado-observatorio.md con 4 secciones.
Sin dependencias externas, sin IA, solo análisis de archivos del repo.
"""

import os
import re
from datetime import datetime, timezone, timedelta
from collections import Counter

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS_DIR = os.path.join(REPO_DIR, "_posts")
PILLAR_PAGE = os.path.join(REPO_DIR, "ia-en-paraguay.markdown")
PLANNING_DIR = os.path.join(REPO_DIR, "_planning")
OUTPUT_FILE = os.path.join(PLANNING_DIR, "estado-observatorio.md")

PARAGUAY_TZ = timezone(timedelta(hours=-4))
MESES = {
    1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
    5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
    9: "setiembre", 10: "octubre", 11: "noviembre", 12: "diciembre",
}

# ─── Helpers ────────────────────────────────────────────────────────────

def parse_frontmatter(content):
    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).split('\n'):
        if ':' in line:
            key, _, val = line.partition(':')
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm


def parse_date(date_str):
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str.strip()[:10], "%Y-%m-%d")
    except ValueError:
        return None


def fmt_fecha(dt):
    return f"{dt.day} de {MESES[dt.month]} de {dt.year}"


# ─── Seccion 1: Cobertura por pilar ─────────────────────────────────────

def section1_pillar_coverage():
    with open(PILLAR_PAGE, 'r', encoding='utf-8') as f:
        # Skip frontmatter
        parts = f.read().split('---', 2)
        body = parts[-1] if len(parts) >= 3 else parts[0]

    pillars = []
    current = None
    in_prox = False

    for line in body.split('\n'):
        if line.startswith('## ') and not line.startswith('### '):
            if current:
                pillars.append(current)
            current = {'name': line[3:].strip(), 'published': 0, 'pending': 0}
            in_prox = False
            continue

        if current is None:
            continue

        if '**Próximamente:**' in line:
            in_prox = True
            continue

        if in_prox and line.strip().startswith('- ') and '[' not in line:
            current['pending'] += 1
            continue

        if line.strip().startswith('- [') or line.strip().startswith('- **['):
            current['published'] += 1
            in_prox = False

    if current:
        pillars.append(current)
    return pillars


# ─── Seccion 2: Articulos vencidos ──────────────────────────────────────

def section2_stale_articles():
    today = datetime.now(PARAGUAY_TZ).date()
    articles = []

    for fname in os.listdir(POSTS_DIR):
        if not fname.endswith('.md'):
            continue
        fpath = os.path.join(POSTS_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        fm = parse_frontmatter(content)
        if 'articulos' not in fm.get('categories', ''):
            continue

        pub = parse_date(fm.get('date', ''))
        mod = parse_date(fm.get('last_modified_at', ''))
        eff = mod if mod and (not pub or mod > pub) else pub
        if not eff:
            continue

        articles.append({
            'title': fm.get('title', fname),
            'date': eff,
            'age_days': (today - eff.date()).days,
            'has_mod': bool(fm.get('last_modified_at', '')),
        })

    articles.sort(key=lambda a: a['age_days'], reverse=True)
    return articles


# ─── Seccion 3: Temas del Pulso sin cobertura ───────────────────────────

STOPWORDS = {
    'de', 'la', 'el', 'en', 'los', 'las', 'del', 'que', 'por', 'con', 'una',
    'para', 'un', 'se', 'no', 'al', 'su', 'lo', 'como', 'mas', 'pero', 'sus',
    'le', 'ya', 'o', 'este', 'fue', 'ha', 'son', 'es', 'era', 'entre', 'hay',
    'hoy', 'sin', 'sobre', 'tras', 'hace', 'tambien', 'muy', 'segun', 'tiene',
    'han', 'que', 'y', 'a', 'e', 'otros', 'otras', 'esa', 'ese', 'eso',
    'esta', 'the', 'and', 'for',
}


def section3_pulso_tech_gaps():
    tech_items = []

    for fname in sorted(os.listdir(POSTS_DIR)):
        if not fname.endswith('.md'):
            continue
        fpath = os.path.join(POSTS_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        fm = parse_frontmatter(content)
        if fm.get('categories', '') != 'pulso-paraguay':
            continue

        lines = content.split('\n')
        for i, line in enumerate(lines):
            if 'TECNOLOG' not in line:
                continue
            # Next non-empty, non-temperature line
            for j in range(i + 1, min(i + 5, len(lines))):
                stripped = lines[j].strip()
                if not stripped or stripped.startswith('📊'):
                    continue
                if 'Sin novedades relevantes' not in stripped:
                    tech_items.append({
                        'title': stripped,
                        'date': fm.get('date', 'sin fecha'),
                    })
                break
            break

    if not tech_items:
        return [], []

    # Build bigram frequency
    bigrams = Counter()
    for item in tech_items:
        words = re.findall(r'\b[a-záéíóúñü]{3,}\b', item['title'].lower())
        for i in range(len(words) - 1):
            if words[i] not in STOPWORDS and words[i + 1] not in STOPWORDS:
                bigrams[f"{words[i]} {words[i+1]}"] += 1

    # Collect existing keywords from articulos titles and tags
    existing = set()
    for fname in os.listdir(POSTS_DIR):
        if not fname.endswith('.md'):
            continue
        with open(os.path.join(POSTS_DIR, fname), 'r', encoding='utf-8') as f:
            fm = parse_frontmatter(f.read())
        if 'articulos' not in fm.get('categories', ''):
            continue
        for word in re.findall(r'\b[a-záéíóúñü]{4,}\b', fm.get('title', '').lower()):
            existing.add(word)
        for tag in fm.get('tags', '').split():
            existing.add(tag.lower())

    gaps = [(bg, c) for bg, c in bigrams.most_common(20)
             if bg.split()[0] not in existing and bg.split()[1] not in existing]

    return tech_items, gaps[:10]


# ─── Seccion 4: Densidad del observatorio ───────────────────────────────

def _count_entries(filepath, is_glosario=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    fm = parse_frontmatter(content)
    last_mod = fm.get('last_modified_at', 'sin dato')

    if is_glosario:
        count = len(re.findall(r'^\*\*[^*].+?\*\* ', content, re.MULTILINE))
    else:
        lines = content.split('\n')
        count = 0
        in_schema = False
        for line in lines:
            if '<script' in line:
                in_schema = True; continue
            if '</script>' in line:
                in_schema = False; continue
            if in_schema:
                continue
            stripped = line.strip()
            if re.match(r'^- \**\[', stripped):
                count += 1
            elif re.match(r'^- \*\*\d{4}\*\* ', stripped):
                count += 1

    return count, last_mod


OBSERVATORIO_PAGES = [
    ("Glosario", "glosario.markdown", True),
    ("Directorio", "directorio.markdown", False),
    ("Cronologia", "cronologia.markdown", False),
    ("Regulacion", "regulacion.markdown", False),
    ("Casos de uso", "casos-de-uso.markdown", False),
]


def section4_observatory_density():
    results = []
    for name, filename, is_glosario in OBSERVATORIO_PAGES:
        fpath = os.path.join(REPO_DIR, filename)
        if not os.path.exists(fpath):
            results.append((name, 0, "no existe"))
            continue
        count, last_mod = _count_entries(fpath, is_glosario)
        results.append((name, count, last_mod))
    return results


# ─── Generar reporte ────────────────────────────────────────────────────

def generate_report():
    now = datetime.now(PARAGUAY_TZ)

    out = []
    out.append(f"# Estado del Observatorio — {fmt_fecha(now)}")
    out.append("")
    out.append("> Generado por `scripts/observatorio_intel.py`. Datos del repositorio, sin IA.")
    out.append("")

    # 1. Pilar coverage
    out.append("## 1. Cobertura por pilar")
    out.append("")
    pillars = section1_pillar_coverage()
    max_pub = max((p['published'] for p in pillars), default=1)
    out.append("| Pilar | Publicados | Pendientes | Total | Completado |")
    out.append("|---|---|---|---|---|")
    for p in pillars:
        total = p['published'] + p['pending']
        pct = int(p['published'] / total * 100) if total else 100
        bar = '█' * (pct // 10) + '░' * (10 - pct // 10)
        out.append(f"| {p['name']} | {p['published']} | {p['pending']} | {total} | {bar} {pct}% |")

    weakest = min(pillars, key=lambda p: p['published'])
    strongest = max(pillars, key=lambda p: p['published'])
    out.append("")
    out.append(f"**Pilar mas debil:** {weakest['name']} ({weakest['published']} arts). "
               f"**Mas fuerte:** {strongest['name']} ({strongest['published']}).")
    if weakest['pending'] == 0 and weakest['published'] < max_pub:
        out.append("Sin temas pendientes. Considerar abrir nuevos temas en este pilar.")
    out.append("")

    # 2. Stale articles
    out.append("## 2. Articulos con datos potencialmente vencidos")
    out.append("")
    articles = section2_stale_articles()
    no_mod = [a for a in articles if not a['has_mod']]
    with_mod = [a for a in articles if a['has_mod']]
    old = [a for a in articles if a['age_days'] > 90]

    if no_mod:
        out.append(f"**{len(no_mod)} articulos sin `last_modified_at`:**")
        out.append("")
        out.append("| Articulo | Publicado | Dias sin revision |")
        out.append("|---|---|---|")
        for a in no_mod[:10]:
            flag = ' ⚠️' if a['age_days'] > 90 else ''
            out.append(f"| {a['title'][:70]} | {a['date'].strftime('%d-%b-%Y')} | {a['age_days']} dias{flag} |")
        out.append("")

    if old:
        out.append(f"**⚠️ {len(old)} articulos con mas de 90 dias sin revision.**")
        out.append("")

    out.append(f"**{len(articles)} articulos** long-form. "
               f"{len(with_mod)} con `last_modified_at`. "
               f"{len(no_mod)} sin fecha de revision.")
    out.append("")

    # 3. Pulso tech gaps
    out.append("## 3. Temas de Tecnologia en el Pulso sin cobertura long-form")
    out.append("")
    tech_items, gaps = section3_pulso_tech_gaps()

    out.append(f"**{len(tech_items)} titulares de tecnologia extraidos** "
               f"(desde que la seccion existe, 24-jul-2026).")
    out.append("")

    if tech_items:
        out.append("Ultimos titulares:")
        out.append("")
        for item in tech_items[-5:]:
            out.append(f"- {item['date']}: {item['title']}")
        out.append("")

    if gaps:
        out.append("**Brechas detectadas** (bigramas frecuentes sin articulo long-form):")
        out.append("")
        out.append("| Tema | Menciones |")
        out.append("|---|---|")
        for bg, count in gaps:
            out.append(f"| {bg} | {count} |")
        out.append("")
        out.append("> Señales para investigar, no reemplazan el criterio editorial.")
    else:
        if tech_items:
            out.append("Todos los temas detectados tienen cobertura existente.")
    out.append("")

    # 4. Observatory density
    out.append("## 4. Densidad del observatorio")
    out.append("")
    obs = section4_observatory_density()
    out.append("| Pagina | Entradas | Ultima actualizacion |")
    out.append("|---|---|---|")
    for name, count, last_mod in obs:
        out.append(f"| {name} | {count} | {last_mod} |")
    out.append("")

    valid = [(n, c) for n, c, _ in obs if c > 0]
    if valid:
        most = max(valid, key=lambda x: x[1])
        least = min(valid, key=lambda x: x[1])
        out.append(f"**Mas densa:** {most[0]} ({most[1]}). **Menos densa:** {least[0]} ({least[1]}).")
    out.append("")

    # Footer
    out.append("---")
    out.append(f"*Generado: {now.strftime('%Y-%m-%d %H:%M')} PYT*")
    out.append("")

    report = '\n'.join(out)

    os.makedirs(PLANNING_DIR, exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"Reporte generado: {OUTPUT_FILE}")


if __name__ == '__main__':
    generate_report()
