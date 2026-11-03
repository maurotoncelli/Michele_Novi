# Decisioni

In caso di dubbio **questo file prevale**.  
Aggiornato: **3 novembre 2026** (recepiti tutti i feedback del Dott. Novi dalla presentazione `MODIFICHE SITO MN.pptx`; dettaglio in `fonti/appunti/2026-11-03_feedback-pptx-michele.md`).

Le voci **PROPOSTA** sono di Mauro, non firmate da Michele.

---

## Relazione e offerta

- Cliente: Dott. Michele Novi. Introduzione: Lorenzo Querci.
- Job CRM **#64**, contatto **#1003**.
- Preventivo **1.500 €** confermato il 31/08/2026 (validità 31/10/2026).
- Pacchetto: sito vetrina + shooting + blog/articoli editabili + SEO di base + go-live. **Senza** calendario in v1.
- Proprietà: codice e contenuti al cliente a saldo. Dominio intestato a lui.
- Gestionale (agenda, cartelle, pagamenti): **fuori scope**.

## Cos’è il sito MN

- Tre compiti in superficie: **cosa fa, dove lo fa, come contattarlo**.
- «Landing page» = chiarezza, **non** monopagina.
- Architettura **multipagina**, albero rovesciato: semplice sopra, profondo sotto.
- Il sito è la **fonte di verità**. I terzi si allineano o si spengono.
- Lo studio è pieno: si allinea la presenza online, non si “procacciano pazienti a vuoto”.
- MN e SV sono **due siti**. SV lo fa Michele; non si ostenta la proprietà.

## Perimetro clinico (incontro San Verano)

- In evidenza: **chirurgia della spalla e dell’arto superiore**.
- Gomito e mano stanno **dentro** l’arto superiore, non come brand a parte.
- Traumatologia sportiva: **sì, con peso**.
- Anca e ginocchio: **sì, ma secondarie** rispetto alla spalla. Testi utili sul vecchio centrosaluteonline.
- Ecografia: solo **esito della sua visita**. Non centro eco su invio di altri.
- Pagina sul **come si opera** (artroscopia / metodo): sì.
- Microchirurgia della mano: formazione vera, **non** servizio di punta.
- CESAT: **Dirigente medico, SOC Ortopedia Protesica**, Ospedale San Pietro Igneo, Fucecchio, dal maggio 2021. Non scrivere “direttore SOC”.
- **Simone Nicoletti: non nominarlo** sul sito MN.
- Maestri e fellowship: **si possono nominare tutti**. Inclusa, dal CV 2026: **MGH Boston / Harvard 2025, Bassem Elhassan** (transfer muscolari di spalla). È la voce che manca su San Rossore.
- Date LinkedIn post-specializzazione (Pisa 2019–20, Modena 2020–21): **confermate**.
- Canone CV: file **Michele Novi CV 2026.docx**. Il PDF europeo 2019 è storico.
- Albo OMCeO Pisa **n. 5749**. Inglese C1. Non pubblicare il tedesco A1 del PDF 2019.

## Sedi (divise in Dove visito e Dove opero — aggiornato 03/11/2026)

| Sede | Visite | Chirurgia |
|------|--------|-----------|
| Casa di Cura San Rossore, Viale delle Cascine 152/F, Pisa | sì | sì (esclusiva) |
| Studi Medici San Pietro, Piazza Toscanini 3, Fucecchio | sì | no |
| Centro Medico San Verano, Viale Cavour 13, Peccioli | sì | no |
| CESAT — Ospedale San Pietro Igneo, Piazza Lavagnini 5, Fucecchio | no | sì (SSN) |
| Villa Donatello, Via Attilio Ragionieri 101, Sesto Fiorentino | no | sì |

- **Dove visito** mostra la mappa illustrata della Toscana nella palette del sito con i 3 pin (Pisa, Fucecchio Piazza Toscanini 3, Peccioli) e i loghi delle strutture (niente foto delle città).
- **Dove opero** mostra le 3 strutture chirurgiche (San Rossore, CESAT Fucecchio, Villa Donatello) con le foto reali degli edifici fornite da Michele.
- Tutto il resto online è **fuori** dal sito MN.

Convenzione di esclusività chirurgica con San Rossore: nota interna, non da sbandierare in home.

## Contatto

- Un solo numero pubblico, da **ricontrollare** (vedi APERTI). Il 329 **non** va online.
- WhatsApp: sì, sul numero pubblico, testo precompilato **non clinico**.
- Canale di prenotazione sul sito: **segreteria**, non Doctolib come bottone principale.
- Nessun telefono di Fucecchio / CUP / centralini struttura sul sito MN.
- Prezzi: **non online**. Li dice la segreteria. Niente convenzioni in elenco.
- Recensioni: nome e cognome **per esteso**; pezzi curati a mano, dalle sue screenshot.

## Dominio e dati legali

