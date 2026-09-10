from pathlib import Path

p = Path('erc-profile.html')
text = p.read_text(encoding='utf-8')

old = '.hero{background:linear-gradient(135deg,#142b4d,#28639f);color:#fff;padding:36px 0 30px;border-bottom:5px solid #1c426d}.hero-grid{display:grid;grid-template-columns:1.25fr 310px;gap:28px;align-items:center}'
new = '.hero{background:linear-gradient(135deg,#142b4d,#28639f);color:#fff;padding:36px 0 30px;border-bottom:5px solid #1c426d;overflow:hidden}.hero-grid{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(220px,300px);gap:28px;align-items:center;width:100%}.hero-grid>*{min-width:0}'
if old not in text:
    raise SystemExit('Expected hero CSS not found')
text = text.replace(old, new, 1)

old = '.portrait{width:100%;max-width:300px;height:230px;object-fit:cover;border-radius:18px;box-shadow:0 14px 35px rgba(0,0,0,.28);border:3px solid rgba(255,255,255,.55)}'
new = '.portrait{display:block;width:100%;max-width:300px;height:auto;aspect-ratio:300/230;object-fit:cover;border-radius:18px;box-shadow:0 14px 35px rgba(0,0,0,.28);border:3px solid rgba(255,255,255,.55);justify-self:end}'
if old not in text:
    raise SystemExit('Expected portrait CSS not found')
text = text.replace(old, new, 1)

old = '@media (max-width:850px){.hero-grid,.two{grid-template-columns:1fr}.grid,.metric-row{grid-template-columns:1fr 1fr}.portrait{max-width:230px;height:210px}}'
new = '@media (max-width:850px){.hero-grid,.two{grid-template-columns:1fr}.grid,.metric-row{grid-template-columns:1fr 1fr}.portrait{width:min(100%,230px);max-width:230px;height:auto;aspect-ratio:230/210;justify-self:center}}'
if old not in text:
    raise SystemExit('Expected responsive CSS not found')
text = text.replace(old, new, 1)

p.write_text(text, encoding='utf-8')
print('Made ERC hero portrait responsive and overflow-safe')
