import os, re, glob, unicodedata

posts_dir = '_posts'
pattern = os.path.join(posts_dir, '*-pulso-paraguay.md')
files = sorted(glob.glob(pattern))

def slugify(text, max_len=50):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text).strip("-")[:max_len].rstrip("-")
    return text

meses = {'01':'enero','02':'febrero','03':'marzo','04':'abril','05':'mayo','06':'junio','07':'julio','08':'agosto','09':'setiembre','10':'octubre','11':'noviembre','12':'diciembre'}

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    topic_match = re.search(r'🌡\s*TEMA\s*#1\s*DEL\s*DÍA\s*:\s*(.+?)$', content, re.MULTILINE | re.IGNORECASE)
    if not topic_match:
        topic_match = re.search(r'TEMA\s*#1\s*DEL\s*DÍA\s*:\s*(.+?)$', content, re.MULTILINE | re.IGNORECASE)

    basename = os.path.basename(fpath)
    date_part = basename[:10]

    if topic_match:
        topic = topic_match.group(1).strip()
        topic_slug = slugify(topic)
        new_name = f'{date_part}-{topic_slug}-pulso-paraguay.md'
        new_path = os.path.join(posts_dir, new_name)

        if fpath != new_path:
            os.rename(fpath, new_path)
            y, m, d = date_part.split('-')
            fecha = f'{int(d)} de {meses[m]} de {y}'
            new_title = f'Pulso Paraguay: {topic} \u2014 {fecha}'
            old_title_match = re.search(r'^title:\s*"(.+?)"', content, re.MULTILINE)
            if old_title_match and old_title_match.group(1) != new_title:
                content = content.replace(f'title: "{old_title_match.group(1)}"', f'title: "{new_title}"', 1)
            with open(new_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'OK: {basename} -> {new_name}')
        else:
            print(f'--: {basename} (no change)')
    else:
        print(f'XX: {basename} (no topic)')

print('Done!')
