from pathlib import Path

ERC = Path('erc-profile.html')
INDEX = Path('index.html')
SITEMAP = Path('sitemap.xml')

html = ERC.read_text(encoding='utf-8')

old_head = '''<title>Javier de Lucas Araujo | Geometric structures for PDEs and field theory</title>
<meta name="description" content="Research profile of Javier de Lucas Araujo: geometric structures for differential equations, field theory, k-contact geometry, jet geometry, integrable systems, symmetries and reduction."/>
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1"/>
<link rel="canonical" href="https://profjavierdelucas.github.io/PaginaWebPersonal/erc-profile.html"/>'''

new_head = '''<title>Javier de Lucas Araujo | Differential Geometry, k-Contact &amp; Jet Geometry</title>
<meta name="description" content="Research profile of Javier de Lucas Araujo at the University of Warsaw: differential geometry, k-contact geometry, jet bundles, geometric mechanics, Lie systems, PDEs, field theory and reduction."/>
<meta name="author" content="Javier de Lucas Araujo"/>
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"/>
<link rel="canonical" href="https://profjavierdelucas.github.io/PaginaWebPersonal/erc-profile.html"/>
<link rel="me" href="https://orcid.org/0000-0001-8643-144X"/>
<link rel="me" href="https://scholar.google.com/citations?user=XNuXyrYAAAAJ"/>
<meta property="og:type" content="profile"/>
<meta property="og:title" content="Javier de Lucas Araujo | Differential Geometry, k-Contact &amp; Jet Geometry"/>
<meta property="og:description" content="Research programme in differential geometry and mathematical physics: k-contact geometry, jet bundles, PDEs, field theory, integrability, symmetries and reduction."/>
<meta property="og:url" content="https://profjavierdelucas.github.io/PaginaWebPersonal/erc-profile.html"/>
<meta property="og:image" content="https://profjavierdelucas.github.io/PaginaWebPersonal/BiaÅystok.jpg"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="Javier de Lucas Araujo | Differential Geometry, k-Contact &amp; Jet Geometry"/>
<meta name="twitter:description" content="Research profile at the University of Warsaw: k-contact geometry, jet geometry, PDEs, geometric mechanics and field theory."/>
<meta name="twitter:image" content="https://profjavierdelucas.github.io/PaginaWebPersonal/BiaÅystok.jpg"/>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfilePage",
  "@id": "https://profjavierdelucas.github.io/PaginaWebPersonal/erc-profile.html#profile",
  "url": "https://profjavierdelucas.github.io/PaginaWebPersonal/erc-profile.html",
  "name": "Research profile of Javier de Lucas Araujo",
  "dateModified": "2026-09-09",
  "mainEntity": {
    "@type": "Person",
    "@id": "https://profjavierdelucas.github.io/PaginaWebPersonal/#person",
    "name": "Javier de Lucas Araujo",
    "alternateName": ["Javier de Lucas", "J. de Lucas"],
    "description": "Differential geometer and mathematical physicist at the University of Warsaw working on k-contact geometry, jet geometry, geometric mechanics, Lie systems, PDEs and field theory.",
    "url": "https://profjavierdelucas.github.io/PaginaWebPersonal/",
    "image": "https://profjavierdelucas.github.io/PaginaWebPersonal/BiaÅystok.jpg",
    "jobTitle": "Professor at the University of Warsaw",
    "worksFor": {
      "@type": "CollegeOrUniversity",
      "name": "University of Warsaw",
      "url": "https://www.uw.edu.pl/"
    },
    "affiliation": [
      {"@type": "CollegeOrUniversity", "name": "University of Warsaw"},
      {"@type": "ResearchOrganization", "name": "Centre de Recherches Mathématiques"}
    ],
    "sameAs": [
      "https://orcid.org/0000-0001-8643-144X",
      "https://scholar.google.com/citations?user=XNuXyrYAAAAJ",
      "https://github.com/ProfJavierDeLucas",
      "https://www.fuw.edu.pl/~delucas/"
    ],
    "knowsAbout": [
      "Differential geometry",
      "Mathematical physics",
      "k-contact geometry",
      "Jet geometry",
      "Jet bundles",
      "Partial differential equations",
      "Geometric field theory",
      "Geometric mechanics",
      "Lie systems",
      "Integrable systems",
      "Symplectic geometry",
      "Contact geometry",
      "Poisson geometry",
      "Multisymplectic geometry"
    ]
  }
}
</script>'''

