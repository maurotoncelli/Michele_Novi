# DECISIONI � Vincoli del progetto

> Raccolta delle scelte chiuse. In caso di dubbio **questo file prevale** sui capitoli.
> Stato: Bozza da validare con Mauro � Aggiornato: **2026-09-04**
> Origine: telefonata 28/08, piano tecnico 29/08, conferma preventivo 31/08, ricerca 04/09.

Le voci marcate **PROPOSTA** sono la raccomandazione di progetto, non ancora firmate da Michele.

---

## Offerta e relazione (@02, @14)

- Cliente: Dott. Michele Novi. Introduzione: Lorenzo Querci.
- Job CRM **#64**, contatto **#1003**.
- Preventivo **1.500 �** confermato il 31/08/2026, validit� fino al 31/10/2026.
- Pacchetto: sito vetrina + shooting + blog editabile + SEO di base + go-live. **Senza** calendario prenotazioni in v1.
- Propriet�: codice e contenuti del cliente a saldo avvenuto. Dominio intestato allo studio.
- Gestionale (clienti, cartelle, agenda, pagamenti): **fuori scope**, quotato a parte quando servir�.

## Cosa � il sito (@01, @04)

- Tre compiti: **farsi trovare**, **trasmettere autorevolezza in pochi secondi**, **rendere immediato il contatto** (telefono / WhatsApp / form).
- Michele lo chiama �landing page�. Interpretazione adottata: **chiarezza e sintesi**, non sito monopagina.
- **PROPOSTA congelata lato Mauro:** architettura **multipagina** (home, chi sono, sedi, patologie/servizi, contatti, blog). Espandibile. Scheletro a parole di ogni pagina: [@04](04_Architettura_Informazione.md). Un one-page renderebbe pi� difficile SEO locale e approfondimenti futuri.
- Il sito deve diventare la **fonte di verit�** rispetto a Doctolib, MiniHospital, directory e social.
- Non � un sito per �procacciarsi pazienti a vuoto�: lo studio � pieno. Serve **allineare** la presenza online.

## Stack (@05)

- Next.js (App Router) + TypeScript + Tailwind CSS.
- Hosting **Vercel** (HTTPS, preview, deploy da git).
- CMS: **Keystatic** nel repo (blog, foto, testi, sedi). Niente WordPress, niente CMS a canone, niente database pazienti.
- i18n: **italiano + inglese**, stile maurotoncelli.it (file di messaggi + rotte `/it` `/en`, hreflang). Non next-intl a 11 lingue.
- Form: email transazionale (stesso schema dei siti Mauro: niente dati sanitari).
- Analytics: GA4 + Search Console, cookie dopo consenso.
- Dati strutturati: `Physician` / `MedicalBusiness` / `MedicalWebPage` + sedi.
- Niente plugin da aggiornare, superficie di attacco minima.

## SEO (@06)

- HTML gerarchico (un H1 per pagina, H2/H3 veri), sitemap, metadata per pagina, JSON-LD.
- SEO locale: una pagina (o blocco forte) per sede; keyword �ortopedico + citt� e patologie a coda lunga.
- Indicizzazione pensata anche per motori conversazionali (titoli chiari, FAQ, `llms.txt` da valutare).
- **Dominio nuovo** (richiesta Michele). Se possiede ancora il vecchio dominio: tenerlo e fare **redirect 301** + Cambio indirizzo in Search Console. Senza propriet� del vecchio dominio **non** si eredita il punteggio.
- Blog come motore di visibilit� nel tempo, collegato a un futuro YouTube / reel Instagram.

## Google Business Profile (@08)

- **Non si pu�** fondere quattro indirizzi fisici in una sola scheda. Regola Google: **una sede verificabile = una scheda**.
- Quello che Michele pu� avere �unico� � il **sito** (e, se vuole, un Account di sedi che gestisce pi� schede).
- Se riceve in ambulatori **non suoi**, non si creano GBP fantasma su quell�indirizzo: si chiede di comparire come professionista sulla scheda della struttura, e si punta al sito.

## Contenuti e privacy (@10, @13)

- Form: solo nome e recapito + consenso. La descrizione del problema **non** passa dal sito.
- **PROPOSTA:** prezzi (se confermati) solo in Contatti, non sulle patologie. Interventi/ricoveri fuori listino vetrina.
- Foto: shooting reale, nessuna stock.
- Recensioni di terze parti: si possono citare/reimpaginare con attribuzione e, dove possibile, consenso; non inventarle.
- Casi clinici e nomi (Alonso incluso): **solo con consenso** e senza dati sanitari identificativi. Default: non pubblicare.
- YMYL: copy sanitario accurato, firma del medico sugli articoli, niente promesse di guarigione.
- **PROPOSTA editoriale:** niente pezzi da agenzia SEO. Articoli originali, in prima persona, nati da un **paper suo** o da una visita (lui detta, Mauro lima). LinkedIn = temi, non copy da incollare. Pila e metodo: `ricerca/2026-09-04_idee-articoli-dai-paper.md`.
- Foglio domande prossima call: `documenti/appunti/2026-09-04_call-prossima-domande.md`.

## Design (@03, @11)

- **PROPOSTA visiva:** stile da concetti suoi (varco, congruenza, quaderno), non da sito medico. Testo pieno: [@16](16_Fondamenta_Visive.md). Hex e font dopo lo shooting.


- Moderno, fruibile, distinto. Informazioni ad albero: in superficie sintesi, in profondit� termini specifici e coda lunga.
- Professionalit� + disponibilit� + chiarezza. Estetica alta, non �sito medico anni 2000�.
- Blog come punto nevralgico, non un appendice.
- CTA ovunque verso contatto / telefono / WhatsApp.

## Fuori v1 (annotato, non costruito)

- Prenotazione online / calendario
- Videochiamate
- Area paziente / cartelle
- Pagamenti
- Pannello recensioni �aggiungi dal vivo� se implica moderazione e dati: in v1 recensioni curate a mano nel CMS
