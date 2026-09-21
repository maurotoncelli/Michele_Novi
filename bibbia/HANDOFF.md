# Handoff

> Prima lettura per una chat nuova. Workspace: `Michele_Novi_Website`.  
> Aggiornato: **21 settembre 2026, pomeriggio**. Upgrade visivo «miaobau» sul ramo `versione-miaobau` (4 commit, è la direzione buona); «quaderno» sparito dal codice; in attesa di due sì per la «Lettura» dei paper.

## In una frase

Sito vetrina **veloce, SEO, italiano + inglese, data-driven** per il Dott. Michele Novi: chirurgo di **spalla e arto superiore**, riferimento in Toscana. Deve far capire **cosa fa, dove, come contattarlo**. Niente WordPress, niente prenotazione in v1. Il codice in `site/` **c’è**: v1 strutturale (16/09) + passata visiva (17/09) + upgrade editoriale in movimento (21/09, ramo `versione-miaobau`). Manca il contenuto che dipende da Michele (telefono, dominio, shooting, 7 PDF a pagamento, validazione dei testi in prima persona). Il prototipo HTML in `_archivio/demo-sito-2026-09/` **non si usa**.

## Stato del sito (`site/`)

- **Stack**: Next.js 16 App Router, TypeScript, Tailwind v4, Keystatic (local ora, GitHub in produzione), i18n `/it` `/en` con slug tradotti, Resend per il form, Vercel (`michele-novi-sito`).
- **Pagine**: home · chi-sono · cosa-curo (+ schede) · dove (+ 4 sedi) · **Approfondimenti** (`/it/approfondimenti`, EN `/en/in-depth`; cartella `approfondimenti/`) · **Pubblicazioni** in menu · contatti · privacy · cookie · 404. I vecchi `/quaderno`, `/notebook`, `/insights` fanno 301.
- **Ramo**: si lavora su **`versione-miaobau`**. Mauro (21/09): «è il nostro nuovo ramo principale». `main` è indietro di 4 commit (`4de5b19`…`5fdf69a`): si porta avanti con un fast-forward quando lo dice lui. Build, lint e typecheck puliti all’ultimo commit.
- **Dev**: `cd site && npm run dev` → `:3000`, pannello `/keystatic`. Vedi `site/README.md`. Se si spostano cartelle in `app/`, il dev server va riavviato (le rewrite si calcolano all’avvio).
- **Quando arrivano i dati** si compilano **solo in Keystatic** (o nei YAML): niente da toccare nel codice, salvo bug.
- **Appunti del 21/09** (cosa, perché, come): [`../fonti/appunti/2026-09-21_upgrade-visivo.md`](../fonti/appunti/2026-09-21_upgrade-visivo.md).

## Scelte importanti (chiuse il 17/09)

Non riaprire in una chat nuova se non lo chiede Mauro. Dettaglio: [DECISIONI.md](DECISIONI.md), appunti in [`../fonti/appunti/2026-09-17_restyling-estetico.md`](../fonti/appunti/2026-09-17_restyling-estetico.md).

### Presenza

