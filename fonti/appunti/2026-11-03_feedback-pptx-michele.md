# Feedback del Dott. Michele Novi da presentazione PPTX — 03/11/2026

Fonte: `fonti/pdf/2026-11-03_MODIFICHE_SITO_MN.pptx` (`/Users/maurotoncelli/Downloads/MODIFICHE SITO MN.pptx`) + foto allegata `/Users/maurotoncelli/Downloads/foto chirurgo.png`.
Ramo di lavoro: `home-hero-wide` (`/Volumes/Siti web/Michele Novi/Hero 1`).

---

## Elenco completo dei feedback (12 slide) e stato di attuazione

### Slide 1 — Hero Home (gerarchia titoli e copy)
- **Indicazione del dottore:**
  - *"Titolo iniziale -> Valutare se è meglio il nome in piccolo o in grande (vedi https://chirurgie-coude.fr/. questo sito di collega francese non è male.) -> buona idea: Dott. Michele Novi più piccolo elegante, chirurgia spalla più grande."*
  - Sopra, più piccolo ed elegante: `Dott. Michele Novi`
  - Titolo principale (H1 grande): `Chirurgia della Spalla. Arto Superiore. Protesica`
  - Sottotitolo in evidenza: `Chirurgia della spalla, trattamento delle patologie complesse e chirurgia ricostruttiva.`
  - Corpo (due paragrafi):
    1. *"Mi occupo del trattamento chirurgico delle patologie della Spalla e dell'Arto Superiore, sia degenerative che traumatiche e sportive, con particolare attenzione alle condizioni complesse della cuffia dei rotatori, di instabilità articolare e alle procedure ricostruttive avanzate."*
    2. *"Svolgo inoltre attività chirurgica nell'ambito della patologia Ortopedica del ginocchio e dell'Anca. Formazione ed esperienza professionale maturate tra l'Italia e i centri internazionali."*
- **Attuazione:** Aggiornati `site/content/home.yaml` (IT/EN) e il componente `Hero` in `site/src/components/blocks/Home.tsx`.

### Slide 2, 3, 4 — Dove visito / Dove opero, Mappa Toscana, Fucecchio e Foto reali strutture
- **Indicazione del dottore:**
  - **Divisione netta:** *"Si deve differenziare bene in due sezioni distaccate «DOVE VISITO» e «DOVE OPERO». Se è tutto insieme così il pz fa confusione e non legge che magari a Villa Donatello ci opero e basta. Quindi lascerei giustamente sulla home il tasto —(dove ricevo)— poi in questa pagina dividere chiaramente dove visito e dove opero."*
  - **Sede visite a Fucecchio:** *"DOVE VISITO: correggere: STUDI MEDICI SAN PIETRO PIAZZA TOSCANINI 3 FUCECCHIO (non è CESAT .. Lì è dove opero)"*.
  - **Mappa per Dove visito:** *"NO LE FOTO DEI POSTI. Preferisco una mappa della Toscana o widget googlemap fatto con la stessa paletta cromatica del sito con i vari Pin sulla mappa della Toscana e intorno già visibile come si chiama lo studio"*.
  - **Mockup mappa (Slide 3):** *"Vedi se può funzionare qualcosa del genere … ovviamente con i loghi giusti delle strutture San Rossore e San Verano (te lo mando io). Fucecchio non ha loghi va bene anche una cosa tipo quella casina lì.. No le scritte senza senso che garbano all'AI tipo questa «la salute vicino a te»."*
  - **Foto per Dove opero (Slide 3 e 4):** *"Mentre sotto sul DOVE OPERO: puoi pure mettere le foto piccoline di San Rossore (no l'Arno), del CESAT e Villa Donatello"*. Nella Slide 4 allega i loghi ufficiali (`logo-san-rossore.png`, `logo-san-verano.png`, `logo-villa-donatello.jpg`) e le foto reali delle 3 strutture chirurgiche (`sede-san-rossore.jpg`, `sede-cesat-fucecchio.jpg`, `sede-villa-donatello.jpg`).
