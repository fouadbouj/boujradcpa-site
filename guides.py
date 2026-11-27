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
  resume='Créer votre compte, nous transmettre vos documents, signer, payer et suivre votre dossier, au même endroit.',
  corps=f'''
<p class="lede">Le portail client est votre espace sécurisé avec Boujrad CPA : vous y déposez vos documents, remplissez nos questionnaires, signez vos documents, consultez ce qui est à payer et nous écrivez. Rien ne passe par courriel : vos pièces sont chiffrées et conservées au Canada.</p>
<div class="need"><strong>En un coup d’œil</strong><ul><li><a href="#compte">Créer votre compte</a></li><li><a href="#impots">Impôts personnels</a></li><li><a href="#entreprise">Espace Entreprise</a></li><li><a href="#signer">Signer un document</a></li><li><a href="#factures">Payer une facture du cabinet</a></li><li><a href="#questionnaires">Questionnaires de service</a></li><li><a href="#representant">Nous autoriser comme représentant</a></li></ul></div>

<h2 id="compte">Créer votre compte</h2><ol class="gsteps">
{step('Ouvrez le portail', f'<p>Allez à <a href="{APPURL}/portail.html">app.boujradcpa.com/portail.html</a>, ou cliquez sur <em>Connexion</em>, puis <em>Portail client</em>, en haut de notre site. Si nous vous avons envoyé un lien d’invitation, utilisez-le : votre entreprise sera ajoutée automatiquement.</p>')}
{step('Cliquez sur « Créer un compte »', '<p>Inscrivez votre nom, votre courriel et un mot de passe d’au moins 8 caractères.</p>', 'portail-1-compte.png', 'Formulaire de création de compte du portail')}
{step('Confirmez votre courriel', '<p>Ouvrez le courriel de confirmation et cliquez sur le lien. Vous pouvez ensuite vous connecter en tout temps, à partir d’un ordinateur, d’une tablette ou d’un téléphone.</p>')}
</ol>
<div class="tip"><strong>Mot de passe oublié?</strong> Sur la page de connexion, entrez votre courriel et cliquez sur « Mot de passe oublié? » : un lien de réinitialisation vous est envoyé.</div>

<h2 id="impots">Impôts personnels : votre déclaration en trois étapes</h2><ol class="gsteps">
{step('Choisissez l’année et votre situation', '<p><em>Nouveau client</em> si c’est votre première année avec nous; <em>Client existant</em> si nous avons déjà préparé votre déclaration : vous indiquez alors seulement ce qui a changé.</p>', 'portail-2-accueil.png', 'Accueil du portail : choix de la situation')}
{step('Remplissez le formulaire', '<p>Les champs marqués d’un astérisque sont requis. Si nous préparons aussi la déclaration de votre conjoint, ses renseignements sont dans le même formulaire : il n’a pas besoin de compte. Vos réponses sont enregistrées au fur et à mesure.</p>', 'portail-3-formulaire.png', 'Formulaire de renseignements')}
{step('Déposez tous vos documents en une seule fois', '<p>La liste des documents à prévoir s’adapte à vos réponses. Attendez d’avoir <strong>tous</strong> vos feuillets et reçus, puis glissez-les tous ensemble dans la zone de dépôt (PDF ou photos) et envoyez votre dossier.</p>', 'portail-3b-documents.png', 'Étape des documents, avec la consigne de tout déposer en une seule fois')}
</ol>
<div class="tip"><strong>Important : tout en une seule fois.</strong> Nous préparons votre déclaration directement à partir des documents déposés, dès leur réception. Ne les envoyez pas au fur et à mesure : s’il vous manque un feuillet, gardez vos documents et revenez lorsque vous aurez tout en main. Cela évite les oublis et les retards.</div>

<h2 id="entreprise">Espace Entreprise</h2><ol class="gsteps">
{step('Ajoutez votre entreprise', '<p>Onglet <em>Entreprise</em> : entrez le code d’invitation que nous vous avons remis, puis cliquez sur <em>Accéder</em>. Vous pouvez ajouter plusieurs entreprises au même compte (bouton <em>Ajouter une autre entreprise</em>).</p>', 'portail-4-code.png', 'Ajout d’une entreprise avec le code d’invitation')}
{step('Consultez ce qui est à payer', '<p>Quand nous préparons une déclaration de taxes ou d’impôt, vous recevez un courriel. Le montant, la date limite et le code de paiement sont dans <em>À payer et documents du cabinet</em>. Le paiement se fait auprès du gouvernement; une fois fait, cliquez sur <em>J’ai fait le paiement</em> pour nous en informer.</p>', 'portail-5-payer.png', 'Montants à payer et documents du cabinet')}
{step('Déposez les documents de la période, tous en une seule fois', '<p>Onglet <em>Déposer des documents</em> : choisissez la période, déposez <strong>tous</strong> les relevés bancaires et de cartes, factures de ventes et d’achats, puis cliquez sur <em>J’ai terminé</em>. Nous préparons vos déclarations directement à partir de ce dépôt : s’il manque quelque chose, attendez d’avoir tout.</p>', 'portail-6-depot.png', 'Dépôt de documents de la période')}
{step('Factures, échéancier et messages', '<p><em>Factures</em> : vos factures du cabinet et leur état. <em>Échéancier</em> : les prochaines dates limites de votre entreprise (taxes, retenues, impôt). <em>Messages</em> : écrivez-nous, avec pièces jointes au besoin; nous vous répondons au même endroit.</p>')}
</ol>

<h2 id="signer">Signer un document</h2>
<p>Votre contrat de services, une procuration de Revenu Québec (formulaire MR-69) ou tout autre document à signer vous attend dans <em>À payer et documents du cabinet</em>, avec la mention <em>Document à signer</em>. Vous recevez aussi un courriel.</p><ol class="gsteps">
{step('Cliquez sur « Lire et signer »', '<p>Le document s’affiche. Lisez-le au complet.</p>', 'portail-8-a-signer.png', 'Document à signer dans le portail')}
{step('Cliquez à l’endroit où signer, puis signez', '<p>Cliquez sur la case de signature du document, inscrivez votre nom (et votre titre si vous signez pour une entreprise), signez avec la souris ou le doigt, puis cochez la case de consentement.</p>', 'portail-8b-signature.png', 'Signature électronique du document')}
{step('Cliquez sur « Signer le document »', '<p>C’est fait : nous sommes avisés, et votre copie signée est disponible en tout temps dans votre portail (bouton <em>Copie signée</em>).</p>')}
</ol>

<h2 id="factures">Payer une facture du cabinet</h2>
<p>Si vous n’êtes pas prélevé par débit préautorisé, vous recevez nos factures par courriel, avec un lien vers une page de paiement sécurisée. Vous pouvez y payer par virement Interac (les instructions y sont indiquées) ou, lorsque l’option est offerte, par carte de crédit. Vos factures sont aussi dans l’onglet <em>Factures</em> du portail.</p>

<h2 id="questionnaires">Questionnaires de service</h2>
<p>Pour certains mandats (ouverture de dossier, constitution d’une société, fin d’exercice, allocations pour enfants, pensions de retraite, succession, etc.), nous vous envoyons un lien vers un questionnaire. Il s’ouvre dans votre portail : répondez aux questions et déposez chaque pièce demandée au bon endroit. Vos réponses sont enregistrées automatiquement; vous pouvez revenir terminer plus tard, puis cliquez sur <em>Envoyer au cabinet</em>.</p>
<img class="shot" src="img/portail-7-questionnaire.png" alt="Questionnaire de service dans le portail" loading="lazy" width="1100">

<h2 id="representant">Nous autoriser comme représentant</h2>
<p>Pour que nous puissions parler à l’ARC et à Revenu Québec en votre nom, la carte <em>Nous autoriser comme représentant</em> du portail vous explique quoi faire. Le plus souvent, nous faisons la demande à l’ARC et vous n’avez qu’à la confirmer dans votre compte; pour Revenu Québec, nous vous faisons signer la procuration dans le portail. Toutes les étapes sont dans le guide <a href="autoriser-representant.html">Autoriser Boujrad CPA comme représentant</a>.</p>
<img class="shot" src="img/portail-9-representant.png" alt="Carte Nous autoriser comme représentant" loading="lazy" width="1100">

<div class="tip"><strong>Sécurité.</strong> Ne nous envoyez jamais de numéro d’assurance sociale, de pièce d’identité ni de document fiscal par courriel : utilisez toujours le portail. Nous ne vous demanderons jamais votre mot de passe.</div>
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
<p>Une fois inscrit, vous pouvez autoriser Boujrad CPA Inc. à consulter votre dossier : nous pourrons alors répondre à l’ARC pour vous et récupérer vos feuillets. Toutes les étapes, pour un particulier comme pour une entreprise, sont dans le guide <a href="autoriser-representant.html">Autoriser Boujrad CPA comme représentant</a>. Notre identifiant vous est donné dans votre portail client.</p>
<div class="src"><strong>Sources officielles</strong> · <a href="https://www.canada.ca/fr/agence-revenu/services/services-electroniques/services-ouverture-session-arc.html" rel="noopener">Se connecter à son compte de l’ARC</a> · <a href="https://www.canada.ca/fr/agence-revenu/services/services-electroniques/services-ouverture-session-arc/aide-services-ouverture-session-arc/verification-identite.html" rel="noopener">Vérification de votre identité</a> · <a href="https://www.canada.ca/fr/agence-revenu/services/impot/particuliers/programmes-educatifs/utiliser-mon-dossier.html" rel="noopener">Leçon de l’ARC : utiliser Mon dossier</a></div>'''),

 dict(slug='autoriser-representant', cat='Gouvernement du Canada et du Québec', titre='Autoriser Boujrad CPA comme représentant (ARC et Revenu Québec)',
  resume='Nous donner accès à votre dossier fiscal pour que nous puissions répondre aux gouvernements et récupérer vos feuillets à votre place.',
  corps='''
<p class="lede">Pour parler à l’Agence du revenu du Canada (ARC) et à Revenu Québec en votre nom, récupérer vos feuillets et répondre à leurs lettres, nous devons être autorisés comme représentant. Côté fédéral, c’est vous qui le faites, en quelques minutes, dans votre compte de l’ARC. Côté Québec, c’est nous qui préparons la procuration et vous la faisons signer.</p>
<div class="need"><strong>À avoir sous la main</strong><ul><li>Votre accès à votre compte de l’ARC (<em>Mon dossier</em> pour un particulier, <em>Mon dossier d’entreprise</em> pour une société). Pas encore inscrit? Voyez le guide <a href="compte-arc.html">Créer votre compte de l’ARC</a>.</li><li>Notre identifiant de représentant : nous vous le donnons dans votre <strong>portail client</strong> (section « Nous autoriser comme représentant ») ou sur simple demande dans le portail. Pour votre sécurité, il n’est pas publié sur ce site.</li></ul></div>
<h2>Le plus simple : confirmer notre demande</h2>
<p>Dans la plupart des cas, c’est nous qui faisons la demande d’autorisation à l’ARC. Vous n’avez qu’à la confirmer :</p><ol class="gsteps">
<li><b>Connectez-vous à votre compte de l’ARC</b><p><em>Mon dossier</em> si vous êtes un particulier, <em>Mon dossier d’entreprise</em> pour une société.</p></li>
<li><b>Ouvrez la demande en attente</b><p>Une demande d’autorisation en attente de « Boujrad CPA Inc. » s’affiche. Sinon, cherchez la section des représentants autorisés : elle y est en attente.</p></li>
<li><b>Vérifiez et confirmez</b><p>Niveau 2, aucune date de fin, accès en ligne (et, pour une entreprise, le numéro d’entreprise au complet). Cliquez sur <em>Confirmer</em>. C’est tout.</p></li>
</ol>
<p>Pas de demande visible, ou vous préférez le faire vous-même? Suivez les étapes ci-dessous.</p>
<h2>ARC : vous êtes un particulier</h2><ol class="gsteps">
<li><b>Connectez-vous à Mon dossier</b><p>Dans votre compte de l’ARC, choisissez <em>Mon dossier</em>.</p></li>
<li><b>Allez à la gestion des représentants</b><p>Dans le menu <em>Profil</em>, choisissez l’option pour autoriser ou gérer vos représentants, puis <em>Autoriser un représentant</em>.</p></li>
<li><b>Entrez notre identifiant</b><p>Saisissez l’identifiant que nous vous avons transmis (numéro d’entreprise du cabinet, ID Rep ou ID Groupe), puis vérifiez que c’est bien « Boujrad CPA Inc. » qui s’affiche.</p></li>
<li><b>Choisissez exactement ces options</b><p><strong>Niveau 2</strong> (voir et mettre à jour les renseignements), <strong>aucune date de fin</strong> (laissez le champ vide : l’autorisation reste valide sans limite) et l’<strong>accès en ligne</strong>. C’est ce qui nous permet de répondre à l’ARC et de faire toutes les corrections pour vous.</p></li>
<li><b>Confirmez</b><p>L’accès est immédiat. Écrivez-nous dans le portail pour nous dire que c’est fait.</p></li>
</ol>
<h2>ARC : vous avez une entreprise (société, entreprise inscrite)</h2><ol class="gsteps">
<li><b>Connectez-vous à Mon dossier d’entreprise</b><p>Seul un propriétaire, un administrateur ou un représentant déjà autorisé au niveau 3 peut donner l’accès.</p></li>
<li><b>Ouvrez « Autoriser ou gérer les représentants »</b><p>Puis choisissez <em>Autoriser un représentant</em>.</p></li>
<li><b>Entrez notre identifiant</b><p>Le même que ci-dessus. Vérifiez le nom du cabinet affiché.</p></li>
<li><b>Choisissez exactement ces options</b><p><strong>Niveau 2</strong>, la portée <strong>numéro d’entreprise au complet</strong> (impôt des sociétés RC, TPS/TVH RT, retenues sur la paie RP et tous les autres comptes), <strong>aucune date de fin</strong> (sans limite) et l’<strong>accès en ligne</strong>. Ainsi, nous pouvons faire toutes les démarches et modifications pour vous.</p></li>
<li><b>Confirmez</b><p>Prévenez-nous dans le portail une fois terminé.</p></li>
</ol>
<div class="tip"><strong>Pourquoi ces options?</strong> Sans date de fin, vous n’avez pas à refaire l’autorisation chaque année; le niveau 2 et l’accès en ligne nous permettent de corriger une déclaration, de répondre à une demande de l’ARC et de mettre votre dossier à jour sans délai. Vous pouvez retirer l’accès en tout temps.</div>

<h2>Revenu Québec : la procuration</h2>
<p>Au Québec, c’est nous qui préparons l’autorisation : le formulaire <em>Autorisation relative à la communication de renseignements ou procuration</em> (MR-69), dans sa version la plus récente, que vous signez, ou une demande que nous transmettons en ligne. Vous pouvez aussi nous l’accorder vous-même dans Mon dossier pour les citoyens ou Mon dossier pour les entreprises, si vous préférez. Une procuration nous permet d’agir pour vous (répondre aux demandes, faire des corrections); une simple autorisation nous permet seulement de consulter vos renseignements.</p>
<h2>Retirer l’accès</h2>
<p>Vous restez en contrôle : vous pouvez en tout temps mettre fin à notre accès dans votre compte de l’ARC (gestion des représentants) et dans Mon dossier de Revenu Québec, ou avec le formulaire de révocation MR-69.R.</p>
<div class="src"><strong>Sources officielles</strong> · <a href="https://www.canada.ca/fr/agence-revenu/services/impot/autorisation-representant/comment.html" rel="noopener">ARC — Comment donner une autorisation</a> · <a href="https://www.canada.ca/fr/agence-revenu/services/impot/autorisation-representant/acces/niveaux-portee.html" rel="noopener">ARC — Niveaux et portée de l’autorisation</a> · <a href="https://www.revenuquebec.ca/fr/citoyens/votre-situation/autorisation-ou-procuration/" rel="noopener">Revenu Québec — Autorisation ou procuration</a> · <a href="https://www.revenuquebec.ca/fr/services-en-ligne/formulaires-et-publications/details-courant/mr-69/" rel="noopener">Formulaire MR-69</a></div>
'''),
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

