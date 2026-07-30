#!/usr/bin/env python3
"""
Build entity pages for muchotexto.net.

Reads _data/entities.yml (curated entity list), scans _posts/ for mentions,
cross-references with observatory pages (glosario, cronologia, directorio,
regulacion, casos-de-uso), and generates individual entity pages in entidades/.

Each page is a Jekyll-compatible markdown file with rich frontmatter.
No AI, no external dependencies. Pure file analysis.
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
MAX_CONTEXT_CHARS = 280

# Accent-insensitive match helpers
ACCENT_MAP = str.maketrans(
    "áéíóúüñÁÉÍÓÚÜÑ",
    "aeiouunAEIOUUN"
)


def normalize(text):
    """Remove accents for case-insensitive, accent-insensitive matching."""
    return text.translate(ACCENT_MAP)


def safe_pattern(text):
    """Build case-insensitive, accent-insensitive regex pattern."""
    normalized = normalize(text)
    # Escape regex special chars, but allow matching original accents too
    return re.compile(re.escape(normalized), re.IGNORECASE)


def load_entities():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def parse_frontmatter(content):
    # Strip BOM and normalize line endings
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
    """Build Jekyll pretty permalink URL from filename.
    Format: /CATEGORY/YYYY/MM/DD/slug/"""
    date_match = re.match(r'(\d{4})-(\d{2})-(\d{2})-(.+)\.md$', fname)
    if not date_match:
        return f"/{categories.strip()}/{fname.replace('.md', '/')}"
    y, m, d, slug = date_match.groups()
    cat = categories.strip() if categories.strip() else "articulos"
    return f"/{cat}/{y}/{m}/{d}/{slug}/"


def clean_title(title_str, fallback_fname):
    """Return a clean human-readable title."""
    if title_str and title_str != fallback_fname:
        cleaned = title_str.strip().strip('"').strip("'")
        if len(cleaned) > 5:
            return cleaned
    # Fallback: format filename into readable title
    parts = fallback_fname.replace('.md', '').split('-')
    if len(parts) > 3 and parts[0].isdigit() and len(parts[0]) == 4:
        parts = parts[3:]  # remove YYYY-MM-DD prefix
    return ' '.join(word.capitalize() for word in parts if word)


def find_mentions_in_posts(keywords, max_results=15):
    if not keywords:
        return []

    primary_kw = keywords[0]
    primary_pat = safe_pattern(primary_kw)
    secondary_pats = [safe_pattern(kw) for kw in keywords[1:]]

    scored = []

    for fname in sorted(os.listdir(POSTS_DIR)):
        if not fname.endswith('.md'):
            continue
        fpath = os.path.join(POSTS_DIR, fname)
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
        except UnicodeDecodeError:
            continue

        fm = parse_frontmatter(content)
        categories = fm.get("categories", "articulos")

        # Only long-form articles (not Pulso or Editorial AI-generated content)
        if 'articulos' not in categories:
            continue

        title = clean_title(fm.get("title", ""), fname)
        post_url = build_post_url(fname, categories)

        score = 0
        matched_pat = None

        # Normalize content once for matching
        norm_content = normalize(content)

        if primary_pat.search(norm_content):
            score = 3
            matched_pat = primary_pat
        else:
            for pat in secondary_pats:
                if pat.search(norm_content):
                    score += 1
                    if not matched_pat:
                        matched_pat = pat

        if score == 0:
            continue

        # Extract context from body
        body = content.split('---', 2)[-1] if content.startswith('---') else content
        context = ""
        if matched_pat:
            m = matched_pat.search(body)
            if m:
                start = max(0, m.start() - 80)
                end = min(len(body), m.end() + 200)
                snippet = body[start:end].strip()
                snippet = re.sub(r'\s+', ' ', snippet)
                snippet = re.sub(r'[#*_\[\]()`]', '', snippet)
                if len(snippet) > MAX_CONTEXT_CHARS:
                    snippet = snippet[:snippet.rfind(' ', 0, MAX_CONTEXT_CHARS)] + "..."
                context = snippet

        scored.append({
            "title": title,
            "url": post_url,
            "date": fm.get("date", ""),
            "category": categories,
            "context": context,
            "score": score,
        })

    scored.sort(key=lambda a: (-a["score"], a.get("date", "")))
    seen = set()
    unique = []
    for item in scored:
        if item["url"] not in seen:
            seen.add(item["url"])
            unique.append(item)

    return unique[:max_results]


def load_observatory_entries():
    """Load all observatory pages, extracting labeled entries with URLs."""
    entries = []
    patterns = {
        "glosario": re.compile(r'^\*\*(.+?)\*\*\s*[-—]\s*(.+)$', re.MULTILINE),
        "cronologia": re.compile(r'^- \*\*(\d{4})\*\*\s*[-—]\s*(.+)$', re.MULTILINE),
        "directorio": re.compile(r'^- \*\*\[(.+?)\]\((.+?)\)\*\*\s*[-—]\s*(.+)$', re.MULTILINE),
        "regulacion": re.compile(r'^- \*\*\[(.+?)\]\((.+?)\)\*\*\s*[-—]\s*(.+)$', re.MULTILINE),
        "casos-de-uso": re.compile(r'^- \*\*\[(.+?)\]\((.+?)\)\*\*\s*[-—]\s*(.+)$', re.MULTILINE),
    }

    for page_name, fpath in OBSERVATORY_PAGES.items():
        if not os.path.exists(fpath):
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        body = content.split('---', 2)[-1] if content.startswith('---') else content

        if page_name == "glosario":
            for m in patterns["glosario"].finditer(body):
                term = m.group(1).strip()
                definition = m.group(2).strip()
                link_match = re.search(r'→\s*\[(.+?)\]\((.+?)\)', body[m.end():m.end()+300])
                entries.append({
                    "page": page_name,
                    "term": term,
                    "context": definition[:200],
                    "url": link_match.group(2) if link_match else f"/{page_name}/",
                })
        elif page_name in ("directorio", "regulacion", "casos-de-uso"):
            for m in patterns[page_name].finditer(body):
                entries.append({
                    "page": page_name,
                    "label": m.group(1).strip(),
                    "url": m.group(2).strip(),
                    "context": m.group(3).strip()[:200],
                })
        elif page_name == "cronologia":
            for m in patterns["cronologia"].finditer(body):
                year = m.group(1).strip()
                desc = m.group(2).strip()
                link_match = re.search(r'\[(.+?)\]\((/articulos/.+?)\)', desc)
                entries.append({
                    "page": page_name,
                    "label": year,
                    "context": desc[:200],
                    "url": link_match.group(2) if link_match else f"/{page_name}/",
                })

    return entries


def find_observatory_matches(entity_name, obs_entries):
    """Cross-reference entity NAME only against observatory entries.
    Uses only the primary name, not secondary keywords, to avoid false positives."""
    matches = []
    name_lower = entity_name.lower()
    for entry in obs_entries:
        search_text = f"{entry.get('term', '')} {entry.get('label', '')} {entry.get('context', '')}"
        if name_lower in search_text.lower():
            matches.append(entry)
    return matches


def extract_glossary_terms(entity_name, obs_entries):
    """Extract glossary entries matching entity name (not secondary keywords)."""
    name_lower = entity_name.lower()
    return [e for e in obs_entries if e["page"] == "glosario"
            and name_lower in (e.get("term", "") + " " + e.get("context", "")).lower()]


def yaml_multiline(text):
    """Format text as YAML literal block scalar."""
    if not text:
        return '""'
    lines = text.strip().split('\n')
    result = "|\n"
    for line in lines:
        result += f"    {line.strip()}\n"
    return result


def generate_entity_page(entity, related_articles, related_glossary, related_observatory):
    """Generate markdown content for a single entity page."""
    slug = entity["slug"]
    name = entity["name"]
    name_full = entity.get("name_full", name)
    description = entity["description"].strip()
    category = entity.get("category", "")

    now = datetime.now(PARAGUAY_TZ)
    today = now.strftime("%Y-%m-%d")

    # Frontmatter
    lines = []
    lines.append("---")
    lines.append("layout: entidad")
    lines.append(f'title: "{name_full}"')
    lines.append(f'description: >')
    lines.append(f'  Perfil de {name} en el Observatorio de IA en Paraguay: artículos, '
                 f'leyes y fuentes verificables sobre {name_full}.')
    lines.append(f"permalink: /entidades/{slug}/")
    lines.append(f"last_modified_at: {today}")
    lines.append(f"entity_name: {name}")
    lines.append(f"entity_name_full: {name_full}")
    lines.append(f"entity_description: >")
    for desc_line in description.split('\n'):
        stripped = desc_line.strip()
        if stripped:
            lines.append(f"  {stripped}")
    lines.append(f"entity_category: {category}")

    # Related articles (as YAML array of objects)
    if related_articles:
        lines.append("related_articles:")
        for art in related_articles[:15]:
            title_clean = art["title"].replace('"', "'")
            ctx_clean = art.get("context", "").replace('"', "'").replace(":", ";")[:200]
            lines.append(f'  - title: "{title_clean}"')
            lines.append(f'    url: {art["url"]}')
            if ctx_clean:
                lines.append(f'    context: "{ctx_clean}"')

    # Laws
    laws = entity.get("related_laws", [])
    if laws:
        lines.append("entity_laws:")
        for law in laws:
            law_clean = law.replace('"', "'")
            lines.append(f'  - "{law_clean}"')

    # Related glossary terms
    if related_glossary:
        lines.append("related_glossary:")
        for g in related_glossary[:5]:
            lines.append(f'  - term: "{g["term"]}"')
            lines.append(f'    url: {g["url"]}')

    # Related observatory entries
    if related_observatory:
        lines.append("related_observatory:")
        for obs in related_observatory[:10]:
            label_clean = obs.get("label", obs.get("term", "")).replace('"', "'")
            ctx_clean = obs.get("context", "")[:150].replace('"', "'")
            lines.append(f'  - label: "{label_clean}"')
            lines.append(f'    url: {obs["url"]}')
            lines.append(f'    context: "{ctx_clean}"')

    lines.append("---")
    lines.append("")

    # Article count summary
    if related_articles:
        lines.append(f"{len(related_articles)} articulos en el observatorio mencionan "
                     f"a {name}.")
        lines.append("")

    return '\n'.join(lines)


def main():
    entities = load_entities()
    obs_entries = load_observatory_entries()
    os.makedirs(ENTITIES_DIR, exist_ok=True)

    generated = 0
    for entity in entities:
        slug = entity["slug"]
        name = entity["name"]
        keywords = entity.get("keywords", [name])

        related = find_mentions_in_posts(keywords)
        obs_matches = find_observatory_matches(name, obs_entries)
        glossary_matches = extract_glossary_terms(name, obs_entries)

        # Generate page
        content = generate_entity_page(entity, related, glossary_matches, obs_matches)
        fpath = os.path.join(ENTITIES_DIR, f"{slug}.markdown")
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)

        art_count = len(related)
        glos_count = len(glossary_matches)
        obs_count = len(obs_matches)
        print(f"  {slug:25s}  {art_count:3d} arts  {glos_count} glos  {obs_count} obs")

        generated += 1

    print(f"\n{generated} entity pages generated in entidades/")
    return 0


if __name__ == "__main__":
    exit(main())
