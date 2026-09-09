from pathlib import Path

old = '<li><strong>2024</strong> — <a href="https://gmcnet.webs.ull.es/sites/default/files/InfosheetGDFT_March.pdf" target="_blank" rel="noopener">The Geometry of Field Theories</a>, Real Colegio María Cristina, El Escorial (Madrid), satellite event of the 9th European Congress of Mathematics.</li>'
new = '<li><strong>2026</strong> — <a href="https://www.fuw.edu.pl/KMMF/GFT2026/" target="_blank" rel="noopener">2nd International Workshop on Geometric Field Theory</a>, University of Warsaw, Warsaw, 6–8 July 2026.</li>'

for filename in ['erc-profile.html', 'index.html']:
    path = Path(filename)
    text = path.read_text(encoding='utf-8')
    if old not in text:
        raise SystemExit(f'Expected old GFT entry not found in {filename}')
    path.write_text(text.replace(old, new, 1), encoding='utf-8')

print('Corrected GFT conference entry in erc-profile.html and index.html')