CHRONIQUES = [
 dict(slug='budget-federal-2026', date='2026-11-25', dlong='25 novembre 2026', cat='Nouveautés fiscales', titre='Budget fédéral du 5 novembre 2026 : ce qui pourrait changer pour vous',
  resume='Date limite du 15 mai, acomptes provisionnels allégés, crédit pour aidants remboursable, nouvelle exemption pour les entrepreneurs : les mesures à surveiller.',
  corps='''
<p class="lede">Le budget fédéral déposé le 5 novembre 2026 propose plusieurs changements concrets pour les particuliers, les travailleurs autonomes et les propriétaires d’entreprise. Attention : ce sont des propositions. Elles doivent encore être adoptées, et Québec doit annoncer s’il s’harmonise pour sa propre déclaration.</p>
<h2>Pour les particuliers</h2><ul>
<li><strong>Une seule date limite : le 15 mai.</strong> À partir de l’année d’imposition 2027, tous les particuliers, y compris les travailleurs autonomes et leurs conjoints, auraient jusqu’au 15 mai pour produire leur déclaration fédérale et payer leur solde.</li>
<li><strong>Moins de gens obligés de verser des acomptes provisionnels.</strong> Au Québec, le seuil fédéral passerait de 1 800 $ à 4 500 $ d’impôt à payer, à compter de l’année 2028. Les travailleurs autonomes pourraient aussi faire un seul versement des deux tiers de leur impôt estimé, au plus tard le 31 décembre, au lieu de quatre versements.</li>
<li><strong>Crédit canadien pour aidant naturel remboursable</strong> à compter de 2027 : il profiterait aussi aux aidants qui ont peu ou pas d’impôt à payer.</li>
<li><strong>Biens à l’étranger (T1135)</strong> : le seuil de déclaration passerait de 100 000 $ à 200 000 $ pour les années qui se terminent après 2026.</li>
<li><strong>Avis d’opposition</strong> : le délai pour contester une cotisation serait resserré et les demandes de prolongation, éliminées. Raison de plus de nous transmettre vos avis de cotisation dès leur réception.</li>
<li><strong>Frais médicaux</strong> : le crédit serait simplifié, avec moins de pièces justificatives pour certaines dépenses, et des montants fixes optionnels seraient offerts pour certains frais (déménagement, adoption, accessibilité domiciliaire).</li></ul>
<h2>Pour les entreprises</h2><ul>
<li><strong>Incitatif à la croissance canadienne</strong> : une nouvelle exemption pouvant atteindre 15 millions de dollars de gains en capital par particulier et par entreprise, sur des actions admissibles émises à compter du jour du budget.</li>
<li><strong>Acomptes des sociétés</strong> : le seuil passerait de 3 000 $ à 7 500 $ pour les années commençant à partir de 2028.</li>
<li><strong>Transferts entre générations</strong> : le roulement des fermes et des entreprises de pêche s’étendrait aux neveux, nièces et petits-neveux à compter de 2027.</li></ul>
<div class="tip"><strong>Ce que nous vous conseillons.</strong> Rien à faire pour l’instant : nous suivrons l’adoption de ces mesures et la position de Québec, et nous en tiendrons compte dans vos dossiers. Si vous êtes travailleur autonome ou si vous songez à vendre ou à transférer votre entreprise, parlons-en dans votre prochaine rencontre.</div>
<div class="src"><strong>Sources</strong> · <a href="https://www.rbcwealthmanagement.com/fr-ca/insights/federal-budget-2026-an-overview-of-key-measures-that-may-impact-you" rel="noopener">RBC Gestion de patrimoine : aperçu des mesures du budget fédéral 2026</a> · <a href="https://www.budget.canada.ca/" rel="noopener">Budget du gouvernement du Canada</a></div>'''),

 dict(slug='fin-annee-2026', date='2026-11-24', dlong='24 novembre 2026', cat='Conseils', titre='Avant le 31 décembre : 8 gestes pour payer moins d’impôt',
  resume='CELI, REER, pertes en capital, dons, dépenses à payer avant la fin de l’année : la liste à vérifier d’ici le 31 décembre 2026.',
  corps='''
<p class="lede">Une bonne partie des économies d’impôt se jouent avant le 31 décembre : après, il est souvent trop tard. Voici les points à vérifier pour 2026.</p>
<ol class="gsteps">
<li><b>Retirez de votre CELI avant le 31 décembre si vous prévoyez le faire</b><p>Le plafond est de 7 000 $ pour 2026. Un montant retiré est ajouté à vos droits de cotisation seulement le 1er janvier suivant : un retrait fait en décembre vous redonne donc ces droits dès janvier, alors qu’un retrait fait en janvier vous oblige à attendre une année de plus. Et attention : remettre en 2026 un montant retiré en 2026 peut créer une cotisation excédentaire pénalisée.</p></li>
<li><b>Préparez votre cotisation REER</b><p>Le plafond pour 2026 est de 33 810 $ (18 % du revenu gagné de l’année précédente, selon vos droits), et vous avez jusqu’au 1er mars 2027 pour cotiser. Le plafond monte à 35 390 $ pour 2027.</p></li>
<li><b>Pensez au CELIAPP si vous achetez votre première propriété</b><p>Jusqu’à 8 000 $ par année, déductibles comme un REER et retirés sans impôt pour l’achat d’une première habitation.</p></li>
<li><b>Réalisez vos pertes en capital</b><p>Vendre des placements qui ont perdu de la valeur avant la fin de l’année peut réduire l’impôt sur vos gains de l’année. Attention aux règles sur les pertes apparentes si vous rachetez le même titre trop vite.</p></li>
<li><b>Faites vos dons avant le 31 décembre</b><p>C’est la date du reçu qui compte. Au-delà des premiers 200 $, le crédit est beaucoup plus élevé.</p></li>
<li><b>Payez avant la fin de l’année les frais qui donnent droit à une déduction ou à un crédit</b><p>Frais de garde, frais médicaux, frais de scolarité, cotisations professionnelles : c’est l’année du paiement qui compte. Au Québec, les frais de placement ne sont déductibles que jusqu’à concurrence de vos revenus de placement de l’année.</p></li>
<li><b>Prêt au conjoint à taux prescrit</b><p>Si vous en avez un, les intérêts de 2026 doivent être payés au plus tard le 30 janvier 2027, sinon le fractionnement de revenu tombe.</p></li>
<li><b>Placez les allocations pour enfants dans un compte à leur nom</b><p>Les revenus générés par l’allocation canadienne pour enfants et l’Allocation famille déposées dans un compte au nom de l’enfant sont imposés à l’enfant, et non aux parents.</p></li>
</ol>
<div class="tip"><strong>Propriétaires d’entreprise</strong> : salaire ou dividendes, achat d’équipement avant la fin de l’exercice, bonis à verser : ces choix se planifient avant la fin de votre exercice. Écrivez-nous dans le portail pour en discuter.</div>
<div class="src"><strong>Sources</strong> · <a href="https://www.canada.ca/fr/agence-revenu/services/impot/particuliers/sujets/compte-epargne-libre-impot/cotiser/calculer-droits.html" rel="noopener">ARC : droits de cotisation au CELI</a> · <a href="https://www.canada.ca/fr/agence-revenu/services/impot/administrateurs-regimes-enregistres/fesp/plafonds-cd-reer-rpdb-celi-mgap.html" rel="noopener">ARC : plafonds REER et CELI</a> · <a href="https://www.crowe.com/ca/crowebgk/fr-ca/publications/yetp-2025-2026" rel="noopener">Crowe BGK : planification fiscale de fin d’année</a></div>'''),

 dict(slug='changements-2026', date='2026-11-20', dlong='20 novembre 2026', cat='Nouveautés fiscales', titre='Impôt 2026 : les changements qui touchent votre déclaration',
  resume='Taux fédéral de 14 %, indexation de 2,05 % au Québec et cotisations au RRQ et au RQAP réduites : ce que vous verrez dans votre déclaration 2026.',
  corps='''
<p class="lede">Votre déclaration de revenus 2026, que vous produirez au printemps 2027, reflétera plusieurs changements entrés en vigueur le 1er janvier 2026.</p>
<h2>Au fédéral : le premier taux passe à 14 %</h2>
<p>Le taux qui s’applique à la première tranche de revenu imposable, qui était de 15 %, a été abaissé à 14 % le 1er juillet 2025 (soit 14,5 % pour l’ensemble de 2025) et s’applique à 14 % pour toute l’année 2026. Comme la plupart des crédits d’impôt non remboursables sont calculés au même taux, leur valeur baisse aussi légèrement.</p>
<h2>Au Québec : indexation de 2,05 %</h2>
<p>Les seuils des tranches d’imposition et la plupart des crédits sont indexés de 2,05 % en 2026. Les taux eux-mêmes ne changent pas : le premier taux de 14 % s’applique jusqu’à 54 345 $ de revenu imposable.</p>
<h2>Cotisations réduites au RRQ et au RQAP</h2>
<p>Québec a réduit les taux de cotisation au Régime de rentes du Québec et au Régime québécois d’assurance parentale à compter de 2026. L’économie maximale est d’environ 137 $ pour un salarié et 259 $ pour un travailleur autonome.</p>
<div class="tip"><strong>Employeurs</strong> : ces nouveaux taux s’appliquent à vos paies depuis janvier 2026. Si vous faites votre paie vous-même, vérifiez que votre logiciel a été mis à jour.</div>
<div class="src"><strong>Sources</strong> · <a href="https://www.canada.ca/fr/ministere-finances/nouvelles/2025/05/une-reduction-dimpot-qui-profitera-a-la-classe-moyenne.html" rel="noopener">Finances Canada : réduction du premier taux</a> · <a href="https://www.revenuquebec.ca/fr/entreprises/retenues-a-la-source-et-cotisations-de-lemployeur/trousse-employeur/principaux-changements-pour-2026-trousse-employeur/" rel="noopener">Revenu Québec : principaux changements pour 2026</a> · <a href="https://www.finances.gouv.qc.ca/Budget_et_mise_a_jour/maj/documents/COMFR_MAJ_20251125.pdf" rel="noopener">Finances Québec : mise à jour de l’automne 2025</a></div>'''),
]

