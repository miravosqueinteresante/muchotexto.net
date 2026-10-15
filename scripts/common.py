"""Helpers compartidos entre los scripts del observatorio."""


def read(path):
    # utf-8-sig: ignora el BOM (muchos _posts lo llevan; con utf-8 plano los
    # regex ^--- no matchean y el front matter se descarta en silencio).
    # errors=replace: tolera bytes sueltos sin romper el build.
    with open(path, "r", encoding="utf-8-sig", errors="replace") as f:
        return f.read()