- **Attuazione:**
  - Creata `site/content/sedi/fucecchio-san-pietro.yaml` (*Studi Medici San Pietro, Piazza Toscanini 3, 50054 Fucecchio*, `visite: true`, `chirurgia: false`).
  - Impostato `site/content/sedi/fucecchio-cesat.yaml` come sede chirurgica (`visite: false`, `chirurgia: true`, foto reale `sede-cesat-fucecchio.jpg`).
  - Sostituite le foto panoramiche delle città con le foto reali delle strutture in `pisa-san-rossore.yaml` (`sede-san-rossore.jpg`, ritagliata sopra la maschera bianca a V) e `villa-donatello.yaml` (`sede-villa-donatello.jpg`); rimossa la foto paesaggistica da `peccioli-san-verano.yaml`.
  - Creato il componente `site/src/components/blocks/MappaToscana.tsx` con la mappa illustrata della Toscana nella palette del sito (`#0f3a5a` / `#1e6aa8` / crema), i 3 pin interattivi, i callout con indirizzo e l'elenco affiancato con i loghi ufficiali di San Rossore e San Verano e l'icona studio/casina per Fucecchio.
  - Divise nettamente le sezioni **Dove visito** e **Dove opero** sia in `/dove` (`site/src/app/[locale]/dove/page.tsx`) sia in Home (`FasciaSedi` in `site/src/components/blocks/Home.tsx`).

### Slide 5 — Rimozione fascia statistiche ("Riga dei fatti")
- **Indicazione del dottore:**
  - *"Queste info messe così hanno poco senso per il paziente .. Non sapendo cosa metterci, forse penserei di levarlo"* (riferito alla striscia `4 sedi in Toscana | dal 2021 SOC Ortopedia Protesica | 2025 Harvard / MGH | 14 pubblicazioni`).
- **Attuazione:** Rimossa `<FasciaFatti />` dalla Home (`site/src/app/[locale]/page.tsx`) e collegata la freccia "Scorri" della Hero direttamente a `#patologie`.

### Slide 6 e Slide 7 — Sezione "01 Patologie trattate", nuovi lead e rimozione caption
- **Indicazione del dottore:**
  - Eyebrow della sezione 01 in Home: **`PATOLOGIE TRATTATE`** (*"Metti PATOLOGIE TRATTATE (non cosa curo)"*).
  - Lead di **La spalla**: *"Trattamento di patologie tendinee, di instabilità, patologie degenerative e traumatiche."*
  - Lead di **Anca e ginocchio**: *"Chirurgia protesica di Ginocchio e Anca."*
  - Rimozione crediti/caption sotto le card (Slide 6 e 7): *"Levare sotto le scritte, quelle caption Fucecchio – Pisa Peccioli, 4 pubblicazioni ecc…"* e in Traumatologia sportiva *"Questo puoi lasciare così ma leva «2 pubblicazioni pisa peccioli»"*.
- **Attuazione:** Aggiornati `spalla/index.mdoc`, `anca-e-ginocchio/index.mdoc`, `it.json`, `en.json` e rimossa la riga `credito(p, dove, locale)` da tutte le varianti di `SchedaPatologia` in `site/src/components/blocks/Schede.tsx`.

### Slide 8 — Nuova foto in sala operatoria con camice sterile
- **Indicazione del dottore:**
  - *"Ho modificato la foto mettendo un camice da sala operatoria perché sennò non è realistico. Trovi la foto nella cartellina"*.
- **Attuazione:** Presa `/Users/maurotoncelli/Downloads/foto chirurgo.png` (1.81 MB), compressa con `sharp` (`mozjpeg`, qualità 82, 1536×1024 px → **103.7 KB**, −94%) e salvata in `site/public/images/patologie/come-si-opera-chirurgo.jpg` (copiata anche nel worktree `Hero 2`).

### Slide 9 — Sezione Sintomi ("Per il paziente")
- **Indicazione del dottore:**
  - *"Invece che da dove parti ---- metti «PER IL PAZIENTE». Poi dopo OK «PARTI DA QUELLO CHE SENTI» va bene"*.