if old_head not in html:
    raise SystemExit('Expected ERC head block not found')
html = html.replace(old_head, new_head, 1)

old_recent = '''    <details>
      <summary>Selected recent work</summary>
      <div class="detail-body">
        <ul>
          <li><em>Jet Bundles as Higher-Order Polarised k-Contact Manifolds</em>, arXiv:2606.09263.</li>
          <li><em>Foundations on k-contact geometry</em>, with X. Rivas and T. Sobczak, arXiv:2409.11001.</li>
          <li><em>Marsden–Meyer–Weinstein reduction for k-contact field theories</em>, with X. Rivas, S. Vilariño and B.M. Zawora, arXiv:2505.05462.</li>
          <li><em>A Guide to Applications of k-Contact Geometry in Dissipative Field Equations</em>, with J. Lange and M. Krych, arXiv:2605.13313.</li>
          <li><em>Hamilton–Jacobi theory for non-conservative field theories in the k-contact framework</em>, with J. Lange, C. Sardón and X. Rivas.</li>
        </ul>
        <p class="note">The complete publication list is available on the full information page.</p>
      </div>
    </details>'''

new_recent = old_recent + '''

    <details open id="selected-work">
      <summary>Selected landmark and highly cited work</summary>
      <div class="detail-body">
        <p class="note">This selection complements the recent-work section. It highlights two monographs, selected papers in major journals, and several publications that rank among my most cited works. The complete publication list and the current citation record are linked below.</p>

        <h3>Monographs</h3>
        <ul>
          <li>J.F. Cariñena and J. de Lucas, <a href="https://doi.org/10.4064/dm479-0-1" target="_blank" rel="noopener"><em>Lie systems: theory, generalisations, and applications</em></a>, <strong>Dissertationes Mathematicae 479</strong> (2011), 1–162.</li>
          <li>J. de Lucas and C. Sardón, <a href="https://doi.org/10.1142/q0208" target="_blank" rel="noopener"><em>A Guide to Lie Systems with Compatible Geometric Structures</em></a>, World Scientific (2020), 408 pp.</li>
        </ul>

        <h3>Selected journal articles</h3>
        <ul>
          <li>J. de Lucas and A.M. Grundland, <a href="https://doi.org/10.1007/s00029-018-0434-y" target="_blank" rel="noopener"><em>A cohomological approach to immersed submanifolds via integrable systems</em></a>, <strong>Selecta Mathematica (N.S.) 24</strong> (2018), 4749–4780.</li>
          <li>J. Grabowski and J. de Lucas, <a href="https://doi.org/10.1016/j.jde.2012.08.020" target="_blank" rel="noopener"><em>Mixed superposition rules and the Riccati hierarchy</em></a>, <strong>Journal of Differential Equations 254</strong> (2013), 179–198.</li>
          <li>J.F. Cariñena, J. Grabowski, J. de Lucas and C. Sardón, <a href="https://doi.org/10.1016/j.jde.2014.05.040" target="_blank" rel="noopener"><em>Dirac–Lie systems and Schwarzian equations</em></a>, <strong>Journal of Differential Equations 257</strong> (2014), 2303–2340.</li>
          <li>J. de Lucas and S. Vilariño, <a href="https://doi.org/10.1016/j.jde.2014.12.005" target="_blank" rel="noopener"><em>k-Symplectic Lie systems: theory and applications</em></a>, <strong>Journal of Differential Equations 258</strong> (2015), 2221–2255.</li>
          <li>A. Ballesteros, A. Blasco, F.J. Herranz, J. de Lucas and C. Sardón, <a href="https://doi.org/10.1016/j.jde.2014.12.031" target="_blank" rel="noopener"><em>Lie–Hamilton systems on the plane: properties, classification and applications</em></a>, <strong>Journal of Differential Equations 258</strong> (2015), 2873–2907.</li>
          <li>A.M. Grundland and J. de Lucas, <a href="https://doi.org/10.1016/j.jde.2017.02.038" target="_blank" rel="noopener"><em>A Lie systems approach to the Riccati hierarchy and partial differential equations</em></a>, <strong>Journal of Differential Equations 263</strong> (2017), 299–337.</li>
          <li>X. Gràcia, J. de Lucas, X. Rivas and N. Román-Roy, <a href="https://doi.org/10.1007/s13398-024-01632-w" target="_blank" rel="noopener"><em>On Darboux theorems for geometric structures induced by closed forms</em></a>, <strong>RACSAM 118</strong> (2024), article 131.</li>
        </ul>

        <h3>Further high-citation landmarks</h3>
        <ul>
          <li>J.F. Cariñena, J. de Lucas and M.F. Rañada, <a href="https://doi.org/10.3842/SIGMA.2008.031" target="_blank" rel="noopener"><em>Recent Applications of the Theory of Lie Systems in Ermakov Systems</em></a>, <strong>SIGMA 4</strong> (2008), 031.</li>
          <li>J.F. Cariñena, J. de Lucas and C. Sardón, <a href="https://doi.org/10.1142/S0219887813500473" target="_blank" rel="noopener"><em>Lie–Hamilton systems: theory and applications</em></a>, <strong>International Journal of Geometric Methods in Modern Physics 10</strong> (2013), 1350047.</li>
          <li>A. Ballesteros, J.F. Cariñena, F.J. Herranz, J. de Lucas and C. Sardón, <a href="https://doi.org/10.1088/1751-8113/46/28/285203" target="_blank" rel="noopener"><em>From constants of motion to superposition rules for Lie–Hamilton systems</em></a>, <strong>Journal of Physics A 46</strong> (2013), 285203.</li>
        </ul>

        <p class="note"><a href="https://scholar.google.com/citations?user=XNuXyrYAAAAJ&hl=en" target="_blank" rel="noopener">Google Scholar profile and current citation record</a> · <a href="index.html#publications">Complete publication list</a></p>
      </div>
    </details>'''