1. **Riferimenti: Aesop + Odyssée.** Pulizia, crema, un accento, aria. Non si implementano le tavole C/D come fork; non si torna al ramo `restyling-osseo` (sagome).
2. **Lastre piatte.** Niente ombre, niente raggio a blob, niente vetro, niente aloni. Scheda = immagine a vivo + titolo. Hover = titolo petrolio.
3. **Accento azzurro `#1E6AA8`** (`--color-petrolio`). Eyebrow, tag, link, bottone, voce attiva. Non il teal vecchio, non l’azzurro da portale.
4. **Niente trattini sotto i titoli, niente filo a tutta riga, niente cucitura a onda.** Mauro (17/09): sembrano un quaderno; prima era più moderno. Il ritmo è **spazio + fascia crema** (`bg-osso-3` su `Sezione tinta="osso"` e sulle Intestazioni), non una riga. Componente `Cucitura.tsx` **eliminato**.
5. **Font: General Sans** (variabile, self-hosted, `--font-sito`), chiuso il 21/09. Percorso: Geist (neutro) → Cabinet Grotesk (Mauro: «troppo femminile») → General Sans («maschile e moderno»). Pesi: **500** per titoli e display (il 600 era «eccessivamente pesante»), 400 per il corpo; `.citazione`/`.citazione-l` (400) per i testi grandi che non sono titoli (recensioni, chiusure), così titolo e sottotitolo non pesano uguale. Un serif entra **solo** per la «Lettura» dei paper, se approvata (vedi sotto): è una voce diversa voluta, non una seconda famiglia di sito.
6. **Disegni:** quelli in `public/images/disegni/` sono atlas a matita, tappabuchi. Serve un’altra mano (Ciccolella / Ponzi / Amargo…). Non copiare un pezzo.

### Movimento e ritmo (chiusi il 21/09, ramo `versione-miaobau`)

Riferimento portato da Mauro: skyclinics.al. Preso il gesto, non il peso: **niente WebGL, niente GSAP/Lenis, niente smooth-scroll dirottato**. Tutto è CSS scroll-driven (`animation-timeline: scroll()` / `view()`) più tre componenti client piccoli (`Contatore`, `PercorsoScorrevole`, `VideoLastra`, `Rotaia`), tutto dietro `prefers-reduced-motion`.

17. **Banda scura = petrolio profondo `#0f3a5a`** (`--color-profondo`, classe `.fascia-scura`), non nera: «colori più medici». Una sola banda per pagina (contatto + footer continui). Bottone primario dentro la banda in osso.
18. **Hero home** a due colonne in CSS esplicito (`.hero-griglia`, `.hero-media`, `.hero-testo`, non classi arbitrarie Tailwind: nel browser di Mauro non si applicavano). Allo scroll il ritratto «si posa» nei margini (`clip-path`) e il testo sale e si attenua. Solo ≥1024px.
19. **Riga dei fatti** sotto l’hero: cifre che si contano (`Contatore`) in **`.cifra-m`**, misura media. Mauro: le grandi erano «troppo».
20. **Cosa curo (home e hub) = tre colonne** (`SchedaPatologia colonna`): Spalla · Gomito e mano · Traumatologia sportiva, lastra 4/5, indice 01–03, lead intero, città, «Scopri». Il disegno **fluttua** nella lastra allo scroll (`.fluttua`, velocità diverse per colonna). Su mobile scorrono in orizzontale (`.binario`). **«Come si opera» è `area: metodo`, non una patologia**: sta in una fascia sua (`SchedaMetodo`) tra Cosa curo e Dove, con eyebrow «Il metodo».
21. **Percorso (home)**: sticky a sinistra l’anno grande + la lastra del lavoro (`home.lavoro`: foto o video muto in loop, `public/videos/`), a destra le tappe che si accendono a metà schermo. Sotto 1024px scorre normale.
22. **Approfondimenti in home = rotaia orizzontale** (`Rotaia`, `.rotaia`): sette schede a filo del bordo destro, snap, linea di avanzamento, due frecce. Bottone **«Vedi tutto in griglia»** → hub, che resta griglia a tre colonne con i tab (Mauro: «io Approfondimenti lo vedo sempre così»).
23. **Trama** a punti al 7% sulle fasce osso; frecce dei bottoni che scorrono di 4px all’hover; titoli con reveal a maschera.
24. **Chi sono**: ritratto **a tutta altezza del testo** (colonna 23rem, `h-full`, min 28rem), fatti allineati al bordo basso della foto. Ritratto **in bianco e nero** (mezzo busto in posa, fondo neutro): a Mauro «fa impazzire» insieme allo stile editoriale, è la direzione anche per lo shooting vero. **Come valuto** = titolo forte + lastra del lavoro + **tre passi della visita** numerati (`profilo.comeValutoPassi`, campo Keystatic).
25. **Cosa curo (hub)**: righe dense, poi tre colonne; **Dove (hub)**: `SchedaSede` riga compatta, tutto in una schermata; **Contatti**: sedi come lista compatta (`ModuloSede compatto`), non 2×2 con foto grandi.
26. **La sezione si chiama Approfondimenti, punto.** Mauro (21/09): «non voglio che si chiami quaderno da nessuna parte». Rinominato nel codice, nel CMS, nelle cartelle. Non reintrodurre il nome nemmeno in un commento.

