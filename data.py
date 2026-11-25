import pathlib, json
OUT=HERE/'site'; (OUT/'en').mkdir(parents=True,exist_ok=True)
APP='https://app.boujradcpa.com'
MAPS='https://www.google.com/maps/search/?api=1&query=672+Boulevard+des+Laurentides+Laval+QC+H7G+2V9'
T={
'fr':dict(lang='fr-CA',title='Boujrad CPA Inc. · Comptables à Laval',desc="Cabinet de comptables professionnels agréés à Laval : tenue de livres, états financiers, impôts des sociétés et des particuliers, TPS/TVQ.",
 other='/en/',otherlbl='EN',otherfull='English',home='/',
 nav=['Services','Approche','Clientèle','Contact'],members='Intranet',
 h1='Des chiffres clairs pour des décisions sereines.',
 lead="Boujrad CPA est un cabinet de comptables professionnels agréés établi à Laval. Nous tenons vos livres, préparons vos états financiers et vos déclarations, et vous expliquons vos chiffres simplement.",
 cta1='Nous écrire',cta2='Voir nos services',
 facts=[('Comptables professionnels agréés','Un cabinet CPA, rigoureux et à jour.'),('Français et anglais','Service dans la langue de votre choix.'),('Au bureau ou à distance','Rencontres à Laval ou en ligne, partout au Québec.')],
 svT='Nos services',svL="De la tenue de livres mensuelle à la déclaration de revenus, un seul cabinet pour l'ensemble de vos obligations comptables et fiscales.",
 sv=[('ledger','Tenue de livres','Saisie et classement de vos transactions, conciliations bancaires mensuelles, livres prêts en tout temps.'),
     ('report','États financiers','Bilan et état des résultats annuels en mission de compilation, pour vous, votre banque et vos partenaires.'),
     ('corp','Impôts des sociétés','Déclarations T2 et CO-17, incluant les sociétés de gestion et les sociétés de professionnels.'),
     ('person','Impôts des particuliers','Déclarations T1 et TP-1 pour particuliers, travailleurs autonomes et actionnaires.'),
     ('tax','TPS et TVQ','Inscription, calcul et production de vos déclarations de taxes de vente, au bon moment.'),
     ('pay','Paie et relevés','Paie des employés et des actionnaires, remises de retenues, feuillets T4 et relevés 1.'),
     ('start','Démarrage d’entreprise','Choix de la structure, incorporation, inscriptions aux gouvernements et mise en place de vos livres.'),
     ('plan','Planification fiscale','Rémunération salaire ou dividendes, société de gestion, fin d’année : des choix éclairés.')],
 apT='Une méthode simple, du relevé au rapport',apL="Vous nous confiez vos documents, nous nous occupons du reste. Nos outils numériques sécurisés accélèrent le traitement, et chaque dossier est révisé par notre équipe.",
 steps=[('Vous transmettez','Relevés bancaires et de cartes, factures et documents, de façon sécurisée.'),('Nous comptabilisons','Classement, conciliation, ajustements de fin d’année et déclarations.'),('Vous décidez','Des états financiers clairs, des échéances respectées et des conseils concrets.')],
 clT='Pour qui nous travaillons',cl=['Professionnels de la santé incorporés','PME et entreprises de services','Travailleurs autonomes','Sociétés de gestion (holdings)','Immeubles locatifs','Particuliers et familles'],
 ctT='Nous joindre',ctL="Écrivez-nous pour une première rencontre. Nous vous répondons en général dans un délai d’un jour ouvrable.",
 adrT='Bureau',adr=['220-672, boulevard des Laurentides','Laval (Québec) H7G 2V9','Canada'],map='Voir sur la carte',
 hrT="Heures d’ouverture",hr=[('Lundi au jeudi','9 h à 16 h'),('Vendredi','9 h à 12 h'),('Samedi et dimanche','Fermé')],
 f=dict(name='Nom complet',company='Entreprise (facultatif)',email='Courriel',phone='Téléphone (facultatif)',svc='Service recherché',other='Autre',msg='Message',send='Envoyer',note="En envoyant ce formulaire, vous acceptez que nous utilisions ces renseignements pour vous répondre."),
 foot='Tous droits réservés.',thanksT='Merci, votre message est envoyé.',thanksL="Nous vous répondrons dans un délai d’un jour ouvrable.",back="Retour à l’accueil",
 alt="Illustration d'un état financier et d'un graphique en hausse"),
'en':dict(lang='en-CA',title='Boujrad CPA Inc. · Accountants in Laval',desc='Chartered professional accountants in Laval: bookkeeping, financial statements, corporate and personal tax, GST/QST.',
 other='/',otherlbl='FR',otherfull='Français',home='/en/',
 nav=['Services','Approach','Clients','Contact'],members='Intranet',
 h1='Clear numbers for confident decisions.',
 lead='Boujrad CPA is a firm of chartered professional accountants based in Laval. We keep your books, prepare your financial statements and tax returns, and explain your numbers in plain terms.',
 cta1='Write to us',cta2='See our services',
 facts=[('Chartered professional accountants','A CPA firm, rigorous and up to date.'),('French and English','Service in the language you prefer.'),('In the office or remotely','Meet us in Laval or online, anywhere in Québec.')],
 svT='Our services',svL='From monthly bookkeeping to year-end tax returns, one firm for all your accounting and tax obligations.',
 sv=[('ledger','Bookkeeping','Recording and classifying your transactions, monthly bank reconciliations, books ready at all times.'),
     ('report','Financial statements','Annual balance sheet and income statement under a compilation engagement, for you, your bank and your partners.'),
     ('corp','Corporate tax','T2 and CO-17 returns, including holding companies and professional corporations.'),
     ('person','Personal tax','T1 and TP-1 returns for individuals, self-employed workers and shareholders.'),
     ('tax','GST and QST','Registration, calculation and filing of your sales tax returns, on time.'),
     ('pay','Payroll and slips','Payroll for employees and shareholders, source deduction remittances, T4 slips and RL-1 slips.'),
     ('start','Starting a business','Choosing a structure, incorporation, government registrations and setting up your books.'),
     ('plan','Tax planning','Salary or dividends, holding companies, year-end: informed choices.')],
 apT='A simple method, from statement to report',apL='You send us your documents and we take care of the rest. Our secure digital tools speed up the work, and every file is reviewed by our team.',
 steps=[('You send','Bank and card statements, invoices and documents, securely.'),('We do the accounting','Classification, reconciliation, year-end adjustments and returns.'),('You decide','Clear financial statements, deadlines met and practical advice.')],
 clT='Who we work with',cl=['Incorporated health professionals','SMEs and service businesses','Self-employed workers','Holding companies','Rental properties','Individuals and families'],
 ctT='Get in touch',ctL='Write to us to set up a first meeting. We usually reply within one business day.',
 adrT='Office',adr=['220-672 Boulevard des Laurentides','Laval, Québec H7G 2V9','Canada'],map='View on map',
 hrT='Office hours',hr=[('Monday to Thursday','9 a.m. to 4 p.m.'),('Friday','9 a.m. to noon'),('Saturday and Sunday','Closed')],
 f=dict(name='Full name',company='Company (optional)',email='Email',phone='Phone (optional)',svc='Service needed',other='Other',msg='Message',send='Send',note='By sending this form, you agree that we use this information to reply to you.'),
 foot='All rights reserved.',thanksT='Thank you, your message has been sent.',thanksL='We will reply within one business day.',back='Back to home',
 alt='Illustration of a financial statement and a rising chart')}
