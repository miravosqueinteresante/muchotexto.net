from gemini_client import (
    clean_body,
    fallback_meta_description,
    validate_meta_description,
)

emoji = "\U0001F4C5"
body = (
    "PULSO TECH PARAGUAY\n\n"
    + emoji
    + " ENERGIA Y DATA CENTERS\n\nParques solares con baterías: el sector productivo "
    "pide más potencia eléctrica para sostener la infraestructura industrial del país. "
    "La demanda crece y la oferta no acompaña."
)
plain = clean_body(body)
assert "PULSO TECH" not in plain, plain
assert emoji not in plain, plain
assert "baterías" in plain

ok = "El sector productivo pidió más potencia eléctrica y propone parques solares con baterías para sostener la industria paraguaya."
t, problems = validate_meta_description(ok)
assert not problems, problems
assert 120 <= len(t.encode()) <= 160, len(t.encode())

for bad in (
    "Descripción corta.",
    "Esta es una descripción que termina con puntos suspensivos y no debería pasar...",
    'Con "comillas" y suficiente longitud para no fallar por tamaño pero sí por comillas.',
):
    assert validate_meta_description(bad)[1], bad

fb = fallback_meta_description(body)
assert not fb.endswith("...") and "…" not in fb, fb
assert fb.endswith("."), fb
assert 120 <= len(fb.encode()) <= 160, len(fb.encode())

print("meta_description OK")
print(fb)
