# Guides pratiques (chroniques) : pages /guides/ du site public. Appelé par build.py.
import shutil, html as H

GCSS = '''
.gmain{padding:120px 0 80px}.gmain .wrap{max-width:860px}.gmain h1{font:700 clamp(30px,4vw,44px)/1.15 'Space Grotesk',sans-serif;margin:0 0 12px}
.gmain .lede{color:var(--mute);font-size:19px;margin:0 0 28px}.crumb{font-size:14px;color:var(--mute);margin-bottom:18px}.crumb a{color:var(--deep)}
.gmain h2{font:700 24px/1.25 'Space Grotesk',sans-serif;margin:40px 0 12px}.gmain h3{font-size:18px;margin:26px 0 8px}
.gsteps{counter-reset:s;list-style:none;padding:0;margin:0}.gsteps>li{counter-increment:s;position:relative;padding:0 0 22px 52px}
.gsteps>li::before{content:counter(s);position:absolute;left:0;top:0;width:34px;height:34px;border-radius:50%;background:var(--deep);color:#fff;display:grid;place-items:center;font-weight:600;font-size:15px}
.gsteps>li b{display:block;margin-bottom:2px}.shot{display:block;max-width:100%;border:1px solid var(--line);border-radius:12px;box-shadow:0 8px 30px rgba(11,22,38,.08);margin:12px 0 6px}
.tip{background:#fbf4e4;border-left:4px solid var(--mint);border-radius:8px;padding:12px 16px;margin:18px 0}.need{background:var(--soft);border-radius:12px;padding:16px 20px;margin:18px 0}
.need ul{margin:6px 0 0;padding-left:20px}.src{font-size:15px;color:var(--mute);border-top:1px solid var(--line);margin-top:40px;padding-top:16px}.src a{color:var(--deep)}
.gcards{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px;margin-top:20px}
.gcard{display:block;border:1px solid var(--line);border-radius:14px;padding:20px;color:inherit;text-decoration:none;transition:border-color .2s,transform .2s}
.gcard:hover{border-color:var(--deep);transform:translateY(-2px)}.gcard small{color:var(--deep);font-weight:600;text-transform:uppercase;letter-spacing:.06em;font-size:12px}
.gcard h2{font-size:20px;margin:6px 0 6px}.gcard p{margin:0;color:var(--mute);font-size:15px}
.gmain a{color:var(--deep)}.gmain .btn{color:#fff}
'''

def step(t, body, img=None, alt=''):
    return f'<li><b>{t}</b>{body}' + (f'<img class="shot" src="img/{img}" alt="{H.escape(alt)}" loading="lazy" width="1100">' if img else '') + '</li>'

APPURL = 'https://app.boujradcpa.com'

