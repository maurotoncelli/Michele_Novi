# Sito Dott. Michele Novi

Next.js 16 (App Router) ù TypeScript ù Tailwind v4 ù Keystatic ù i18n `/it` `/en` ù Vercel.

La documentazione di progetto (brief, decisioni, contenuti, design) ù in `../bibbia/`. Leggi prima `../bibbia/HANDOFF.md`.

## Comandi

```bash
npm install
npm run dev        # http://localhost:3000  (Keystatic: /keystatic)
npm run build      # build di produzione, tutte le rotte SSG
npm run start      # serve la build
npm run lint
npm run typecheck
```

## Variabili d'ambiente

Copia `.env.example` in `.env.local`. Nessuna variabile ù obbligatoria per il build:

| Variabile | Serve a |
|-----------|---------|
| `NEXT_PUBLIC_SITE_URL` | URL canonico finchù `settings.dominio` ù vuoto |
| `KEYSTATIC_STORAGE` | `local` (scrive su `content/`) o `github` (produzione) |
| `KEYSTATIC_GITHUB_*`, `KEYSTATIC_SECRET` | Solo con storage `github` |
| `RESEND_API_KEY`, `RESEND_FROM` | Invio email del form. Senza chiave il form logga e risponde ok |
| `NEXT_PUBLIC_GA_ID` | GA4. Se assente: niente banner, niente analytics |

## Dove sta cosa

```
content/            dati (YAML + Markdoc) gestiti da Keystatic ù unica fonte dei contenuti
public/images/disegni/  disegni del catalogo (singleton Keystatic `disegni`)
keystatic.config.tsx  schema: settings, profilo, home ó sedi, patologie, pubblicazioni, approfondimenti, faq, recensioni
src/i18n/           routing.ts (slug tradotti), messages/{it,en}.json (stringhe UI), legale.ts
src/lib/content.ts  unico punto di lettura dei dati (reader Keystatic + cache)
src/lib/seo.ts      metadata, hreflang, JSON-LD
src/lib/markdoc.tsx rendering del corpo (H1?H2, fallback EN?IT)
src/app/[locale]/   pagine; [...rest] ? 404 nel layout del sito
src/app/api/        contatto (Resend, honeypot, rate limit) ù keystatic
src/components/     Header, Footer, CookieBanner, ContactForm, ui/ (Segno, Reveal, Strati, Cucitura), blocks/
src/proxy.ts        redirect / ? /it|/en da Accept-Language + cookie mn_lang
```

## Regole

- Niente testo o numero hardcoded nelle pagine: stringhe UI in `messages/`, dati in `content/`.
- I campi bilingui sono oggetti `{ it, en }`; `pick()` ricade sull'italiano se manca l'inglese.
- I corpi Markdoc: `index.mdoc` (IT) + `corpoEn.mdoc` (EN). Nel corpo si parte da `##` (un `#` viene comunque reso come H2).
- Slug: `slug` per l'italiano, `slugEn` per l'inglese. Le rotte EN sono mappate in `routing.ts`; `next.config.ts` fa rewrite/redirect.
- Tutto SSG. Dopo un salvataggio in Keystatic (GitHub mode) parte il deploy Vercel.

## Deploy

Vercel, team `atstudio`, progetto `michele-novi-sito`, **root directory `site`** (il repo git sta una cartella sopra). Anteprima: <https://michele-novi-sito.vercel.app>.

```bash
# dalla radice del workspace (dove sta .git)
vercel deploy --scope atstudio          # anteprima
vercel deploy --prod --scope atstudio   # produzione
vercel env ls --scope atstudio
```

Con il repo collegato (`vercel git connect`), ogni push su `main` va in produzione da solo. Il `robots.txt` blocca l'indicizzazione finchù `settings.dominio` ù vuoto.
