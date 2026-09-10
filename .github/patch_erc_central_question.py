from pathlib import Path

p = Path('erc-profile.html')
text = p.read_text(encoding='utf-8')
old = 'The central question is whether modern contact-type and jet-type geometries can become a structural language for differential equations, field theories, transformations, reductions and integrability phenomena.'
new = 'The central question is how modern differential geometric structures can provide a structural language for differential equations, field theories, transformations, reductions and integrability phenomena, while opening new avenues for physical applications.'
if old not in text:
    raise SystemExit('Expected central-question sentence not found')
text = text.replace(old, new, 1)
p.write_text(text, encoding='utf-8')
print('Updated central research question')