GUIDES = [
 dict(slug='portail-client', cat='Notre plateforme', titre='Utiliser le portail client de Boujrad CPA',
  resume='Créer votre compte, envoyer vos documents d’impôt, suivre votre entreprise et payer vos acomptes et vos taxes.',
  corps=f'''
<p class="lede">Le portail client est l’endroit sécurisé pour nous transmettre vos renseignements et vos documents. Rien ne passe par courriel : vos pièces sont chiffrées et conservées au Canada.</p>
<h2>Créer votre compte</h2><ol class="gsteps">
{step('Ouvrez le portail', f'<p>Allez à <a href="{APPURL}/portail.html">app.boujradcpa.com/portail.html</a>, ou cliquez sur <em>Connexion</em> puis <em>Portail client</em> en haut de notre site.</p>')}
{step('Cliquez sur « Créer un compte »', '<p>Inscrivez votre nom, votre courriel et un mot de passe d’au moins 8 caractères.</p>', 'portail-1-compte.png', 'Formulaire de création de compte du portail')}
{step('Confirmez votre courriel', '<p>Ouvrez le courriel de confirmation et cliquez sur le lien. Vous pouvez ensuite vous connecter en tout temps.</p>')}
</ol>
<div class="tip"><strong>Mot de passe oublié?</strong> Entrez votre courriel sur la page de connexion, puis cliquez sur « Mot de passe oublié? » : un lien de réinitialisation vous est envoyé.</div>
<h2>Impôts personnels : votre déclaration en trois étapes</h2><ol class="gsteps">
{step('Choisissez l’année et votre situation', '<p><em>Nouveau client</em> si c’est votre première année avec nous, <em>Client existant</em> si nous avons déjà préparé votre déclaration : vous indiquez alors seulement ce qui a changé.</p>', 'portail-2-accueil.png', 'Choix nouveau client ou client existant')}
{step('Remplissez le formulaire', '<p>Les champs marqués d’un astérisque sont requis. Si vous faites votre déclaration avec votre conjoint, ses renseignements sont dans le même formulaire : il n’a pas besoin de compte.</p>', 'portail-3-formulaire.png', 'Formulaire des impôts personnels')}
{step('Déposez tous vos documents en une seule fois', '<p>La liste des documents à prévoir s’adapte à vos réponses. Glissez vos fichiers (PDF ou photos) dans la zone de dépôt, puis envoyez votre dossier.</p>')}
</ol>
<h2>Espace Entreprise</h2><ol class="gsteps">
{step('Entrez votre code d’invitation', '<p>Nous vous remettons un code pour chaque entreprise. Onglet <em>Entreprise</em>, entrez le code, puis cliquez sur <em>Accéder</em>. Vous pouvez ajouter plusieurs entreprises au même compte.</p>', 'portail-4-code.png', 'Saisie du code d’invitation')}
{step('Consultez ce qui est à payer', '<p>Quand nous préparons une déclaration de taxes ou d’impôt, vous recevez un courriel. Le montant, la date limite et le code de paiement sont dans <em>À payer et documents du cabinet</em>. Une fois le paiement fait à votre institution financière, cliquez sur <em>J’ai fait le paiement</em> : nous sommes avisés.</p>', 'portail-5-payer.png', 'Documents à payer dans l’espace Entreprise')}
{step('Déposez vos documents de la période', '<p>Onglet <em>Déposer des documents</em> : choisissez la période (relevés bancaires, factures), déposez tout, puis cliquez sur <em>J’ai terminé</em>.</p>', 'portail-6-depot.png', 'Dépôt de documents par période')}
{step('Factures, échéancier et messages', '<p>Retrouvez vos factures, les prochaines dates limites de votre entreprise, et écrivez-nous dans <em>Messages</em> (avec pièces jointes au besoin).</p>')}
</ol>
<h2>Questionnaires de service</h2>
<p>Pour certains mandats (constitution d’une société, allocations pour enfants, pensions de retraite, succession, etc.), nous vous envoyons un lien vers un questionnaire. Il s’ouvre dans votre portail : répondez aux questions et déposez chaque pièce demandée à l’endroit prévu. Vos réponses sont enregistrées au fur et à mesure; cliquez sur <em>Envoyer au cabinet</em> quand tout est complet.</p>
<img class="shot" src="img/portail-7-questionnaire.png" alt="Questionnaire de constitution de société" loading="lazy" width="1100">
<div class="tip"><strong>Sécurité.</strong> Ne nous envoyez jamais de numéro d’assurance sociale ni de documents d’identité par courriel. Utilisez toujours le portail.</div>
<p style="margin-top:28px"><a class="btn deep" href="{APPURL}/portail.html">Aller au portail client</a></p>'''),

 dict(slug='compte-arc', cat='Gouvernement du Canada', titre='Créer votre compte de l’ARC (Mon dossier)',
  resume='Consulter vos avis de cotisation, vos feuillets et vos prestations en ligne auprès de l’Agence du revenu du Canada.',
  corps='''
<p class="lede">Mon dossier vous donne accès en tout temps à vos avis de cotisation, à vos feuillets (T4, T5…), à vos droits de cotisation REER et CELI, et au suivi de vos prestations (allocation canadienne pour enfants, crédit pour la TPS).</p>
<div class="need"><strong>À avoir sous la main</strong><ul><li>Votre numéro d’assurance sociale (NAS)</li><li>Votre date de naissance et votre code postal actuel</li><li>Votre déclaration de revenus de l’an dernier ou de cette année : un montant vous sera demandé</li><li>Une pièce d’identité avec photo émise par le gouvernement (passeport, permis de conduire ou carte d’identité provinciale), si vous voulez un accès immédiat</li></ul></div>
<h2>Les étapes</h2><ol class="gsteps">
<li><b>Allez à la page de connexion de l’ARC</b><p>Cherchez « compte de l’ARC » ou utilisez le lien plus bas, puis choisissez <em>Mon dossier</em>.</p></li>
<li><b>Choisissez une façon de vous connecter</b><p>Le plus simple : un <em>partenaire de connexion</em>, c’est-à-dire les accès de votre banque en ligne. Vous pouvez aussi créer un ID utilisateur et un mot de passe de l’ARC.</p></li>
<li><b>Entrez vos renseignements personnels</b><p>NAS, date de naissance, code postal et le montant demandé tiré de votre déclaration de revenus.</p></li>
<li><b>Vérifiez votre identité</b><p>Deux options : le <em>service de vérification des documents</em> (vous photographiez votre pièce d’identité avec votre téléphone : l’accès complet est immédiat), ou un <em>code de sécurité de l’ARC</em> envoyé par la poste à l’adresse au dossier, en général dans un délai de 10 jours ouvrables.</p></li>
<li><b>Si vous avez choisi le code par la poste</b><p>Connectez-vous de nouveau quand vous le recevez et entrez-le avant sa date d’expiration. En attendant, votre accès à Mon dossier est limité.</p></li>
<li><b>Ajoutez votre courriel et le dépôt direct</b><p>Pour recevoir les avis par courriel et vos remboursements et prestations directement dans votre compte bancaire.</p></li>
</ol>
<div class="tip"><strong>Vous avez déménagé?</strong> Le code de sécurité est envoyé à l’adresse que l’ARC a dans votre dossier. Faites d’abord corriger votre adresse, sinon le code ira à l’ancienne.</div>
<h2>Nous autoriser comme représentant</h2>
<p>Une fois inscrit, vous pouvez autoriser Boujrad CPA Inc. à consulter votre dossier : nous pourrons alors répondre à l’ARC pour vous et récupérer vos feuillets. Dans Mon dossier, allez au menu <em>Profil</em>, choisissez l’option pour autoriser un représentant, puis entrez le numéro que nous vous fournirons. Écrivez-nous dans le portail pour l’obtenir.</p>
<div class="src"><strong>Sources officielles</strong> · <a href="https://www.canada.ca/fr/agence-revenu/services/services-electroniques/services-ouverture-session-arc.html" rel="noopener">Se connecter à son compte de l’ARC</a> · <a href="https://www.canada.ca/fr/agence-revenu/services/services-electroniques/services-ouverture-session-arc/aide-services-ouverture-session-arc/verification-identite.html" rel="noopener">Vérification de votre identité</a> · <a href="https://www.canada.ca/fr/agence-revenu/services/impot/particuliers/programmes-educatifs/utiliser-mon-dossier.html" rel="noopener">Leçon de l’ARC : utiliser Mon dossier</a></div>'''),

 dict(slug='mon-dossier-revenu-quebec', cat='Gouvernement du Québec', titre='Accéder à Mon dossier de Revenu Québec',
  resume='Voir vos avis de cotisation du Québec, vos relevés et vos remboursements, et faire vos démarches en ligne.',
  corps='''
<p class="lede">Mon dossier pour les citoyens vous permet de consulter vos avis de cotisation, vos relevés (relevé 1, relevé 31…), vos remboursements et vos crédits, et de faire plusieurs démarches en ligne.</p>
<h2>Option 1 : avec votre institution financière (la plus rapide)</h2>
<p>Pas besoin d’avoir un avis de cotisation récent : vous utilisez les accès de votre banque en ligne.</p><ol class="gsteps">
<li><b>Allez sur le site de Revenu Québec</b><p>Cliquez sur <em>Mon dossier</em>, section Citoyens, puis sur <em>Accéder à Mon dossier</em>.</p></li>
<li><b>Choisissez votre institution financière</b><p>Cliquez sur son logo, puis connectez-vous avec le même code et le même mot de passe que sur le site de votre banque.</p></li>
<li><b>Acceptez les conditions et confirmez votre identité</b><p>Répondez aux questions demandées.</p></li>
<li><b>Inscrivez-vous à Mon dossier</b><p>Suivez les instructions à l’écran. La prochaine fois, vous passerez directement par votre banque.</p></li>
</ol>
<h2>Option 2 : avec un compte du service d’authentification du gouvernement</h2>
<p>Cette option demande un avis de cotisation récent de Revenu Québec, car des renseignements qui y figurent vous seront demandés.</p><ol class="gsteps">
<li><b>Accédez à Mon dossier, puis choisissez le service d’authentification gouvernemental</b><p>Le gouvernement remplace graduellement clicSÉQUR par ce nouveau service; si vous avez déjà un compte clicSÉQUR, il fonctionne encore : connectez-vous simplement.</p></li>
<li><b>Créez votre compte</b><p>Choisissez un code d’utilisateur, vos options de sécurité et vos questions de sécurité, puis acceptez les conditions d’utilisation.</p></li>
<li><b>Confirmez votre identité</b><p>Entrez les renseignements demandés, tirés de votre avis de cotisation.</p></li>
<li><b>Inscrivez-vous à Mon dossier</b><p>Suivez les instructions à l’écran.</p></li>
</ol>
<div class="tip"><strong>Code ou mot de passe oublié?</strong> Revenu Québec devra vérifier votre identité de nouveau. Le plus simple est alors de passer par votre institution financière (option 1).</div>
<div class="src"><strong>Sources officielles</strong> · <a href="https://www.revenuquebec.ca/fr/citoyens/mon-dossier-pour-les-citoyens/" rel="noopener">Mon dossier pour les citoyens</a> · <a href="https://www.revenuquebec.ca/fr/services-en-ligne/services-en-ligne/inscription-a-mon-dossier-pour-les-citoyens/" rel="noopener">Inscription à Mon dossier (avec tutoriels vidéo de Revenu Québec)</a> · <a href="https://www.quebec.ca/gouvernement/identite-numerique/authentification-gouvernementale/a-propos" rel="noopener">Service d’authentification gouvernementale</a></div>'''),

 dict(slug='allocations-enfants', cat='Familles', titre='Allocations pour enfants : ce qu’il faut savoir',
  resume='Allocation famille du Québec et allocation canadienne pour enfants : quand faire une demande et quels documents préparer.',
  corps='''
<p class="lede">Deux allocations sont versées aux familles du Québec : l’<strong>Allocation famille</strong> (Retraite Québec) et l’<strong>allocation canadienne pour enfants</strong> (Agence du revenu du Canada). Les deux sont calculées selon le revenu familial : les deux conjoints doivent produire leurs déclarations chaque année, même sans revenu.</p>
<h2>Naissance au Québec</h2>
<p>En général, aucune démarche : la déclaration de naissance avise Retraite Québec. Pour l’allocation canadienne, le formulaire de déclaration de naissance permet d’en faire la demande en même temps, à condition de consentir au partage des renseignements avec l’ARC. Si ce n’est pas fait, il faut présenter une demande.</p>
<h2>Quand faut-il faire une demande?</h2><ul>
<li>Naissance hors du Québec ou hors du Canada</li><li>Arrivée au Canada ou au Québec, ou retour au pays</li><li>Adoption</li><li>Un enfant vient vivre avec vous, ou une garde partagée commence, change ou prend fin</li></ul>
<h2>Les documents généralement demandés</h2><div class="need"><ul>
<li>Une preuve de naissance de chaque enfant (certificat de naissance, passeport ou document d’immigration au nom de l’enfant)</li>
<li>Une preuve de statut au Canada, pour les nouveaux arrivants (carte ou confirmation de résidence permanente, permis de travail ou d’études…)</li>
<li>Deux preuves de résidence au Québec à votre nom, si vous arrivez au Québec (bail, facture d’électricité ou d’Internet, permis de conduire)</li>
<li>Une preuve de la présence de l’enfant au Québec dans certains cas (bulletin scolaire, attestation de garderie, carnet de vaccination)</li>
<li>Le jugement ou l’entente de garde, s’il y a lieu</li></ul></div>
<div class="tip"><strong>Ne tardez pas.</strong> Les versements rétroactifs sont limités : une demande trop tardive peut vous faire perdre des mois d’allocations.</div>
<p>Nous pouvons préparer les demandes pour vous : nous vous enverrons un questionnaire dans votre portail, avec la liste exacte des pièces selon votre situation.</p>
<div class="src"><strong>Sources officielles</strong> · <a href="https://www.canada.ca/fr/agence-revenu/services/prestations-enfants-familles/allocation-canadienne-enfants/comment-demande.html" rel="noopener">ARC : comment demander l’ACE</a> · <a href="https://www.canada.ca/fr/agence-revenu/services/prestations-enfants-familles/documents-justificatifs.html" rel="noopener">ARC : documents justificatifs</a> · <a href="https://www.retraitequebec.gouv.qc.ca/fr/formulaires/formulaires-concernant-allocation-famille" rel="noopener">Retraite Québec : formulaires de l’Allocation famille</a></div>'''),
]

