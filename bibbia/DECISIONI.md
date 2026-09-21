# Decisioni

In caso di dubbio **questo file prevale**.  
Aggiornato: **17 settembre 2026** (restyling presenza + trattini aboliti).

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

## Sedi (quattro, stop)

| Sede | Visite | Chirurgia |
|------|--------|-----------|
| CESAT / San Pietro Igneo, Fucecchio | sì | sì |
| Casa di Cura San Rossore, Pisa | sì | sì (esclusiva) |
| Centro Medico San Verano, Via Cavour 13, Peccioli | sì | no |
| Villa Donatello | no | sì (un po’ borderline rispetto all’esclusiva San Rossore) |

Tutto il resto online è **fuori** dal sito MN.

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
- **Paper**: testo integrale solo se open access (5 su 7); con copyright dell’editore, solo abstract. Approvato da Mauro, da fare **dopo**.
- **Pagina patologia**: sommario sticky a sinistra con voce che si accende; Dove, Ne ho scritto qui e FAQ nel flusso dell'articolo, non in colonna.
- **Recensioni**: citazioni tipografiche una alla volta, virgolette in petrolio chiaro, piattaforma e stelle in eyebrow. Campo `stelle` in Keystatic.

## Fuori v1 (annotato, non costruito)

- Prenotazione / calendario
- Videochiamate
- Area paziente
- Pagamenti
- Widget recensioni live
- Sito del Centro San Verano (lo fa lui)