ICON={
'ledger':'<rect x="5" y="4" width="22" height="24" rx="2"/><path d="M10 10h12M10 15h12M10 20h7"/>',
'report':'<rect x="6" y="4" width="20" height="24" rx="2"/><path d="M11 22v-5M16 22v-9M21 22v-12"/>',
'corp':'<path d="M6 27V9l10-5 10 5v18"/><path d="M11 27v-7h10v7M11 13h2M19 13h2"/>',
'person':'<circle cx="16" cy="11" r="5"/><path d="M7 27c1-6 5-9 9-9s8 3 9 9"/>',
'tax':'<path d="M8 24 24 8"/><circle cx="10" cy="10" r="3"/><circle cx="22" cy="22" r="3"/>',
'pay':'<rect x="4" y="9" width="24" height="15" rx="2"/><circle cx="16" cy="16.5" r="3.5"/><path d="M8 13v7M24 13v7"/>',
'start':'<path d="M16 4c5 4 7 10 5 17h-10C9 14 11 8 16 4z"/><path d="M11 21l-4 5M21 21l4 5M16 26v2"/>',
'plan':'<path d="M5 26h22"/><path d="M8 21l6-6 4 4 7-9"/><path d="M20 10h5v5"/>'}
LOGO_B='M24.75826330532213 44.0Q21.75546218487395 44.0 20.14201680672269 42.96918767507003Q18.528571428571432 41.938375350140056 17.766666666666666 40.68347338935575H16.95994397759104V43.372549019607845H11.402521008403362V12.000000000000004H17.049579831932775V23.69747899159664H17.856302521008402Q18.349299719887956 22.89075630252101 19.17843137254902 22.173669467787114Q20.007563025210086 21.456582633053223 21.37450980392157 20.985994397759107Q22.741456582633056 20.515406162464988 24.75826330532213 20.515406162464988Q27.44733893557423 20.515406162464988 29.733053221288518 21.837535014005603Q32.018767507002806 23.15966386554622 33.40812324929972 25.714285714285715Q34.79747899159664 28.268907563025213 34.79747899159664 31.899159663865547V32.61624649859944Q34.79747899159664 36.246498599439775 33.40812324929972 38.801120448179276Q32.018767507002806 41.35574229691877 29.733053221288518 42.67787114845939Q27.44733893557423 44.0 24.75826330532213 44.0ZM23.055182072829133 39.070028011204485Q25.654621848739495 39.070028011204485 27.40252100840336 37.38935574229692Q29.150420168067228 35.70868347338936 29.150420168067228 32.48179271708683V32.03361344537815Q29.150420168067228 28.806722689075634 27.424929971988796 27.12605042016807Q25.699439775910363 25.445378151260506 23.055182072829133 25.445378151260506Q20.455742296918768 25.445378151260506 18.707843137254905 27.12605042016807Q16.95994397759104 28.806722689075634 16.95994397759104 32.03361344537815V32.48179271708683Q16.95994397759104 35.70868347338936 18.707843137254905 37.38935574229692Q20.455742296918768 39.070028011204485 23.055182072829133 39.070028011204485Z'
def logo(sz=34,inv=False):
  bg,fg,dot=('#fff','#0d1a16','#0d5c44') if inv else ('#0d1a16','#fff','#b8f5d0')
  return f'<svg width="{sz}" height="{sz}" viewBox="0 0 56 56" aria-hidden="true"><rect width="56" height="56" rx="12" fill="{bg}"/><path d="{LOGO_B}" fill="{fg}"/><rect x="37.8" y="36.57" width="6.8" height="6.8" rx="1.3" fill="{dot}"/></svg>'

