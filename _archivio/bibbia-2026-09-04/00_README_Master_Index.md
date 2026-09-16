# 00. Master Index � Bibbia di progetto

Progetto: **Sito web Dott. Michele Novi** (ortopedico traumatologo, Toscana).
Documento maestro che indicizza la Bibbia. Indice e convenzioni da leggere insieme a [HANDOFF_AGENTE.md](HANDOFF_AGENTE.md).

---

## Scopo della Bibbia

Documentare business, presenza online, UX, stack, SEO, privacy e roadmap in file Markdown modulari. Obiettivo: dare a ogni nuova chat agentica un contesto chiuso e verificabile, prima di scrivere codice.

Il sito v1 � una **vetrina data-driven**, non un gestionale. Non copiare lo scope di `successioniarmellin.it`. Il riferimento tecnico pi� vicino � `maurotoncelli.it` (Next.js + Keystatic + i18n custom + Vercel).

## Come usarla con l'AI

1. Si lavora **un capitolo (o un sotto-tema) alla volta**.
2. Contesto minimo: questo README + [HANDOFF_AGENTE.md](HANDOFF_AGENTE.md) + [DECISIONI.md](DECISIONI.md) + il capitolo in lavorazione.
3. Quando un capitolo � validato da Mauro (e dove serve da Michele), passa a **Congelato**.
4. Le scelte chiuse vanno in [DECISIONI.md](DECISIONI.md). I dubbi restano in [DOMANDE_APERTE.md](DOMANDE_APERTE.md).

## Convenzioni

- Naming file: `NN_Titolo_Capitolo.md`.
- Lingua della Bibbia: **italiano**.
- I riferimenti incrociati usano `@NN_Nome`.
- Dati anagrafici e sedi: unica fonte in `@15` (profilo) e `@08` (sedi). Non duplicare elenchi discordanti.
- Niente segreti in git (password Keystatic, token Vercel, account Google). Quando arriveranno, file locale git-ignored.

## Legenda stati

| Stato | Significato |
|-------|-------------|
| Bozza | Prima stesura da fonti CRM / web / CV |
| In revisione | Completo, da validare con Mauro e/o Michele |
| Congelato | Validato; non si riapre senza motivo esplicito |

## Stato globale

| Cap | Titolo | Stato | Ultimo agg. |
|-----|--------|-------|-------------|
| 01 | Executive Summary e Visione | Bozza | 2026-09-04 |
| 02 | Cliente e Brief | Bozza | 2026-09-04 |
| 03 | Brand Identity e Posizionamento | Bozza | 2026-09-04 |
| 04 | Architettura dell'Informazione | Bozza | 2026-09-04 (scheletro pagine) |
| 05 | Stack Tecnologico | Bozza | 2026-09-04 |
| 06 | SEO e Indicizzazione AI | Bozza | 2026-09-04 |
| 07 | Presenza Online | Bozza | 2026-09-04 (quadro siti) |
| 08 | Sedi e Google Business | Bozza | 2026-09-04 (civici estratti) |
| 09 | Recensioni | Bozza | 2026-09-04 |
| 10 | Contenuti, Blog e Editoria | Bozza | 2026-09-04 |
| 11 | Design e UX | Bozza | 2026-09-04 |
| 12 | Benchmark e Concorrenza | Bozza | 2026-09-04 |
| 13 | Privacy e GDPR | Bozza | 2026-09-04 |
| 14 | Offerta, Roadmap e Fasi | Bozza | 2026-09-04 |
| 15 | Profilo Clinico e CV | Bozza | 2026-09-04 (LinkedIn+PubMed) |
| 16 | Fondamenta visive | Bozza | 2026-09-04 |

## Indice dei capitoli

