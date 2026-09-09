from pathlib import Path

NEW = 'https://users.fuw.edu.pl/~kmmf/gamma/'
OLD_URLS = [
    'https://m.fuw.edu.pl/gamma-seminar.html',
    'https://www.fuw.edu.pl/KMMF/gamma/'
]

for filename in ['erc-profile.html', 'index.html']:
    path = Path(filename)
    text = path.read_text(encoding='utf-8')
    old_text = text
    for old in OLD_URLS:
        text = text.replace(old, NEW)
    if text == old_text:
        print(f'No Gamma URL change needed in {filename}')
    else:
        path.write_text(text, encoding='utf-8')
        print(f'Updated Gamma URL in {filename}')