def guides(OUT, CSS, wordmark, APP):
    d = OUT / 'guides'
    (d / 'img').mkdir(parents=True, exist_ok=True)
    src = OUT.parent / 'img-guides'
    for p in src.glob('*.png'):
        shutil.copy(p, d / 'img' / p.name)
    def shell(title, desc, body, canon):
        return f'''<!DOCTYPE html><html lang="fr-CA"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{H.escape(title)} · Boujrad CPA Inc.</title><script>document.documentElement.classList.add('js')</script><meta property="og:type" content="article"><meta property="og:site_name" content="Boujrad CPA Inc."><meta name="description" content="{H.escape(desc)}"><link rel="canonical" href="https://boujradcpa.com{canon}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><meta property="og:title" content="{H.escape(title)}"><meta property="og:description" content="{H.escape(desc)}">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet"><style>{CSS}{GCSS}</style></head><body>
{header('fr','/')}
<main class="gmain"><div class="wrap">{body}</div></main>
<footer><div class="wrap"><div><a class="brand" href="/">{wordmark(24)}</a></div><div><p style="margin:0">Ces guides sont fournis à titre informatif. Les étapes des sites gouvernementaux peuvent changer : en cas de doute, fiez-vous aux sources officielles indiquées.</p><p style="margin:4px 0 0">© 2026 Boujrad CPA Inc.</p></div></div></footer><script>{JS}</script></body></html>'''
    card = lambda g, extra='': f'<a class="gcard" href="/guides/{g["slug"]}.html"><small>{g["cat"]}{extra}</small><h2>{g["titre"]}</h2><p>{g["resume"]}</p></a>'
    CH = sorted(CHRONIQUES, key=lambda c: c['date'], reverse=True)
    cc = ''.join(card(c, ' · ' + c['dlong']) for c in CH)
    gc = ''.join(card(g) for g in GUIDES)
    (d / 'index.html').write_text(shell('Chroniques et guides', 'Nouveautés fiscales, conseils et guides pas à pas : portail client, comptes de l’ARC et de Revenu Québec, allocations et plus.',
        f'<h1>Chroniques et guides</h1><p class="lede">Les nouveautés fiscales qui vous touchent, des conseils pratiques et des marches à suivre simples pour vos démarches en ligne.</p><h2 style="margin-top:8px">Chroniques</h2><div class="gcards">{cc}</div><h2>Guides pratiques</h2><div class="gcards">{gc}</div>', '/guides/'), encoding='utf-8')
    for c in CH:
        body = f'<p class="crumb"><a href="/guides/">Chroniques</a> · {c["cat"]} · {c["dlong"]}</p><h1>{c["titre"]}</h1>{c["corps"]}<p class="src" style="border:0;margin-top:20px">Cette chronique est fournie à titre informatif et ne remplace pas un conseil adapté à votre situation. Information à jour au {c["dlong"]}.</p><p style="margin-top:20px"><a href="/guides/">← Toutes les chroniques</a></p>'
        (d / f'{c["slug"]}.html').write_text(shell(c['titre'], c['resume'], body, f'/guides/{c["slug"]}.html'), encoding='utf-8')
    for g in GUIDES:
        body = f'<p class="crumb"><a href="/guides/">Guides</a> · {g["cat"]}</p><h1>{g["titre"]}</h1>{g["corps"]}<p style="margin-top:36px"><a href="/guides/">← Tous les guides</a></p>'
        (d / f'{g["slug"]}.html').write_text(shell(g['titre'], g['resume'], body, f'/guides/{g["slug"]}.html'), encoding='utf-8')