def guides(OUT, CSS, wordmark, APP):
    d = OUT / 'guides'
    (d / 'img').mkdir(parents=True, exist_ok=True)
    src = OUT.parent / 'img-guides'
    for p in src.glob('*.png'):
        shutil.copy(p, d / 'img' / p.name)
    def shell(title, desc, body, canon):
        return f'''<!DOCTYPE html><html lang="fr-CA"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{H.escape(title)} · Boujrad CPA Inc.</title><meta name="description" content="{H.escape(desc)}"><link rel="canonical" href="https://boujradcpa.com{canon}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><meta property="og:title" content="{H.escape(title)}"><meta property="og:description" content="{H.escape(desc)}">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet"><style>{CSS}{GCSS}</style></head><body>
<header class="solid"><div class="wrap nav"><a class="brand" href="/">{wordmark()}</a><nav class="links" aria-label="Navigation"><a href="/#services">Services</a><a href="/guides/">Guides</a><a href="/#contact">Contact</a></nav><a class="btn deep" href="{APP}/portail.html">Portail client</a></div></header>
<main class="gmain"><div class="wrap">{body}</div></main>
<footer><div class="wrap"><div><a class="brand" href="/">{wordmark(24)}</a></div><div><p style="margin:0">Ces guides sont fournis à titre informatif. Les étapes des sites gouvernementaux peuvent changer : en cas de doute, fiez-vous aux sources officielles indiquées.</p><p style="margin:4px 0 0">© 2026 Boujrad CPA Inc.</p></div></div></footer></body></html>'''
    cards = ''.join(f'<a class="gcard" href="/guides/{g["slug"]}.html"><small>{g["cat"]}</small><h2>{g["titre"]}</h2><p>{g["resume"]}</p></a>' for g in GUIDES)
    (d / 'index.html').write_text(shell('Guides pratiques', 'Guides pas à pas : portail client, comptes de l’ARC et de Revenu Québec, allocations et plus.',
        f'<h1>Guides pratiques</h1><p class="lede">Des marches à suivre simples pour vos démarches en ligne : notre portail client, vos comptes auprès des gouvernements et vos prestations.</p><div class="gcards">{cards}</div>', '/guides/'), encoding='utf-8')
    for g in GUIDES:
        body = f'<p class="crumb"><a href="/guides/">Guides</a> · {g["cat"]}</p><h1>{g["titre"]}</h1>{g["corps"]}<p style="margin-top:36px"><a href="/guides/">← Tous les guides</a></p>'
        (d / f'{g["slug"]}.html').write_text(shell(g['titre'], g['resume'], body, f'/guides/{g["slug"]}.html'), encoding='utf-8')
