from pathlib import Path

path = Path('erc-profile.html')
text = path.read_text(encoding='utf-8')
entries = [
'''          <li>J. Grabowski and J. de Lucas, <a href="https://doi.org/10.1016/j.jde.2012.08.020" target="_blank" rel="noopener"><em>Mixed superposition rules and the Riccati hierarchy</em></a>, <strong>Journal of Differential Equations 254</strong> (2013), 179–198.</li>\n''',
'''          <li>J.F. Cariñena, J. Grabowski, J. de Lucas and C. Sardón, <a href="https://doi.org/10.1016/j.jde.2014.05.040" target="_blank" rel="noopener"><em>Dirac–Lie systems and Schwarzian equations</em></a>, <strong>Journal of Differential Equations 257</strong> (2014), 2303–2340.</li>\n'''
]
for entry in entries:
    if entry not in text:
        raise SystemExit('Expected historical entry not found')
    text = text.replace(entry, '', 1)
path.write_text(text, encoding='utf-8')
print('Removed two historical JDE entries from ERC profile')