### Header e albero

7. **Header desktop = una riga:** nome a sinistra, voci al centro, lingua + Scrivi a destra. Sticky, crema, bordo basso. Il **ruolo sotto il nome è nascosto da `lg` in su**: collideva con il menu. In tablet/mobile il ruolo può restare; hamburger sotto `lg`.
8. **Menu:** Chi sono · Cosa curo · Dove · Approfondimenti · **Pubblicazioni** · Contatti. Non si toglie Pubblicazioni.

### Pagine

9. **Chi sono — apertura.** Ritratto a sinistra, testo a destra. Dal 21/09 il ritratto **prende tutta l’altezza del testo** (vedi 24), non più 4:5 fisso «allineato in alto»: Mauro lo voleva «alto almeno fino alla fine del testo». Sotto il nome sta il titolo professionale (corpo, non maiuscoletto sotto la foto). Poi l’apertura, poi la riga dei fatti (albo, incarico, lingue) in basso. **Niente** monogramma MN, **niente** colophon dei fellowship (è già In evidenza), **niente** didascalia sotto il ritratto.
10. **Dove (hub).** In desktop **due colonne:** Dove visito | Dove opero. Un colpo d’occhio.
11. **Scheda sede.** A destra (sticky in desktop) iframe **Google Maps** (`maps.google.com/...&output=embed`). Query = `nome + indirizzo` (Google piazza il posto; le coordinate in YAML restano per JSON-LD). Info in **griglia iconografica** 2×2: prenota, come arrivare, accessibilità, parcheggio (si spezza il testo se c’è «parchegg-»). Bottone «Apri in Google Maps».
12. **Barre CV** (Formazione e percorso): tre colonne, ogni voce è `grid` **binario + testo**. I puntini stanno nella colonna del filo, **non sopra i titoli**. Non tornare al posizionamento assoluto.

### Pubblicazioni

13. Rosa «tra le principali»: 14 voci, fede in [`../fonti/pdf/PUBBLICAZIONI.md`](../fonti/pdf/PUBBLICAZIONI.md).
14. **PDF originali solo se open access.** 7 file in `site/public/paper/` (+ copia in `fonti/pdf/paper/`). Campo Keystatic `pdf`. Bottone **PDF**.
15. **Paywall (7):** niente file hostato. Bottone **Articolo** → DOI (`hrefArticolo`). Li deve mandare lui (accepted manuscript / copia autore) se li vuole in sito: 3D Minerva, scafoide Minerva, gomito AOTS, lussazione bloccata, Gartland/Injury, claims PTH, head-split JBJS.

## Cosa è ancora aperto (design)

- ~~Font con più carattere~~ chiuso: General Sans (21/09).
- Famiglia illustrazioni. Nella rotaia i paper sulla spalla mostrano tutti lo stesso disegno (scelto dal tag): se serve varietà, si assegna un’`immagine` ai paper principali da Keystatic, non un trucco nel codice.
- Shooting: ritratto (**in bianco e nero, mezzo busto in posa**, è la direzione) e foto delle sedi e del lavoro (`home.lavoro`). Oggi placeholder generati; nomi file e alt già pronti.
- Scelta C vs D del 16/09: **superata come fork**; l’hero è già foto full-bleed, le fasce sono piatte + disegni-tappabuchi.

