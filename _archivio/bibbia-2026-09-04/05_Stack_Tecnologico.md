# 05. Stack tecnologico

> Parte della Bibbia. Indice: [00_README_Master_Index.md](00_README_Master_Index.md).

## Metadati
- ID: CAP-05
- Stato: Bozza
- Ultimo aggiornamento: 2026-09-04
- Dipendenze: @04_IA, @06_SEO, @13_Privacy
- Owner: Mauro

## Sintesi
Stesso filo di **maurotoncelli.it**: Next.js su Vercel, contenuti nel git, pannello Keystatic per blog e foto, i18n custom IT/EN. Niente WordPress, niente canoni CMS, niente backend pazienti. Il piano tecnico del 29/08 lo ha già venduto così.

## Stato attuale del progetto

### Scelte (allineate al PDF allegato al preventivo)

| Livello | Tecnologia | Perché |
|---------|------------|--------|
| Framework | Next.js (App Router) + TypeScript + Tailwind | Pagine pre-generabili, veloci, manutenibili |
| i18n | Custom come maurotoncelli.it: `messages/it.ts` + `messages/en.ts`, rotte `/it` `/en` | Preferenza Mauro («18in»); due lingue, non undici |
| CMS | Keystatic (`/keystatic`) | Blog, foto, sedi, recensioni editabili; commit ? deploy Vercel |
| Form | Route handler + email transazionale | Solo contatto, consenso privacy |
| Hosting | Vercel | HTTPS, preview PR, CDN |
| Dominio | Intestato a Michele | Proprietà dal giorno 1 |
| Analytics | GA4 + Search Console | Dopo consenso cookie |
| Repo | GitHub (da creare) | Keystatic GitHub mode in produzione |

Riferimento implementativo da copiare (pattern, non copy):  
`/Volumes/Programs/Temporary files/Progetti cursor/sito web mt 2026/site`  
— `keystatic.config.tsx`, `src/i18n/messages/`, `content/`, script prebuild se serve.

Non copiare: proof gallery clienti, 5+ lingue, iris loader, hero moda.

Non copiare da Armellin: Supabase, Stripe, CRM, OTP, 11 locale.

### Data-driven: cosa vive nel CMS vs nel codice

**Keystatic (Michele / Mauro / segreteria):**

- Articoli blog (markdown)
- Recensioni curate
- Foto gallerie (home, chi sono, sedi)
- Anagrafica sedi (indirizzo, orari, tel, mappe)
- Eventuali FAQ

**Codice / messages i18n (sviluppo):**

- Navigation, CTA, microcopy
- Struttura pagine
- Schema JSON-LD (valori letti dai dati CMS)

**Mai nel CMS pubblico:** dati pazienti, cartelle, agenda.

### i18n — regole
- Italiano lingua di default; `x-default` ? IT.
- Ogni stringa UI in entrambi i file. Niente testo hardcoded nei componenti.
- Slug EN tradotti (`/en/conditions/rotator-cuff`, non `/en/patologie/cuffia`).
- hreflang su ogni pagina.
- Traduzione EN: AI + revisione (Michele C1 o Mauro). Testi sanitari: revisione umana obbligatoria.

### Performance
- SSG/ISR per pagine pubbliche.
- Immagini: `next/image`, WebP, ritratto e sedi da shooting (non 4K raw in git).
- Video: compresso, poster, niente autoplay con audio.
- Font: self-hosted, pochi pesi.
- Obiettivo: LCP forte sulla home (foto hero ottimizzata).

### Form
Campi: nome, email e/o telefono, sede di interesse (select), messaggio **libero non clinico** (etichetta: «Come possiamo richiamarti?», non «Descrivi il tuo dolore»).
Consenso privacy obbligatorio. Honeypot + (se serve) Turnstile.
Destinazione: casella della segreteria, non Gmail personale se si può evitare.

### Auth Keystatic
In produzione: GitHub App, come maurotoncelli. Solo account Mauro (e in seguito Michele se vuole pubblicare da solo).
Mai lasciare `/keystatic` aperto.

### Espandibilità (senza costruirla ora)
Il data model sedi/patologie deve essere file/JSON, non sezioni hardcodate. Quando arriverà l’agenda, si aggiunge un modulo, non si riscrive il sito.
Un gestionale tipo Flowdesk resta **progetto separato**.

## Idee future
- `llms.txt` + pagine FAQ per citazioni AI.
- Webhook Keystatic ? notifica «articolo pubblicato».
- Newsletter: no in v1.

## Nodi da sciogliere
- Account Vercel / GitHub del progetto (Mauro vs org).
- Provider email (Resend vs altro già in uso).
- Dominio registrar.

## Passi successivi
1. Creare repo quando si inizia lo scaffold.
2. Copiare il minimo vitale da maurotoncelli (i18n + Keystatic), non l’intero site.
3. `site/README.md` con comandi `dev` / `build` / Keystatic local.

## Decisioni congelate (lock-in)
- Next + Tailwind + TS + Keystatic + Vercel.
- IT+EN custom i18n.
- Niente WordPress, niente CMS a pagamento, niente DB pazienti.
- Form senza dati sanitari.

## Rischi / Compliance & Riferimenti
- Keystatic GitHub scrive sul repo: branch protection e preview prima di mergiare articoli.
- Residenza analytics: GA4 è extra-UE ? cookie banner e base giuridica (@13).
- Piano tecnico pp. 1–2.
