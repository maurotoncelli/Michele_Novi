# Correzioni Michele Novi — 26 novembre 2026

File sorgente archiviato: `fonti/pdf/2026-11-26_correzioni.pptx` (12 slide).

## Sintesi interventi applicati

1. **Slide 1 — Ordine sedi *Dove visito***
   - Peccioli (Centro Medico San Verano) spostata al 1° posto (`peso: 1`), seguita da Pisa (`peso: 2`) e Fucecchio Studi Medici San Pietro (`peso: 3`).
   - Ordine *Dove opero* invariato (Casa di Cura San Rossore, CESAT, Villa Donatello).

2. **Slide 2 — Pagina *Chi sono***
   - Nuovo titolo professionale su due righe: *Ortopedico e Traumatologo. Chirurgia della Spalla e Arto Superiore. / Chirurgia Protesica e Artroscopica*.
   - Nuovo testo di apertura su 2 paragrafi (con elenco centri Italia/estero e Ospedale San Pietro Igneo di Fucecchio).
   - Rimossa la riga grigia dei fatti sotto l'apertura (barrata nella slide; OMCeO resta nel footer e nella privacy).

3. **Slide 3 — Home (*Profilo clinico*)**
   - Nuovo titolo su 2 righe: *Chirurgia della Spalla e Arto Superiore. / Chirurgia ricostruttiva Artroscopica e Protesica*.
   - Nuovi 2 paragrafi aggiornati (`home.yaml` + supporto titolo su 2 righe in `FasciaIntro`).

4. **Slide 4 — Sezione *Il metodo / Attività chirurgica***
   - Sostituito il testo `lead` in `patologie/come-si-opera/index.mdoc` con i 2 nuovi paragrafi (IT + EN).

5. **Slide 5–7 — Corpo della pagina `/cosa-curo/come-si-opera`**
   - Aggiornati introduzione e i 4 capitoli (*Artroscopia*, *Chirurgia aperta*, *Protesi di spalla*, *Ecografia interventistica*) con i nuovi testi estesi del dottore (IT + `corpoEn.mdoc`).

6. **Slide 8 — Rimozione *Chi decide* e *Dove si tratta***
   - Rimossa la sezione `# Chi decide` (`# Who decides`) da `come-si-opera`.
   - Rimossa la sezione `#dove` (*Dove si tratta*) e la relativa voce dal Sommario nelle pagine di dettaglio patologia (`cosa-curo/[slug]/page.tsx`).

7. **Slide 9–11 — FAQ sulla chirurgia della spalla + SEO/AI**
   - Aggiornate le 3 FAQ esistenti e aggiunte le 2 nuove FAQ (protesi anatomica vs inversa; re-tear/recidiva della cuffia) in `patologie/spalla/index.mdoc` (IT + EN).
   - Titolo H2 dedicato sulla pagina Spalla: *Domande frequenti sulla chirurgia della spalla*.
   - Domande rese come `<h3>` dentro `<summary>` e risposte formattate a paragrafi multipli (`Faq.tsx`).
   - Aggiornato `cosaCuro.disclaimer` con la formula divulgativa indicata in Slide 9.
   - Schema JSON-LD `FAQPage` già presente e attivo su tutte le schede patologia.

8. **Slide 12 — Dati attività scientifica (Scopus + ORCID)**
   - Aggiunto blocco `attivitaScientifica` in `profilo.yaml` e schema Keystatic: **26** documenti su riviste internazionali, **310** citazioni, **H-index 11**, **Scopus ID 57198887872**, **ORCID 0000-0003-4867-463X**.
   - Mostrati nella sezione Pubblicazioni (Home e `/pubblicazioni`) con link diretti a Scopus e ORCID.
   - Recuperate e aggiunte in `site/content/pubblicazioni/` le **15 pubblicazioni internazionali peer-reviewed mancanti** (2016–2025, verificate tramite ORCID `0000-0003-4867-463X`, PubMed e Crossref, con abstract ufficiali, DOI, PubMed ID, link PMC open-access e riassunto divulgativo IT/EN). Totale archivio: **29 pubblicazioni** (tutte le 26 indicizzate su Scopus + 3 su PubMed/MDPI/OTODI). Le 14 principali del CV restano contrassegnate `principale: true` per la pagina *Chi sono*.
   - Inseriti Scopus e ORCID in `sameAs` nel JSON-LD `Physician` (`seo.ts`).