### «Lettura» dei paper: proposta in attesa di due sì (21/09)

Idea di Mauro: per i paper con PDF, estrarre il testo e metterlo nella pagina dell’articolo «con stile universitario, font specifico, aspetto autorevole, come fosse un testo a sé». **Possibile**: i 7 PDF hanno testo estraibile pulito (provato con pypdf). Il paletto è il **copyright**, letto dentro ogni PDF:

| Paper | Rivista | Copyright | Cosa si può mettere |
|---|---|---|---|
| Remplissage Hill-Sachs 2022 | Osteology (MDPI) | © autori, CC BY | testo integrale |
| Cuffia irreparabile 2018 | Orthopedic Research and Reviews (Dove) | © Novi et al., CC BY-NC | testo integrale |
| Frattura periprotesica omero 2021 | Geriatric Orthop. Surg. & Rehab. (SAGE) | © autori, CC BY-NC | testo integrale |
| Tecnologia protesi spalla 2019 | J. Orthop. Traumatol. (Springer OA) | © autori, CC BY | testo integrale |
| Bicipite distale 2020 | Acta Biomedica (Mattioli) | OA, CC BY-NC-ND | testo integrale **tal quale**, non riadattato |
| Chirurgia assistita protesi inversa 2021 | Indian J. Orthop. | © Indian Orthopaedics Association | **solo abstract** + link |
| Fratture periprotesiche spalla 2018 | Lo Scalpello 2018 (Springer) | © SIOT | **solo abstract** + link |

Progetto: sotto la testata esistente (titolo, autori, rivista, DOI, bottoni PDF/Articolo) una sezione **«Lettura»** impaginata come estratto da rivista: serif accademico self-hosted **solo lì** (candidati **Newsreader** o **Source Serif 4**, licenze libere), colonna ~62 caratteri, titoli di sezione in maiuscoletto (Abstract, Introduction, Methods, Results, Discussion, Conclusions), capolettera, bibliografia in coda, riga di attribuzione «© autori, licenza…, riprodotto da…» con DOI. In inglese com’è. Sopra resta il **«In breve, per chi non è medico»** in General Sans. Il testo va in Keystatic (campo `testoIntegrale`, markdown a sezioni), estratto con uno script e **ripulito a mano** (sillabazioni, didascalie, numeri di pagina, intestazioni di colonna, riferimenti): circa 30–40 pagine di rivista, lavoro editoriale.

**Decisioni che servono da Mauro:** (1) integrale per i 5 OA + abstract per i 2 con copyright editore, oppure abstract per tutti; (2) Newsreader o Source Serif 4, o una pagina di prova con entrambi.

### Idee proposte il 21/09, non decise

- Pagina sede come luogo: foto grande a vivo, orari e come arrivare come «scheda di viaggio», mappa monocroma nei colori del sito al posto dell’embed Google colorato.
- Pagina patologia con sommario sticky a sinistra (sintomi, diagnosi, cure, chirurgia, recupero, FAQ) e voce attiva che si accende, come il Percorso in home.
- Cifre animate anche in Chi sono (stesso `Contatore`, misura `cifra-m`).
- Transizioni di pagina con la View Transitions API (il titolo della scheda «vola» al titolo della pagina), solo CSS.
- Recensioni come citazioni tipografiche: virgolette grandi in petrolio chiaro, una alla volta in orizzontale.
- Piè di pagina con la firma: nome in display-l a tutta larghezza come chiusura editoriale.

## Deploy e repo

