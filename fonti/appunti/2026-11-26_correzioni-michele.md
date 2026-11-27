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

## Addendum del pomeriggio — revisione di Mauro

Dopo il giudizio complessivo sul sito, Mauro ha risposto punto per punto. Fatto:

1. **Contatti:** tolta la frase «Gli orari saranno pubblicati a breve». Gli orari non si pubblicano; la riga compare solo se un giorno `settings.orari` viene compilato.
2. **Anteprima social:** la home passava a `og:image` il nome nudo del file (`hero-novi-v8.jpg`), che diventava `https://michele-novi-sito.vercel.apphero-novi-v8.jpg`. Ora `/images/home/hero-novi-v8.jpg`. Stesso errore nell'immagine del JSON-LD `Physician`; in più `jobTitle` conteneva un a capo. `buildMetadata()` ora regge anche un percorso senza barra iniziale.
3. **Sitemap:** l'indirizzo del tag «prima visita» usciva con lo spazio; ora `prima%20visita` (in `href()`).
4. **Autori:** `site/src/lib/autori.ts` riconosce il titolare nelle forme «Michele Novi», «M. Novi», «Novi M». Nell'elenco: primo autore + lui in evidenza + «et al.»; nella pagina del paper l'elenco resta com'è in rivista, con il suo nome più marcato.
5. **Telefono:** mappa delle sedi con le sole tre città in grande sotto i 640px (i riquadri con indirizzo scendevano a 6–7px); collegamenti del piè di pagina, «Leggi tutto», Scopus e ORCID con area di tocco più alta.
6. **Le 15 schede aggiunte al mattino, corrette contro le fonti:**
   - `abstract`: testo della fonte parola per parola (PubMed per 11, pagina dell'editore per MLTJ, pagine Minerva Medica per 3). Al mattino in alcuni casi avevo ritoccato la grammatica: tolto.
   - `autori`: come in rivista. Avevo completato a intuito nomi che la rivista dà con le iniziali (Poland 2025, Brunelli 2018, clavicola 2016) e scritto «Gian Mario» dove la rivista scrive «Gianmario». Corretto.
   - `licenza`: titolare del copyright e licenza presi dalla pagina dell'articolo. Due erano sbagliati (MLTJ è © I.S.Mu.L.T.; Poland è «under exclusive licence to Istituto Ortopedico Rizzoli»), tre Minerva erano vuoti.
   - `volume` dei tre articoli Minerva: fascicolo e pagine dalla pagina dell'editore.
   - `riassunto`: riscritti; ogni affermazione è nell'abstract (tolti, per esempio, la «radiotrasparenza» della placca in PEEK e l'esito non dichiarato nel caso della clavicola).
   - Clavicola 2016: il DOI `10.13107/jocr.2250-0685.482` **non è registrato** su doi.org. Campo svuotato, il pulsante porta a PubMed Central. Tolto anche un refuso di conversione (`::`) nei titoletti dell'abstract.
7. **Controlli:** tutti gli altri 28 DOI rispondono. Scopus (anteprima pubblica, 26/11): 26 documenti, 310 citazioni da 296 documenti, h-index 11: i numeri sul sito sono giusti. L'anteprima elenca solo 2 documenti su 26, quindi **non si può dire quali** dei 29 in archivio siano i 26 di Scopus: l'ipotesi fatta al mattino sui tre esclusi non ha fonte ed è ritirata. La nota in pagina è stata riscritta di conseguenza.

Non toccato, per decisione di Mauro: i testi integrali con licenza NC / NC-SA. Idee e cose da far vedere a Michele: in `bibbia/HANDOFF.md`.

## 27 novembre — correzione di Michele (screenshot dal telefono)

In «Come si prenota» (Home, `/dove`, pagine delle sedi) Michele ha barrato «non tramite il centralino della struttura». La frase ora è solo «Tramite la segreteria del Dott. Novi.» (`dove.prenotaTesto`, IT + EN).
