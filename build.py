import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
exec(open(HERE / 'data.py', encoding='utf-8').read())

EXTRA = {
 'fr': dict(rot=['Des chiffres clairs.', 'Des impôts maîtrisés.', 'Une croissance accompagnée.'], pre='Avec nous,',
   vT='Notre façon de travailler',
   vals=[('Clarté', 'Des états financiers et des explications que vous comprenez, sans jargon.'),
         ('Rigueur', "Chaque dossier est révisé et concilié avant d'être remis."),
         ('Proximité', 'Un interlocuteur qui connaît votre dossier et répond rapidement.'),
         ('Efficacité', 'Des outils numériques sécurisés pour moins de papier et plus de temps pour vous.')],
   mq=['Tenue de livres', 'États financiers', 'Impôts des sociétés', 'Impôts des particuliers', 'TPS / TVQ', 'Paie', "Démarrage d'entreprise", 'Planification fiscale'],
   talk='Parlons de vos projets', scroll='Défiler'),
 'en': dict(rot=['Clear numbers.', 'Taxes under control.', 'Growth with support.'], pre='With us,',
   vT='How we work',
   vals=[('Clarity', 'Financial statements and explanations you understand, without jargon.'),
         ('Rigour', 'Every file is reviewed and reconciled before it is delivered.'),
         ('Close at hand', 'One contact who knows your file and replies quickly.'),
         ('Efficiency', 'Secure digital tools for less paper and more time for you.')],
   mq=['Bookkeeping', 'Financial statements', 'Corporate tax', 'Personal tax', 'GST / QST', 'Payroll', 'Starting a business', 'Tax planning'],
   talk="Let's talk about your projects", scroll='Scroll')}

CSS = open(HERE / 'site2.css', encoding='utf-8').read()
JS = open(HERE / 'site2.js', encoding='utf-8').read()
ARROW = '→'

