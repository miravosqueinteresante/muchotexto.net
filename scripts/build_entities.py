#!/usr/bin/env python3
"""
Build entity pages for muchotexto.net (v2 — quality rewrite).

Key improvements over v1:
- Articles matched by entity name in title + first 800 chars of body (not full body)
- Context extracted by paragraph, not arbitrary char offset
- URLs from observatory pages are accent-normalized to match deployed URLs
- Observatory entries are grouped by source page in layout
"""

import os
import re
import yaml
from datetime import datetime, timezone, timedelta
from collections import defaultdict

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS_DIR = os.path.join(REPO_DIR, "_posts")
ENTITIES_DIR = os.path.join(REPO_DIR, "entidades")
DATA_FILE = os.path.join(REPO_DIR, "_data", "entities.yml")
OBSERVATORY_PAGES = {
    "glosario": os.path.join(REPO_DIR, "glosario.markdown"),
    "cronologia": os.path.join(REPO_DIR, "cronologia.markdown"),
    "directorio": os.path.join(REPO_DIR, "directorio.markdown"),
    "regulacion": os.path.join(REPO_DIR, "regulacion.markdown"),
    "casos-de-uso": os.path.join(REPO_DIR, "casos-de-uso.markdown"),
}

PARAGUAY_TZ = timezone(timedelta(hours=-4))
BODY_SCAN_LIMIT = 800  # Only scan first N chars of body for entity mentions
MAX_RESULTS = 12


# ─── Accent normalization ────────────────────────────────────────────────

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


# ─── Frontmatter ─────────────────────────────────────────────────────────

def parse_frontmatter(content):
    content = content.lstrip('\ufeff').replace('\r\n', '\n')
    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).split('\n'):
        if ':' in line:
            key, _, val = line.partition(':')
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm


def build_post_url(fname, categories):
    date_match = re.match(r'(\d{4})-(\d{2})-(\d{2})-(.+)\.md$', fname)
    if not date_match:
        return f"/{categories.strip()}/{fname.replace('.md', '/')}"
    y, m, d, slug = date_match.groups()
    cat = categories.strip() if categories.strip() else "articulos"
    return f"/{cat}/{y}/{m}/{d}/{slug}/"


def clean_title(title_str, fallback_fname):
    if title_str and title_str != fallback_fname:
        cleaned = title_str.strip().strip('"').strip("'")
        if len(cleaned) > 5:
            return cleaned
    parts = fallback_fname.replace('.md', '').split('-')
    if len(parts) > 3 and parts[0].isdigit() and len(parts[0]) == 4:
        parts = parts[3:]
    return ' '.join(word.capitalize() for word in parts if word)


# ─── Article matching ────────────────────────────────────────────────────

def extract_paragraph_containing(body, pattern, max_len=250):
    """Extract the paragraph that contains the match."""
    m = pattern.search(body)
    if not m:
        return ""
    match_pos = m.start()
    # Find paragraph boundaries
    para_start = body.rfind('\n\n', 0, max(0, match_pos))
    para_start = para_start + 2 if para_start != -1 else 0
    para_end = body.find('\n\n', match_pos)
    para_end = para_end if para_end != -1 else min(len(body), match_pos + 300)
    snippet = body[para_start:para_end].strip()
    snippet = re.sub(r'\s+', ' ', snippet)
    snippet = re.sub(r'[#*_>`|~]', '', snippet)
    if len(snippet) > max_len:
        snippet = snippet[:snippet.rfind(' ', 0, max_len)] + "..."
    return snippet


