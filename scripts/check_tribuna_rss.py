import urllib.request
import xml.etree.ElementTree as ET

urls = [
    'https://www.latribuna.com.py/arc/outboundfeeds/rss/ciencia-y-tecnologia/',
    'https://www.latribuna.com.py/arc/outboundfeeds/rss/ciencia-y-tecnologia',
    'https://www.latribuna.com.py/feed/ciencia-y-tecnologia',
    'https://www.latribuna.com.py/feed/ciencia-y-tecnologia',
]

for url in urls:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=10) as resp:
            xml_text = resp.read().decode('utf-8', errors='replace')
            root = ET.fromstring(xml_text)
            items = list(root.iter('item'))
            print('OK:', url, '-', len(list(root.iter('item'))), 'items')
            for item in root.iter('item')[:3]:
                title = item.findtext('title', '').strip()
                link = item.findtext('link', '').strip()
                print('  ', title[:60], '... |', link)
            break
    except Exception as e:
        print('404/Error:', url, '-', e)