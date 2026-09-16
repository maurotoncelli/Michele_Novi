# 05. Architettura del sito MN

Multipagina. Home da landing. Sezioni che si potranno approfondire senza rifare tutto.  
Niente di questo è copy definitivo.

---

## Perché non una pagina sola

Lui ha detto «landing page». Tre motivi per non fare un one-page:

1. Vuole potenziare (agenda, YouTube, paper): le ancore diventano un cimitero.
2. SEO locale e paper vogliono URL propri.
3. L’inglese ha bisogno di title e slug suoi.

La home può *sembrare* una landing: hero, pochi blocchi, CTA fisso.

Albero **rovesciato**: cosa / dove / contatto in superficie; CV, patologie, paper sotto, a richiesta.

---

## Chrome (tutte le pagine)

**Header.** Wordmark Dott. Michele Novi. Sottotitolo corto: *Ortopedico — spalla e arto superiore*. Menu: Chi sono · Cosa curo · Dove · Articoli · Contatti. IT | EN. CTA: **Chiama** + **Scrivi**. WhatsApp quando il numero è chiuso.

**Footer.** Nome, una riga di specialità, telefono, orari (quando ci sono), email `info@`. Le quattro sedi come città + link. Instagram, LinkedIn. Privacy, cookie, P. IVA. Niente Doctolib come canale principale. Niente CUP.

**Sempre.** Disclaimer corto su patologie e articoli. Nessun form clinico.

---

## Rotte v1

Stesso albero sotto `/en/...`. Default `/it`.

| Rotta IT | Pagina | Menu |
|----------|--------|------|
| `/it` | Home | logo |
| `/it/chi-sono` | Chi sono | sì |
| `/it/cosa-curo` | Hub | sì |
| `/it/cosa-curo/spalla` | Spalla (pagina pilastro) | no |
| `/it/cosa-curo/arto-superiore` | Gomito e mano | no |
| `/it/cosa-curo/traumatologia-sportiva` | Sport | no |
| `/it/cosa-curo/come-si-opera` | Metodo (artroscopia) | no |
| `/it/cosa-curo/anca-e-ginocchio` | Secondaria, onesta | no |
| `/it/dove` | Hub sedi | sì |
| `/it/dove/fucecchio-cesat` | CESAT | no |
| `/it/dove/pisa-san-rossore` | San Rossore | no |
| `/it/dove/peccioli-san-verano` | San Verano | no |
| `/it/dove/villa-donatello` | Villa Donatello | no |
| `/it/contatti` | Contatti | sì |
| `/it/articoli` | Hub pubblicazioni + dal lavoro | sì |
| `/it/articoli/pubblicazioni/[slug]` | Paper | no |
| `/it/articoli/[slug]` | Nota / placeholder | no |
| `/it/privacy`, `/it/cookie` | Legale | footer |

**Non in v1:** `/prenota`, pagina Nicoletti, pagina equipe, URL per le sedi morte, pagina eco come “servizio a catalogo”, `/pubblicazioni` staccata (stanno sotto Articoli).

Ecografia: un paragrafo in Chi sono / Cosa curo / scheda sede se c’è la macchina. **Non** una sesta specialità da prenotare.

---

## Scheletro, pagina per pagina

### Home

Scopo: in tre secondi chi è, cosa cura, dove, che numero. Non il CV.

1. Hero. Ritratto (placeholder). Frase spalla / arto superiore. CTA segreteria. Secondario: Dove.
2. Cosa curo. Card: Spalla (grande), Arto superiore, Sport, Come si opera. Anca/ginocchio come riga, non come ero.
3. Dove. Quattro posti, etichetta visita / chirurgia. San Verano = visite. Villa Donatello = solo intervento.
4. Perché fidarsi. CESAT, Pisa, Harvard/MGH 2025, Berlino, Seattle. Link a Chi sono. Niente Nicoletti.
5. Recensioni. 2–3 *se* ci sono i file. Altrimenti il blocco **non esiste**.
6. Articoli. Ultimi paper o la nota placeholder. Se vuoto, niente fascia.
7. Chiusura contatto. Telefono, WhatsApp, form. Non «prenota su Doctolib».

