from pathlib import Path

ERC = Path('erc-profile.html')
INDEX = Path('index.html')

# ERC profile: keep research keywords on one line and add Differential equations first.
text = ERC.read_text(encoding='utf-8')
old_css = '.badges{display:flex;flex-wrap:wrap;gap:9px;margin:18px 0}.badge{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.28);padding:7px 10px;border-radius:999px;font-weight:700;font-size:.92rem;color:#fff}'
new_css = '.badges{display:flex;flex-wrap:nowrap;gap:7px;margin:16px 0;overflow-x:auto}.badge{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.28);padding:6px 8px;border-radius:999px;font-weight:700;font-size:.84rem;color:#fff;white-space:nowrap}'
if old_css not in text:
    raise SystemExit('Expected badge CSS not found')
text = text.replace(old_css, new_css, 1)
old_badges = '''      <div class="badges">\n        <span class="badge">k-contact geometry</span>\n        <span class="badge">Jet geometry</span>\n        <span class="badge">Integrable systems</span>\n        <span class="badge">Geometric mechanics</span>\n        <span class="badge">Reduction and symmetries</span>\n      </div>'''
new_badges = '''      <div class="badges">\n        <span class="badge">Differential equations</span>\n        <span class="badge">k-contact geometry</span>\n        <span class="badge">Jet geometry</span>\n        <span class="badge">Integrable systems</span>\n        <span class="badge">Geometric mechanics</span>\n        <span class="badge">Reduction and symmetries</span>\n      </div>'''
if old_badges not in text:
    raise SystemExit('Expected badge block not found')
text = text.replace(old_badges, new_badges, 1)
text = text.replace('https://www.fuw.edu.pl/KMMF/gamma/', 'https://m.fuw.edu.pl/gamma-seminar.html')
ERC.write_text(text, encoding='utf-8')

# Main page: use the current Faculty of Physics Gamma seminar page as well.
text = INDEX.read_text(encoding='utf-8')
text = text.replace('https://www.fuw.edu.pl/KMMF/gamma/', 'https://m.fuw.edu.pl/gamma-seminar.html')
INDEX.write_text(text, encoding='utf-8')

print('Updated badges and Gamma seminar links')
