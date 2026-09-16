# HANDOFF per il prossimo agente

> Documento di passaggio di consegne. Aggiornato: **2026-09-04**.
> Scopo: permettere a un nuovo agente (senza contesto di chat) di riprendere il lavoro.
> Leggere **questo file per primo**, poi [DECISIONI.md](DECISIONI.md) e [00_README_Master_Index.md](00_README_Master_Index.md).
> Workspace: `/Volumes/Programs/Temporary files/Progetti cursor/Michele_Novi_Website`

---

## In una frase

Sito vetrina **veloce, SEO, IT+EN, data-driven**, per il Dott. Michele Novi (ortopedico traumatologo, focus arto superiore). Obiettivo: far capire **chi �, dove riceve, cosa cura**, e **invitare al contatto** con la segreteria. Niente WordPress, niente prenotazione calendario in v1. Codice ancora da scrivere (`site/` vuoto).

## Stato al 4 settembre 2026

| Cosa | Stato |
|------|--------|
| Brief + preventivo | Preventivo **1.500 �** inviato 29/08, **confermato 31/08** (valido fino al 31/10). Job CRM **#64** `planned`. |
| Piano tecnico PDF | Allegato �parte 2� del preventivo 29/08. Copie in `documenti/fonti/` (file Downloads + copia CRM). Contenuto gi� in @04 @05 @14. |
| CV europeo 2019 | MiniHospital PDF: formazione/fellowship. **Non** copre CESAT/Modena. |
| CV LinkedIn | Profilo [michele-novi-5897775a](https://www.linkedin.com/in/michele-novi-5897775a/) ricostruito in `ricerca/2026-09-04_linkedin-e-pubmed.md` (fetch diretto LinkedIn bloccato; timeline + PubMed 16 record). |
| Bibbia di progetto | Prima stesura (tutti i capitoli in **Bozza**) |
| Codice sito | **Non iniziato** |
| Dominio | **Non scelto**. Michele vuole un nome nuovo, non il vecchio dominio. |
| Shooting | Incluso nel prezzo; da fissare |
| Contenuti definitivi | Da raccogliere (sedi attive, orari, recensioni, testi, foto) |
| Quadro presenza online | Estratto 4/09 in `ricerca/2026-09-04_quadro-dottor-novi.md` (bios, sedi, NAP, prezzi). Da validare con Michele. |
| Linea articoli | Originali dai paper, non pseudo-SEO. Idee: `ricerca/2026-09-04_idee-articoli-dai-paper.md`. |
| Fondamenta visive | Capitolo [@16](16_Fondamenta_Visive.md). Tavole in `ricerca/2026-09-04_fondamenta-visual.md`. Palette dopo shooting. |
| Prossima call | Interno: `documenti/appunti/2026-09-04_call-prossima-domande.md`. Da mandare: `documenti/appunti/2026-09-08_questionario-michele-novi.pdf`. |

Non c'� ancora repo git remoto, n� progetto Vercel, n� Keystatic.

## Cosa fare adesso (ordine)

1. **Validare con Mauro** le decisioni in [DECISIONI.md](DECISIONI.md) (architettura multipagina, stack, no calendario v1).
2. Chiudere i nodi con Michele usando `documenti/appunti/2026-09-04_call-prossima-domande.md` (sedi, telefono, prezzi, collega, paper, Doctolib).
3. Far spuntare il quadro (`ricerca/2026-09-04_quadro-dottor-novi.md`). Lo scheletro delle pagine � in [@04](04_Architettura_Informazione.md) � non � copy, � IA.
4. Solo dopo: scaffold Next.js in `site/`, i18n IT/EN, Keystatic, pagine.

Non partire a scrivere codice finch� dominio, elenco sedi **attive** e telefono pubblico non sono confermati: sono NAP e finiscono in JSON-LD / GBP.

## Chi � il cliente

- **Dott. Michele Novi**, nato 27/10/1987, Pisa.
- Ortopedico traumatologo. Specializzazione Pisa 110/110 e lode. Focus: **spalla, gomito, mano**, traumatologia sportiva, artroscopia, protesi, eco MSK.
- Ruolo pubblico: dirigente medico **CESAT � Ospedale San Pietro Igneo, Fucecchio** (da maggio 2021). Collega di reparto: Dott. Simone Nicoletti.
- Libera professione su pi� ambulatori (elenco instabile: va verificato uno per uno, [@08](08_Sedi_e_Google_Business.md)).
- Ha una **segreteria**. Lo studio � pieno: il sito serve a **chiarire**, non a �riempire l�agenda a tutti i costi�.
- Introdotto da **Lorenzo Querci** (parente acquisito; contatto CRM #4).
- Ha visto il sito di Mauro e lo ha trovato troppo complesso: chiede qualcosa di pi� semplice, che lui chiama �landing page�.

Contatti CRM (non pubblicare alla cieca):

- Email: `miche.novi@gmail.com`
- Cellulare in anagrafica CRM / CV: `+39 329 7382673`
- Telefono pubblico (Instagram + Doctolib + LinkedIn, segreteria): `+39 348 4331733`
- Nel CRM il job title � errato: �Fisioterapista�. � **ortopedico**.

Dettaglio profilo: [@15](15_Profilo_Clinico_e_CV.md), quadro `ricerca/2026-09-04_quadro-dottor-novi.md`, CV `documenti/fonti/CV-NOVI-1.pdf`.

## Cosa ha chiesto (dal primo contatto, 28/08)

Trascrizione in `documenti/appunti/2026-08-28_primo-contatto.md`. Sintesi:

- Vetrina chiara: **dove si trova** e **cosa fa**. Sta togliendo presenza da altri siti perch� creano confusione.
- Invito al contatto (telefono / messaggio), non self-booking in v1.
- Sito **espandibile** (futuro: appuntamenti, videochiamate). Data-driven.
- **IT + EN** (i18n come piace a Mauro).
- **SEO ossessiva**: gerarchia H1/H2, sitemap, keyword, indicizzazione Google **e AI**.
- Recensioni sparse (MioDottore, altre piattaforme, screenshot): reimpaginarle nello stile del sito.
- Blog alimentato da un piano editoriale social (riuso). Esempio contenuto: caso Alonso � **non pubblicare senza consenso** ([@13](13_Privacy_GDPR.md)).
- Foto/video: shooting incluso; Mauro ha proposto anche video in pacchetto.
- Non vuole WordPress n� CMS a canone. Pannello tipo Keystatic (foto, articoli).

## Cosa � gi� deciso (non riaprire senza motivo)

Elenco completo: [DECISIONI.md](DECISIONI.md). I tre vincoli che evitano errori di scope:

1. **Multipagina**, non one-page. �Landing page� = chiarezza, non un�unica scrollata.
2. **Stack**: Next.js App Router + Tailwind + TypeScript + Keystatic + Vercel + i18n custom IT/EN. Come maurotoncelli.it, **non** come successioniarmellin (niente Stripe, area riservata, CRM paziente).
3. **Form v1**: nome + recapito + consenso. **Mai** dati clinici nel form.

## Cosa non fare

- Non copiare pagamenti, area cliente, CRM, 11 lingue, ADS dal progetto Armellin.
- Non inventare sedi, orari, prezzi, recensioni.
- Non pubblicare nomi di pazienti (Alonso incluso) senza autorizzazione scritta.
- Non creare un unico Google Business Profile per quattro indirizzi: Google non lo permette ([@08](08_Sedi_e_Google_Business.md)).
- Non usare foto stock. Shooting vero.
- Non mettere Keystatic / CMS in produzione senza auth.
- Non committare `.env`, token, password.

## File utili, in ordine di lettura

1. Questo Handoff
2. [DECISIONI.md](DECISIONI.md)
3. [DOMANDE_APERTE.md](DOMANDE_APERTE.md)
4. [`../documenti/appunti/2026-09-04_call-prossima-domande.md`](../documenti/appunti/2026-09-04_call-prossima-domande.md) � foglio domande call
5. [`../ricerca/2026-09-04_quadro-dottor-novi.md`](../ricerca/2026-09-04_quadro-dottor-novi.md)
6. [02_Cliente_e_Brief.md](02_Cliente_e_Brief.md)
7. [04_Architettura_Informazione.md](04_Architettura_Informazione.md)
8. [05_Stack_Tecnologico.md](05_Stack_Tecnologico.md)
9. [07_Presenza_Online.md](07_Presenza_Online.md) + mappatura in `ricerca/`
10. [08_Sedi_e_Google_Business.md](08_Sedi_e_Google_Business.md)
11. [16_Fondamenta_Visive.md](16_Fondamenta_Visive.md) — concetti visivi
12. Piano tecnico PDF e CV in `documenti/fonti/`

## Riferimenti tecnici Mauro (fuori da questa cartella)

- Sito personale (pattern da copiare): `/Volumes/Programs/Temporary files/Progetti cursor/sito web mt 2026` � i18n custom, Keystatic, Vercel.
- CRM job: SQLite `server/data/flowdesk.db`, tabella `jobs` id 64, `job_interactions` id 55 (call).
- Non modificare il CRM da questa chat salvo richiesta esplicita.

## Offerta economica (da piano tecnico)

- **1.500 �** tutto compreso, prezzo di lancio fuori listino.
- Include: sito su misura, shooting in studio, blog Keystatic, SEO locale, form/WhatsApp/mappe, go-live, formazione blog.
- **Non include** (a parte): rinnovo dominio, casella email, hosting/manutenzione continuativa, gestionale appuntamenti.
- Gestionale futuro: progetto separato, da 1.500 � in su.

Fasi previste dal piano: avvio settimana 1 ? design/dev settimane 1�2 ? shooting in parallelo ? revisione/go-live settimane 3�4, dal momento in cui arrivano i materiali.

## Prompt minimo per una chat nuova

```
Leggi bibbia/HANDOFF_AGENTE.md, poi bibbia/DECISIONI.md.
Workspace: Michele_Novi_Website.
Non scrivere codice finch� non te lo chiedo.
Compito: �
```
