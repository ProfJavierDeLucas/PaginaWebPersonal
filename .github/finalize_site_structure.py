from pathlib import Path

ROOT = 'https://profjavierdelucas.github.io/PaginaWebPersonal/'
DETAILED = ROOT + 'detailed.html'

# Preserve the current detailed page before replacing index.html.
old_index = Path('index.html').read_text(encoding='utf-8')
erc = Path('erc-profile.html').read_text(encoding='utf-8')

# --- Detailed page ---------------------------------------------------------
detailed = old_index
# Make the detailed page explicitly subordinate for search engines / sharing.
detailed = detailed.replace(
    '<link rel="canonical" href="https://profjavierdelucas.github.io/PaginaWebPersonal/"/>',
    f'<link rel="canonical" href="{DETAILED}"/>',
    1,
)
detailed = detailed.replace(
    '<meta property="og:url" content="https://profjavierdelucas.github.io/PaginaWebPersonal/"/>',
    f'<meta property="og:url" content="{DETAILED}"/>',
    1,
)
detailed = detailed.replace(
    '<li><a href="erc-profile.html">Research profile</a></li>',
    '<li><a href="index.html">Research profile</a></li>',
    1,
)

# Add PDF links to the recent talks for which an unambiguous slide deck is available.
pdf_style = 'style="color:blue; text-decoration:none; font-weight:600; margin-left:8px;" target="_blank" rel="noopener"'
talk_replacements = {
    'Invited talk in the XXXIV Fall Workshop on Geometric and Physics, Tarragona, Spain, 1-9/4-9-2026.<br/>':
        f'Invited talk in the XXXIV Fall Workshop on Geometric and Physics, Tarragona, Spain, 1-9/4-9-2026. <a href="https://drive.google.com/file/d/1QS6ZaUyvtIMdo77mKrMEz_0jB_53vte4/view?usp=drivesdk" {pdf_style}>[PDF]</a><br/>',
    'Invited talk in the XLIII International Workshop on Geometric Methods in Physics, Białystok, 29-VI/4-VII-2026<br/>':
        f'Invited talk in the XLIII International Workshop on Geometric Methods in Physics, Białystok, 29-VI/4-VII-2026 <a href="https://drive.google.com/file/d/1Gqj0rW6Jkxohv7DpDxmDKqgHZJM0-TS4/view?usp=drivesdk" {pdf_style}>[PDF]</a><br/>',
    'Gamma seminar, University of Warsaw, October 23rd 2025, Warsaw, Poland<br/>':
        f'Gamma seminar, University of Warsaw, October 23rd 2025, Warsaw, Poland <a href="https://drive.google.com/file/d/1M3_Krz3wj8ar_tOummYPa9d3DoQ7mz96/view?usp=drivesdk" {pdf_style}>[PDF]</a><br/>',
}
for old, new in talk_replacements.items():
    if old not in detailed:
        raise SystemExit(f'Expected talk line not found: {old}')
    detailed = detailed.replace(old, new, 1)

Path('detailed.html').write_text(detailed, encoding='utf-8')

# --- Polished profile becomes the root index ------------------------------
main = erc
main = main.replace(
    '<link rel="canonical" href="https://profjavierdelucas.github.io/PaginaWebPersonal/erc-profile.html"/>',
    f'<link rel="canonical" href="{ROOT}"/>',
    1,
)
main = main.replace(
    '<meta property="og:url" content="https://profjavierdelucas.github.io/PaginaWebPersonal/erc-profile.html"/>',
    f'<meta property="og:url" content="{ROOT}"/>',
    1,
)
main = main.replace(
    '"@id": "https://profjavierdelucas.github.io/PaginaWebPersonal/erc-profile.html#profile"',
    '"@id": "https://profjavierdelucas.github.io/PaginaWebPersonal/#profile"',
    1,
)
main = main.replace(
    '"url": "https://profjavierdelucas.github.io/PaginaWebPersonal/erc-profile.html"',
    '"url": "https://profjavierdelucas.github.io/PaginaWebPersonal/"',
    1,
)
main = main.replace('"dateModified": "2026-09-09"', '"dateModified": "2026-09-10"', 1)
main = main.replace('href="index.html">Full information page</a>', 'href="detailed.html">Full information page</a>', 1)
main = main.replace(
    '<summary>Publications, CV, theses, talks and links</summary>',
    '<summary>Publications, CV, theses, talks, teaching and links</summary>',
    1,
)
main = main.replace(
    'Complete publication, supervision and activity records are available on the full information page and in the detailed curriculum.',
    'Complete publication, supervision, teaching and activity records are available on the detailed information page and in the detailed curriculum.',
    1,
)
# The former full-page links must now target the subordinate detailed page.
main = main.replace('href="index.html#', 'href="detailed.html#')
# Add an explicit teaching entry, reusing the existing teaching-materials section on the detailed page.
needle = '          <li><a href="detailed.html#links">Useful links</a></li>'
if needle not in main:
    raise SystemExit('Expected Useful links item not found in main profile')
main = main.replace(
    needle,
    '          <li><a href="detailed.html#links">Teaching materials</a></li>\n' + needle,
    1,
)
Path('index.html').write_text(main, encoding='utf-8')

# Keep the old ERC URL alive, but make it a redirect to the new canonical root.
redirect = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Javier de Lucas Araujo | Research profile</title>
<link rel="canonical" href="https://profjavierdelucas.github.io/PaginaWebPersonal/"/>
<meta http-equiv="refresh" content="0; url=index.html"/>
<script>window.location.replace('index.html');</script>
</head>
<body>
<p>This research profile is now the main page. <a href="index.html">Continue to Javier de Lucas Araujo's homepage</a>.</p>
</body>
</html>
'''
Path('erc-profile.html').write_text(redirect, encoding='utf-8')

# Update the sitemap: root is canonical main page, detailed page is subordinate,
# and the redirecting ERC URL is omitted.
sitemap = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://profjavierdelucas.github.io/PaginaWebPersonal/</loc>
    <lastmod>2026-09-10</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://profjavierdelucas.github.io/PaginaWebPersonal/detailed.html</loc>
    <lastmod>2026-09-10</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://profjavierdelucas.github.io/PaginaWebPersonal/AboutMe.html</loc>
    <lastmod>2026-09-06</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://profjavierdelucas.github.io/PaginaWebPersonal/Curric-Eng.pdf</loc>
    <lastmod>2026-09-06</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
</urlset>
'''
Path('sitemap.xml').write_text(sitemap, encoding='utf-8')

print('Promoted polished profile to index.html; preserved detailed page and updated links/SEO.')