- [01. Executive Summary e Visione](01_Executive_Summary_e_Visione.md)
- [02. Cliente e Brief](02_Cliente_e_Brief.md)
- [03. Brand Identity e Posizionamento](03_Brand_Identity_e_Posizionamento.md)
- [04. Architettura dell'Informazione](04_Architettura_Informazione.md)
- [05. Stack Tecnologico](05_Stack_Tecnologico.md)
- [06. SEO e Indicizzazione AI](06_SEO_Indicizzazione_AI.md)
- [07. Presenza Online](07_Presenza_Online.md)
- [08. Sedi e Google Business](08_Sedi_e_Google_Business.md)
- [09. Recensioni](09_Recensioni.md)
- [10. Contenuti, Blog e Editoria](10_Contenuti_Blog_e_Editoria.md)
- [11. Design e UX](11_Design_UX.md)
- [12. Benchmark e Concorrenza](12_Benchmark_e_Concorrenza.md)
- [13. Privacy e GDPR](13_Privacy_GDPR.md)
- [14. Offerta, Roadmap e Fasi](14_Offerta_Roadmap_e_Fasi.md)
- [15. Profilo Clinico e CV](15_Profilo_Clinico_e_CV.md)
- [16. Fondamenta visive (concetti e metafore)](16_Fondamenta_Visive.md)

## Documenti di governo

- [HANDOFF_AGENTE.md](HANDOFF_AGENTE.md) � primo file per una chat nuova.
- [DECISIONI.md](DECISIONI.md) � vincoli chiusi (prevalgono in caso di dubbio).
- [DOMANDE_APERTE.md](DOMANDE_APERTE.md) � nodi da sciogliere con Michele / Mauro.

## Materiali a supporto (fuori dalla Bibbia)

- [`../documenti/fonti/CV-NOVI-1.pdf`](../documenti/fonti/CV-NOVI-1.pdf)
- [`../documenti/fonti/Piano_Tecnico_Sito_Michele_Novi_2026.pdf`](../documenti/fonti/Piano_Tecnico_Sito_Michele_Novi_2026.pdf)
- [`../documenti/appunti/2026-08-28_primo-contatto.md`](../documenti/appunti/2026-08-28_primo-contatto.md)
- [`../documenti/appunti/2026-08-31_scheda-crm.md`](../documenti/appunti/2026-08-31_scheda-crm.md)
- [`../documenti/appunti/2026-09-04_call-prossima-domande.md`](../documenti/appunti/2026-09-04_call-prossima-domande.md) (interno)
- [`../documenti/appunti/2026-09-08_questionario-michele-novi.pdf`](../documenti/appunti/2026-09-08_questionario-michele-novi.pdf) (da mandare a Michele)
- [`../ricerca/2026-09-04_mappatura-presenza-online.md`](../ricerca/2026-09-04_mappatura-presenza-online.md)
- [`../ricerca/2026-09-04_benchmark-siti-colleghi.md`](../ricerca/2026-09-04_benchmark-siti-colleghi.md)
- [`../ricerca/2026-09-04_linkedin-e-pubmed.md`](../ricerca/2026-09-04_linkedin-e-pubmed.md)
- [`../ricerca/2026-09-04_linkedin-post-come-articoli.md`](../ricerca/2026-09-04_linkedin-post-come-articoli.md)
- [`../ricerca/2026-09-04_idee-articoli-dai-paper.md`](../ricerca/2026-09-04_idee-articoli-dai-paper.md)
- [`../ricerca/2026-09-04_fondamenta-visual.md`](../ricerca/2026-09-04_fondamenta-visual.md) — tavole; il testo pieno è @16
- [`../ricerca/2026-09-04_quadro-dottor-novi.md`](../ricerca/2026-09-04_quadro-dottor-novi.md) � sintesi identita/sedi/NAP estratta dai siti (4/09/2026)
- [`../documenti/fonti/2026.08.29_Preventivo_Michele_Novi_JOB__0064_parte2.pdf`](../documenti/fonti/2026.08.29_Preventivo_Michele_Novi_JOB__0064_parte2.pdf) � allegato tecnico al preventivo (stesso contenuto del Piano tecnico CRM)

## Template standard (ogni capitolo)

```
## Metadati
- ID: CAP-NN
- Stato: Bozza
- Ultimo aggiornamento: AAAA-MM-GG
- Dipendenze: @NN_Nome
- Owner:

## Sintesi
## Stato attuale del progetto
## Idee future
## Nodi da sciogliere
## Passi successivi
## Decisioni congelate (lock-in)
## Rischi / Compliance & Riferimenti
```

## Glossario rapido

- **Vetrina**: sito che orienta e invita al contatto; niente prenotazione calendario in v1.
- **NAP**: Name, Address, Phone � devono coincidere su tutti i canali.
- **GBP**: Google Business Profile (ex Google My Business).
- **Keystatic**: pannello contenuti nel repo (blog, foto, testi), come su maurotoncelli.it.
- **i18n**: internazionalizzazione. Qui: italiano + inglese, routing `/it` `/en` (preferenza Mauro).
- **YMYL**: Your Money or Your Life � i contenuti sanitari hanno scrutinio SEO/E-E-A-T alto.
- **E-E-A-T**: Experience, Expertise, Authoritativeness, Trust.
- **CESAT**: Centro di Eccellenza per la Sostituzione Articolare Toscana, Ospedale San Pietro Igneo, Fucecchio. Sede ospedaliera pubblica di Michele.
- **Landing page** (nel linguaggio di Michele): sito chiaro e semplice. **Non** va interpretato come monopagina: l'architettura scelta � multipagina espandibile.

## CRM (riferimento interno Mauro)

- Gestione: Flowdesk � `/Volumes/Programs/Temporary files/sviluppo CRM personale`
- Job id **64**, contatto id **1003**, importo **1500 �**, stato `planned`, preventivo confermato **2026-08-31**.
