#!/usr/bin/env python3
"""Gate de proceso long-form: exige los artefactos y un minimo de contenido.

Uso:
    python scripts/check_longform_process.py --staged
    python scripts/check_longform_process.py --range <before> <after>
    python scripts/check_longform_process.py _posts/archivo.md

No valida la verdad de los datos; valida que el proceso deje evidencia.
La verdad sigue requiriendo fact-check humano/agente.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))


def git(*args: str) -> list[str]:
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        return []
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def changed_posts(args: argparse.Namespace) -> tuple[list[str], set[str]]:
    if args.staged:
        posts = git("diff", "--cached", "--name-only", "--diff-filter=ACM", "--", "_posts/")
        new = set(git("diff", "--cached", "--name-only", "--diff-filter=A", "--", "_posts/"))
        return posts, new
    if args.range:
        before, after = args.range
        posts = git("diff", "--name-only", "--diff-filter=ACM", before, after, "--", "_posts/")
        new = set(git("diff", "--name-only", "--diff-filter=A", before, after, "--", "_posts/"))
        return posts, new
    return args.paths, set()


def category(text: str) -> str:
    m = re.search(r"^categories:\s*(.+)$", text, re.MULTILINE)
    return m.group(1) if m else ""


def manifest_entry(post: Path) -> dict | None:
    manifest = ROOT / "_data" / "cierres.yml"
    if not manifest.exists():
        return None
    try:
        data = yaml.safe_load(manifest.read_text(encoding="utf-8")) or {}
        for entry in data.get("cierres", []):
            if entry.get("slug") == post.stem:
                return entry
    except yaml.YAMLError:
        pass
    return None


def research_dir(post: Path) -> Path:
    slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", post.stem)
    entry = manifest_entry(post)
    if entry and entry.get("research_dir"):
        return ROOT / entry["research_dir"]
    return ROOT / f"research_{slug}"


def nonempty_lines(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for line in path.read_text(encoding="utf-8", errors="ignore").splitlines() if line.strip())


def findings_chars(directory: Path) -> int:
    total = 0
    for path in directory.glob("findings_*.md"):
        total += len(path.read_text(encoding="utf-8", errors="ignore"))
    return total


def check_post(path: Path, is_new: bool, require_local: bool = True) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8", errors="ignore")
    if "articulos" not in category(text):
        return errors

    entry = manifest_entry(path)
    directory = research_dir(path)
    rel = directory.relative_to(ROOT)
    local = directory.is_dir()

    if not local:
        if require_local:
            return [f"Proceso: falta la carpeta '{rel}/'"]
        if not entry or entry.get("estado") != "completo" or entry.get("faltantes"):
            return [f"Proceso: falta '{rel}/' y el manifiesto no la registra como completa"]

    if local:
        if is_new and nonempty_lines(directory / "brief.md") < 5:
            errors.append(f"Proceso: falta '{rel}/brief.md' o tiene menos de 5 respuestas")

        minimums = {
            "research_plan.md": 3,
            "gap_report.md": 5,
            "spotcheck.md": 5,
        }
        for name, minimum in minimums.items():
            count = nonempty_lines(directory / name)
            if count < minimum:
                errors.append(f"Proceso: '{rel}/{name}' vacio o incompleto ({count} lineas utiles)")

        if findings_chars(directory) < 500:
            errors.append(f"Proceso: '{rel}/findings_*.md' vacio o demasiado corto")

    try:
        from validate_publish import check_post as validate_post, get_last_n_posts
        validation_errors, _ = validate_post(str(path), get_last_n_posts(3), require_cierre=local)
        errors.extend(f"Formato: {error}" for error in validation_errors)
    except Exception as exc:
        errors.append(f"Formato: no se pudo ejecutar validate_publish ({exc})")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--staged", action="store_true")
    group.add_argument("--range", nargs=2, metavar=("BEFORE", "AFTER"))
    parser.add_argument("paths", nargs="*")
    args = parser.parse_args()
    if not args.staged and not args.range and not args.paths:
        parser.error("indica --staged, --range o al menos un post")

    posts, new = changed_posts(args)
    errors: list[str] = []
    for raw in posts:
        path = ROOT / raw
        if path.suffix != ".md" or not path.exists():
            continue
        errors.extend(check_post(path, raw in new, require_local=not bool(args.range)))

    if errors:
        print(f"X Proceso long-form incompleto ({len(errors)} hallazgo(s)):")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("OK: proceso long-form con evidencia completa.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