- **Vercel**: `michele-novi-sito`, team ATSTUDIO, root `site`, Node 24. <https://michele-novi-sito.vercel.app>. Env: `KEYSTATIC_STORAGE=github`, owner/repo `maurotoncelli/Michele_Novi`, `KEYSTATIC_PATH_PREFIX=site`. Da aggiungere: chiavi GitHub App, `KEYSTATIC_SECRET`, `RESEND_API_KEY`, `NEXT_PUBLIC_GA_ID`.
- **Git**: un repo alla radice (bibbia + fonti + site). GitHub `maurotoncelli/Michele_Novi`, **privato**. Vercel builda solo `site/`.
- **robots.txt**: `Disallow: /` finché `settings.dominio` è vuoto. Appena c’è il dominio, Keystatic → settings → Dominio.
- **Dominio**: lo compra il cliente. Poi Vercel Domains + DNS.
- Tutto il lavoro del 21/09 è **committato** su `versione-miaobau` (ultimo: `5fdf69a`), non pushato: il push e il fast-forward di `main` li decide Mauro.

## Cosa è successo

| Data | Cosa |
|------|------|
| 28/08/2026 | Primo contatto. Brief: chiarezza, SEO, vetrina, IT+EN. |
| 31/08 | Preventivo 1.500 € confermato. |
| 4/09 | Prima bibbia. |
| ~inizio/09 | Demo HTML magnetica. **Archiviata.** |
| set 2026 | Incontro San Verano. Sedi, perimetro, P. IVA. |
| 16/09 | CV 2026. Stack + v1 in `site/`. Repo + Vercel. Mauro: troppo statico, serif no → Geist, hero full-bleed. |
| 16/09 sera | Menu **Approfondimenti**. |
| 17/09 | **Pubblicazioni** in menu. 14 paper da Drive; 7 PDF OA. Recensioni in Keystatic. Restyling Aesop/Odyssée: header a una riga, lastre piatte, petrolio `#1E6AA8`, Dove a due colonne, Maps + icone in sede, barre CV sistemate. **Trattini e cucitura via** (effetto quaderno). |
| 21/09 mattina | Piano «upgrade awwwards» e prima passata (ramo `passata-visiva-schede`, poi in `main`): copy dei titoli come affermazioni, tre tipi di fascia, banda scura, hero a due colonne, Chi sono ristrutturata, placeholder generati. Correzioni di Mauro: hero rotta nel suo browser → CSS esplicito; Cabinet Grotesk «troppo femminile» → General Sans; pesi 600 «troppo pesanti» → 500 + `.citazione`; Cosa curo e Dove «più informazioni a colpo d’occhio» → righe dense; banda «non nera» → `#0f3a5a`; sedi in Contatti e ritratto in Chi sono «troppo grandi» → compatti. |
| 21/09 pomeriggio | Ramo **`versione-miaobau`** («nuovo ramo principale»). Da skyclinics.al senza librerie: hero che si posa, cifre che si contano, Percorso sticky con lastra del lavoro, trama, frecce. Poi: cifre `cifra-m`; **Come si opera fuori da Cosa curo** (fascia «Il metodo»); Cosa curo a **tre colonne che fluttuano**; Chi sono con **ritratto b/n a tutta altezza** (Mauro: «mi fa impazzire»); **Come valuto** con lastra e tre passi; Approfondimenti in **rotaia** + «Vedi tutto in griglia»; **«quaderno» rinominato ovunque** in `approfondimenti`. Proposta «Lettura» dei paper con verifica copyright: in attesa. |

## Cosa fare adesso (ordine)

**Dati (bloccano il go-live, non il design)**

1. Far **ricontrollare il cellulare** (348 4332733 detto vs 348 4331733 online). Poi `settings.telefono` / `whatsapp`.
2. Dominio (cliente) → `settings.dominio`. Orari segreteria → `settings.orari`.
3. 7 PDF paywall da Michele, se li vuole sul sito.
4. URL delle 4 schede Google. Shooting ritratto (b/n, mezzo busto) + sedi + lavoro.
5. Far validare le bozze `site/content/patologie/*`.
6. **Far validare a Michele i testi in prima persona scritti il 21/09** (sono in Keystatic/messages, non nel codice): titoli-affermazione delle fasce home (`home.*Titolo`), i tre **passi della visita** (`profilo.comeValutoPassi`), la riga del **metodo** (`cosaCuro.metodoLead`: «Prima di dire come si opera, si decide se operare…»), la chiusura di Cosa curo, le tappe del Percorso.

