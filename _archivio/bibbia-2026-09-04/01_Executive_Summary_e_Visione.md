# 01. Executive Summary e Visione

> Parte della Bibbia. Indice: [00_README_Master_Index.md](00_README_Master_Index.md).

## Metadati
- ID: CAP-01
- Stato: Bozza
- Ultimo aggiornamento: 2026-09-04
- Dipendenze: @02_Cliente, @04_IA, @06_SEO, @14_Roadmap
- Owner: Mauro

## Sintesi
Costruire il **sito ufficiale** del Dott. Michele Novi come punto unico, chiaro e veloce: chi ù, cosa cura, dove riceve, come contattarlo. Oggi i pazienti lo trovano su troppe schede diverse, spesso vecchie. Il sito deve riordinare quella presenza e restare abbastanza semplice da piacergli (ùlanding pageù) e abbastanza strutturato da crescere (blog, SEO, un giorno agenda).

## Stato attuale del progetto

### Problema
Michele ha lo studio pieno e fa lavoro clinico di livello (CESAT, fellowship internazionali, ricerca, screening di territorio). Online, perù, chi cerca ùdove sta il dottor Noviù o ùdi cosa si occupaù si perde tra Doctolib, MiniHospital, directory, LinkedIn non aggiornato, schede inesatte (Localshop24) e profili di strutture in cui magari non visita più.

Sta giù riducendo la presenza su terzi. Senza un hub proprio, togliere schede **aumenta** il vuoto informativo.

### Promessa del sito
In pochi secondi: *chirurgo ortopedico, arto superiore / traumatologia sportiva, riceve in Toscana (elenco vero), chiama o scrivi alla segreteria.*

Poi, scendendo: percorso formativo, patologie, sedi con mappa e GBP, recensioni vere, articoli. Albero delle pagine (blocchi, cosa c'Ë / cosa manca): [@04](04_Architettura_Informazione.md).

### Posizionamento
Non ùortopedico generico vicino a meù in stile directory.  
Sù: **specialista riconoscibile** (spalla e arto superiore) con radicamento Valdera / Empolese / Pisa, credibilitù ospedaliera (CESAT) e tono umano (disponibilitù, chiarezza).

Dettaglio del perimetro clinico da chiudere con lui (@DOMANDE D5).

### Successo misurabile (v1)
- Un dominio nuovo online, IT+EN, Core Web Vitals verdi.
- NAP coerente su sito + (dove possibile) GBP e directory residue.
- Ogni sede attiva ha una pagina o sezione con mappa, telefono, come arrivare, link alla scheda Google della **struttura** se non ù sua.
- Blog pronto, primo articolo pubblicato dal medico.
- Form / click-to-call / WhatsApp funzionanti, senza dati sanitari.
- Search Console e GA4 consegnati.

### Cosa non ù questo progetto
Non ù un clone di successioniarmellin.it. Non ù un portale di prenotazione. Non ù WordPress. Non ù una campagna Ads (non richiesta).

## Idee future
- Agenda e videochiamata (interesse espresso al telefono).
- Canale YouTube + riuso reel ? articoli.
- Gestionale studio (anagrafica, cartelle, preventivi, pagamenti): offerta a parte, stessa famiglia tecnica del CRM Mauro.
- Unificazione progressiva delle schede Google e chiusura directory spazzatura.

## Nodi da sciogliere
Vedi [DOMANDE_APERTE.md](DOMANDE_APERTE.md) D1ùD4.

## Passi successivi
1. Validare questa visione con Mauro.
2. Call di allineamento sedi/dominio con Michele.
3. Scaffold solo dopo D1ùD3.

## Decisioni congelate (lock-in)
- Sito = fonte di veritù della presenza online.
- v1 = vetrina + blog + contatto. Niente booking.
- Multipagina espandibile, non one-page.

## Rischi / Compliance & Riferimenti
- Rischio principale: pubblicare sedi o prezzi sbagliati e **peggiorare** la confusione.
- Rischio YMYL: copy sanitario superficiale ? fiducia e ranking.
- Piano tecnico: `documenti/fonti/Piano_Tecnico_Sito_Michele_Novi_2026.pdf`
- Brief: @02
