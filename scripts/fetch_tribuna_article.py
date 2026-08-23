import urllib.request
import re

url = 'http://latribuna.com.py/lifestyle/ciencia-y-tecnologia/2026/08/22/brasil-licita-la-construccion-de-supercomputadores-para-ia/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=15) as resp:
    html = resp.read().decode('utf-8', errors='replace')

patterns = [
    r'<article[^>]*>(.*?)</article>',
    r'<div class="article-content"[^>]*>(.*?)</div>',
    r'<div class="entry-content"[^>]*>(.*?)</div>',
    r'<main[^>]*>(.*?)</main>',
]

for pattern in patterns:
    matches = re.findall(pattern, html, re.DOTALL)
    if matches:
        text = re.sub('<[^>]+>', '', matches[0])
        text = re.sub(r'\s+', ' ', text).strip()
        print(text[:3000])
        break