if old_recent not in html:
    raise SystemExit('Expected recent-work block not found')
html = html.replace(old_recent, new_recent, 1)
ERC.write_text(html, encoding='utf-8')

index = INDEX.read_text(encoding='utf-8')
old_nav = '''        <li><a href="#cv">CV</a></li>
        <li><a href="#publications">Publications</a></li>'''
new_nav = '''        <li><a href="erc-profile.html">Research profile</a></li>
        <li><a href="#cv">CV</a></li>
        <li><a href="#publications">Publications</a></li>'''
if old_nav not in index:
    raise SystemExit('Expected index navigation block not found')
index = index.replace(old_nav, new_nav, 1)
INDEX.write_text(index, encoding='utf-8')

sitemap = SITEMAP.read_text(encoding='utf-8')
sitemap = sitemap.replace('<lastmod>2026-09-06</lastmod>', '<lastmod>2026-09-09</lastmod>', 1)
entry = '''  <url>
    <loc>https://profjavierdelucas.github.io/PaginaWebPersonal/erc-profile.html</loc>
    <lastmod>2026-09-09</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.95</priority>
  </url>
'''
if 'erc-profile.html</loc>' not in sitemap:
    sitemap = sitemap.replace('</urlset>', entry + '</urlset>')
SITEMAP.write_text(sitemap, encoding='utf-8')

print('Patched erc-profile.html, index.html and sitemap.xml')
