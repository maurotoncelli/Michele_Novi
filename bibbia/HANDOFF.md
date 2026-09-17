# Handoff

> Prima lettura per una chat nuova. Workspace: `Michele_Novi_Website`.  
> Aggiornato: **17 settembre 2026, mattina**. Restyling presenza (Aesop/Odyssée) in codice; trattini «da quaderno» aboliti.

## In una frase

Sito vetrina **veloce, SEO, italiano + inglese, data-driven** per il Dott. Michele Novi: chirurgo di **spalla e arto superiore**, riferimento in Toscana. Deve far capire **cosa fa, dove, come contattarlo**. Niente WordPress, niente prenotazione in v1. Il codice in `site/` **c’è**: v1 strutturale + passata visiva del 17/09. Manca il contenuto che dipende da Michele (telefono, dominio, shooting, 7 PDF a pagamento). Il prototipo HTML in `_archivio/demo-sito-2026-09/` **non si usa**.

## Stato del sito (`site/`)

- **Stack**: Next.js 16 App Router, TypeScript, Tailwind v4, Keystatic (local ora, GitHub in produzione), i18n `/it` `/en` con slug tradotti, Resend per il form, Vercel (`michele-novi-sito`).
- **Pagine**: home · chi-sono · cosa-curo (+ schede) · dove (+ 4 sedi) · **Approfondimenti** (`/it/approfondimenti`, EN `/en/in-depth`; cartella `quaderno/`) · **Pubblicazioni** in menu · contatti · privacy · cookie · 404. I vecchi `/quaderno` e `/notebook` fanno 301.
- **Dev**: `cd site && npm run dev` → `:3000`, pannello `/keystatic`. Vedi `site/README.md`.
- **Quando arrivano i dati** si compilano **solo in Keystatic** (o nei YAML): niente da toccare nel codice, salvo bug.

## Scelte importanti (chiuse il 17/09)

Non riaprire in una chat nuova se non lo chiede Mauro. Dettaglio: [DECISIONI.md](DECISIONI.md), appunti in [`../fonti/appunti/2026-09-17_restyling-estetico.md`](../fonti/appunti/2026-09-17_restyling-estetico.md).

### Presenza

1. **Riferimenti: Aesop + Odyssée.** Pulizia, crema, un accento, aria. Non si implementano le tavole C/D come fork; non si torna al ramo `restyling-osseo` (sagome).
2. **Lastre piatte.** Niente ombre, niente raggio a blob, niente vetro, niente aloni. Scheda = immagine a vivo + titolo. Hover = titolo petrolio.
3. **Accento azzurro `#1E6AA8`** (`--color-petrolio`). Eyebrow, tag, link, bottone, voce attiva. Non il teal vecchio, non l’azzurro da portale.
4. **Niente trattini sotto i titoli, niente filo a tutta riga, niente cucitura a onda.** Mauro (17/09): sembrano un quaderno; prima era più moderno. Il ritmo è **spazio + fascia crema** (`bg-osso-3` su `Sezione tinta="osso"` e sulle Intestazioni), non una riga. Componente `Cucitura.tsx` **eliminato**.
5. **Font: Geist** per tutto, ancora. Newsreader resta fuori. Un carattere «con spina» è **aperto**, non si mescolano due famiglie.
6. **Disegni:** quelli in `public/images/disegni/` sono atlas a matita, tappabuchi. Serve un’altra mano (Ciccolella / Ponzi / Amargo…). Non copiare un pezzo.

### Header e albero

7. **Header desktop = una riga:** nome a sinistra, voci al centro, lingua + Scrivi a destra. Sticky, crema, bordo basso. Il **ruolo sotto il nome è nascosto da `lg` in su**: collideva con il menu. In tablet/mobile il ruolo può restare; hamburger sotto `lg`.
8. **Menu:** Chi sono · Cosa curo · Dove · Approfondimenti · **Pubblicazioni** · Contatti. Non si toglie Pubblicazioni.

### Pagine

9. **Chi sono — apertura.** Ritratto 4:5 a sinistra, testo a destra, **allineati in alto**, blocco `max-w-5xl`. Sotto il nome sta il titolo professionale (corpo, non maiuscoletto sotto la foto). Poi l’apertura, poi le lingue. **Niente** monogramma MN, **niente** colophon dei fellowship (è già In evidenza), **niente** didascalia sotto il ritratto.
10. **Dove (hub).** In desktop **due colonne:** Dove visito | Dove opero. Un colpo d’occhio.
11. **Scheda sede.** A destra (sticky in desktop) iframe **Google Maps** (`maps.google.com/...&output=embed`). Query = `nome + indirizzo` (Google piazza il posto; le coordinate in YAML restano per JSON-LD). Info in **griglia iconografica** 2×2: prenota, come arrivare, accessibilità, parcheggio (si spezza il testo se c’è «parchegg-»). Bottone «Apri in Google Maps».
12. **Barre CV** (Formazione e percorso): tre colonne, ogni voce è `grid` **binario + testo**. I puntini stanno nella colonna del filo, **non sopra i titoli**. Non tornare al posizionamento assoluto.

### Pubblicazioni

13. Rosa «tra le principali»: 14 voci, fede in [`../fonti/pdf/PUBBLICAZIONI.md`](../fonti/pdf/PUBBLICAZIONI.md).
14. **PDF originali solo se open access.** 7 file in `site/public/paper/` (+ copia in `fonti/pdf/paper/`). Campo Keystatic `pdf`. Bottone **PDF**.
15. **Paywall (7):** niente file hostato. Bottone **Articolo** → DOI (`hrefArticolo`). Li deve mandare lui (accepted manuscript / copia autore) se li vuole in sito: 3D Minerva, scafoide Minerva, gomito AOTS, lussazione bloccata, Gartland/Injury, claims PTH, head-split JBJS.

