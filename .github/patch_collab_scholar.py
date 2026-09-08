from pathlib import Path

p = Path("erc-profile.html")
s = p.read_text(encoding="utf-8")

old_css = ".metric{background:#f7f9fd;border:1px solid var(--line);border-radius:12px;padding:12px}.metric strong{display:block;font-size:1.35rem;color:var(--blue)}"
new_css = ".metric{background:#f7f9fd;border:1px solid var(--line);border-radius:12px;padding:12px}.metric strong{display:block;font-size:1.35rem;color:var(--blue)}.metric-link{display:block;color:var(--ink);font-weight:400;text-decoration:none;transition:border-color .15s ease,box-shadow .15s ease,transform .15s ease}.metric-link:hover{text-decoration:none;border-color:var(--blue);box-shadow:0 4px 14px rgba(37,79,136,.12);transform:translateY(-1px)}"
if old_css not in s:
    raise SystemExit("metric CSS block not found")
s = s.replace(old_css, new_css, 1)

old_metrics = '''          <div class="metric"><strong>1423</strong>Google Scholar citations</div>
          <div class="metric"><strong>22</strong>H-index</div>'''
new_metrics = '''          <a class="metric metric-link" href="https://scholar.google.com/citations?user=XNuXyrYAAAAJ&hl=en" target="_blank" rel="noopener"><strong>1423</strong>Google Scholar citations</a>
          <a class="metric metric-link" href="https://scholar.google.com/citations?user=XNuXyrYAAAAJ&hl=en" target="_blank" rel="noopener"><strong>22</strong>H-index</a>'''
if old_metrics not in s:
    raise SystemExit("metric block not found")
s = s.replace(old_metrics, new_metrics, 1)

old_collab = '''        <p>Current visible group and collaboration network includes B.M. Zawora, J. Lange, A. Maskalaniec, T. Sobczak, X. Rivas, S. Vilariño, A. Lopez-Gordon, M. Krych and other collaborators working on k-contact geometry, reductions, field theories, integrable systems and geometric mechanics.</p>'''
new_collab = '''        <p>Current visible group and collaboration network includes <a href="https://bmzawora.github.io/" target="_blank" rel="noopener">B.M. Zawora</a>, <a href="https://orcid.org/0000-0001-6516-0839" target="_blank" rel="noopener">J. Lange</a>, A. Maskalaniec, T. Sobczak, <a href="https://xrivas.com/" target="_blank" rel="noopener">X. Rivas</a>, <a href="https://sideral.unizar.es/sideral/sid900perfilPublico.faces?id=silvia-vilarino-fernandez" target="_blank" rel="noopener">S. Vilariño</a>, <a href="https://www.alopezgordon.xyz/" target="_blank" rel="noopener">A. Lopez-Gordon</a> and other collaborators working on k-contact geometry, reductions, field theories, integrable systems and geometric mechanics.</p>'''
if old_collab not in s:
    raise SystemExit("collaborator paragraph not found")
s = s.replace(old_collab, new_collab, 1)

p.write_text(s, encoding="utf-8")
