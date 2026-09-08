from pathlib import Path

p = Path("erc-profile.html")
s = p.read_text(encoding="utf-8")
old = '''        <ul class="compact-list">
          <li>Weekly online Gamma seminar.</li>
          <li>Hybrid reading group on Lie groupoids and Lie algebroids.</li>
          <li>Monographic courses and student research projects.</li>
          <li>Collaborations with URV Tarragona, UPC Barcelona, CRM Montréal and other institutions.</li>
        </ul>'''
new = '''        <ul class="compact-list">
          <li><a href="https://www.fuw.edu.pl/KMMF/gamma/">Weekly online Gamma seminar</a>, with recorded talks and lecture series on the <a href="https://www.youtube.com/@GammaSeminar">Gamma Seminar YouTube channel</a>.</li>
          <li><a href="https://readinggroupoid.org/talks.html">Hybrid Reading Groupoid sessions</a> on Lie groupoids and Lie algebroids.</li>
          <li><a href="https://informatorects.uw.edu.pl/en/courses/view?prz_kod=1100-MGTP">Monographic course on Geometric Mechanics II - Field Theory</a> and student research projects.</li>
          <li>Collaborations with the <a href="https://www.urv.cat/en/">Universitat Rovira i Virgili</a> in Tarragona, UPC Barcelona, CRM Montréal and other institutions.</li>
        </ul>'''
if old not in s:
    raise SystemExit("Gamma environment block not found")
p.write_text(s.replace(old, new, 1), encoding="utf-8")
