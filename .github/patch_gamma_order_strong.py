from pathlib import Path

p = Path('erc-profile.html')
text = p.read_text(encoding='utf-8')

old_collab = '          <li>Collaborations with the <a href="https://www.urv.cat/en/">Universitat Rovira i Virgili</a> in Tarragona, UPC Barcelona, CRM Montréal and other institutions.</li>'
new_collab = '          <li><strong>Strong collaborations</strong> with the <a href="https://www.urv.cat/en/">Universitat Rovira i Virgili</a> in Tarragona, UPC Barcelona, CRM Montréal and other institutions.</li>'
if old_collab not in text:
    raise SystemExit('Expected collaborations line not found')
text = text.replace(old_collab, new_collab, 1)

old_conf = '''          <li><strong>2024</strong> — <a href="https://www.fuw.edu.pl/KMMF/18ywgmc/index.html" target="_blank" rel="noopener">XVIII International Young Researchers Workshop in Geometry, Dynamics and Field Theory</a>, University of Warsaw, Warsaw.</li>
          <li><strong>2026</strong> — <a href="https://www.fuw.edu.pl/KMMF/GFT2026/" target="_blank" rel="noopener">2nd International Workshop on Geometric Field Theory</a>, University of Warsaw, Warsaw, 6–8 July 2026.</li>
          <li><strong>2025</strong> — <a href="https://conference-gsi.org/gsi-2025/program/29-october-2025/" target="_blank" rel="noopener">Geometric Science of Information 2025</a>, Saint-Malo: session on geometric approaches to differential equations.</li>
          <li><strong>2026</strong> — <a href="https://www.contactgeom2026.uni.lodz.pl/" target="_blank" rel="noopener">International Workshop on k-Contact Geometry and Applications</a>, University of Łódź, 17–18 December 2026.</li>'''
new_conf = '''          <li><strong>2024</strong> — <a href="https://www.fuw.edu.pl/KMMF/18ywgmc/index.html" target="_blank" rel="noopener">XVIII International Young Researchers Workshop in Geometry, Dynamics and Field Theory</a>, University of Warsaw, Warsaw.</li>
          <li><strong>2025</strong> — <a href="https://conference-gsi.org/gsi-2025/program/29-october-2025/" target="_blank" rel="noopener">Geometric Science of Information 2025</a>, Saint-Malo: session on geometric approaches to differential equations.</li>
          <li><strong>2026</strong> — <a href="https://www.fuw.edu.pl/KMMF/GFT2026/" target="_blank" rel="noopener">2nd International Workshop on Geometric Field Theory</a>, University of Warsaw, Warsaw, 6–8 July 2026.</li>
          <li><strong>2026</strong> — <a href="https://www.contactgeom2026.uni.lodz.pl/" target="_blank" rel="noopener">International Workshop on k-Contact Geometry and Applications</a>, University of Łódź, 17–18 December 2026.</li>'''
if old_conf not in text:
    raise SystemExit('Expected conference block not found')
text = text.replace(old_conf, new_conf, 1)

p.write_text(text, encoding='utf-8')
print('Updated Gamma collaborations wording and conference order')