WORD_D='M36.800000000000004 101.4Q30.1 101.4 26.5 99.1Q22.900000000000002 96.8 21.200000000000003 94.0H19.400000000000002V100.0H7.0V30.0H19.6V56.099999999999994H21.400000000000002Q22.5 54.3 24.35 52.699999999999996Q26.200000000000003 51.099999999999994 29.250000000000004 50.05Q32.300000000000004 49.0 36.800000000000004 49.0Q42.800000000000004 49.0 47.900000000000006 51.95Q53.0 54.9 56.1 60.599999999999994Q59.2 66.3 59.2 74.4V76.0Q59.2 84.1 56.1 89.8Q53.0 95.5 47.900000000000006 98.45Q42.800000000000004 101.4 36.800000000000004 101.4ZM33.0 90.4Q38.800000000000004 90.4 42.7 86.65Q46.6 82.9 46.6 75.7V74.7Q46.6 67.5 42.75 63.75Q38.900000000000006 60.0 33.0 60.0Q27.200000000000003 60.0 23.300000000000004 63.75Q19.400000000000002 67.5 19.400000000000002 74.7V75.7Q19.400000000000002 82.9 23.300000000000004 86.65Q27.200000000000003 90.4 33.0 90.4ZM94.0 101.4Q81.0 101.4 73.4 94.15Q65.80000000000001 86.9 65.80000000000001 73.4V56.599999999999994Q65.80000000000001 43.099999999999994 73.4 35.849999999999994Q81.0 28.599999999999994 94.0 28.599999999999994Q106.9 28.599999999999994 113.95 35.64999999999999Q121.0 42.699999999999996 121.0 55.0V55.599999999999994H108.0V54.599999999999994Q108.0 48.4 104.55000000000001 44.4Q101.10000000000001 40.4 94.0 40.4Q87.0 40.4 83.0 44.7Q79.0 49.0 79.0 56.4V73.6Q79.0 80.9 83.0 85.25Q87.0 89.6 94.0 89.6Q101.10000000000001 89.6 104.55000000000001 85.55Q108.0 81.5 108.0 75.4V73.6H121.0V75.0Q121.0 87.3 113.95 94.35Q106.9 101.4 94.0 101.4ZM128.8 100.0V30.0H157.60000000000002Q164.20000000000002 30.0 169.25 32.65Q174.3 35.3 177.15000000000003 40.099999999999994Q180.00000000000003 44.9 180.00000000000003 51.5V52.9Q180.00000000000003 59.4 177.05 64.25Q174.10000000000002 69.1 169.05 71.75Q164.00000000000003 74.4 157.60000000000002 74.4H142.00000000000003V100.0ZM142.00000000000003 62.4H156.3Q161.00000000000003 62.4 163.90000000000003 59.8Q166.8 57.199999999999996 166.8 52.699999999999996V51.699999999999996Q166.8 47.199999999999996 163.90000000000003 44.599999999999994Q161.00000000000003 42.0 156.3 42.0H142.00000000000003ZM181.40000000000003 100.0 199.8 30.0H222.8L241.20000000000002 100.0H227.60000000000002L223.8 84.6H198.8L195.00000000000003 100.0ZM201.90000000000003 72.4H220.70000000000002L212.20000000000002 38.3H210.40000000000003Z'
def wordmark(h=30,label='bCPA'):
  w=round(h*264/104,1)
  return f'<svg class="wm" width="{w}" height="{h}" viewBox="0 -2 264 104" role="img" aria-label="{label}"><path d="{WORD_D}" fill="currentColor"/><g class="wdot"><rect x="244.0" y="83" width="17" height="17" rx="3"/></g></svg>'