- Dominio **nuovo** (nome ancora da scegliere).
- Vecchio sito: `centrosaluteonline.it`, **ancora suo** → tenerlo acceso e fare 301 quando il nuovo è live.
- Titolare: Dott. Michele Novi. P. IVA **02296540509**. PEC **michele.novi.w5is@pi.omceo.it**.

## Stack

- Next.js App Router + TypeScript + Tailwind.
- Hosting Vercel.
- CMS Keystatic nel repo (foto, testi, sedi, paper, 1 nota blog). Niente WordPress, niente CMS a canone, niente database pazienti.
- i18n: italiano + inglese, rotte `/it` `/en` (stile maurotoncelli.it).
- Form: email transazionale, niente dati sanitari.
- Analytics: GA4 + Search Console, cookie dopo consenso.

## SEO

- HTML gerarchico, un H1 a pagina, sitemap, JSON-LD, keyword vere.
- Indicizzazione pensata anche per motori conversazionali (titoli chiari, FAQ, `llms.txt` da valutare).
- Blog / articoli come motore nel tempo, collegabile a YouTube e reel.
- **PROPOSTA:** niente pezzi da agenzia SEO.

## Contenuti

- I paper del Drive vanno **tutti**, impaginati da articoli scientifici, DOI/link fonti funzionanti.
- PDF in sito **solo OA** (`site/public/paper/`). Paywall: bottone Articolo → DOI, niente file. I 7 mancanti li manda lui.
- Blog non scientifico: **1 placeholder** al lancio (non tre).
- Chi pubblica: **Michele**.
- Caso Alonso: solo con consenso. Default: non pubblicare il nome.
- Foto: shooting reale, niente stock.
- Form: niente descrizione del problema.

## Design

- Moderno, fruibile, distinto. Base molto chiara, non giallognola. Un accento.
- **Riferimenti chiusi (17/09):** Aesop + Odyssée — pulizia, crema, aria. Lastre **piatte** (niente ombra, blob, vetro). Accento **`#1E6AA8`**.
- **Niente trattini** sotto i titoli, niente filo a tutta riga, niente cucitura a onda. Mauro: effetto quaderno. Ritmo = spazio + fascia `osso-3`.
- Header desktop: **una riga** (nome | menu | azioni). Ruolo sotto il nome **nascosto da lg**. Menu include **Pubblicazioni**.
- Chi sono: ritratto + testo in alto; titolo sotto il nome. Niente MN, niente colophon, niente didascalia sotto la foto.
- Dove hub: **due colonne** desktop (visito | opero). Scheda sede: **Google Maps** (query nome+indirizzo) + griglia icone (prenota / arrivare / accessibilità / parcheggio).
- Barre CV: puntini in colonna propria, non assoluti sul testo.
- Font: **Geist** (unico). Un sans più marcato è ancora aperto; non si mescolano famiglie.
- Disegni atlas in `public/images/disegni/`: tappabuchi. Altra mano da scegliere.
- Appunti: `fonti/appunti/2026-09-17_restyling-estetico.md`.
- Informazione ad albero: sintesi in superficie, termini precisi in profondità.
- Motion fluida. Non cursori o magnetismo che **rallentano**.
- Recensioni e schede sede curate. Home più semplice del portfolio Mauro.

### Chiuse il 21/09 (dettaglio in [HANDOFF.md](HANDOFF.md) §Movimento e ritmo)

