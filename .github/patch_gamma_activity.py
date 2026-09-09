from pathlib import Path

ERC = Path('erc-profile.html')
INDEX = Path('index.html')

activity_block_erc = '''
        <h3>Selected conference organisation and network activity</h3>
        <ul class="compact-list">
          <li><strong>2024</strong> — <a href="https://www.fuw.edu.pl/KMMF/18ywgmc/index.html" target="_blank" rel="noopener">XVIII International Young Researchers Workshop in Geometry, Dynamics and Field Theory</a>, University of Warsaw, Warsaw.</li>
          <li><strong>2024</strong> — <a href="https://gmcnet.webs.ull.es/sites/default/files/InfosheetGDFT_March.pdf" target="_blank" rel="noopener">The Geometry of Field Theories</a>, Real Colegio María Cristina, El Escorial (Madrid), satellite event of the 9th European Congress of Mathematics.</li>
          <li><strong>2025</strong> — <a href="https://conference-gsi.org/gsi-2025/program/29-october-2025/" target="_blank" rel="noopener">Geometric Science of Information 2025</a>, Saint-Malo: session on geometric approaches to differential equations.</li>
          <li><strong>2026</strong> — <a href="https://www.contactgeom2026.uni.lodz.pl/" target="_blank" rel="noopener">International Workshop on k-Contact Geometry and Applications</a>, University of Łódź, 17–18 December 2026.</li>
        </ul>
'''

html = ERC.read_text(encoding='utf-8')
anchor = '''        <ul class="compact-list">
          <li><a href="https://www.fuw.edu.pl/KMMF/gamma/">Weekly online Gamma seminar</a>, with recorded talks and lecture series on the <a href="https://www.youtube.com/@GammaSeminar">Gamma Seminar YouTube channel</a>.</li>
          <li><a href="https://readinggroupoid.org/talks.html">Hybrid Reading Groupoid sessions</a> on Lie groupoids and Lie algebroids.</li>
          <li><a href="https://informatorects.uw.edu.pl/en/courses/view?prz_kod=1100-MGTP">Monographic course on Geometric Mechanics II - Field Theory</a> and student research projects.</li>
          <li>Collaborations with the <a href="https://www.urv.cat/en/">Universitat Rovira i Virgili</a> in Tarragona, UPC Barcelona, CRM Montréal and other institutions.</li>
        </ul>
'''
if activity_block_erc.strip() not in html:
    if anchor not in html:
        raise SystemExit('ERC Gamma activity anchor not found')
    html = html.replace(anchor, anchor + activity_block_erc, 1)
ERC.write_text(html, encoding='utf-8')

activity_block_index = '''
  <h3>Selected conference organisation and network activity</h3>
  <ul>
    <li><strong>2024</strong> — <a href="https://www.fuw.edu.pl/KMMF/18ywgmc/index.html" target="_blank" rel="noopener">XVIII International Young Researchers Workshop in Geometry, Dynamics and Field Theory</a>, University of Warsaw, Warsaw.</li>
    <li><strong>2024</strong> — <a href="https://gmcnet.webs.ull.es/sites/default/files/InfosheetGDFT_March.pdf" target="_blank" rel="noopener">The Geometry of Field Theories</a>, Real Colegio María Cristina, El Escorial (Madrid), satellite event of the 9th European Congress of Mathematics.</li>
    <li><strong>2025</strong> — <a href="https://conference-gsi.org/gsi-2025/program/29-october-2025/" target="_blank" rel="noopener">Geometric Science of Information 2025</a>, Saint-Malo: session on geometric approaches to differential equations.</li>
    <li><strong>2026</strong> — <a href="https://www.contactgeom2026.uni.lodz.pl/" target="_blank" rel="noopener">International Workshop on k-Contact Geometry and Applications</a>, University of Łódź, 17–18 December 2026.</li>
  </ul>
'''

index = INDEX.read_text(encoding='utf-8')
anchor_index = '''  <h3>Impact</h3>
'''
if activity_block_index.strip() not in index:
    if anchor_index not in index:
        raise SystemExit('Index Gamma activity anchor not found')
    index = index.replace(anchor_index, activity_block_index + '\n' + anchor_index, 1)
INDEX.write_text(index, encoding='utf-8')

print('Added Gamma conference activity to ERC and main profile pages')