**Decisioni di Mauro in sospeso**

7. Fast-forward di `main` su `versione-miaobau`.
8. «Lettura» dei paper: integrale per i 5 OA + abstract per i 2, o abstract per tutti; Newsreader o Source Serif 4.
9. Quale delle idee del 21/09 fare per prima (sede come luogo, sommario sticky in patologia, transizioni…).

**Design (non bloccante, non mescolare)**

10. Nuova mano di disegni; sostituire l’atlas. Foto/video vero del lavoro al posto di `lavoro-placeholder.jpg`.
11. Telefono: quando arriva, appare in display nella chiusura di Contatti (già predisposto).

Il codice è pronto ma i campi vuoti restano vuoti. Non inventare telefono, orari o civici «tanto poi si cambia».

## Vincoli che non si riaprono

Elenco pieno: [DECISIONI.md](DECISIONI.md). I quattro che evitano errori:

1. **Multipagina**, non one-page.
2. **Quattro sedi**, stop. CESAT, San Rossore, San Verano (solo visite), Villa Donatello (solo chirurgia).
3. Stack: Next.js + Tailwind + TypeScript + Keystatic + Vercel + i18n `/it` `/en`.
4. Form: nome + recapito + consenso. **Mai** dati clinici. Prezzi **non** online.

## Cosa non fare

- Non copiare `_archivio/demo-sito-2026-09/`.
- Non rimettere trattini sotto i titoli, filo a tutta riga, cucitura a onda, monogramma MN, ruolo in header desktop.
- Non hostare PDF di riviste a pagamento. Non riprodurre il testo integrale dei paper con copyright dell’editore (Indian J. Orthop. 2021, Lo Scalpello 2018): solo abstract.
- Non chiamare la sezione «quaderno», da nessuna parte.
- Non aggiungere librerie di animazione (GSAP, Lenis, Framer, WebGL): il movimento è CSS scroll-driven + componenti client piccoli, sempre dietro `prefers-reduced-motion`.
- Non usare classi Tailwind arbitrarie per griglie critiche (hero): CSS esplicito in `globals.css`.
- Non inventare sedi. Non nominare Nicoletti. Non ostentare che San Verano è suo.
- Non pubblicare Alonso senza consenso. Non fondere quattro indirizzi in una scheda Google.
- Non committare `.env`, token, password. Non committare se non lo chiede Mauro.

## Chi è

- **Dott. Michele Novi**, nato 27/10/1987. Albo Pisa n. 5749.
- Dirigente medico, **SOC Ortopedia Protesica**, San Pietro Igneo / CESAT, Fucecchio, dal 2021. Fellowship 2025 a **Harvard / MGH** (Elhassan). Focus spalla e arto superiore; anche sport, artroscopia, protesi; anca/ginocchio in ospedale.
- Segreteria. Studio pieno: il sito **allinea**, non “riempie l’agenda”.
- Introdotto da Lorenzo Querci. Ha visto il sito di Mauro: troppo complicato.

Contatti di lavoro: [03_sedi_e_contatti.md](03_sedi_e_contatti.md).

## Prompt minimo per una chat nuova

```
Leggi bibbia/HANDOFF.md e bibbia/DECISIONI.md, poi site/README.md
e fonti/appunti/2026-09-21_upgrade-visivo.md.
Workspace: Michele_Novi_Website. Il sito è in site/ (Next.js + Keystatic).
Ramo di lavoro: versione-miaobau.
Non usare _archivio/demo-sito-2026-09.
Non rimettere trattini sotto i titoli né la cucitura. Niente librerie di animazione.
La sezione si chiama Approfondimenti, mai «quaderno».
Testi e dati stanno in site/content e site/src/i18n/messages: niente hardcoded nelle pagine.
Compito: …
```
