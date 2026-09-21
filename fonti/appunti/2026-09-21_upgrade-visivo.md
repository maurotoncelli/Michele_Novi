# Upgrade visivo e copy — 21/09/2026

Ramo: `passata-visiva-schede`. Questo appunto è il piano concordato e lo stato di attuazione. Le decisioni qui prese chiudono due aperti della bibbia (font, banda scura) e vanno riportate in `bibbia/HANDOFF.md` al prossimo giro.

## Diagnosi

Il sito aveva una voce (prima persona, calma, editoriale) ma non una messa in scena: una sola grammatica di fascia (eyebrow + H2 + griglia), Geist 500 a 2.4rem, spaziatura uniforme, titoli-etichetta («Dove», «Perché fidarsi», «Dicono di me», «Prendi contatto»). Risultato: un blog ordinato.

## Principio

Da etichette ad affermazioni. L'eyebrow nomina la sezione (orientamento, SEO), l'H2 dice una cosa che Michele direbbe in visita. Prima persona, luoghi e anni al posto degli aggettivi. Mai un merito («fidarsi», «competente», «eccellenza»).

## Decisioni chiuse

- **Font: General Sans** (Fontshare, licenza FFL, self-hosted in `site/src/app/fonts/`). Una sola famiglia, variabile 200–700. Corpo a 400, titoli a 500 (600 provato e scartato: troppo pesante). Testi grandi non-titolo (recensione, chiusura) in `.citazione` a 400, così sotto un display non pesano quanto lui. Chiude l'aperto «font con spina». (Prima prova: Cabinet Grotesk, scartato dal cliente come «troppo femminile»; General Sans è geometrico, terminali piatti, più deciso.)
- **Scala display** in `globals.css`: `display-xl` (hero), `display-l` (H1 pagine, fasce-affermazione, chiusura), `display-m` (H2 griglia), `cifra` (numeri), `cifra-fondo` (anno dietro al pezzo grande), `lead`, `indice`.
- **Tre misure di fascia** (`Sezione misura=`): `griglia` (schede, py-16/24), `affermazione` (una frase in display-l, py-20/32), `varco` (un oggetto grande). Alternate lungo la pagina.
- **Banda scura di chiusura**: una sola per pagina, `FasciaContatto` su `profondo` (#0f3a5a, petrolio profondo: non nero, colore medico), footer in continuità. Il bottone primario sulla banda diventa osso. Chiude l'aperto «base molto chiara»: resta chiara, l'accordo finale è scuro.
- **Eyebrow indicizzati** in home: `01 Cosa curo … 05 Approfondimenti`.
- **Motion**: titoli display entrano da maschera di riga (`Reveal maschera`, clip su un figlio perché Chrome tiene conto del clip-path del target nell'IntersectionObserver); parallasse hero solo CSS (`animation-timeline: scroll()`), tutto sotto `prefers-reduced-motion`.
- **Foto placeholder** (da sostituire dopo lo shooting; alt lo dichiara): ritratto verticale per hero e Chi sono (`public/images/home/ritratto-verticale-placeholder.jpg`, `public/images/profilo/ritratto-placeholder.jpg`), quattro sedi in `public/images/sedi/`. Le sedi hanno ora `foto[]` in Keystatic; `ModuloSede` e `SchedaSede` preferiscono la foto al disegno.

## Copy (IT / EN in `messages/*.json` e `content/home.yaml`)

| Dove | Prima | Ora |
|---|---|---|
| Hero eyebrow | Dott. Michele Novi · Ortopedico | Dott. Michele Novi · Ortopedico · Toscana |
| Hero lead | Ti dico dove ricevo… | Chirurgo ortopedico. Visito a Fucecchio, Pisa e Peccioli; opero a Fucecchio, Pisa e Sesto Fiorentino. La prima visita serve a decidere la strada, non l'intervento. |
| 01 | Cosa curo | Spalla, gomito, mano. E chi fa sport. |
| 02 | Dove | Quattro sedi, una segreteria. |
| 03 | Perché fidarsi | Boston, Berlino, Seattle. E ogni giorno Fucecchio. (eyebrow «Percorso») |
| 04 | Dicono di me | Dopo la visita. (eyebrow «Recensioni · Doctolib, MioDottore») |
| 05 | Dagli approfondimenti | Quello che scrivo, per colleghi e per pazienti. |
| Chiusura | Prendi contatto | Il primo passo è una visita. |
| Chi sono | In evidenza | Dove ho imparato. (eyebrow «Cinque tappe») |
| Chi sono | Formazione e percorso | Il percorso, anno per anno. |
| Chi sono | Pubblicazioni principali | Quello che ho pubblicato. |
| Chi sono | Docenza e società scientifiche | Insegno · Società scientifiche |
| Dove H1 | Dove ricevo | Dove visito e dove opero. |

Il manifesto di Chi sono («La prima visita può cambiare la strada.») è la prima frase di `profilo.comeValuto`, spezzata in codice: nessun testo nuovo, solo un titolo che prima era nascosto in un box.

Metadata e briciole di Dove usano `nav.dove` («Dove»), non l'H1-affermazione.

## Home, struttura

Hero a due colonne (testo 47%, ritratto a vivo 53%, parallasse) → **Riga dei fatti** (4 sedi · dal 2021 SOC · 2025 Harvard/MGH · 14 pubblicazioni, calcolati dai dati) → 01 Cosa curo (bento) → 02 Dove (città in display, foto) → 03 Percorso (Harvard con cifra di fondo + quattro tappe in lista, da `profilo.inEvidenza`) → 04 Recensioni (una grande, due a lato) → 05 Approfondimenti (una nota grande, paper in lista) → chiusura scura → footer scuro.

`home.fiducia` in Keystatic non è più letto: la fascia 03 usa `profilo.inEvidenza`, che è più ricco. Da rimuovere dallo schema al prossimo giro o riusare.

## Chi sono, struttura

Apertura (ritratto 4:5, nome display-l, apertura come lead, riga fatti: albo · incarico attuale · lingue) → Manifesto (affermazione) → Cinque tappe (varco) → Il percorso, anno per anno (barre) → Quello che ho pubblicato → Insegno · Territorio · Società (testo, non scatole) → chiusura.

## Pagine interne

- Contatti: numero in display-l quando c'è; form con H2 display-m.
- Cosa curo: chiusura come fascia-affermazione su osso.
- Scheda sede: foto a varco 21:9 sotto l'intestazione; H1 display-l.
- H1 di patologia, nota, paper, 404 sulla scala display.

## Seconda passata (feedback cliente, stesso giorno)

- Hero home: la griglia a due colonne è in CSS puro (`.hero-griglia`, `.hero-media`, `.hero-testo` in `globals.css`), non più in classi Tailwind arbitrarie: nel browser del cliente la colonna non si applicava e la foto finiva schiacciata sotto al testo. Altezza minima con tetto a 54rem.
- Cosa curo (home e hub): niente bento con card grande vuota. Quattro righe dense in griglia 2×2: disegno piccolo a sinistra, titolo, lead intero, città dove si tratta. `SchedaPatologia riga`.
- Dove (hub): `SchedaSede` diventa riga (foto 10rem, nome, indirizzo+CAP, regime, servizi). Le due colonne stanno in una schermata.
- Contatti: sedi come lista compatta con miniatura (`ModuloSede compatto`), non più 2×2 con foto grandi.
- Chi sono: ritratto a 13rem/16rem, non più 19/24.

## Terza passata: movimento in home (ramo `versione-miaobau`)

Riferimento portato dal cliente: skyclinics.al (Vite, Lenis, WebGL, cinque video). Preso il gesto, lasciato il peso: niente librerie, niente canvas, niente smooth-scroll dirottato.

- **Hero che si posa**: scendendo, il ritratto a vivo rientra nei margini (`clip-path` inset) e il testo sale e si attenua. `animation-timeline: scroll(root)`, solo ≥1024px e senza reduced-motion. Altrove sta fermo. In `globals.css`: `hero-posa`, `hero-sale`.
- **Cifre che si contano** (`ui/Contatore.tsx`): la riga dei fatti parte da zero (gli anni da 24 prima) quando entra in vista, ~1.1s ease-out. Il server rende il valore finale: senza JS non cambia niente.
- **Percorso a scorrimento** (`blocks/PercorsoScorrevole.tsx`): a sinistra sticky l'anno grande (cambia con `anno-entra`) e la lastra del lavoro; a destra le tappe, quella a metà schermo accesa, le altre al 35%. Sotto 1024px scorre normale, tutto a piena opacità.
- **Lastra del lavoro** (`ui/VideoLastra.tsx`): video muto in loop se c'è (`home.lavoro.video`, file in `public/videos`), altrimenti la foto (`home.lavoro.foto`). Parte solo in vista, `preload="none"`. Oggi c'è il placeholder `lavoro-placeholder.jpg`.
- **Trama**: griglia di punti al 7% sulle fasce osso (`.trama`, un `radial-gradient`).
- **Frecce**: nei bottoni la freccia scorre di 4px all'hover (`svg[data-segno="freccia"]`).

### Ritocchi dopo la revisione del cliente

- **Cifre più piccole**: la riga dei fatti usa `.cifra-m` (tetto 3.3rem, non più 5.25). `.cifra` resta per l'anno sticky del Percorso, ridotto a 4.6rem.
- **Come si opera esce da Cosa curo**: è `area: metodo` nel contenuto, non una patologia. Sta in una fascia sua (`SchedaMetodo`), bianca, tra Cosa curo e Dove: disegno 5/4 a sinistra, eyebrow «Il metodo», titolo display, lead e una riga di copy in più (`cosaCuro.metodoLead`). Stessa cosa nell'hub `/cosa-curo`, prima della chiusura.
- **Tre colonne** (`SchedaPatologia colonna`): Spalla, Gomito e mano, Traumatologia sportiva una accanto all'altra. Lastra 4/5 alta, indice 01–03, titolo grande, lead intero, città, «Scopri» con freccia. Entrano a scatti di 130ms. Il disegno **fluttua** dentro la lastra mentre la si attraversa (`animation-timeline: view()`, `.fluttua`, velocità diverse per colonna via `--fluttua-da/--fluttua-a`); all'hover la lastra vira al petrolio chiaro e il disegno cresce.
- **Binario su mobile** (`.binario`): sotto 640px le tre colonne scorrono in orizzontale a scatti (76vw ciascuna, snap, gutter rispettato con `scroll-padding-inline`); da sm in su è griglia a tre.

### Chi sono e Approfondimenti

- **Apertura Chi sono**: il ritratto prende tutta l'altezza del testo (colonna 19rem/23rem, `h-full`, minimo 28rem); la riga dei fatti chiude in basso col `mt-auto`, allineata al bordo della foto. Ritratto provvisorio **in bianco e nero** generato (`profilo/ritratto-bn.jpg`, mezzo busto in posa, fondo neutro): da sostituire con lo shooting, alt già scritto.
- **Come valuto** non è più una frase sola: `misura="varco"` con titolo display-l, sotto la lastra del lavoro (stessa `home.lavoro`, video se c'è) che fluttua allo scroll, e i **tre passi della visita** numerati 01–03 in rame (`profilo.comeValutoPassi`, campo nuovo in Keystatic: titolo + una riga, IT/EN). Il lead mostra solo la seconda frase del paragrafo, la terza è diventata i passi.
- **Approfondimenti in rotaia** (`ui/Rotaia.tsx` + `.rotaia`): sette schede in fila orizzontale a filo del bordo destro della finestra, snap, linea di avanzamento e due frecce tonde; scroll nativo con trackpad e dito. Note dal lavoro prima, poi i paper. Il bottone della fascia diventa «Vedi tutto in griglia» e porta all'hub `/quaderno`, già a tre colonne con i tab. Per farla sbordare dentro il contenitore centrato: `--sbordo = max(gutter, (100vw − 76rem)/2 + gutter)` usato per margine, padding e `scroll-padding`; `html { overflow-x: clip }` assorbe la barra verticale.

### «Quaderno» non esiste più

Mauro (21/09): la sezione si chiama **Approfondimenti** e basta, in nessun posto «quaderno». Rinominato tutto nel codice: cartella `app/[locale]/approfondimenti/`, collezione Keystatic `approfondimenti` (`content/approfondimenti/`), immagini `public/images/approfondimenti/`, video `public/video/approfondimenti/`, componenti `TabApprofondimenti`/`ListaApprofondimenti`, chiavi messaggi (`nav.approfondimenti`, `home.approfondimentiTitolo`…), route kind `approfondimenti*`, disegno `approfondimenti.png`. Gli URL pubblici erano già `/it/approfondimenti` e `/en/in-depth`; `/quaderno`, `/notebook`, `/insights` restano solo come alias 301.

## Cosa resta

- Shooting: sostituire i placeholder (ritratto, quattro sedi). Nomi file e alt già predisposti.
- Michele valida i titoli in prima persona.
- Telefono: quando arriva, appare in display nella chiusura e in Contatti.
- Strati su Cosa curo (componente esistente, non montato).
- Aggiornare `bibbia/HANDOFF.md`: font chiuso, banda scura chiusa.
