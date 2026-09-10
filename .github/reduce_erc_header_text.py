from pathlib import Path

p = Path('erc-profile.html')
text = p.read_text(encoding='utf-8')
replacements = {
    '.kicker{letter-spacing:.11em;text-transform:uppercase;font-size:.76rem;': '.kicker{letter-spacing:.11em;text-transform:uppercase;font-size:.684rem;',
    '.name{font-size:clamp(1.25rem,2.2vw,1.7rem);': '.name{font-size:clamp(1.125rem,1.98vw,1.53rem);',
    'h1{font-size:clamp(2rem,5vw,4.05rem);': 'h1{font-size:clamp(1.8rem,4.5vw,3.645rem);',
    '.lead{font-size:clamp(1.05rem,2vw,1.34rem);': '.lead{font-size:clamp(.945rem,1.8vw,1.206rem);',
    'font-size:.84rem;color:#fff;white-space:nowrap}': 'font-size:.756rem;color:#fff;white-space:nowrap}',
    '.btn{display:inline-block;padding:10px 14px;': '.btn{display:inline-block;padding:10px 14px;font-size:.9rem;',
    '@media (max-width:520px){.grid,.metric-row{grid-template-columns:1fr}h1{font-size:2.3rem}}': '@media (max-width:520px){.grid,.metric-row{grid-template-columns:1fr}h1{font-size:2.07rem}}',
}
for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f'Expected CSS fragment not found: {old}')
    text = text.replace(old, new, 1)
p.write_text(text, encoding='utf-8')
print('Reduced ERC header typography to 90 percent')