Non mettere: listino, Lungarno, Alonso, tutte le vecchie location.

### Chi sono

Punti fondamentali subito. Poi blocchi che si aprono.

1. Apertura: titolo del CV 2026 (spalla, gomito, arto superiore), Toscana, dirigente medico SOC Ortopedia Protesica / CESAT.
2. In evidenza, non nascosto: **Harvard / MGH 2025, Elhassan, transfer muscolari**. Poi le altre fellowship a blocchi (Berlino, Seattle, Londra, Cattolica).
3. Formazione Pisa (108, 110 e lode) + timeline Modena, date confermate.
4. Pubblicazioni: lista «principali» del CV, click → riassunto + DOI. Poi tutte quelle del Drive.
5. Docenza (Stryker ICLO 2023–25, Master, SIUMB): espandibile.
6. Come valuta: la prima visita può cambiare la strada (curare vs protesi).
7. Territorio / didattica solo ciò che vuole (screening Peccioli). Niente “il mio centro”.
8. CTA verso Dove / Contatti.

Curriculum **ritmato a blocchi**, dal CV 2026, non dal PDF 2019.

### Cosa curo

Mappa mentale. Intro: specialista arto superiore; anche sport; in ospedale anche anca e ginocchio; eco solo in sede di visita.

Griglia. Poi link al metodo.

Chiusura: la prima visita decide il percorso.

### Spalla

Pagina più importante dopo home e dove. H2 veri: cuffia, instabilità, protesi, fratture, conservativo vs chirurgico, esercizi (o link a un articolo), FAQ. Niente prezzi, niente nomi pazienti.

### Arto superiore

Gomito e mano insieme, più corto della spalla. Microchirurgia: una frase onesta, non un hero.

### Traumatologia sportiva

Ritorno allo sport, instabilità, overuse. Si può dire medicina dello sport di alto livello **senza** Alonso.

### Come si opera

Cos’è l’artroscopia, per cosa la usa, recupero tipo, differenza con l’aperto. Rimanda a spalla / arto. Non duplicare l’elenco malattie. Icona/disegno a lato della parola difficile.

### Anca e ginocchio

Onesta, secondaria. Prenotazione diversa se è ospedale (segreteria MN per il privato; non mischiare CUP). Testi da ripescare da centrosaluteonline, riscritti e firmati da lui.

### Dove + quattro schede

Hub: due gruppi (visito / opero), mappa a quattro pin veri, nota accessibilità.

Ogni scheda: ruolo, indirizzo, mappa, foto, come arrivare, «chiama la segreteria», link Google della struttura, cosa si fa qui vs altrove. Amenity e logo struttura se arrivano.

### Contatti

Un numero. Form: nome, recapito, sede preferita (le 4), consenso, messaggio **non clinico**. WhatsApp neutro. **Nessun prezzo.** «Il costo lo comunica la segreteria.»

### Articoli

Vedi [08_contenuti.md](08_contenuti.md). Hub con due binari. Menu visibile: i paper ci sono.

---

## Interlink

```
Home → card patologie, 4 sedi, chi sono, contatti
Chi sono → sedi, spalla, 1 paper
Spalla → metodo, sport, sedi, esercizi/articolo
Ogni sede → 1–2 patologie tipiche, contatti
Paper → patologia + chi sono
```

Niente URL `città+articolazione` in v1 (lezione Nicoletti: thin content). Si ottiene con i link interni.

## Keystatic (dati, non codice)

Collezioni: `sedi` (4), `patologie`, `pubblicazioni`, `note`, `recensioni`.  
Singleton: hero, telefono, orari, social, flag recensioni.

Finché il telefono non è ricontrollato, i singleton restano vuoti. Non si scaffolda col 348 «tanto poi si cambia».