def find_mentions_in_posts(entity_name):
    """Find articulos posts where entity name appears in title or first BODY_SCAN_LIMIT chars."""
    entity_pat = safe_pattern(entity_name)
    results = []

    for fname in sorted(os.listdir(POSTS_DIR)):
        if not fname.endswith('.md'):
            continue
        fpath = os.path.join(POSTS_DIR, fname)
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
        except UnicodeDecodeError:
            continue

        # Strip BOM before any processing
        content = content.lstrip('\ufeff')

        fm = parse_frontmatter(content)
        categories = fm.get("categories", "articulos")
        if 'articulos' not in categories:
            continue

        title = clean_title(fm.get("title", ""), fname)
        url = build_post_url(fname, categories)

        # Check: entity name in title?
        title_match = entity_pat.search(strip_accents(title))

        # Check: entity name in first N chars of body?
        body = content.split('---', 2)[-1] if content.startswith('---') else content
        body_head = strip_accents(body[:BODY_SCAN_LIMIT])
        body_match = entity_pat.search(body_head)

        if not title_match and not body_match:
            continue

        # Score: title match > body match
        score = 3 if title_match else 1

        context = extract_paragraph_containing(body, entity_pat)

        results.append({
            "title": title,
            "url": url,
            "date": fm.get("date", ""),
            "context": context,
            "score": score,
        })

    results.sort(key=lambda a: (-a["score"], a.get("date", "")))
    seen = set()
    unique = []
    for item in results:
        if item["url"] not in seen:
            seen.add(item["url"])
            unique.append(item)
    return unique[:MAX_RESULTS]


# ─── Observatory cross-references ────────────────────────────────────────

def fix_url(url):
    """Strip accents from URLs extracted from markdown (deployed URLs have no accents)."""
    if url.startswith('/'):
        return strip_accents(url)
    return url


def load_observatory_entries():
    """Extract entries from observatory pages grouped by source."""
    entries = {"glosario": [], "cronologia": [], "directorio": [],
               "regulacion": [], "casos-de-uso": []}

    patterns = {
        "glosario": re.compile(r'^\*\*(.+?)\*\*\s*[-—]\s*(.+)$', re.MULTILINE),
        "cronologia": re.compile(r'^- \*\*(\d{4})\*\*\s*[-—]\s*(.+)$', re.MULTILINE),
        "directorio": re.compile(r'^- \*\*\[(.+?)\]\((.+?)\)\*\*\s*[-—]\s*(.+)$', re.MULTILINE),
        "regulacion": re.compile(r'^- \*\*\[(.+?)\]\((.+?)\)\*\*\s*[-—]\s*(.+)$', re.MULTILINE),
        "casos-de-uso": re.compile(r'^- \*\*\[(.+?)\]\((.+?)\)\*\*\s*[-—]\s*(.+)$', re.MULTILINE),
    }

    def clean_context(text):
        """Strip markdown links and formatting from context text."""
        text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)  # [text](url) -> text
        text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)  # **bold** -> bold
        return text.strip()

    for page_name, fpath in OBSERVATORY_PAGES.items():
        if not os.path.exists(fpath):
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        body = content.split('---', 2)[-1] if content.startswith('---') else content
        pat = patterns[page_name]

        if page_name == "glosario":
            for m in pat.finditer(body):
                term = m.group(1).strip()
                definition = clean_context(m.group(2).strip())[:200]
                link_match = re.search(r'→\s*\[.+?\]\((.+?)\)', body[m.end():m.end()+400])
                url = fix_url(link_match.group(1)) if link_match else f"/{page_name}/"
                entries[page_name].append({"term": term, "url": url, "context": definition})

        elif page_name == "cronologia":
            for m in pat.finditer(body):
                year = m.group(1).strip()
                desc = clean_context(m.group(2).strip())[:200]
                link_match = re.search(r'\[(.+?)\]\((.+?)\)', desc)
                url = fix_url(link_match.group(2)) if link_match else f"/{page_name}/"
                entries[page_name].append({"label": year, "url": url, "context": desc})

        else:
            for m in pat.finditer(body):
                name = m.group(1).strip()
                url = fix_url(m.group(2).strip())
                desc = clean_context(m.group(3).strip())[:200]
                entries[page_name].append({"label": name, "url": url, "context": desc})

    return entries


def match_entity_in_observatory(entity_name, obs_entries):
    """Find observatory entries mentioning the entity name.
    - glosario/directorio: match in term/label only (avoid false positives from descriptions)
    - cronologia/regulacion/casos-de-uso: match in full text"""
    name_lower = strip_accents(entity_name).lower()
    matches = {"glosario": [], "cronologia": [], "directorio": [],
               "regulacion": [], "casos-de-uso": []}

    for page_name, entries in obs_entries.items():
        for entry in entries:
            if page_name in ("glosario", "directorio"):
                # Only match if entity name is in the entry's own name
                label = entry.get("term", entry.get("label", ""))
                if name_lower not in strip_accents(label).lower():
                    continue
            # For other pages, match in full text
            search = f"{entry.get('term', '')} {entry.get('label', '')} {entry.get('context', '')}"
            if name_lower in strip_accents(search).lower():
                matches[page_name].append(entry)
    return matches