- **Attuazione:** Aggiornato `cosaCuro.sintomiEyebrow` in `"Per il paziente"` (`"For the patient"` in EN).

### Slide 10 — Sezione "Il metodo": da "Come si opera" ad "Attività chirurgica" + 4 infografiche
- **Indicazione del dottore:**
  - *"NO «COME SI OPERA». ATTIVITÀ CHIRURGICA"*
  - Nuovo testo descrittivo:
    - *"Quello che molti non sanno è che la maggior parte dei pazienti non necessita sempre di un intervento chirurgico."*
    - *"Quando dobbiamo operare, perché scegliamo un trattamento piuttosto che un altro e cosa cambia per il paziente?"*
    - *"(Trattamenti mini invasivi in chirurgia artroscopica, Chirurgia ricostruttiva open, Sostituzione articolare protesica, Tecniche mininvasive ecoguidate)"*
  - *"Le 4 infografiche con Artroscopia, chirurgia open, chirurgia protesica (no didascalia sotto il titoletto) e un ecografo con scritto ecografia interventistica"*
  - Frase conclusiva: *"L'indicazione precede la tecnica. Una corretta diagnosi è il punto da cui partire."*
- **Attuazione:** Aggiornato `site/content/patologie/come-si-opera/index.mdoc`, disegnata la 4ª icona SVG `ecografia` in `site/src/components/ui/IconaTecnica.tsx`, portate a 4 le tecniche in `it.json`/`en.json` svuotando le note sottostanti, e aggiornata la griglia a 4 colonne in `SchedaMetodo` (`Schede.tsx`).

### Slide 11 — Sezione 03 in Home: "Percorso formativo" e date grandi alternate
- **Indicazione del dottore:**
  - *"Qui va un po' cambiato.. Incarico ospedaliero e fellowship di spalla è accozzato insieme da AI ma non si capisce. Metterei giustamente percorso formativo."*
  - Titolo: **`INCARICHI PROFESSIONALI E FELLOWSHIP INTERNAZIONALI`**
  - Layout: *"E con le grafiche date grosse come hai messo (anzi magari alternando destra e sinistra date e descrizioni ,,, tipo DATA GROSSA A DX a [sx descrizione])"*.
- **Attuazione:** Aggiornati `home.fiduciaEyebrow` (`"Percorso formativo"`) e `home.fiduciaTitolo` (`"Incarichi professionali e fellowship internazionali."`) in `it.json`/`en.json`, e riscritto `site/src/components/blocks/PercorsoScorrevole.tsx` con layout alternato destra/sinistra per le date grandi (`2015`, `2017`, `2018`, `dal 2021`, `2025`).

### Slide 12 — Pagina e Menu "Cosa curo" → "Percorsi di cura" + nuovo sintomo ginocchio
- **Indicazione del dottore:**
  - Rinominare `Cosa curo` in **`PERCORSI DI CURA`** (menu e H1 della pagina).
  - Nuovo sottotitolo (lead): *"Trattamenti personalizzati basati sulle evidenze scientifiche. L'ascolto del paziente porta ad una corretta diagnosi, la fiducia nel medico ad una rapidità nei risultati."*
  - Rimuovere la scritta a destra di "Parti da quello che senti" (*"Il nome del problema arriva dopo. Scegli la frase più vicina alla tua situazione."*).
  - Sintomi: confermati quelli presenti + aggiunta la voce **`Ho sempre più difficoltà a camminare e fare le scale`** (collegata a Ginocchio / `anca-e-ginocchio`).
- **Attuazione:** Aggiornati `nav.cosaCuro`, `cosaCuro.titolo`, `cosaCuro.lead`, `cosaCuro.sintomiLead` in `it.json`/`en.json`, aggiunto il 9° sintomo in `site/content/cosa-curo.yaml` e nascosto il paragrafo vuoto in `site/src/app/[locale]/cosa-curo/page.tsx`.
