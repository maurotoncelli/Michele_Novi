# 09. Tecnica, SEO, privacy

> **Stato 16/09/2026**: implementato in `site/` come descritto qui, con due scostamenti minimi: le animazioni sono in **CSS puro + IntersectionObserver** (nessuna libreria `motion`: non serviva) e Next.js è alla **16** (il middleware si chiama `proxy.ts`). Riferimento pratico: `site/README.md`.

---

## Stack

Stesso filo di **maurotoncelli.it**. Il piano tecnico del 29/08 lo ha già venduto così ([`../fonti/pdf/Piano_Tecnico_Sito_Michele_Novi_2026.pdf`](../fonti/pdf/Piano_Tecnico_Sito_Michele_Novi_2026.pdf)).

| Livello | Scelta | Perché |
|---------|--------|--------|
| Framework | Next.js App Router + TypeScript + Tailwind | Veloce, manutenibile, SSG |
| i18n | File `messages/it` + `en`, rotte `/it` `/en` | Due lingue, non undici |
| CMS | Keystatic `/keystatic` | Paper, 1 nota, foto, sedi, recensioni; commit → Vercel |
| Form | Route handler + email | Solo contatto |
| Hosting | Vercel | HTTPS, preview, CDN |
| Dominio | Intestato a Michele | Dal giorno 1 |
| Analytics | GA4 + Search Console | Dopo consenso |
| Repo | GitHub (da creare) | Keystatic in GitHub mode |
| Motion | CSS + `motion` (ex Framer) solo dove serve | Giunti, strati, cucitura; rispetta `prefers-reduced-motion` |
| Ricerca | Nessuna in v1 | Filtri sugli Approfondimenti bastano |