## Cosa è ancora aperto (design)

- Font con più carattere (Geist è neutro).
- Famiglia illustrazioni.
- Shooting: ritratto e foto sedi. Oggi placeholder.
- Scelta C vs D del 16/09: **superata come fork**; l’hero è già foto full-bleed, le fasce sono piatte + disegni-tappabuchi.

## Deploy e repo

- **Vercel**: `michele-novi-sito`, team ATSTUDIO, root `site`, Node 24. <https://michele-novi-sito.vercel.app>. Env: `KEYSTATIC_STORAGE=github`, owner/repo `maurotoncelli/Michele_Novi`, `KEYSTATIC_PATH_PREFIX=site`. Da aggiungere: chiavi GitHub App, `KEYSTATIC_SECRET`, `RESEND_API_KEY`, `NEXT_PUBLIC_GA_ID`.
- **Git**: un repo alla radice (bibbia + fonti + site). GitHub `maurotoncelli/Michele_Novi`, **privato**. Vercel builda solo `site/`.
- **robots.txt**: `Disallow: /` finché `settings.dominio` è vuoto. Appena c’è il dominio, Keystatic → settings → Dominio.
- **Dominio**: lo compra il cliente. Poi Vercel Domains + DNS.
- La passata 17/09 può essere **ancora in working tree** (non committare se non lo chiede Mauro).

## Cosa è successo

| Data | Cosa |
|------|------|
| 28/08/2026 | Primo contatto. Brief: chiarezza, SEO, vetrina, IT+EN. |
| 31/08 | Preventivo 1.500 € confermato. |
| 4/09 | Prima bibbia. |
| ~inizio/09 | Demo HTML magnetica. **Archiviata.** |
| set 2026 | Incontro San Verano. Sedi, perimetro, P. IVA. |
| 16/09 | CV 2026. Stack + v1 in `site/`. Repo + Vercel. Mauro: troppo statico, serif no → Geist, hero full-bleed. |
| 16/09 sera | Menu **Approfondimenti**. |
| 17/09 | **Pubblicazioni** in menu. 14 paper da Drive; 7 PDF OA. Recensioni in Keystatic. Restyling Aesop/Odyssée: header a una riga, lastre piatte, petrolio `#1E6AA8`, Dove a due colonne, Maps + icone in sede, barre CV sistemate. **Trattini e cucitura via** (effetto quaderno). |

## Cosa fare adesso (ordine)

**Dati (bloccano il go-live, non il design)**

1. Far **ricontrollare il cellulare** (348 4332733 detto vs 348 4331733 online). Poi `settings.telefono` / `whatsapp`.
2. Dominio (cliente) → `settings.dominio`. Orari segreteria → `settings.orari`.
3. 7 PDF paywall da Michele, se li vuole sul sito.
4. URL delle 4 schede Google. Shooting ritratto + sedi.
5. Far validare le bozze `site/content/patologie/*`.

**Design (non bloccante, non mescolare)**

6. Font con spina — una famiglia sola, poi si cambia in `layout` + `globals.css`.
7. Nuova mano di disegni; sostituire l’atlas.

Il codice è pronto ma i campi vuoti restano vuoti. Non inventare telefono, orari o civici «tanto poi si cambia».

## Vincoli che non si riaprono

Elenco pieno: [DECISIONI.md](DECISIONI.md). I quattro che evitano errori:

1. **Multipagina**, non one-page.
2. **Quattro sedi**, stop. CESAT, San Rossore, San Verano (solo visite), Villa Donatello (solo chirurgia).
3. Stack: Next.js + Tailwind + TypeScript + Keystatic + Vercel + i18n `/it` `/en`.
4. Form: nome + recapito + consenso. **Mai** dati clinici. Prezzi **non** online.

## Cosa non fare

- Non copiare `_archivio/demo-sito-2026-09/`.
- Non rimettere trattini sotto i titoli, filo a tutta riga, cucitura a onda, monogramma MN, ruolo in header desktop.
- Non hostare PDF di riviste a pagamento.
- Non inventare sedi. Non nominare Nicoletti. Non ostentare che San Verano è suo.
- Non pubblicare Alonso senza consenso. Non fondere quattro indirizzi in una scheda Google.
- Non committare `.env`, token, password. Non committare se non lo chiede Mauro.

## Chi è

- **Dott. Michele Novi**, nato 27/10/1987. Albo Pisa n. 5749.
- Dirigente medico, **SOC Ortopedia Protesica**, San Pietro Igneo / CESAT, Fucecchio, dal 2021. Fellowship 2025 a **Harvard / MGH** (Elhassan). Focus spalla e arto superiore; anche sport, artroscopia, protesi; anca/ginocchio in ospedale.
- Segreteria. Studio pieno: il sito **allinea**, non “riempie l’agenda”.
- Introdotto da Lorenzo Querci. Ha visto il sito di Mauro: troppo complicato.

Contatti di lavoro: [03_sedi_e_contatti.md](03_sedi_e_contatti.md).

## Prompt minimo per una chat nuova

```
Leggi bibbia/HANDOFF.md e bibbia/DECISIONI.md, poi site/README.md.
Workspace: Michele_Novi_Website. Il sito è in site/ (Next.js + Keystatic).
Non usare _archivio/demo-sito-2026-09.
Non rimettere trattini sotto i titoli né la cucitura.
Testi e dati stanno in site/content e site/src/i18n/messages: niente hardcoded nelle pagine.
Compito: …
```
