# 14. Offerta, roadmap e fasi

> Parte della Bibbia. Indice: [00_README_Master_Index.md](00_README_Master_Index.md).

## Metadati
- ID: CAP-14
- Stato: Bozza
- Ultimo aggiornamento: 2026-09-04
- Dipendenze: @01_Visione, @05_Stack, @02_Cliente
- Owner: Mauro

## Sintesi
Cosa è incluso nei **1.500 €**, cosa è a parte, in che ordine si lavora. Fonte: job CRM 64 (conferma 31/08, validità 31/10) e allegato tecnico al preventivo del 29/08 (`parte2`).

### Due PDF del 29/08
Il CRM genera il preventivo commerciale (QuoteGenerator, **parte 1**: `2026.08.29_Preventivo_Michele_Novi_JOB_0064.pdf` — non presente in Downloads in questa sessione) e un **allegato tecnico** esportato come `…JOB__0064_parte2.pdf`. Il parte2 è il Piano tecnico a 3 pagine (stack, pagine, GDPR, fasi, gestionale futuro). Copie in `documenti/fonti/`.

## Stato attuale del progetto

### Incluso (offerta base)

- Sito custom, ~pagine in @04, mobile
- Shooting professionale in studio (ritratti + ambienti)
- Blog Keystatic (articoli in autonomia, no canone)
- Contatto: form, tel, WhatsApp, mappe sedi
- SEO locale, JSON-LD, collegamento GBP dove possibile, GA4, GSC
- Dominio intestato a lui, go-live, formazione blog

Prezzo: **1.500 �** lancio, fuori listino. Voce unica in CRM (`quote_items`: �Sito web� 1500).

### A parte (gestione continuativa)
Dominio rinnovo, email `info@`, hosting/presenza, manutenzione. Da quotare in accordo annuale se lo vuole.

### Espansione futura (non v1)
Gestionale su misura �stessa famiglia� del CRM Mauro, da 1.500 � in su:

- clienti / cartelle
- appuntamenti
- pagamenti
- preventivi

Video nel sito: in call Mauro ha proposto un pacchetto vantaggioso sito+foto+video. Il PDF elenca lo shooting; il video extra va chiarito se � gi� dentro i 1500 o � upsell. **Nodo commerciale da chiudere con Mauro.**

### Fasi (dal PDF)

| Fase | Attivit� | Durata indicativa |
|------|----------|-------------------|
| 1 Avvio | Materiali, sedi, patologie, recensioni | settimana 1 |
| 2 Design e sviluppo | Sito, pagine trattamento, blog | settimane 1�2 |
| 3 Shooting | Mezza giornata in parallelo | mezza giornata |
| 4 Revisione e go-live | Dominio, analytics, formazione | settimane 3�4 |

I tempi **partono dai materiali**. Oggi (4/09) i materiali non ci sono ancora: la Fase 1 � questa Bibbia + call di chiusura domande.

Stato CRM: `planned`, `start_date` 2026-08-31, `smartworking` s�, `paid` 0.

### Roadmap contenuto (parallela, non codice)

1. Congelare NAP e sedi
2. Registrare dominio
3. Scaffold `site/`
4. Shooting
5. Copy IT (+ EN in scia)
6. Recensioni in CMS
7. Primo articolo
8. Go-live + allineamento terzi (@07)

### Propriet�
Codice e contenuti al cliente a saldo. File nel repo, non un DB proprietario. Passaggio di consegne = git + Vercel account + DNS.

## Idee future
Manutenzione annuale light (ore) vs forfait. Da non spingere ora: prima il sito deve esistere.

## Nodi da sciogliere
- Video incluso o extra?
- Acconto / saldo (non in CRM `paid`).
- Chi registra il dominio (Mauro per lui vs lui diretto).

## Passi successivi
Dopo validazione Bibbia: call Michele con [DOMANDE_APERTE.md](DOMANDE_APERTE.md), poi scaffold.

## Decisioni congelate (lock-in)
- v1 nei 1500: vetrina + blog + shooting + SEO base. Niente agenda.
- Gestionale = progetto nuovo.

## Rischi / Compliance & Riferimenti
- Scope creep �gi� che ci sei metti il calendario�: rimandare al modulo futuro.
- PDF: `documenti/fonti/Piano_Tecnico_Sito_Michele_Novi_2026.pdf`
