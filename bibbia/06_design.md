# 06. Design

Due strati. Sopra: quello che Mauro vuole far vedere (16/09). Sotto: filtri per non fare un sito che *sembra* complicato come maurotoncelli.it, o un cartoon anatomico.

Token (hex, font) **dopo** lo shooting e dopo aver visto palette SV — che **non** si copia in MN.

---

## Brief visivo (Mauro, 16/09)

Moderno, fruibile, distinto. Approccio da designer. Informazioni ad albero: in superficie sintesi e navigabilità; sotto, termini specifici e coda lunga che centrano lui.

Comunicare: professionalità, disponibilità, affidabilità, chiarezza, sintesi proattiva.

Estetica che tiene: base **molto chiara, non giallognola**; gradient muted; font invitanti; colori accent; spazi che regolano sezioni ed elementi.

Il sito è il punto di riferimento delle informazioni sul web, e **invita al contatto**.

### Motion

Deve essere unico soprattutto per le **animazioni fluide**:

- parallassi
- apparizioni graduali
- attrazione magnetica usata bene, come **incastri / alloggi** (giunti, non cursori-gioco)
- strati che scorrendo si sovrappongono e si aprono — come parti del corpo, articolazioni
- card vive

Quasi tutti gli elementi possono essere animati, come un corpo. **Non** esagerare il campo magnetico. **Non** cursori che rallentano o peggiorano l’uso.

Va bene glass morphism e bordi che si illuminano, se restano in linea.

### Segni

Catalogo di **icone / disegni / segni** in una sola famiglia, piacevoli, utili due volte: schematici e stilosi. Una parola come *artroscopia* deve capirsi subito con un disegno a lato.

Immagini vere per sedi e (dove ha senso) parti del corpo. Larga scala di interagibilità, senza ostacolare.

### Sedi e recensioni

Ogni studio: possibilità di logo/icona, amenity, foto, mappa.  
Recensioni raccolte e messe in bello stile; in CMS si possono aggiungerne. In v1 non c’è un form pubblico «lascia una recensione».

### Chi sono

Blocchi ritmati, zone espandibili. Si vede l’essenziale; chi è curioso apre formazione e paper.

---

## Filtri (per non tradire il brief «semplice»)

Presi dalla prima fondazione visiva del 4/09, ancora utili come *prova*, non come veto sulle icone.

1. **Varco.** In tre secondi so chi è e che numero chiamare? Se la home ha due centri visivi, è già un cruscotto.
2. **Congruenza.** Due schede sede devono sembrare la stessa famiglia. NAP identico è già un gesto visivo.
3. **Osso.** In bianco e nero la pagina resta ordinata. H1/H2 veri, margini costanti.
4. **Calma.** Lo studio è pieno: niente rosso da carrello, niente “PRENOTA ORA”.
5. **Due tempi.** Paese (Peccioli) e sala (CESAT / San Rossore) nello stesso occhio, non due brand.
6. **Irreparabile ≠ magia.** Niente before/after, niente osso che si salda, niente claim di guarigione.

La metafora articolare **si può vedere** (incastri, strati, icone). Non si illustra un artroscopio come logo e non si fa un simulatore clinico da Awwwards: quello era il demo, ed è in archivio.

## Cosa non copiare

- Il demo in `_archivio/demo-sito-2026-09/` (magnetismo estremo, simulatori di cuffia, cockpit return-to-play).
- Checcucci: SEO forte, UI datata.
- Nicoletti: URL città+articolazione utili come lezione, Trustindex e look generico no.
- maurotoncelli.it: disciplina sì, hero moda / iris / dark no.
- Template medico blu + stock.

## UX

- Mobile first. Tap 44px, contrasto, testo non nel jpeg. Obiettivo WCAG 2.2 AA.
- CTA telefono sempre raggiungibile.
- Recensioni: modulo tipografico, non slider nervoso.
- Articolo scientifico: impaginato da paper (titolo, autori, rivista, DOI, abstract/riassunto, link fonte).
- Nota «Dal lavoro»: titolo, lead, corpo, disclaimer, CTA.
- Stati vuoti: fascia recensioni assente se non ci sono pezzi; il menu Articoli c’è perché i paper ci sono.

## Token (vuoti di proposito)

| Token | Quando |
|-------|--------|
| `--bg` | dopo foto; partenza: chiaro freddo, non crema |
| `--fg` | dopo foto |
| `--accent` | uno, dalle foto o da un segno MN — non la palette SV |
| Font titoli / corpo | self-hosted, pochi pesi, invitanti |

## Shooting (incluso)

Ritratto, studio, **foto di tutte e 4 le sedi** (lui: «da capire, foto di tutte»). Ingresso, come si arriva, parcheggio, scalini.  
Video: proposto in call come extra vantaggioso nel pacchetto; non è scritto chiaro nei 1.500 € — da chiudere in [10_offerta.md](10_offerta.md).
