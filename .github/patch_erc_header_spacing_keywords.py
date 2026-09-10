from pathlib import Path

p = Path('erc-profile.html')
text = p.read_text(encoding='utf-8')

old_css = '.badges{display:flex;flex-wrap:nowrap;gap:7px;margin:16px 0;overflow-x:auto}'
new_css = '.badges{display:flex;flex-wrap:wrap;gap:7px;margin:0;overflow:visible}.hero-keywords{margin-top:18px}.hero>.wrap{width:min(1120px,calc(100% - 48px))}'
if old_css not in text:
    raise SystemExit('Expected badges CSS not found')
text = text.replace(old_css, new_css, 1)

old_media = '@media (max-width:850px){.hero-grid,.two{grid-template-columns:1fr}.grid,.metric-row{grid-template-columns:1fr 1fr}.portrait{width:min(100%,230px);max-width:230px;height:auto;aspect-ratio:230/210;justify-self:center}}'
new_media = '@media (max-width:850px){.hero>.wrap{width:min(1120px,calc(100% - 32px))}.hero-grid,.two{grid-template-columns:1fr}.grid,.metric-row{grid-template-columns:1fr 1fr}.portrait{width:min(100%,230px);max-width:230px;height:auto;aspect-ratio:230/210;justify-self:center}.hero-keywords{margin-top:16px}}'
if old_media not in text:
    raise SystemExit('Expected responsive media query not found')
text = text.replace(old_media, new_media, 1)

old_badges = '''      <div class="badges">\n        <span class="badge">Differential equations</span>\n        <span class="badge">k-contact geometry</span>\n        <span class="badge">Jet geometry</span>\n        <span class="badge">Integrable systems</span>\n        <span class="badge">Geometric mechanics</span>\n        <span class="badge">Reduction and symmetries</span>\n      </div>\n'''
if old_badges not in text:
    raise SystemExit('Expected keyword badge block not found')
text = text.replace(old_badges, '', 1)

old_end = '''    <img class="portrait" src="BiaÅystok.jpg" alt="Javier de Lucas Araujo"/>\n  </div>\n</header>'''
new_end = '''    <img class="portrait" src="BiaÅystok.jpg" alt="Javier de Lucas Araujo"/>\n  </div>\n  <div class="wrap hero-keywords">\n    <div class="badges">\n      <span class="badge">Differential equations</span>\n      <span class="badge">k-contact geometry</span>\n      <span class="badge">Jet geometry</span>\n      <span class="badge">Integrable systems</span>\n      <span class="badge">Geometric mechanics</span>\n      <span class="badge">Reduction and symmetries</span>\n    </div>\n  </div>\n</header>'''
if old_end not in text:
    raise SystemExit('Expected hero closing block not found')
text = text.replace(old_end, new_end, 1)

p.write_text(text, encoding='utf-8')
print('Improved ERC header margins and moved keywords below hero grid')
