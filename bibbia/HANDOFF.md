# Handoff

> Prima lettura per una chat nuova. Workspace: `Michele_Novi_Website`.  
> Aggiornato: **16 settembre 2026, sera**. Sezione **Approfondimenti**, header solido, barre CV, pubblicazioni espandibili.

## In una frase

Sito vetrina **veloce, SEO, italiano + inglese, data-driven** per il Dott. Michele Novi: chirurgo di **spalla e arto superiore**, riferimento in Toscana. Deve far capire **cosa fa, dove, come contattarlo**. Niente WordPress, niente prenotazione in v1. Il codice in `site/` **c'è ed è completo in v1** (build pulita, tutte le rotte statiche): manca solo il contenuto che dipende da Michele. Il prototipo HTML in `_archivio/demo-sito-2026-09/` **non si usa**.

## Stato del sito (`site/`)

Fatto il 16/09/2026, dopo l'ok a stack ([09_tecnica.md](09_tecnica.md)) e direzione estetica «schede ossee» ([06_design.md](06_design.md)).

- **Stack**: Next.js 16 App Router, TypeScript, Tailwind v4, Keystatic (local ora, GitHub in produzione), i18n `/it` `/en` con slug tradotti, Resend per il form, Vercel come target.
- **Pagine**: home · chi-sono · cosa-curo (+ 5 schede) · dove (+ 4 sedi) · **Approfondimenti** (`/it/approfondimenti`, EN `/en/in-depth`; cartella interna `quaderno/`) · contatti · privacy · cookie · 404. Tutte in IT e EN. I vecchi URL `/quaderno` e `/notebook` fanno 301.
- **SEO**: metadata + canonical + hreflang, JSON-LD (Physician, MedicalBusiness per sede, MedicalWebPage, ScholarlyArticle, Article, FAQPage, Breadcrumb), sitemap, robots, `/llms.txt`, OG image generata.
- **Contenuti seminati** da questa bibbia: settings, profilo, home, 4 sedi, 5 patologie (IT+EN, bozze), 12 paper dal CV, 1 nota di esempio, 5 FAQ. Recensioni: vuote.
- **Volutamente vuoti** (in `site/content/settings.yaml`): `telefono`, `whatsapp`, `email`, `emailDestinazioneForm`, `orari`, `dominio`. Il sito degrada bene: senza telefono mostra «numero a breve» e spinge sul form.
- **Come si lavora**: `cd site && npm run dev` → sito su `:3000`, pannello su `/keystatic`. Comandi e variabili in `site/README.md`.

Quando arrivano i dati mancanti si compilano **solo in Keystatic** (o nei YAML): niente da toccare nel codice.

## Passata aperta: design (16/09 pomeriggio)

Il sito v1 è **strutturalmente ok** e online, ma visivamente è ancora un telaio: hero con ovale-placeholder, card pulite, icone a tratto singolo, titoli in **Newsreader** (serif). Mauro: **non va**. Prossimo lavoro = rinfrescare la home, non toccare lo stack.

**Cosa deve cambiare**

1. **Ritratto grande in home.** Non un bollino a destra: una foto vera, bella, a tutta altezza (o quasi). Finché non c’è lo shooting, si progetta il *posto* della foto; non si inventa la faccia di Michele in produzione.
2. **Home più dinamica.** Più strati, più incastri, più movimento (già nel brief: ventaglio, docking, cucitura). Oggi è troppo statica e “da template chiaro”.
3. **Iconografia disegnata.** Non più solo SVG schematici. Famiglia di disegni carini (spalla, gomito, sport, artroscopia, sedi, quaderno) — stilosa, subito leggibile, una sola mano. Le foto restano per lui e per le sedi.
4. **Font: tutto moderno.** Newsreader **esce**. Niente serif da editoriale medico. Una sola sans contemporanea (titoli + UI), tracking stretto, pesi pochi. Candidati da provare in codice: Geist / Satoshi / Switzer / Cabinet Grotesk — si sceglie dopo le tavole.
5. **Colori: la base resta.** Campo, osso, petrolio, rame, menta/pesca. Si rinfresca l’uso (più contrasto, più tinta sulle lastre), non si cambia palette.

**Chiuso in implementazione (16/09 sera)**

