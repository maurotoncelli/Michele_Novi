# 09. Recensioni

> Parte della Bibbia. Indice: [00_README_Master_Index.md](00_README_Master_Index.md).

## Metadati
- ID: CAP-09
- Stato: Bozza
- Ultimo aggiornamento: 2026-09-04
- Dipendenze: @03_Brand, @07_Presenza, @13_Privacy
- Owner: Mauro

## Sintesi
Michele ha recensioni **sparse** (MioDottore, altre piattaforme, screenshot sul telefono), non concentrate sui GBP. Idea condivisa in call: raccoglierle e reimpaginarle nello stile del sito. In v1 sono **contenuti curati nel CMS**, non un widget live.

## Stato attuale del progetto

### Cosa abbiamo trovato online (4/09)
- Doctolib: fetch senza recensioni visibili.
- MioDottore Capannoli: Michele **non** compare tra gli ortopedici suggeriti del MiniHospital; esiste almeno una **risposta** sua a una domanda paziente, firmata Capannoli.
- TrovaOrtopedico: form recensioni vuoto, listing non reclamato.
- GBP: non ispezionabili da qui; Michele dice che le recensioni **non** stanno lì.

Quindi il materiale vero è quasi certamente negli screenshot e negli account che solo lui vede.

### Come le mettiamo sul sito
- Componente recensioni: citazione, nome (o iniziali), sede/piattaforma di origine, eventuale data.
- Design curato (non stelline gialle da plugin).
- Sorgente Keystatic: facile aggiungerne altre.
- Attribuzione: «Recensione su MioDottore» / «Paziente, Fucecchio».
- Filtro: niente testo che espone patologie identificative di terzi.

### Cosa non fare
- Inventare recensioni.
- Importare in automatico da Google senza API e senza controllo.
- Schema `AggregateRating` gonfiato.
- In v1: form pubblico «lascia una recensione» (moderazione + GDPR + recensioni sanitarie delicate). Semmai un CTA «Lascia un feedback su Google» puntato alla scheda giusta, quando esisterà.

### Raccolta
1. Export / screenshot da Michele.
2. Trascrizione in un foglio (originale + versione editata per lunghezza).
3. Consenso se il nome è per esteso.
4. Selezione 6–12 pezzi forti, mix di sedi e di tipi di visita (prima visita / post-op / sportivo).
5. Stesso ritratto/stile grafico del sito.

Nicoletti usa Trustindex su Google: funziona per la SEO ma è esteticamente povero. Noi: curate, poche, belle. Poi, se i GBP si popolano, si potrà aggiungere il badge.

## Idee future
- Dopo shooting: video-testimonianze (Checcucci lo fa). Consenso firmato.
- Campagna gentile post-visita via segreteria: link alla scheda Google della **sede in cui sono stati**, non a una pagina generica.

## Nodi da sciogliere
D6. Dove sono i file screenshot? Quanti pezzi usabili?

## Passi successivi
Cartella `documenti/recensioni/` (da creare quando arrivano i file) con originali e testi approvati.

## Decisioni congelate (lock-in)
- Recensioni vere, curate a mano in v1.
- Niente widget a pagamento obbligatorio.
- Niente dati clinici identificativi nelle citazioni.

## Rischi / Compliance & Riferimenti
- Recensioni sanitarie: non alterare il senso. Tagli di lunghezza ok, stravolgimenti no.
- Linee guida Google: non incentivare recensioni con sconti.
- @13 GDPR: base giuridica (legittimo interesse / consenso) per pubblicare nomi.
