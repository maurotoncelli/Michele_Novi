# 04. Architettura dell'informazione

> Parte della Bibbia. Indice: [00_README_Master_Index.md](00_README_Master_Index.md).
> Contenuti candidato (non copy): [`../ricerca/2026-09-04_quadro-dottor-novi.md`](../ricerca/2026-09-04_quadro-dottor-novi.md).
> Conferme da call: [DOMANDE_APERTE.md](DOMANDE_APERTE.md) (checklist in testa).

## Metadati
- ID: CAP-04
- Stato: Bozza (scheletro pagine 2026-09-04; testi e NAP da validare)
- Ultimo aggiornamento: 2026-09-04
- Dipendenze: @01_Visione, @03_Brand, @06_SEO, @08_Sedi, @09_Recensioni, @10_Blog, @15_Profilo
- Owner: Mauro

## Sintesi
Struttura **multipagina**. Home da landing (orienta e converte), sezioni autonome che si potranno approfondire. Questo capitolo è lo **scheletro a parole**: cosa c'è su ogni pagina, in che ordine, con quale materiale già trovato online e cosa **non** si pubblica finché Michele non conferma.

Allineata al piano tecnico del 29/08 (Home, Chi sono, aree, Dove ricevo, Contatti, Blog) con due precisazioni SEO: **una URL per sede attiva** e **una URL per area di trattamento**, più privacy/cookie.

Niente di quanto segue è copy definitivo. I prezzi, il telefono, le sedi, il titolo al CESAT e il modo di citare il collega Nicoletti restano **placeholder**.

---

## Stato attuale del progetto

### Perché non one-page
Michele ha detto «landing page». In gergo spesso significa «una pagina sola». Qui è sbagliato per tre motivi:

1. Vuole **potenziare** il sito (agenda, articoli, YouTube): un one-page diventa un cimitero di ancore.
2. La SEO locale vive su URL distinti (`/sedi/fucecchio`, `/patologie/cuffia-dei-rotatori` o `/patologie/spalla`).
3. L'EN ha bisogno di URL e title propri, non di un blocco nascosto.

La home può comunque *sembrare* una landing: hero, pochi blocchi, CTA fisso.

### Chrome globale (tutte le pagine)

**Header**
- Wordmark: Dott. Michele Novi (o logo se arriverà).
- Sottotitolo corto solo su mobile ridotto / desktop discreto: *Ortopedico · spalla e arto superiore* (D5).
- Menu: Chi sono · Cosa curo · Dove ricevo · [Nome blog] · Contatti.
- Lingua: IT | EN.
- CTA persistente: **Chiama** (`tel:` sul numero confermato) + secondario **Scrivi** (ancora a `/contatti`). WhatsApp solo se il numero pubblico è anche WhatsApp.

**Footer**
- Nome, specialità in una riga, telefono, orari segreteria, email `info@` se esisterà.
- Elenco sedi attive (solo nome città + link), non un secondo romanzo.
- Instagram, LinkedIn, Doctolib (finché resta il canale prenotazione).
- Privacy, cookie, crediti shooting/Mauro se si usa.
- P. IVA e titolare del trattamento: quando li abbiamo. Non inventarli.

**Elementi ricorrenti (componente, non pagina)**
- Fascia «Segreteria»: lun–gio, fascia oraria, cosa succede se chiami fuori orario (ririchiamo / Doctolib — da chiedere).
- Disclaimer sanitario corto in patologie e articoli: *non sostituisce la visita*.
- Niente form clinico da nessuna parte.

**Due geografie da non mescolare** (quando si scrivono le sedi)
- **Dove visito** = ambulatori di libera professione.
- **Dove opero** = ospedale / cliniche di ricovero (CESAT; Villa Donatello se confermato come solo ricovero). In vetrina non devono sembrare lo stesso tipo di appuntamento.

---

### Mappa rotte v1

Stesso albero sotto `/en/...` con slug tradotti e hreflang. `x-default` ? `/it`.