def page(L):
    d = T[L]; x = EXTRA[L]
    ids = ['services', 'approche' if L == 'fr' else 'approach', 'clientele' if L == 'fr' else 'clients', 'contact']
    nav = ''.join(f'<a href="#{i}">{n}</a>' for i, n in zip(ids, d['nav']))
    heights = [22, 30, 26, 38, 34, 46, 42, 55, 50, 62, 58, 70, 66, 80, 76, 92]
    cols = ''.join(f'<i class="{"hi" if j == len(heights) - 1 else ""}" style="height:{h}%;animation-delay:{j*70}ms"></i>' for j, h in enumerate(heights))
    mq = ''.join(f'<span>{m}</span>' for m in x['mq'] * 2)
    rows = ''.join(f'<article class="row rv" data-d="{(i%4)*60}"><svg viewBox="0 0 32 32" aria-hidden="true">{ICON[k]}</svg><h3>{t}</h3><p>{p}</p><span class="go" aria-hidden="true">{ARROW}</span></article>' for i, (k, t, p) in enumerate(d['sv']))
    vals = ''.join(f'<div class="rv" data-d="{i*90}"><span class="dot"></span><h3>{a}</h3><p>{b}</p></div>' for i, (a, b) in enumerate(x['vals']))
    steps = ''.join(f'<li class="rv" data-d="{i*150}"><b>{i+1}</b><h3>{a}</h3><p>{b}</p></li>' for i, (a, b) in enumerate(d['steps']))
    cl = ''.join(f'<li class="rv" data-d="{i*60}">{c}</li>' for i, c in enumerate(d['cl']))
    hr = ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in d['hr'])
    f = d['f']
    opts = ''.join(f'<option>{t}</option>' for _, t, _ in d['sv']) + f'<option>{f["other"]}</option>'
    thanks_url = '/merci.html' if L == 'fr' else '/en/merci.html'
    words = json.dumps(x['rot'], ensure_ascii=False).replace("'", '&#39;')
    return f'''<!DOCTYPE html>
<html lang="{d['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{d['title']}</title><meta name="description" content="{d['desc']}">
<link rel="alternate" hreflang="fr-CA" href="https://boujradcpa.com/"><link rel="alternate" hreflang="en-CA" href="https://boujradcpa.com/en/">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><meta property="og:title" content="{d['title']}"><meta property="og:description" content="{d['desc']}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<header><div class="wrap nav"><a class="brand" href="{d['home']}">{wordmark()}</a><nav class="links" aria-label="Navigation">{nav}</nav>
<a class="lang" href="{d['other']}" hreflang="{'en' if L == 'fr' else 'fr'}" title="{d['otherfull']}">{d['otherlbl']}</a><a class="btn mint" href="{APP}">{d['members']}</a></div></header>
<main>
<section class="hero"><div class="cols" aria-hidden="true">{cols}</div><div class="veil"></div>
<div class="wrap in"><p class="pre">{x['pre']}</p><h1><span data-w='{words}'>{x['rot'][0]}</span></h1><p>{d['lead']}</p>
<div class="acts"><a class="btn mint" href="#contact">{d['cta1']} <span class="ar">{ARROW}</span></a><a class="btn" href="#services">{d['cta2']}</a></div></div>
<div class="cue" aria-hidden="true"><b></b>{x['scroll']}</div></section>
<div class="mq" aria-hidden="true"><div>{mq}</div></div>
<section class="band" id="services"><div class="wrap"><div class="head rv"><h2>{d['svT']}</h2><p>{d['svL']}</p></div><div class="rows">{rows}</div></div></section>
<section class="band" style="padding-top:0"><div class="wrap"><div class="head rv"><h2>{x['vT']}</h2><p>{' · '.join(a for a, _ in d['facts'])}</p></div><div class="vals">{vals}</div></div></section>
<section class="band soft" id="{ids[1]}"><div class="wrap"><div class="head rv"><h2>{d['apT']}</h2><p>{d['apL']}</p></div><ol class="steps">{steps}</ol></div></section>
<section class="band" id="{ids[2]}"><div class="wrap"><div class="head rv"><h2>{d['clT']}</h2><p>{d['facts'][2][1]}</p></div><ul class="cl">{cl}</ul></div></section>
<section class="band contact" id="contact"><div class="wrap ct">
<div class="rv"><h2>{x['talk']}</h2><p class="lead">{d['ctL']}</p>
<div class="card"><h3>{d['adrT']}</h3><address>{'<br>'.join(d['adr'])}</address><p style="margin:12px 0 0"><a class="maplink" href="{MAPS}" rel="noopener" target="_blank">{d['map']} {ARROW}</a></p></div>
<div class="card"><h3>{d['hrT']}</h3><table class="hours">{hr}</table></div></div>
<form class="rv" data-d="120" name="contact" method="POST" action="{thanks_url}" data-netlify="true" netlify-honeypot="bot-field">
<h3 class="full">{d['ctT']}</h3>
<input type="hidden" name="form-name" value="contact"><input type="hidden" name="langue" value="{L}">
<p class="hp"><label>Ne pas remplir <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
<label>{f['name']}<input id="c-nom" name="nom" required autocomplete="name"></label>
<label>{f['company']}<input id="c-ent" name="entreprise" autocomplete="organization"></label>
<label>{f['email']}<input id="c-mail" name="courriel" type="email" required autocomplete="email"></label>
<label>{f['phone']}<input id="c-tel" name="telephone" type="tel" autocomplete="tel"></label>
<label class="full">{f['svc']}<select id="c-svc" name="service">{opts}</select></label>
<label class="full">{f['msg']}<textarea id="c-msg" name="message" required></textarea></label>
<p class="note full">{f['note']}</p><div class="full"><button class="btn deep" type="submit">{f['send']} <span class="ar">{ARROW}</span></button></div></form>
</div></section></main>
<footer><div class="wrap"><div><a class="brand" href="{d['home']}">{wordmark(24)}</a><p style="margin:12px 0 0">{', '.join(d['adr'][:2])}</p></div>
<div><p style="margin:0;color:#fff">{d['hrT']}</p><p style="margin:4px 0 0">{d['hr'][0][0]} : {d['hr'][0][1]} · {d['hr'][1][0]} : {d['hr'][1][1]}</p></div>
<div><p style="margin:0"><a href="{APP}">{d['members']}</a> · <a href="{d['other']}">{d['otherfull']}</a></p><p style="margin:4px 0 0">© 2026 Boujrad CPA Inc. {d['foot']}</p></div></div></footer>
<script>{JS}</script></body></html>'''

def thanks(L):
    d = T[L]
    return f'''<!DOCTYPE html><html lang="{d['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{d['thanksT']}</title><link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet"><style>{CSS}</style></head><body>
<header class="solid"><div class="wrap nav"><a class="brand" href="{d['home']}">{wordmark()}</a><a class="btn deep" href="{APP}">{d['members']}</a></div></header>
<main class="thanks"><div class="wrap"><h1>{d['thanksT']}</h1><p style="color:#cdd6e3">{d['thanksL']}</p><p><a class="btn mint" href="{d['home']}">{d['back']}</a></p></div></main></body></html>'''

for p in OUT.glob('**/*'):
    if p.is_file(): p.unlink()
(OUT / 'en').mkdir(parents=True, exist_ok=True)
(OUT / 'index.html').write_text(page('fr'), encoding='utf-8')
(OUT / 'en' / 'index.html').write_text(page('en'), encoding='utf-8')
(OUT / 'merci.html').write_text(thanks('fr'), encoding='utf-8')
(OUT / 'en' / 'merci.html').write_text(thanks('en'), encoding='utf-8')
(OUT / 'favicon.svg').write_text(logo(64).replace('width="64" height="64" ', ''), encoding='utf-8')
(OUT / '_redirects').write_text('/intranet  ' + APP + '  302\n/espace-membres  ' + APP + '  302\n/members  ' + APP + '  302\n', encoding='utf-8')
print('ok')