# ─── Page generation ─────────────────────────────────────────────────────

def generate_entity_page(entity, related_articles, obs_matches):
    slug = entity["slug"]
    name = entity["name"]
    name_full = entity.get("name_full", name)
    description = entity["description"].strip()
    category = entity.get("category", "")
    now = datetime.now(PARAGUAY_TZ)
    today = now.strftime("%Y-%m-%d")

    lines = []
    lines.append("---")
    lines.append("layout: entidad")
    lines.append(f'title: "{name_full}"')
    lines.append("description: >")
    lines.append(f'  Perfil de {name} en el Observatorio de IA en Paraguay: articulos, '
                 f'leyes y fuentes verificables sobre {name_full}.')
    lines.append(f"permalink: /entidades/{slug}/")
    lines.append(f"last_modified_at: {today}")
    lines.append(f"entity_name: {name}")
    lines.append(f"entity_name_full: {name_full}")
    lines.append("entity_description: >")
    for desc_line in description.split('\n'):
        stripped = desc_line.strip()
        if stripped:
            lines.append(f"  {stripped}")
    lines.append(f"entity_category: {category}")

    if related_articles:
        lines.append("related_articles:")
        for art in related_articles:
            title_clean = art["title"].replace('"', "'")
            ctx = art.get("context", "")
            ctx = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', ctx)
            ctx = ctx.replace('"', "'").replace(":", ";")[:250]
            lines.append(f'  - title: "{title_clean}"')
            lines.append(f'    url: {art["url"]}')
            if ctx:
                lines.append(f'    context: "{ctx}"')

    laws = entity.get("related_laws", [])
    if laws:
        lines.append("entity_laws:")
        for law in laws:
            lines.append(f'  - "{law}"')

    # Observatory sections, separated by page
    obs_sections = [
        ("glosario", "Glosario", obs_matches.get("glosario", [])),
        ("cronologia", "Cronologia", obs_matches.get("cronologia", [])),
        ("directorio", "Directorio", obs_matches.get("directorio", [])),
        ("regulacion", "Regulacion", obs_matches.get("regulacion", [])),
        ("casos-de-uso", "Casos de uso", obs_matches.get("casos-de-uso", [])),
    ]
    for slug_key, label, entries in obs_sections:
        if entries:
            key = f"obs_{slug_key}"
            lines.append(f"{key}:")
            for entry in entries[:8]:
                e_label = entry.get("label", entry.get("term", "")).replace('"', "'")
                e_ctx = entry.get("context", "")
                e_ctx = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', e_ctx)
                e_ctx = e_ctx[:200].replace('"', "'")
                lines.append(f'  - label: "{e_label}"')
                lines.append(f'    url: {entry["url"]}')
                lines.append(f'    context: "{e_ctx}"')

    lines.append("---")
    lines.append("")
    if related_articles:
        lines.append(f"{len(related_articles)} articulos en el observatorio mencionan a {name}.")
        lines.append("")

    return '\n'.join(lines)


def load_entities():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    entities = load_entities()
    obs_entries = load_observatory_entries()
    os.makedirs(ENTITIES_DIR, exist_ok=True)

    generated = 0
    for entity in entities:
        slug = entity["slug"]
        name = entity["name"]

        related = find_mentions_in_posts(name)
        obs_matches = match_entity_in_observatory(name, obs_entries)

        content = generate_entity_page(entity, related, obs_matches)
        fpath = os.path.join(ENTITIES_DIR, f"{slug}.markdown")
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)

        g_count = len(obs_matches.get("glosario", []))
        c_count = len(obs_matches.get("cronologia", []))
        d_count = len(obs_matches.get("directorio", []))
        r_count = len(obs_matches.get("regulacion", []))
        cu_count = len(obs_matches.get("casos-de-uso", []))
        print(f"  {slug:25s}  {len(related):3d} arts  g:{g_count} c:{c_count} d:{d_count} r:{r_count} cu:{cu_count}")

        generated += 1

    print(f"\n{generated} entity pages generated in entidades/")
    return 0


if __name__ == "__main__":
    exit(main())
