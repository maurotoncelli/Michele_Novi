# 11. Design e UX

> Parte della Bibbia. Indice: [00_README_Master_Index.md](00_README_Master_Index.md).

## Metadati
- ID: CAP-11
- Stato: Bozza
- Ultimo aggiornamento: 2026-09-04 (@16)
- Dipendenze: @03_Brand, @04_IA, @05_Stack, @16_Visivo
- Owner: Mauro

## Sintesi
Sito da designer, non da template medico. Deve �spaccare� restando fruibile su telefono (la segreteria e i pazienti over 50 ci devono capire). I colori e i font si chiudono dopo lo shooting: prima si definiscono principi e gerarchia.

## Stato attuale del progetto

Concetti approfonditi: [@16](16_Fondamenta_Visive.md). Questo capitolo è la traduzione in UI. Home = polo **varco**.




### Dai concetti ai componenti (traduzione UI)

Testo pieno dei concetti: [@16](16_Fondamenta_Visive.md). Qui solo come diventano schermo.

**Varco (home).** Un hero, non un cruscotto: nome, una frase, una foto-finestra (ingresso o mezzo busto), CTA chiama. Sotto, poche card. Se la home ha più di un “centro visivo”, il varco è chiuso.

**Congruenza (sedi, patologie, header/footer).** Stesso stampo di scheda; stesso header ovunque; titolo e foto sulla stessa colonna. Due font, pochi pesi. Il NAP nel footer è identico a quello in Contatti.

**Osso (tutto il sito).** H1/H2 veri, margini costanti, niente ombre da template. Una pagina deve reggere in bianco e nero. Accessibilità = struttura, non un badge.

**Luce.** Campo neutro; un `--accent` dalle foto; niente overlay sul ritratto. CTA nello stesso colore accento, non in rosso urgenza.

**Due tempi.** Stesso linguaggio fotografico per Peccioli e Fucecchio. CESAT è una riga in home, non una copertina da congresso.

**Quaderno (`/articoli/[slug]`).** Titolo, lead, corpo, DOI, CTA. Indice tipografico. Non entra in home come “magazine”. Voce menu assente se zero pezzi.

**Gesto.** Motion: fade/slide corti. Ritratto a mezzo busto. Niente icone sport.

**Costellazione.** Hub sedi + pin veri. Niente mosaico di loghi clinica.

**Irreparabile.** Vietati before/after e claim visivi di guarigione. CTA calmo.

### Principi
1. **Albero informativo visibile**: hero = una idea; sotto = card; dentro = profondit�.
2. **CTA sempre l�**: chiama / WhatsApp / scrivi. Non un hamburger di 12 voci.
3. **Foto vere**, crop editoriali, molto bianco (o molto scuro) ma non �blu ospedale + stock sorriso�.
4. **Tipografia** con carattere: una famiglia per titoli, una per testo. Pochi pesi. Accenti di colore dalla palette dello shooting (camice, sala, paesaggio toscano � da vedere, non da stereotipo).
5. **Motion** sobria. Niente cursori custom pesanti (lezione Fattoria di Monti).
6. **Accessibilit�**: contrasto, focus, tap 44px, testo non nel jpeg, WCAG 2.2 AA come obiettivo.
7. **Sedi**: ogni scheda pu� avere logo struttura, foto ingresso, nota accessibilit�, mappa. Richiesta CRM.

### Layout
- Mobile first. Header compatto + CTA telefono in icona.
- Desktop: nav orizzontale, CTA pillola.
- Recensioni: modulo tipografico, non slider infinito nervoso.
- Blog: pagina articolo da rivista (titolo grande, lead, ritratto autore piccolo).

### Cosa non copiare
- Checcucci: SEO forte, UI datata, chatta-con-noi, muro di patologie.
- Nicoletti: struttura keyword citt�+articolazione utile; trustindex e look generico da evitare.
- maurotoncelli.it: troppo complesso per questo cliente (hero slider moda, iris, dark mode non necessari). Si copiano **disciplina e pulizia**, non l�estetica fashion.
- Armellin: prodotto fintech-burocrazia, altro mondo.

### Token (da compilare post-moodboard)

| Token | v1 placeholder | Definitivo |
|-------|----------------|------------|
| `--bg` | da definire | dopo foto |
| `--fg` | da definire | |
| `--accent` | da definire | un colore, non cinque |
| Font titoli | self-hosted, da scegliere | |
| Font corpo | idem | |

Non inventare una corporate identity nel codice prima delle foto.

### UX contatto
- Click-to-call con `tel:`
- WhatsApp con testo precompilato non clinico (�Vorrei informazioni per una visita�)
- Form corto (@05)
- Scelta sede nel form se le sedi sono >2
- Orari segreteria visibili

### Stati vuoti
Blog senza articoli: non mostrare un indice vuoto. O c�� il primo pezzo al go-live, o la voce menu aspetta.

## Idee future
- Video looping muto in hero (dal pacchetto video).
- Micro-interazione mappa sedi.

## Nodi da sciogliere
D9 logo e shooting. Moodboard solo con scatti veri o con un set di riferimento approvato.

## Passi successivi
Quando si passa al codice: 1 homepage desktop + 1 mobile in browser prima di tutte le altre pagine.

## Decisioni congelate (lock-in)
- Design custom, no theme Themeforest / no Elementor.
- Niente stock.
- CTA contatto persistente.
- Home = polo varco; articoli = quaderno; sedi/patologie = congruenza (@16).
- Accessibilit� non � un extra.

## Rischi / Compliance & Riferimenti
- Overdesign che a Michele sembra �complicato come il tuo sito�: tenere la home pi� semplice del portfolio Mauro.
- Design dei blocchi home e pagine: @04 scheletro; questo capitolo resta principi visivi e UX.