- Hero home: **foto a tutto schermo**, niente buco/ovale osseo. File in Keystatic `home.ritratto` → `public/images/home/`. Oggi è un placeholder da sostituire con Michele.
- Font: **Geist** per tutto (titoli e UI). Newsreader e Jakarta via.
- Disegni: cartella `site/public/images/disegni/`, catalogo Keystatic singleton `disegni` (`content/disegni.yaml`). Nelle card esistenti (patologie, sedi, fiducia) c’è un riquadro più grande che ospita il disegno. Se una patologia ha `immagine`, quella vince sul catalogo.

**Due direzioni visive** (stessa palette, due tempi). Tavole in `bibbia/tavole/`:

| | C — Ritratto moderno | D — Atlante disegnato |
|---|---|---|
| File | `proposta-C-ritratto-moderno.png` | `proposta-D-atlante-disegnato.png` |
| Centro | Foto a tutta altezza, testo a sinistra, card sotto | Figura ritagliata + costellazione di schede illustrate che si incastrano |
| Disegno | Chip piccoli, secondari | Primario: le schede *sono* i disegni |
| Font | Grotesk geometrica, tutto sans | Sans un po’ più caratterizzata, comunque no serif |

Foglio segni: `proposta-iconografia-moderna.png`.  
Le tavole A/B e la fusione ossea restano come storia; **non** sono più la direzione da implementare così com’è (troppo calma, troppo serif).

**Vincoli che restano:** niente rosso da carrello, niente before/after, niente cartoon anatomico da Awwwards, niente stock medico blu. Il ritratto in produzione è quello di Michele, non un generate.

## Deploy e repo

- **Vercel**: progetto `michele-novi-sito`, team **ATSTUDIO** (`atstudio`), root directory `site`, Node 24. URL provvisorio: <https://michele-novi-sito.vercel.app>. Env già impostate (production + preview): `KEYSTATIC_STORAGE=github`, `KEYSTATIC_GITHUB_OWNER=maurotoncelli`, `KEYSTATIC_GITHUB_REPO=Michele_Novi`, `KEYSTATIC_PATH_PREFIX=site`. Da aggiungere quando ci sono: `KEYSTATIC_GITHUB_CLIENT_ID`, `KEYSTATIC_GITHUB_CLIENT_SECRET`, `KEYSTATIC_SECRET`, `RESEND_API_KEY`, `NEXT_PUBLIC_GA_ID`.
- **Git**: un solo repo alla **radice del workspace** (bibbia + fonti + site). Su GitHub: `maurotoncelli/Michele_Novi`, **privato** (contiene CV e recapiti del cliente). Vercel builda solo `site/`.
- **robots.txt**: `Disallow: /` finché `settings.dominio` è vuoto o il deploy è di anteprima. Così `*.vercel.app` non viene indicizzato. Appena c'è il dominio, si scrive in Keystatic → settings → Dominio e il sito diventa indicizzabile.
- **Dominio**: lo compra **il cliente** (intestato a lui). Poi: Vercel → progetto → Domains → aggiungere; DNS `A 76.76.21.21` (apex) + `CNAME cname.vercel-dns.com` (www); redirect 301 dal vecchio `centrosaluteonline.it` se ancora suo.
- **Keystatic in produzione**: serve una **GitHub App** (una volta sola): in locale con `KEYSTATIC_STORAGE=github` in `.env.local`, `npm run dev`, aprire `/keystatic` → il wizard crea la App e scrive le tre chiavi in `.env.local`; copiarle su Vercel. Da quel momento ogni salvataggio in `/keystatic` è un commit su `main` → deploy automatico.

## Cosa è successo

| Data | Cosa |
|------|------|
| 28/08/2026 | Primo contatto telefonico. Brief: chiarezza, SEO, vetrina, IT+EN. |
| 29–31/08 | Preventivo 1.500 € + piano tecnico. Confermato. |
| 4/09 | Prima bibbia + ricerca web. Tante sedi online, molte poi scartate. |
| ~inizio/09 | Demo HTML di prova (incastro magnetico). **Archiviata, non è il sito.** |
| 8/09 | Questionario scritto per Michele. |
| set 2026 | Incontro al **San Verano**. Chiuse sedi, perimetro clinico, prezzi, paper, P. IVA. Interrotto a metà G. |
| 16/09/2026 | Letto il **CV 2026** (docx). Canone formazione. Fellowship **Harvard / MGH Boston 2025** (Elhassan). |
| 16/09/2026 | Scelta estetica **«schede ossee»** (tavole in `bibbia/tavole/FUSIONE_osso_*.png`). Stack approvato. **Sito v1 costruito in `site/`**: tutte le pagine IT+EN, Keystatic, SEO, form. Build pulita. |
| 16/09/2026 | Repo GitHub `maurotoncelli/Michele_Novi` + Vercel `michele-novi-sito` collegati. URL provvisorio online. |
| 16/09/2026 pomeriggio | Mauro: la v1 è troppo statica e **il serif non piace**. Si riapre il design: ritratto grande, home dinamica, disegni, **tutto moderno**. Tavole C/D + foglio segni in `bibbia/tavole/`. |

