from pathlib import Path

# ERC profile
p = Path('erc-profile.html')
text = p.read_text(encoding='utf-8')
text = text.replace('"jobTitle": "Professor at the University of Warsaw"', '"honorificPrefix": "dr hab.",\n    "jobTitle": "prof. UW"')
p.write_text(text, encoding='utf-8')

# Main page
p = Path('index.html')
text = p.read_text(encoding='utf-8')
text = text.replace('Associate Professor at the University of Warsaw. Research in differential geometry, mathematical physics, k-contact geometry, jet geometry, geometric field theory and Lie systems.', 'dr hab. Javier de Lucas Araujo, prof. UW, at the University of Warsaw. Research in differential geometry, mathematical physics, k-contact geometry, jet geometry, geometric field theory and Lie systems.')
text = text.replace('"jobTitle": "Associate Professor"', '"honorificPrefix": "dr hab.",\n  "jobTitle": "prof. UW"')
p.write_text(text, encoding='utf-8')

print('Updated formal academic title in structured metadata')
