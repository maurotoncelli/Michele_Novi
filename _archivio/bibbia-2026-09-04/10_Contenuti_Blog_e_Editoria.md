# 10. Contenuti, blog e piano editoriale

> Parte della Bibbia. Indice: [00_README_Master_Index.md](00_README_Master_Index.md).

## Metadati
- ID: CAP-10
- Stato: Bozza
- Ultimo aggiornamento: 2026-09-04
- Dipendenze: @03_Brand, @04_IA, @06_SEO, @13_Privacy, @15_Profilo
- Owner: Mauro + Michele (editoria)

## Sintesi
Il blog ù il **motore** del sito nel tempo: interesse vero, coda lunga, materiale da riversare su YouTube e Instagram. Michele vuole scrivere ciclicamente e sta giù pensando un piano social. Keystatic gli permette di pubblicare senza WordPress. v1: struttura pronta + primi articoli di qualitù, non 40 pagine vuote.

## Stato attuale del progetto

### Ruolo
Non e un magazine e **non e un blog da agenzia SEO**. E il posto dove Michele spiega **una cosa che ha gia studiato o visto**, in prima persona. I paper sono la materia prima: non si riassume l'abstract. Linea e pila: [`../ricerca/2026-09-04_idee-articoli-dai-paper.md`](../ricerca/2026-09-04_idee-articoli-dai-paper.md). Collegato in futuro a video (stesso tema, due formati).

### Nome della sezione
Aperto (D7). In linea con i paper: Note, Dal lavoro, In ambulatorio, Quaderno di spalla. Evitare Blog, Insights, Magazine. URL: `/articoli`.

### Chi pubblica
Idealmente Michele (o la segreteria) da `/keystatic`. Mauro: formazione inclusa nel preventivo. Workflow:

1. Lui detta 15-20 minuti (un paper, un dubbio, un caso anonimo).
2. Mauro mette in forma (prima persona, un intento).
3. Lui taglia cio che suona da brochure.
4. IT + EN (EN puo uscire in ritardo).

### Fonti giù disponibili (da trasformare, non da copiare-incollare)

| Fonte | Idea articolo | Note |
|-------|---------------|------|
| Call: ùquando ha curato Alonsoù | Solo se consenso. Angolo possibile: lavoro in un centro motorsport (Athletica), **senza** nome paziente | Default: NON pubblicare il nome |
| Quinews screening Peccioli over 50 | Territorio, prevenzione, sensori inerziali, tele-riabilitazione | Giù pubblico |
| LinkedIn Shoulder School Fucecchio 2025 | Formazione, CESAT come hub spalla | |
| USL Cutting Edge Techniques | Protesi di spalla, comitato locale con Nicoletti | |
| Pubblicazione ORR 2018 cuffia irreparabile | Versione paziente della review | Citare DOI, linguaggio accessibile |
| Case report clavicola + triathlon (2016) | Traumatologia sportiva | Anonimato giù nel paper |
| Tesi Bankart solid vs all-suture | Troppo tecnico per home; ok approfondimento |
| Doctolib / CV fellowship | Serie ùcome si forma un chirurgo di spallaù (Londra, Seattle, Berlino, Porcellini) | |
| LinkedIn attivitù recente | Corsi Stryker, SICSeG | Bassa prioritù paziente |

| Osteology 2022 Remplissage (Novi + Nicoletti) | Instabilitù di spalla nello sportivo | Paper CESAT |
| J Orthop Traumatol 2025 quadrilateral space | Dolore posteriore di spalla ùche non si spiegaù | Coda lunga |
| JSES Int 2025 ML protesi (con Nicoletti) | Tecnologia in sala | Non prioritù v1 |

### Linee guida editoriali
- Un intento: una domanda paziente per articolo.
- H2 che somigliano a query.
- Autore: Dott. Michele Novi. Data. Disclaimer: ùnon sostituisce la visitaù.
- CTA finale: contatti / sede.
- Niente keyword stuffing, niente copy da Checcucci.
- Immagini: schema anatomico con licenza, o foto shooting, o frame video. Niente Getty random.
- Lunghezza: 800ù1500 parole per i pillar; i post ùponte socialù possono essere più corti se puntano a una pagina patologia.

Ogni articolo punta a una pagina patologia o sede (@04), non vive isolato.

### LinkedIn: si riusa il tema, non il post

Inventario e URL: [`../ricerca/2026-09-04_linkedin-post-come-articoli.md`](../ricerca/2026-09-04_linkedin-post-come-articoli.md).

Il feed (2024ù2025) ù quasi tutto **peer-to-peer**: locandine di corsi, ringraziamenti faculty, repost Arthrex/Stryker/NCS. Quasi niente ù giù un articolo per pazienti. Inoltre molti pezzi **non sono suoi** (repost Mantovani sullo screening Peccioli; copy Arthrex).

**Si fa**
- Partire dal tema (instabilitù, protesi inversa, screening over 50, spalla e sport).
- Riscrivere 800ù1500 parole, domanda paziente come H1, lui firma il clinico.
- Usare il corso/evento come *proof in chiusura*, non come notizia ùiscrivitiù (la School 2025 ù giù passata).
- Dopo go-live: LinkedIn punta all'articolo sul sito (canonical sul dominio suo).

**Non si fa**
- Incollare il post o la locandina.
- Copiare testi di Arthrex, Stryker, NCS, Mantovani, Gabrieli.
- Scaricare foto LinkedIn (sala, colleghi, loghi brand) per il sito.
- Tre articoli-diario ùbella giornata al congressoù: quello sta in Chi sono, una riga.

Proposta lancio dal feed: (1) instabilitù/artroscopia, (2) protesi inversa in parole semplici, (3) screening Peccioli. Corsi Stryker/SICSeG ? Chi sono.

### Calendario (proposta, da ritmare sul piano social)
Mese 1-2 (lancio): 3 pillar (cuffia *o* instabilitù dal tema School, screening Peccioli, dove visito e perchù più sedi).  
Poi: 1 pezzo/mese ù giù meglio di zero. Allineare al piano Instagram invece di inventare un secondo redazionale.

### YouTube / reel
Non in v1 di produzione video continua. Il CMS deve giù avere un campo `youtubeId` opzionale. Shooting: un video corto da hero o da Chi sono vale più di un canale vuoto.

## Idee future
- Serie ùuna patologia, un reel, un articoloù.
- Newsletter: no.
- Guest post / PR locale (Quinews) che linka il sito.

## Nodi da sciogliere
D7, D8, D11. Piano social di Michele: da farsi mandare.

## Passi successivi
Template Markdoc Keystatic: titolo, excerpt, cover, sede correlata, patologia correlata, YouTube, autore.

## Decisioni congelate (lock-in)
- Blog in v1, editabile da pannello, niente WordPress.
- Articoli firmati dal medico, originali (giudizio suo, non listicle).
- Niente casi identificativi senza consenso.
- LinkedIn = fonte di *temi*, non di copy da incollare. Repost e testi brand non si ripubblicano.
- Niente pezzi scritti per catturare keyword. Un H1 che e una domanda vera basta per la SEO.

## Rischi / Compliance & Riferimenti
- YMYL / E-E-A-T.
- Deontologia: informazione sanitaria, non pubblicitù ingannevole.
- CV e papers: @15.
