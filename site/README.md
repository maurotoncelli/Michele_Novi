# Sito Dott. Michele Novi

Next.js 16 (App Router) · TypeScript · Tailwind v4 · Keystatic · i18n `/it` `/en` · Vercel.

La documentazione di progetto (brief, decisioni, contenuti, design) è in `../bibbia/`. Leggi prima `../bibbia/HANDOFF.md`.

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

Copia `.env.example` in `.env.local`. Nessuna variabile è obbligatoria per il build:

| Variabile | Serve a |
|-----------|---------|
| `NEXT_PUBLIC_SITE_URL` | URL canonico finché `settings.dominio` è vuoto |
| `KEYSTATIC_STORAGE` | `local` (scrive su `content/`) o `github` (produzione) |
| `KEYSTATIC_GITHUB_*`, `KEYSTATIC_SECRET` | Solo con storage `github` |
| `RESEND_API_KEY`, `RESEND_FROM` | Invio email del form. Senza chiave il form logga e risponde ok |
| `NEXT_PUBLIC_GA_ID` | GA4. Se assente: niente banner, niente analytics |

## Dove sta cosa

```
content/            dati (YAML + Markdoc) gestiti da Keystatic — unica fonte dei contenuti
keystatic.config.tsx  schema: settings, profilo, home · sedi, patologie, pubblicazioni, quaderno, faq, recensioni
src/i18n/           routing.ts (slug tradotti), messages/{it,en}.json (stringhe UI), legale.ts
src/lib/content.ts  unico punto di lettura dei dati (reader Keystatic + cache)
src/lib/seo.ts      metadata, hreflang, JSON-LD
src/lib/markdoc.tsx rendering del corpo (H1?H2, fallback EN?IT)
src/app/[locale]/   pagine; [...rest] ? 404 nel layout del sito
src/app/api/        contatto (Resend, honeypot, rate limit) · keystatic
src/components/     Header, Footer, CookieBanner, ContactForm, ui/ (Segno, Reveal, Strati, Cucitura), blocks/
src/proxy.ts        redirect / ? /it|/en da Accept-Language + cookie mn_lang
```

## Regole

- Niente testo o numero hardcoded nelle pagine: stringhe UI in `messages/`, dati in `content/`.
- I campi bilingui sono oggetti `{ it, en }`; `pick()` ricade sull'italiano se manca l'inglese.
- I corpi Markdoc: `index.mdoc` (IT) + `corpoEn.mdoc` (EN). Nel corpo si parte da `##` (un `#` viene comunque reso come H2).
- Slug: `slug` per l'italiano, `slugEn` per l'inglese. Le rotte EN sono mappate in `routing.ts`; `next.config.ts` fa rewrite/redirect.
- Tutto SSG. Dopo un salvataggio in Keystatic (GitHub mode) parte il deploy Vercel.
