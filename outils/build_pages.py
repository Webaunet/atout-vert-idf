import re
R="/home/claude/atout-vert-idf/"
idx=open(R+"index.html",encoding="utf-8").read()
head,rest=idx.split('<main id="contenu">')
foot=rest.split('</main>')[1]
def page(fn,title,desc,cur,body):
    h=head.replace('<title>Atout Vert IDF</title>','<title>%s</title>'%title)
    h=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="%s">'%desc,h)
    h=h.replace(' aria-current="page"','')
    h=h.replace('href="%s">'%cur,'href="%s" aria-current="page">'%cur,1)
    open(R+fn,"w",encoding="utf-8").write(h+'<main id="contenu">\n'+body+'\n</main>'+foot)

TEL='tel:+33660498852'
prest='''<section class="ph pnext-bg" style="--next:var(--bg)">
  <div class="wrap grid">
    <div>
      <p class="eyebrow">Prestations</p>
      <h1>Ce que ATOUT VERT IDF réalise dans votre jardin</h1>
      <p class="lead">Création, terrasses et allées, maçonnerie paysagère et entretien : quatre savoir-faire d'aménagement paysager à Évry-Courcouronnes et alentours.</p>
      <div class="actions"><a class="btn p" href="tel:+33660498852">Appeler le 06 60 49 88 52</a><a class="btn o" href="contact.html">Décrire mon projet</a></div>
    </div>
    <div class="mos"><img src="images/terrasse-bois.jpg" width="1200" height="655" alt="Terrasse en bois en cours de pose devant une maison en pierre"><img src="images/maconnerie.jpg" width="1000" height="545" alt="Muret en pierre et escalier de jardin"><img src="images/creation.jpg" width="1000" height="545" alt="Jardin aménagé avec pelouse et massifs"></div>
  </div>
</section>

<section class="sec bandA" id="creation">
  <div class="wrap pair">
    <div class="txt">
      <p class="eyebrow">Création de jardins</p>
      <h2>Un espace vert pensé pour votre terrain</h2>
      <p>Pelouses, massifs, plantations : l'aménagement est adapté à la surface, à l'exposition et à l'usage que vous faites de votre extérieur.</p>
      <ul><li>Aménagement de pelouses et de massifs</li><li>Plantations d'arbustes et de végétaux</li><li>Préparation et mise en forme du terrain</li></ul>
    </div>
    <div class="imgs two"><img src="images/creation.jpg" width="1000" height="545" loading="lazy" alt="Jardin fraîchement aménagé"><img src="images/plantation.jpg" width="1000" height="546" loading="lazy" alt="Plantation dans un massif de jardin"></div>
  </div>
</section>

<section class="sec svc" id="terrasses" style="--next:var(--s3)">
  <div class="wrap pair rev">
    <div class="txt">
      <p class="eyebrow">Terrasses et allées</p>
      <h2>Des surfaces solides pour circuler et vivre dehors</h2>
      <p>Une terrasse en bois prolonge la maison, une allée dallée ou pavée relie les espaces du jardin.</p>
      <ul><li>Terrasses en bois</li><li>Allées dallées ou pavées</li><li>Cheminements et abords de la maison</li></ul>
    </div>
    <div class="imgs two"><img src="images/allee-dallee.jpg" width="1000" height="545" loading="lazy" alt="Allée dallée en pierre devant une maison, éclairée en soirée"><img src="images/allee-paves.jpg" width="1000" height="545" loading="lazy" alt="Allée pavée et jardin devant une maison"></div>
  </div>
</section>

<section class="sec bandB" id="maconnerie">
  <div class="wrap">
    <div class="head"><p class="eyebrow">Maçonnerie paysagère et entretien</p><h2>Structurer le terrain, puis le garder soigné</h2></div>
    <div class="duo">
      <article><img src="images/maconnerie.jpg" width="1000" height="545" loading="lazy" alt="Pose de pierres pour un muret et un escalier de jardin"><div class="txt"><h3>Maçonnerie paysagère</h3><p>Murets, marches et soutènements en pierre pour structurer un terrain en pente ou en niveaux.</p></div></article>
      <article><img src="images/tonte.jpg" width="1000" height="558" loading="lazy" alt="Pelouse tondue"><div class="txt"><h3>Entretien des espaces verts</h3><p>Un suivi régulier pour garder pelouses et massifs en bon état toute l'année.</p></div></article>
    </div>
  </div>
</section>

<section class="strip">
  <div class="wrap">
    <div><h2>Un projet de terrasse, d'allée ou de jardin ?</h2><p>Laurence Lelièvre et son équipe vous répondent par téléphone.</p></div>
    <div class="actions"><a class="btn p" href="tel:+33660498852">06 60 49 88 52</a><a class="btn o" href="contact.html">Formulaire de contact</a></div>
  </div>
</section>'''

