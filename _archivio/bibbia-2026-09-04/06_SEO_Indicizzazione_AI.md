# 06. SEO e indicizzazione AI

> Parte della Bibbia. Indice: [00_README_Master_Index.md](00_README_Master_Index.md).

## Metadati
- ID: CAP-06
- Stato: Bozza
- Ultimo aggiornamento: 2026-09-04
- Dipendenze: @04_IA, @05_Stack, @08_Sedi, @10_Blog
- Owner: Mauro

## Sintesi
Michele ha centrato la call sulla SEO. Il sito deve nascere già “da libro”: gerarchia HTML, sitemap, keyword vere (specialità + città + patologie), dati strutturati, velocità. Dominio **nuovo**: l’autorità si costruisce; il vecchio dominio aiuta **solo** se resta suo e si redirige.

## Stato attuale del progetto

### Situazione SERP oggi (4/09, ricerca)
Chi cerca il dottore trova **terzi**: MiniHospital, Doctolib, TrovaOrtopedico, LinkedIn, Quinews, Athletica, Casa di Cura San Paolo. Non risulta un sito personale posizionato. Quindi un dominio nuovo non “ruba” traffico a se stesso: parte da zero sul brand, ma può puntare subito query locali e di specialità se i terzi restano coerenti e linkano il sito.

### Dominio vecchio ? punteggio nuovo
Risposta al dubbio di Mauro:

**Sì, si può trasferire molta dell’autorità**, ma con tre condizioni:

1. Michele **possiede** ancora il vecchio dominio (DNS).
2. Redirect **301/308** URL-per-URL (non tutto in home) dal vecchio al nuovo.
3. Entrambe le proprietà in Search Console + strumento **Cambio di indirizzo**, vecchio dominio acceso mesi (meglio 12+).

Se il “vecchio sito” è solo `michelenovi.centrosaluteonline.it` (terza parte), **non** si eredita nulla: si chiede alla piattaforma di aggiornare/cancellare la scheda.

Google non “regala” lo score di un dominio che si abbandona senza redirect. Non esiste un trucco per attaccare il PageRank di un dominio non proprio.

### On-page (v1 obbligatorio)
- Un **H1** per pagina, uguale all’intento (es. «Ortopedico a Fucecchio — Dott. Michele Novi», non tre H1).
- H2/H3 reali, non span stilizzati.
- `title` + `meta description` per pagina, IT e EN.
- Canonical + hreflang (`it`, `en`, `x-default`).
- `sitemap.xml` (entrambe le lingue) in robots.txt.
- URL corti, slug parlanti.
- Alt text fotografici descrittivi (non “IMG_0234”).
- Internal linking: home ? patologie ? sedi ? articoli correlati.
- Performance = ranking (e requisito di brief).

### Keyword — albero (bozza, da validare)

**Testa (home / chi sono):**  
`ortopedico Novi`, `Michele Novi`, `chirurgo spalla Toscana`, `ortopedico Fucecchio`, `ortopedico Pisa`

**Locali (pagine sede):**  
`ortopedico Peccioli`, `ortopedico Capannoli`, `ortopedico Fornacette`, `ortopedico Santa Croce sull'Arno` — solo per sedi **attive**.

**Coda lunga (pagine + blog):**  
`lesione cuffia dei rotatori`, `lussazione spalla sportivo`, `protesi spalla inversa`, `artroscopia spalla`, `ecografia muscoloscheletrica spalla`, `infiltrazione eco-guidata`, `ortopedico traumatologia sportiva Valdera`

Non inquinare il hero con 15 keyword. Le code lunghe stanno nelle foglie.

### Dati strutturati
- `Physician` (nome, immagine, specialità, telefono, `worksFor` / `affiliation`)
- `MedicalBusiness` o `LocalBusiness` per ogni sede propria
- `MedicalWebPage` / `FAQPage` sulle patologie
- `Review` / `AggregateRating` **solo** se le recensioni sono vere e le linee guida Google lo consentono (attenzione allo schema finto)
- `BreadcrumbList`
- `Article` sui post (autore = Michele Novi, `reviewedBy` se serve)

Doctolib ha già un JSON-LD Physician con prezzi e un solo indirizzo (San Pietro Fucecchio): il sito ufficiale deve essere **più completo e più vero**.

### Local SEO
- NAP identico ovunque.
- Ogni sede: pagina + embed mappa + link GBP **corretto** (struttura o proprio).
- Citazioni: aggiornare MiniHospital, Doctolib, Athletica, LinkedIn col nuovo URL; reclamare TrovaOrtopedico («Not verified»).
- Directory spazzatura (Localshop24, Reteimprese): chiedere correzione o removal.

### Indicizzazione AI
Obiettivo dichiarato in call. Cose che aiutano davvero (niente magie):

- Frasi-risposta nette in H2 («Di cosa si occupa il Dott. Novi?», «Dove visita a Peccioli?»).
- FAQ con domande reali dei pazienti.
- Autore visibile, date, affiliation ospedaliera (E-E-A-T / YMYL).
- Eventuale `/llms.txt` con sintesi factual del medico e link alle pagine canoniche.
- Markup pulito, niente testo nei canvas/immagini.

Non promettere “primo su ChatGPT”.

### Analytics
GA4 + Search Console dal giorno 1. Eventi: `click_call`, `click_whatsapp`, `form_submit`, `click_maps`.  
Niente GTM obeso.

## Idee future
- Articoli pillar collegati a YouTube (stesso H1, embed).
- Monitoraggio ranking query locali vs Nicoletti/Checcucci (concorrenza di indicizzazione, @12).

## Nodi da sciogliere
D1 dominio, D2 città da spingere, D5 perimetro keyword, D12 URL colleghi citati da Michele.

## Passi successivi
- Lista keyword concordata in 1 pagina, non un file da 200 righe.
- Alla registrazione dominio: Search Console immediata (anche in preview noindex finché non è pronto).

## Decisioni congelate (lock-in)
- SEO strutturale da giorno 1, non “dopo”.
- Dominio nuovo ok; 301 solo se il vecchio è suo.
- Niente keyword stuffing nel hero.

## Rischi / Compliance & Riferimenti
- YMYL: contenuti medici mediocri possono **non** rankingare e fare danno reputazionale.
- Documentazione Google: redirect 301/308 permanenti.
- Ricerca interna: `ricerca/2026-09-04_mappatura-presenza-online.md`