## Cosa fare adesso (ordine)

**Adesso (design — questa chat)**

1. Scegliere tra **C** (ritratto grande, home più pulita) e **D** (atlante disegnato, più incastri), o una fusione (“C per l’hero, D per le fasce”).
2. Chiudere il **font**: una sans moderna per tutto. Newsreader via. Poi si cambia in `site/` (layout + `globals.css`), non si mescolano due famiglie.
3. Progettare il sistema di **disegni** (stessa mano delle tavole) e il posto del **ritratto a tutta altezza**. In produzione la foto è quella di Michele: va chiesta / shooting.

**In parallelo (dati, non bloccano il design)**

4. Far **ricontrollare il cellulare** (348 4332733 detto vs 348 4331733 online). Poi `settings.telefono` / `whatsapp`.
5. Ritirare: Drive dei paper, screenshot recensioni, URL delle 4 schede Google.
6. Dominio (lo compra il cliente) → `settings.dominio`. Orari segreteria → `settings.orari`.
7. Repo GitHub: **passare a privato** (è ancora public, contiene CV e PEC). Poi GitHub App di Keystatic.
8. Far validare a Michele le bozze in `site/content/patologie/*`. Nome sezione chiuso: **Approfondimenti** (EN *In depth*).

Il codice è pronto ma i campi vuoti restano vuoti finché non arrivano i dati veri. Non inventare telefono, orari o indirizzi «tanto poi si cambia»: finisce pubblicato.

## Vincoli che non si riaprono

Elenco pieno: [DECISIONI.md](DECISIONI.md). I quattro che evitano errori:

1. **Multipagina**, non one-page. «Landing» = semplice, non un’unica scrollata.
2. **Quattro sedi**, stop. CESAT, San Rossore, San Verano (solo visite), Villa Donatello (solo chirurgia).
3. Stack: Next.js + Tailwind + TypeScript + Keystatic + Vercel + i18n `/it` `/en`. Come maurotoncelli.it, **non** come successioniarmellin.
4. Form: nome + recapito + consenso. **Mai** dati clinici. Prezzi **non** online.

## Cosa non fare

- Non copiare `_archivio/demo-sito-2026-09/`.
- Non inventare sedi. Fisiomed, Kinetic, Athletica, MiniHospital, Santa Croce, San Paolo, You, Studi San Pietro **non** vanno sul sito MN.
- Non nominare Nicoletti (chiesto no).
- Non ostentare che San Verano è suo.
- Non pubblicare Alonso senza consenso.
- Non fondere quattro indirizzi in una scheda Google.
- Non committare `.env`, token, password.

## Chi è

- **Dott. Michele Novi**, nato 27/10/1987. Albo Pisa n. 5749.
- Dirigente medico, **SOC Ortopedia Protesica**, San Pietro Igneo / CESAT, Fucecchio, dal 2021. Fellowship 2025 a **Harvard / MGH** (Elhassan). Focus spalla e arto superiore; anche sport, artroscopia, protesi; anca/ginocchio in ospedale.
- Segreteria. Studio pieno: il sito **allinea**, non “riempie l’agenda”.
- Introdotto da Lorenzo Querci. Ha visto il sito di Mauro: troppo complicato.

Contatti di lavoro (non pubblicare alla cieca): vedi [03_sedi_e_contatti.md](03_sedi_e_contatti.md).

## Prompt minimo per una chat nuova

```
Leggi bibbia/HANDOFF.md e bibbia/DECISIONI.md, poi site/README.md.
Workspace: Michele_Novi_Website. Il sito è in site/ (Next.js + Keystatic).
Non usare _archivio/demo-sito-2026-09.
Testi e dati stanno in site/content e site/src/i18n/messages: niente hardcoded nelle pagine.
Compito: …
```