ent='''<section class="ph" style="--next:var(--bg)">
  <div class="wrap">
    <p class="eyebrow">L'entreprise</p>
    <h1>Un paysagiste d'Évry-Courcouronnes depuis 2004</h1>
    <p class="lead">ATOUT VERT IDF est une société d'aménagement paysager de l'Essonne, dirigée par Laurence Lelièvre.</p>
  </div>
</section>

<section class="sec" style="--next:var(--bg2);background:var(--bg)">
  <div class="wrap">
    <div class="head"><p class="eyebrow">Repères</p><h2>Ce que disent les registres officiels</h2><p>Informations issues de l'Annuaire des entreprises et du répertoire SIRENE.</p></div>
    <ul class="kp">
      <li><b>2004</b><span>Année de création de l'entreprise</span></li>
      <li><b>SARL</b><span>Société à responsabilité limitée</span></li>
      <li><b>Métiers</b><span>Inscrite au Répertoire des métiers</span></li>
      <li><b>8130Z</b><span>Services d'aménagement paysager</span></li>
    </ul>
  </div>
</section>

<section class="sec zone" id="zone">
  <div class="wrap pair">
    <div class="imgs"><img src="images/conception.jpg" width="1000" height="545" loading="lazy" alt="Plan de jardin sur tablette, présenté devant un massif"></div>
    <div class="txt">
      <p class="eyebrow">Où nous trouver</p>
      <h2>Évry-Courcouronnes et ses alentours</h2>
      <p>L'entreprise est installée à Évry-Courcouronnes (91000), dans l'Essonne, et intervient dans le secteur.</p>
      <p>Le plus simple pour parler de votre projet : un appel, au mobile ou au fixe.</p>
      <div class="actions" style="margin-top:22px"><a class="btn p" href="tel:+33660498852">06 60 49 88 52</a><a class="btn o" style="color:var(--ink);border-color:var(--forest)" href="tel:+33148816563">01 48 81 65 63</a></div>
    </div>
  </div>
</section>

<section class="sec" style="min-height:70svh;background:var(--forest);color:var(--forest-ink);--next:var(--forest)">
  <div class="wrap"><div class="panel" style="background:transparent;box-shadow:none;padding:0;max-width:44em">
    <h2>Découvrir ce que nous réalisons</h2>
    <p>Terrasses, allées, massifs, murets et entretien : le détail de chaque prestation est sur la page dédiée.</p>
    <div class="actions" style="margin-top:22px"><a class="btn p" href="prestations.html">Voir les prestations</a><a class="btn o" href="contact.html">Nous contacter</a></div>
  </div></div>
</section>'''