| Rotta IT | Pagina | In menu v1 |
|----------|--------|------------|
| `/it` | Home | logo |
| `/it/chi-sono` | Chi sono | sì |
| `/it/patologie` | Hub «Cosa curo» | sì (voce unica) |
| `/it/patologie/spalla` | Spalla | no (dall'hub e dalla home) |
| `/it/patologie/gomito` | Gomito | no |
| `/it/patologie/mano` | Mano e polso | no |
| `/it/patologie/traumatologia-sportiva` | Traumatologia sportiva | no |
| `/it/patologie/artroscopia` | Artroscopia (metodo) | no |
| `/it/patologie/ecografia-muscoloscheletrica` | Eco MSK | no |
| `/it/patologie/protesi-anca-ginocchio` | Solo se D5 = sì | no |
| `/it/sedi` | Dove ricevo (hub) | sì |
| `/it/sedi/[slug]` | Una sede attiva | no |
| `/it/contatti` | Contatti | sì + CTA |
| `/it/articoli` (nome visibile TBD, D7) | Indice blog | sì se c'è almeno 1 pezzo |
| `/it/articoli/[slug]` | Articolo | no |
| `/it/privacy`, `/it/cookie` | Legale | footer |
| `/it/404` | Non trovato | — |

Slug sede: città o nome struttura (`fucecchio-san-pietro`, `peccioli-san-verano`, `pisa-athletica`, `capannoli-minihospital`, …) — si chiudono quando la lista è spuntata.

**PROPOSTA:** «Artroscopia» è una pagina **metodo** (come si opera), non una sesta articolazione. Evita di ripetere cuffia/instabilità due volte. Il piano tecnico la elencava come area: resta in IA, ma con questo ruolo.

**Non in v1 (rotte riservate, non in menu)**
- `/it/prenota` — calendario futuro.
- `/it/video` o sezione YouTube.
- `/it/pubblicazioni` — per ora un blocco in Chi sono basta; pagina propria se i paper crescono.
- `/it/faq` — le FAQ vivono nelle patologie; una FAQ globale solo se servono 8+ domande vere.

---

## Scheletro pagina per pagina

Ogni blocco è **proposta di contenuto**. Dove c'è già testo online lo si indica come *candidato*, da far rileggere a Michele. Non copiare i terzi alla lettera (Doctolib, MiniHospital): riformulare, far firmare.

### 1. Home — `/it`

**Scopo.** In pochi secondi: chi è, cosa cura, dove lo trovi, come lo chiami. Non il CV. Non dieci sedi in hero.

**H1 (bozza).** Dott. Michele Novi — chirurgo ortopedico, spalla e arto superiore.  
(Se D5 include anca/ginocchio in superficie: una riga sotto, non nel H1.)

**Title SEO (bozza).** Ortopedico spalla e arto superiore in Toscana | Dott. Michele Novi

**Blocchi, dall'alto**

1. **Hero.** Ritratto shooting (placeholder finché non c'è). Nome. Una frase da bio Instagram, riformulata: ortopedico traumatologo, chirurgia della spalla e dell'arto superiore, artroscopica e protesica. CTA primario: Chiama la segreteria. CTA secondario: Dove ricevo. Micro-riga: lun–gio + numero *solo dopo conferma*.
2. **Cosa curo.** 4–6 card (Spalla, Gomito, Mano, Sport, Eco, Artroscopia). Una riga ciascuna, link alle pagine. Card anca/ginocchio **assente** finché D5 non la vuole.
3. **Dove ricevo.** Non la mappa di tutte le directory. Lista compatta delle sedi **confermate**: città · struttura · «visita» o «chirurgia». Link all'hub sedi. CESAT etichettato come ospedale, non come studio.
4. **Perché fidarsi (corto).** Una riga: CESAT Fucecchio · formazione Pisa · fellowship (Londra, Seattle, Berlino) · Porcellini. Link a Chi sono. Non elencare Nicoletti in home come «team» senza chiedere come nominarlo.
5. **Parola dei pazienti.** 2–3 recensioni curate *se* arrivano screenshot (D6). Se al go-live non ci sono, **il blocco non esiste** — niente stelline vuote.
6. **Ultimi articoli.** Max 3. Se il blog è vuoto, il blocco non c'è.
7. **Chiusura contatto.** Ripeti telefono, orari, bottone form. Eventuale: «Puoi prenotare anche su Doctolib» *se* Michele vuole ancora quel canale.

**Candidato già in casa.** Bio IG; elenco card da Doctolib `availableService`; foto da sostituire.

**Da confermare.** Numero in hero, orari, quali 3–5 sedi in lista, Doctolib sì/no, prezzi **non** in home.

**Non mettere.** Listino, indirizzo Lungarno, Alonso, «direttore SOC», tutte le 11 location, CV 2019 PDF.

---

### 2. Chi sono — `/it/chi-sono`

**Scopo.** Autorevolezza umana: percorso, ospedale, ricerca, tono da medico che spiega. Non pagina «team» di clinica.

**H1.** Dott. Michele Novi

**Blocchi**

1. **Apertura in prima persona** (derivata da Doctolib, da far riscrivere a lui): chi è, focus spalla/arto superiore, dove opera oggi (CESAT).
2. **Ruolo attuale.** Dirigente? Chirurgo della SOC? Formulazione **esatta** da lui. Ospedale San Pietro Igneo, Fucecchio. Cosa fa in ospedale vs in ambulatorio.
3. **Colleghi / contesto CESAT.** Candidato: Simone Nicoletti, direttore SOC (da altre fonti). **Da chiedere:** se e come citarlo (collega, direttore, co-autore, Shoulder School). Non invertire i titoli. Non una pagina dedicata a Nicoletti.
4. **Formazione.** Pisa laurea 108/110, spec. 110/110 e lode (Lisanti / tesi Bankart). Diploma SIUMB eco MSK. Timeline Modena/UNIMORE (Porcellini) 2020–21 — assente dal CV PDF, presente su LinkedIn: da confermare date.
5. **Fellowship** (asset EN e IT). Londra RNOH nervo periferico; Harborview Seattle mano/microchirurgia; Charité Scheibel spalla/gomito; Cervesi Porcellini. Una frase ciascuna, non il diario.
6. **Ricerca (selezione).** 4–6 paper, non i 16 PubMed. Candidati: review cuffia 2018; JBJS 2020 head-split; Remplissage 2022 con Nicoletti; JSES Int 2025 ML protesi; quadrilateral space 2025. Link DOI. Eventuale «elenco completo su PubMed».
7. **Territorio e didattica (opzionale, 1 blocco).** Screening Peccioli over 50; Fucecchio Arthroscopy Shoulder School; Cutting Edge Techniques. Solo ciò che vuole raccontare.
8. **Fuori dalla sala (opzionale).** Interessi CV (moto, MTB, tennis, climbing, sci, running) — solo se le foto shooting lo sostengono; altrimenti tagliare. Croce Rossa: da chiedere se è ancora vero.
9. **CTA.** Dove ricevo / Contatti.

**Non mettere.** Indirizzo di casa Pisa. Telefono 329. Qualifica «direttore» senza sua parola. Foto Doctolib come definitiva.

---

### 3. Hub patologie — `/it/patologie` (voce menu: Cosa curo)

**Scopo.** Mappa mentale. Il paziente sceglie l'articolazione o il tipo di intervento. Keyword di testa «ortopedico spalla» vivono soprattutto sulla pagina Spalla, non qui.

**H1.** Cosa curo

**Intro (5–8 righe).** Specialista dell'arto superiore; visita, eco, infiltrazioni, chirurgia artroscopica e protesica. Anca/ginocchio: una frase *solo se* D5 le vuole, con link alla pagina dedicata o a «in ospedale al CESAT».

**Griglia card.** Stesse 5–6 della home, con 2–3 bullet paziente ciascuna (es. Spalla: cuffia, instabilità, protesi, calcificazioni).

**Blocco metodo.** Link ad Artroscopia e a Eco MSK: «come lavoro», non «un altro organo».

**Chiusura.** «La prima visita è il momento in cui si decide il percorso» ? Contatti. Niente autodiagnosi.

---

### 4. Spalla — `/it/patologie/spalla`

**Scopo.** Pagina più importante del sito dopo home e sedi. Coda lunga + E-E-A-T.

**H1.** Chirurgia e patologie della spalla

**Blocchi**

1. Per chi è questa pagina (dolore, debolezza, lussazioni, esiti sportivi).
2. Cosa si valuta in visita (esame + eco se disponibile in sede — non promettere eco ovunque).
3. Percorsi, in linguaggio paziente, ciascuno con H2 proprio:
   - Cuffia dei rotatori (inclusa cuffia irreparabile: ha una review da primo autore — versione paziente, non il paper).
   - Instabilità / lussazione (Bankart, Remplissage — papers 2022).
   - Protesi di spalla (anche navigazione/ML 2025: un accenno sobrio, non «intelligenza artificiale che opera»).
   - Fratture / traumatologia (head-split JBJS: non da hero).
   - Calcificazioni, conflitto, capsulite — solo se lui le visita di routine (da chiedere).
   - Spazio quadrilatero / dolore posteriore «inspiegabile» — meglio un articolo che un capitolo qui.
4. Conservativo vs chirurgico: quando ha senso aspettare, quando no — scritto da lui o rivisto riga per riga.
5. FAQ 4–5 (schema FAQPage). Esempi: quanto dura il recupero cuffia; si può fare sport dopo protesi; la prima lussazione si opera sempre? — **risposte sue**.
6. Link: Artroscopia, Sport, Eco, Sedi dove si fa la visita, Contatti.

**Non mettere.** Prezzi di intervento (variano per SSN/privato/clinica). Garantire esiti. Nome di pazienti.

---

### 5. Gomito — `/it/patologie/gomito`

**H1.** Gomito: traumatologia, artroscopia, chirurgia

Più corta della spalla. Candidati da papers (da filtrare con lui): fratture, instabilità, bicipite distale, pediatrico solo se ancora nel perimetro. Stesso schema: visita ? opzioni ? FAQ corte ? CTA. Se il volume reale è basso, tenere una pagina densa e non spezzarla in 8 URL.

---

### 6. Mano e polso — `/it/patologie/mano`

**H1.** Mano e polso

Fellowship Harborview + microchirurgia Doctolib: c'è credibilità. Contenuto da far spuntare: tunnel carpale, rizoartrosi, traumatologia, tendini — **solo ciò che opera/visita oggi**. Microchirurgia: una frase onesta («formazione in…») senza promettere replant se non lo fa.

---

### 7. Traumatologia sportiva — `/it/patologie/traumatologia-sportiva`

**H1.** Traumatologia sportiva

Anima Athletica / territorio. Ritorno allo sport, instabilità, traumi da contatto e da overuse. Link a Spalla e a Eco.  
**Non:** Alonso, scuderie, «medico della Formula 1». Si può dire (se conferma) che visita in un centro di medicina dello sport / motorsport a Pisa, senza nomi di atleti.

---

### 8. Artroscopia — `/it/patologie/artroscopia`

**H1.** Chirurgia artroscopica

Pagina metodo: cos'è, per quali articolazioni lui la usa (spalla in primis; ginocchio/anca solo se D5), recupero tipo, differenza rispetto alla chirurgia aperta. Link in uscita verso Spalla / Gomito / Sport. Non duplicare l'elenco malattie.

---

### 9. Ecografia muscoloscheletrica — `/it/patologie/ecografia-muscoloscheletrica`

**H1.** Ecografia muscoloscheletrica

Diploma SIUMB (diagnostica e interventistica). Cosa si vede in ambulatorio, infiltrazioni eco-guidate, cosa *non* sostituisce (RMN, visita). Utile al territorio Peccioli/screening. Indicare **in quali sedi c'è l'ecografo** — campo Keystatic per sede, non una frase generica.

---

### 10. Protesi anca e ginocchio — `/it/patologie/protesi-anca-ginocchio` (condizionata)

**Esiste solo se D5 = sì.** Altrimenti: una riga in Chi sono / hub («in ospedale, chirurgia protesica anche di anca e ginocchio») senza pagina propria.

Se sì: chiarire che è attività **CESAT / ospedaliera**, prenotazione diversa dalla libera professione (CUP vs segreteria). Non mischiare il 348 con il CUP.

---

### 11. Dove ricevo — `/it/sedi`

**Scopo.** La domanda che Michele vuole chiudere: dove lo trovo. Una schermata, poi il dettaglio.

**H1.** Dove ricevo

**Blocchi**

1. Intro: più ambulatori, una segreteria. Come si prenota (telefono confermato / Doctolib / centralino clinica — mix da lui).
2. **Visite ambulatoriali** — card per sede attiva: città, nome struttura, una riga (es. «visite e infiltrazioni»), link alla scheda.
3. **Chirurgia / ricoveri** — CESAT; altre cliniche solo se confermate. Linguaggio diverso: non «vieni in piazza Lavagnini 5 come in studio».
4. Mappa d'insieme (tutti i pin **confermati**). Un pin = un indirizzo vero.
5. Nota accessibilità generale + «dettagli sulla pagina della sede» (richiesta CRM).

**Da confermare prima dello scaffold serio:** tabella D2. Meglio 4 card vere che 11.

**Non pubblicare:** You 2021, CentroSaluteOnline, Reteimprese, Localshop24, civici discordanti San Verano finché non è chiuso Cavour vs Carmine.

---

### 12. Scheda sede — `/it/sedi/[slug]`

Stesso stampo per ogni sede attiva. Campi Keystatic (@08).

**H1.** Ortopedico a [Città] — [Nome struttura]  
(es. *Ortopedico a Fucecchio — Studi Medici San Pietro*)

**Blocchi**

1. Ruolo della sede: visita / eco / infiltrazione / solo chirurgia.
2. Indirizzo, mappa, «come arrivare», parcheggio, barriere (foto shooting ingresso).
3. Telefono **di quella sede**: segreteria Michele vs centralino vs CUP. Non mettere il 348 sull'ospedale pubblico se le visite SSN passano dal CUP.
4. Orari **suoi** in quella sede, o «su appuntamento».
5. Logo struttura (opzionale), link sito clinica, link scheda Google **della struttura** (non una GBP clone).
6. Cosa si fa qui vs cosa si fa altrove (es. «la chirurgia è al CESAT, qui la visita»).
7. CTA identico alle altre pagine.

**Sedi candidato (testo bozza solo dopo spunta):** San Pietro Fucecchio; San Verano Peccioli; Fisiomed Fornacette; Kinetic Pisa; Athletica Pisa; MiniHospital Capannoli; CESAT come scheda «ospedale». Santa Croce, San Paolo, Villa Donatello: pagine **no** finché non è sì.

CESAT: Piazza Lavagnini **5**. Studio San Pietro: Lavagnini **6**. Non unificarle.

---

### 13. Contatti — `/it/contatti`

**Scopo.** Conversione. Un solo recapito pubblico. Il form non raccoglie il quadro clinico.

**H1.** Contatti

**Blocchi**

1. Segreteria: numero confermato, giorni, fascia. Candidato online: **348 4331733**, lun–gio, LinkedIn 15:30–17:30 vs Doctolib mer 16–18 — **unificare**.
2. Cosa chiedere alla telefono (visita, quale sede, richiamo). Cosa **non** scrivere (referti, diagnosi).
3. Form: nome, recapito, sede preferita (select delle attive), consenso privacy. Messaggio libero **non clinico** (es. «vorrei informazioni per una visita»).
4. WhatsApp: stesso numero? Testo precompilato neutro.
5. Doctolib: bottone «Prenota online» solo se resta canale ufficiale.
6. **Prezzi (D10).** Candidato Doctolib: prima visita 120 €, controllo 80–90 €, infiltrazione HA 80–150 €.  
   - Se sì: riquadro «visite in libera professione» + nota «possono variare per sede / prestazione; interventi e ricoveri hanno listini diversi».  
   - Se no: «il costo della visita viene comunicato in segreteria».  
   Non spargere i prezzi sulle patologie.
7. Pagamenti (Doctolib: contanti, assegno, carta, bonifico) — da confermare.
8. Assicurazioni / convenzioni: solo se ne ha (Checcucci le mostra; noi no di default).
9. Mini-elenco sedi o link all'hub.

**Non:** gmail `miche.novi@` in chiaro se nasce `info@dominio`. Non il 329. Non CUP in evidenza uguale al privato.

---

### 14. Indice articoli — `/it/articoli` (label D7)

**H1.** Nome scelto (non «News»).

Elenco con cover, data, excerpt, tag patologia/sede. Filtro semplice se i pezzi sono >6.  
Se zero articoli al go-live: **niente voce menu** (lock-in @11).

---

### 15. Articolo — `/it/articoli/[slug]`

Layout rivista: titolo, lead, ritratto piccolo, data, disclaimer, corpo, CTA, correlati (patologia + eventuale sede). Campo YouTube opzionale. Autore: Dott. Michele Novi.

**Candidati lancio** (@10): cuffia; instabilità/remplissage; «perché visito in più sedi»; screening Peccioli; Shoulder School. Alonso: no.

---

### 16. Privacy e cookie

Titolare, finalità del form, cookie GA4 dopo consenso, niente dati sanitari. Testi quando abbiamo ragione sociale / P. IVA / pec. EN: traduzione, non un secondo legale.

---

### 17. 404

Una frase, link home / sedi / contatti, stesso header. Utile se arriveranno 301 dal vecchio dominio.

---

## Interlinking (v1)

```
Home ? patologie card, sedi, chi sono, contatti
Chi sono ? sedi, 2–3 patologie, 1 articolo
Ogni patologia ? artroscopia e/o eco se pertinenti, sedi, contatti, 1 articolo
Ogni sede ? 2 patologie «tipiche» di quel luogo se ha senso (Athletica?sport, Peccioli?territorio/eco), contatti
Articolo ? patologia + sede + contatti
```

Niente pagine combo `città+articolazione` in v1 (lezione Nicoletti): si ottiene con interlink, non con 20 URL sottili.

---

## Contenuti Keystatic (cosa è dato, non codice)

Collezioni v1: `sedi`, `patologie` (testo MD), `articoli`, `recensioni` (citazione curata).  
Singleton: home hero, orari segreteria, telefono, social, flag «mostra prezzi», flag «mostra Doctolib».

Finché telefono e sedi non sono confermati, i singleton restano vuoti o `TODO` — non si fa lo scaffold con il 348 «tanto poi si cambia»: finisce in JSON-LD.

---

## Idee future
- Pagina «per lo sportivo» se Athletica diventa un posizionamento voluto.
- FAQ globale + FAQPage.
- Biglietto da visita digitale / PDF per la segreteria.
- `/prenota` quando c'è l'agenda.

## Nodi da sciogliere
D2, D3, D5, D6, D7, D10, D12. Checklist in [DOMANDE_APERTE.md](DOMANDE_APERTE.md).

## Passi successivi
1. Call: spuntare checklist (numero, sedi, prezzi, collega, Doctolib).
2. Congelare quali URL patologia e quali slug sede esistono al lancio.
3. Poi scaffold `app/[locale]/...`.

## Decisioni congelate (lock-in)
- Multipagina.
- Home da landing, sezioni autonome.
- i18n a prefisso di path, non sottodominio.
- Una pagina per ogni sede **attiva** e per ogni area di trattamento **con testo vero**.
- Artroscopia = pagina metodo (proposta Mauro, da validare).
- Anca/ginocchio = pagina propria solo se D5.
- Blog in menu solo con almeno un articolo.
- Prezzi, se ci sono, solo in Contatti (o non ci sono).
- CESAT ? studio privato nella IA.

## Rischi / Compliance & Riferimenti
- Troppe pagine patologia vuote = thin content.
- Pubblicare sedi o prezzi non confermati **peggiora** la confusione che il sito deve togliere.
- Piano tecnico: `documenti/fonti/Piano_Tecnico_Sito_Michele_Novi_2026.pdf`
- Benchmark IA: @12 (Nicoletti città+articolazione; Checcucci pillar).
- Design dei blocchi: @11.