Non copiare da Armellin: Stripe, Supabase, CRM, OTP, 11 lingue.  
Non copiare da maurotoncelli: gallery moda, iris, dark mode.  
Non copiare da `_archivio/demo-sito-2026-09/` (il codice; l'estetica sì, vedi `06_design.md`).

Pattern da guardare (fuori da questa cartella):  
`/Volumes/Programs/Temporary files/Progetti cursor/sito web mt 2026/site`

### Principio: tutto è dato

Il sito è un **renderer** di due sorgenti, mai un posto dove si scrive contenuto.

| Sorgente | Cosa contiene | Chi la tocca |
|----------|---------------|--------------|
| **Keystatic** (`content/`) | Sedi, patologie, pubblicazioni, note degli Approfondimenti, recensioni, profilo/CV, FAQ, foto, orari, telefono, impostazioni globali (dominio, social, WhatsApp) | Michele + Mauro |
| **i18n** (`messages/it.json`, `en.json`) | Navigazione, label, bottoni, microcopy, meta di default, testi legali brevi | Mauro |

Regole:

- **Zero stringhe hardcoded** nei componenti. Se un testo appare a schermo, viene da Keystatic o da `messages/`. Lint rule su stringhe letterali in JSX.
- **Zero numeri a mano**: telefono, indirizzi, orari, P. IVA, OMCeO stanno in `settings` e `sedi`. Header, footer, pagina sede, JSON-LD, `tel:` link li **leggono**.
- **Una collezione → una rotta dinamica**: aggiungere una sede o una patologia è creare un file, non toccare codice.
- Le fasce home che dipendono da dati (recensioni, Approfondimenti, video) **non si renderizzano** se la collezione è vuota.
- Contenuti bilingue: ogni entry Keystatic ha campi `it` / `en` affiancati (o entry gemella con `locale`); mai file EN duplicati a mano.

### Modello contenuti Keystatic

**Singleton**

- `settings` — nome, ruolo, telefono segreteria, WhatsApp, email, orari segreteria, P. IVA, OMCeO, PEC, social, dominio.
- `profilo` — bio breve/lunga, foto, CV strutturato (formazione, fellowship, incarichi, società, docenze).
- `home` — ordine e attivazione delle fasce.

**Collezioni**

- `sedi` — nome, struttura, indirizzo, città, coordinate, telefono proprio, orari, regime (SSN / privato / sport), servizi, foto, link Maps, `gbpUrl`.
- `patologie` — titolo, area (spalla / arto superiore / sport / come si opera), lead, corpo MDX, FAQ, patologie correlate, sedi dove si tratta, pubblicazioni correlate.
- `pubblicazioni` — titolo originale, autori, rivista, anno, DOI, PubMed ID, abstract, **riassunto per pazienti** (opzionale), PDF (se lecito), tag, patologie correlate. Ordine: anno desc.
- `approfondimenti` (etichetta CMS: Approfondimenti — Dal lavoro) — titolo, data, lead, corpo MDX, copertina (anteprima), tag, `video` (file) e/o `youtube` (URL o ID), pubblicazioni correlate, autore (fisso: Michele), stato bozza/pubblicato.
- `recensioni` — nome, testo, piattaforma, data, sede, mostra sì/no.
- `faq` — domanda, risposta, contesto (spalla / prima visita / sede).

Ogni entry ha `seo: { title, description, ogImage }` opzionale con fallback generato dal titolo.

### Approfondimenti (blog / news)

Nome della sezione: **Approfondimenti**. Rotta pubblica `/it/approfondimenti` (EN `/en/in-depth`). Cartella app: `approfondimenti/`.  
I vecchi slug `/quaderno` e `/notebook` fanno 301.

Dentro, due binari con filtro, stesso hub:

- **Pubblicazioni** — i paper, `/approfondimenti/pubblicazioni/[slug]`, impaginati da scientifici, `ScholarlyArticle`. Lista espandibile: prime 3, poi «Mostra tutte».
- **Dal lavoro** — le note per pazienti, `/approfondimenti/[slug]`, `Article` con autore visibile. Ogni nota ha copertina e slot video (file o YouTube).

Peso nel sito: voce di primo livello nel menu, fascia in home con gli ultimi 3 pezzi (misti), feed RSS `/approfondimenti/feed.xml`, ogni patologia linka i pezzi correlati e viceversa. Pagina tag `/approfondimenti/tag/[tag]`.

Flusso di pubblicazione: Michele scrive in `/keystatic` → bozza su branch → preview Vercel → merge → ISR rigenera la pagina, la home, il feed e la sitemap. Nessun deploy manuale.

### Rendering e velocità

- **SSG** per tutto; **ISR on-demand** via webhook GitHub al merge (o revalidate su deploy). Niente SSR per pagina.
- Contenuto MDX compilato a build; componenti MDX limitati (callout, figura, citazione paper, FAQ).
- `next/image` con AVIF/WebP, dimensioni dichiarate, `priority` solo sull'LCP di home.
- Font self-hosted via `next/font`: Newsreader (2 pesi) + Plus Jakarta Sans (2 pesi). Subset latino.
- CSS: Tailwind + token in `theme` (osso, menta, pesca, petrolio, rame). Niente CSS-in-JS runtime.
- JS al minimo: componenti server di default, `"use client"` solo per giunti/strati animati, tab, form, cookie banner.
- Budget: LCP < 2 s, CLS ≈ 0, INP < 200 ms, JS iniziale < 100 kB gz. Lighthouse ≥ 95 su mobile come soglia di merge.
- Video: poster + `preload="none"`, niente autoplay con audio.

### i18n

- Rotte `/it/...` e `/en/...`, `it` default con redirect da `/` in base ad `Accept-Language` (una volta, poi cookie).
- Slug tradotti dove ha senso SEO (`/it/approfondimenti` → `/en/in-depth`, `/it/dove` → `/en/locations`) tramite mappa in `i18n/routing.ts`.
- `hreflang` reciproco + `x-default` su ogni pagina; sitemap con alternates.
- Formattazione date/numeri via `Intl`, non stringhe.
- Contenuto senza traduzione EN: la pagina EN mostra l'IT con avviso, non 404. I paper restano in inglese in entrambe le lingue.

### Form

Nome, email e/o telefono, sede (select dalla collezione `sedi`), messaggio «come possiamo richiamarti?». Consenso. Honeypot + rate limit. Destinazione: `info@` della segreteria via Resend. Nessun dato salvato.

### Struttura repo (`site/`)

```
site/
  app/[locale]/            rotte (home, chi-sono, sedi/[slug], patologie/[slug], approfondimenti/..., contatti)
  components/ui/           osso, strati, giunto, docking, cucitura, tab
  components/blocks/       fasce home e pagina
  content/                 dati Keystatic (md/mdx/json/yaml)
  keystatic.config.ts      schema CMS
  messages/it.json en.json i18n
  lib/content.ts           reader Keystatic (unico punto di accesso ai dati)
  lib/seo.ts               metadata + JSON-LD generati dai dati
  i18n/routing.ts          locali, slug tradotti
```

Mai nel CMS: pazienti, cartelle, agenda.

### Form

Nome, email e/o telefono, sede (select delle 4), messaggio «come possiamo richiamarti?». Consenso. Honeypot. Destinazione: `info@` della segreteria.

### Auth Keystatic

In produzione chiuso (GitHub App). Mai `/keystatic` aperto.

Espandibilità: sedi e patologie sono dati. Quando arriverà l’agenda si aggiunge un modulo, non si riscrive il sito.

---

## SEO

Lui ha centrato la prima call su questo. Il sito nasce già a posto: un H1, H2 veri, title/description IT+EN, canonical, hreflang, sitemap, alt descrittivi, internal linking, Core Web Vitals.

### Dominio vecchio → nuovo

`centrosaluteonline.it` **è suo**. Si può trasferire molta autorità **se**:

1. Resta acceso 12+ mesi.
2. Redirect 301 URL per URL (non tutto in home).
3. Entrambe le proprietà in Search Console + Cambio indirizzo.

Senza proprietà del vecchio dominio non si eredita nulla. Qui la proprietà c’è: usarla.

### Keyword (albero, bozza)

**Testa (home / chi sono):** Michele Novi, ortopedico spalla Toscana, chirurgo spalla Pisa / Fucecchio / Peccioli.

**Locali (pagine sede):** solo le 4 città/strutture vere. Togliere dalla testa Capannoli, Fornacette, Santa Croce.

**Coda (spalla + paper):** cuffia dei rotatori, lussazione spalla, protesi spalla, artroscopia spalla, traumatologia sportiva Valdera, ecc.

Le code lunghe stanno nelle foglie e nei paper, non nel hero.

### Dati strutturati

`Physician`, `MedicalBusiness` / `LocalBusiness` per sede propria, `MedicalWebPage`, `BreadcrumbList`, `ScholarlyArticle` / `Article` sui paper, `FAQPage` sulla spalla.  
`Review` solo su recensioni vere. Niente `AggregateRating` gonfiato.

### Indicizzazione AI

Frasi-risposta nette negli H2, FAQ vere, autore visibile, affiliation CESAT, eventuale `/llms.txt`. Niente «primo su ChatGPT».

Eventi GA4: `click_call`, `click_whatsapp`, `form_submit`, `click_maps`.

---

## Privacy e deontologia

I dati di salute sono categoria particolare. Il sito **non li raccoglie**.

- Titolare: Dott. Michele Novi, P. IVA 02296540509, PEC michele.novi.w5is@pi.omceo.it, OMCeO Pisa **n. 5749**. Indirizzo di residenza **non** in vetrina.
- Cookie: GA4 dopo consenso.
- Recensioni: lui vuole nome e cognome — base giuridica da tenere a mente (consenso / già pubbliche). Non stravolgere il senso.
- Alonso e VIP: consenso scritto, o niente nome.
- Foto shooting: liberatoria sua; altri volti solo con liberatoria.
- Pubblicità sanitaria: informativa, non ingannevole (codice deontologia).
- Testi policy: Mauro redige bozza, non è consulenza legale.

YMYL: copy sanitario mediocre fa danno due volte (fiducia e ranking).
