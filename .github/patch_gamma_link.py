from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')
old = 'https://users.fuw.edu.pl/~kmmf/gamma/'
new = 'https://www.fuw.edu.pl/KMMF/gamma/'
if old not in text:
    raise SystemExit('Old Gamma seminar URL not found')
text = text.replace(old, new)
path.write_text(text, encoding='utf-8')
print('Updated Gamma seminar URL in index.html')
