import os
import re
import glob

POSTS_DIR = os.path.join(os.path.dirname(__file__), "..", "_posts")


def clean_body(content: str) -> str:
    content = re.sub(r"(\S)[ \t]*\n📊 Temperatura social", r"\1\n\n📊 Temperatura social", content)

    lines = content.split("\n")
    result = []
    in_fuentes = False
    for line in lines:
        if "🔎 FUENTES CONSULTADAS HOY" in line:
            in_fuentes = True
            result.append(line)
            continue
        if in_fuentes and line.strip():
            if line.strip().startswith("- "):
                in_fuentes = False
                result.append(line)
                continue
            sources = [s.strip() for s in line.split(",") if s.strip()]
            for source in sources:
                result.append(f"- {source}")
            in_fuentes = False
            continue
        result.append(line)
    return "\n".join(result)


def fix_post(filepath: str) -> bool:
    with open(filepath, encoding="utf-8") as f:
        raw = f.read()

    parts = raw.split("---", 2)
    if len(parts) < 3:
        return False

    front = parts[0] + "---" + parts[1] + "---"
    body = parts[2]
    new_body = clean_body(body)

    if new_body == body:
        return False

    new_content = front + new_body
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


def main():
    pattern = os.path.join(POSTS_DIR, "*pulso-paraguay*.md")
    files = glob.glob(pattern)
    changed = 0
    for fp in sorted(files):
        if fix_post(fp):
            print(f"Fixed: {os.path.basename(fp)}")
            changed += 1
    print(f"\nDone. {changed}/{len(files)} files changed.")


if __name__ == "__main__":
    main()