cont='''<section class="ph" style="--next:var(--bg)">
  <div class="wrap grid">
    <div>
      <p class="eyebrow">Contact</p>
      <h1>Parlons de votre jardin</h1>
      <p class="lead">Dites-nous ce que vous imaginez : vous obtenez un message prêt à envoyer par SMS à ATOUT VERT IDF. Vous préférez parler ? Un appel suffit.</p>
      <div class="actions"><a class="btn p" href="tel:+33660498852">Appeler le 06 60 49 88 52</a><a class="btn o" href="#formulaire">Remplir le formulaire</a></div>
    </div>
    <div class="leaf"><img src="images/creation.jpg" width="1000" height="545" alt="Jardin aménagé avec pelouse, massifs et allée"></div>
  </div>
</section>

<section class="sec cform" id="formulaire" style="background:var(--bg);--next:var(--bg2);align-items:flex-start">
  <div class="wrap ct">
    <div class="side txt">
      <p class="eyebrow">Votre demande</p>
      <h2>Quatre informations suffisent</h2>
      <p>Votre nom, un numéro pour vous rappeler, votre commune et le type de travaux. Un message libre est possible, sans obligation.</p>
      <ul><li>Création de jardin, terrasse ou allée</li><li>Maçonnerie paysagère</li><li>Entretien des espaces verts</li></ul>
    </div>
    <div>
      <form class="form" id="cform" novalidate>
        <div class="row">
          <div class="fld"><label for="nom">Nom</label><input id="nom" name="nom" type="text" autocomplete="name" placeholder="Prénom et nom" required aria-describedby="e-nom"><p class="err" id="e-nom" role="alert"></p></div>
          <div class="fld"><label for="tel">Téléphone</label><input id="tel" name="tel" type="tel" inputmode="tel" autocomplete="tel" placeholder="06 12 34 56 78" required aria-describedby="e-tel"><p class="err" id="e-tel" role="alert"></p></div>
        </div>
        <div class="row">
          <div class="fld"><label for="commune">Commune</label><input id="commune" name="commune" type="text" autocomplete="address-level2" placeholder="Évry-Courcouronnes" required aria-describedby="e-commune"><p class="err" id="e-commune" role="alert"></p></div>
          <div class="fld"><label for="besoin">Votre besoin</label><select id="besoin" name="besoin" required aria-describedby="e-besoin"><option value="">Choisir…</option><option>Création de jardin</option><option>Terrasse ou allée</option><option>Maçonnerie paysagère</option><option>Entretien des espaces verts</option><option>Autre demande</option></select><p class="err" id="e-besoin" role="alert"></p></div>
        </div>
        <div class="fld"><label for="msg">Message <span class="opt">(facultatif)</span></label><textarea id="msg" name="msg" rows="4" placeholder="Surface, type de terrain, délai souhaité…"></textarea></div>
        <button class="btn p" type="submit">Préparer mon message</button>
      </form>
      <div class="recap" id="recap" hidden tabindex="-1">
        <p class="ok">Message prêt</p>
        <h2 style="font-size:1.4rem">Envoyez-le à ATOUT VERT IDF</h2>
        <pre id="recaptxt"></pre>
        <div class="actions"><a class="btn p" id="sms" href="sms:+33660498852">Envoyer par SMS</a><button class="btn o" type="button" id="copy">Copier</button><a class="btn o" href="tel:+33660498852">Appeler</a></div>
        <p id="copied" role="status" style="margin-top:10px;font-weight:600"></p>
      </div>
    </div>
  </div>
</section>

<section class="sec coord" id="coord" style="background:var(--bg2);--next:var(--forest);min-height:70svh">
  <div class="wrap">
    <div class="head"><p class="eyebrow">Plutôt par téléphone ?</p><h2>ATOUT VERT IDF, à Évry-Courcouronnes</h2></div>
    <ul class="tiles">
      <li><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/></svg><small>Mobile</small><a href="tel:+33660498852">06 60 49 88 52</a></li>
      <li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg><small>Fixe</small><a href="tel:+33148816563">01 48 81 65 63</a></li>
      <li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg><small>Commune</small><span class="v">91000 Évry-Courcouronnes</span></li>
    </ul>
  </div>
</section>'''

page("prestations.html","Prestations – Atout Vert IDF","Prestations d'ATOUT VERT IDF à Évry-Courcouronnes : création de jardins, terrasses et allées, maçonnerie paysagère, entretien des espaces verts.","prestations.html",prest)
page("entreprise.html","L'entreprise – Atout Vert IDF","ATOUT VERT IDF, société d'aménagement paysager installée à Évry-Courcouronnes (Essonne) depuis 2004.","entreprise.html",ent)
page("contact.html","Contact – Atout Vert IDF","Contacter ATOUT VERT IDF à Évry-Courcouronnes : formulaire, téléphone mobile 06 60 49 88 52 et fixe 01 48 81 65 63.","contact.html",cont)
print("ok")