- **Font General Sans**, pesi 500 titoli / 400 corpo. Geist e Cabinet Grotesk fuori. Un serif solo per la «Lettura» dei paper, se approvata.
- **Banda scura petrolio profondo `#0f3a5a`**, non nera.
- **Movimento senza librerie**: CSS scroll-driven + componenti client piccoli, sempre dietro `prefers-reduced-motion`. Riferimento skyclinics.al per il gesto, non per lo stack.
- **Cosa curo a tre colonne**; **Come si opera** è metodo, fascia a sé.
- **Ritratto in bianco e nero**, mezzo busto in posa, a tutta altezza del testo in Chi sono: direzione anche per lo shooting.
- **Approfondimenti** è il solo nome della sezione: «quaderno» non esiste, nemmeno nel codice.
- **Paper**: testo integrale solo se open access (5 su 7); con copyright dell’editore, solo abstract. **Fatto** il 21/09 sera: campi `testoIntegrale` e `licenza`, serif Source Serif 4 solo nella Lettura, sommario sticky.
- **Pagina patologia**: sommario sticky a sinistra con voce che si accende; Dove, Ne ho scritto qui e FAQ nel flusso dell'articolo, non in colonna.
- **Recensioni**: citazioni tipografiche in misura da lettura (24rem, 1.2rem), virgolette piccole in petrolio chiaro, piattaforma e stelle in eyebrow, parole che si compongono. Campo `stelle` in Keystatic. La versione «una alla volta, gigante» è stata bocciata.
- **Scorrimento orizzontale in home** (recensioni, approfondimenti): **niente frecce né snap**. Desktop: la sezione si appunta e le schede scorrono con lo scroll della pagina (CSS scroll-driven). Telefono: colonna. Mauro: «controlli scomodi; automatici su desktop, verticali su smartphone».
- **Chi sono, «Dove opero, dove ho imparato»**: grande = **l'incarico di oggi** (Fucecchio, dal 2021; flag `attuale` in Keystatic), a destra le fellowship **in ordine cronologico**. Prima era grande la prima voce dell'elenco (Harvard 2025) senza un criterio leggibile e l'elenco non era in ordine: Mauro ha chiesto il senso della gerarchia. Regola: la dimensione deve dire qualcosa (presente vs percorso). `inEvidenza` va tenuto cronologico perché la home lo scorre in quell'ordine.
- **Titolo del percorso in home** (aggiornato 03/11 su richiesta di Michele): eyebrow **«Percorso formativo»**, titolo **«Incarichi professionali e fellowship internazionali.»**, mantenendo lo **scorrimento sticky originale** (`PercorsoScorrevole.tsx`, con l'anno grande e la foto fermi a sinistra che si aggiornano scorrendo le tappe a destra).

### Chiuse il 03/11 (presentazione `MODIFICHE SITO MN.pptx` di Michele)

- **Hero Home e Fascia Profilo clinico**: gerarchia invertita (ispirazione `chirurgie-coude.fr`): sopra in piccolo elegante `Dott. Michele Novi`, sotto in grande (H1) **`Chirurgia della Spalla. Arto Superiore. Protesica`**. Il sottotitolo e i due paragrafi descrittivi di Michele stanno subito sotto la Hero in colonna singola (`FasciaIntro`, eyebrow `Profilo clinico`), al posto della vecchia `FasciaFatti` coi numeri (rimossa perché poco comprensibile per il paziente).
- **Nomenclatura sezioni e menu**:
  - La voce di menu e il titolo della pagina `/cosa-curo` diventano **«Percorsi di cura»** (non più «Cosa curo»), con nuovo lead scritto da Michele (*«Trattamenti personalizzati basati sulle evidenze scientifiche. L'ascolto del paziente porta ad una corretta diagnosi, la fiducia nel medico ad una rapidità nei risultati.»*).
  - In Home la sezione `01` si intitola **«Patologie trattate»**.
  - L'eyebrow dei sintomi diventa **«Per il paziente»** (con titolo «Parti da quello che senti.» e senza la frase a destra nell'hub); aggiunto il 9° sintomo sul ginocchio (*«Ho sempre più difficoltà a camminare e fare le scale»*); nell'hub `/cosa-curo` la fascia sintomi ha sfondo azzurro chiaro (`bg-petrolio-3`) e griglia 3×3 per staccare dal blocco bianco sottostante (*La spalla.*).
  - Rimosse da tutte le card di patologia le caption inferiori con numero di pubblicazioni e città (`4 pubblicazioni · Pisa · Peccioli`, ecc.).
- **Il metodo → «Attività chirurgica»**: titolo cambiato da «Come si opera» a **«Attività chirurgica»**, nuovo testo introduttivo di Michele, **4 icone senza sottotitoli** (`Artroscopia`, `Chirurgia open`, `Chirurgia protesica`, `Ecografia interventistica`) e chiusura *«L'indicazione precede la tecnica. Una corretta diagnosi è il punto da cui partire.»*. Foto del chirurgo sostituita con la versione modificata da Michele con il **camice sterile da sala operatoria** (compressa a `103.7 KB`).
- **Dove visito / Dove opero ovunque**: divise in **Home**, **`/dove`**, **`/contatti`** e nelle schede patologia; in **Dove visito** mappa vettoriale reale ad alto dettaglio della Toscana (senza triangolo tratteggiato né linea FI-PI-LI/Arno) e 3 card con riquadri logo uniformi (`logo-san-rossore.png`, `logo-san-pietro.png` ricostruito in vettoriale dal cartello di Piazza Toscanini 3, `logo-san-verano.png`).
- **Logo ufficiale del Dott. Michele Novi**: estratto in vettoriale da `fonti/pdf/logo_michele_novi.ai`/`.pdf` (`site/src/components/ui/Logo.tsx`, `site/public/images/logo-michele-novi.svg`/`.png`) e inserito in `Header.tsx` (al posto dell'icona provvisoria nel quadrato), `Footer.tsx`, `opengraph-image.tsx` e favicon (`icon.svg`, `apple-icon.png`, `favicon.ico`).

## Fuori v1 (annotato, non costruito)

- Prenotazione / calendario
- Videochiamate
- Area paziente
- Pagamenti
- Widget recensioni live
- Sito del Centro San Verano (lo fa lui)
