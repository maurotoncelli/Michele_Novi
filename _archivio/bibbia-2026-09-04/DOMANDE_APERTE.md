# Domande aperte

> Nodi che bloccano copy, NAP, JSON-LD e go-live. Aggiornare qui le risposte, poi spostare le decisioni in [DECISIONI.md](DECISIONI.md).
> Aggiornato: **2026-09-04**
> Scheletro pagine: [@04](04_Architettura_Informazione.md). Quadro siti: `ricerca/2026-09-04_quadro-dottor-novi.md`.
>
> **Foglio da usare in chiamata (domande complete):** [`../documenti/appunti/2026-09-04_call-prossima-domande.md`](../documenti/appunti/2026-09-04_call-prossima-domande.md) (interno Mauro). **Da mandare a Michele:** [`../documenti/appunti/2026-09-08_questionario-michele-novi.pdf`](../documenti/appunti/2026-09-08_questionario-michele-novi.pdf). La checklist sotto � il riassunto; in call si usa il foglio.

---

## Checklist call Michele (da stampare)

Tutto ci� che segue � **gi� visibile online**. Non � copy: � da spuntare s� / no / correggi. Finch� non torna, non si mettono telefono, prezzi e sedi nel codice.

### Recapiti
- [ ] Il numero pubblico del sito � **348 4331733** (Instagram, Doctolib, LinkedIn)?
- [ ] Il **329 7382673** resta personale, mai in footer?
- [ ] WhatsApp � lo stesso 348?
- [ ] Orari segreteria: lun�gio **15:30�17:30**, o mercoled� Doctolib **16�18**, o un'altra fascia unica?
- [ ] Fuori orario: richiamo / Doctolib / niente?
- [ ] Email sul sito: gmail, oppure `info@` sul dominio nuovo (chi la legge)?

### Dove lavora (visite vs chirurgia)
Per ogni riga: ancora attiva? visita / infiltrazione / eco / solo chirurgia? telefono di quella sede? orari suoi?

- [ ] CESAT � Ospedale San Pietro Igneo, Piazza Lavagnini **5**, Fucecchio (pubblico; CUP, non segreteria)
- [ ] Studi Medici San Pietro, Piazza Lavagnini **6**, Fucecchio (Doctolib)
- [ ] Centro Medico San Verano, Peccioli � civico: **Viale Cavour 13** o Piazza del Carmine 6?
- [ ] Fisiomed, Via Tosco Romagnola Ovest 210, Fornacette
- [ ] Kinetic Center, Via Impastato 3, Pisa
- [ ] Athletica Cetilar, Via delle Lenze 216/B, Pisa
- [ ] MiniHospital Capannoli, Via Gramsci 29
- [ ] Santa Croce Medical Center, Piazza F.lli Cervi 11
- [ ] Casa di Cura San Paolo, Pistoia
- [ ] Villa Donatello (online: solo ricovero)
- [ ] Studi Medici You (Facebook 2021): morto?

### Prezzi (Doctolib, da non pubblicare senza s�)
- [ ] Prima visita **120 �** � ok sul sito?
- [ ] Controllo **80�90 �** � quale dei due?
- [ ] Infiltrazione acido ialuronico **80�150 �** � range o cifra unica?
- [ ] Stessi prezzi in tutte le sedi private?
- [ ] Interventi / ricoveri: **mai** in listino sul sito (proposta: s�, mai)?
- [ ] Pagamenti: contanti, assegno, carta, bonifico � ancora veri?
- [ ] Convenzioni assicurative da elencare?

### Collega e ospedale
- [ ] Qualifica **esatta** al CESAT (dirigente medico SOC�)?
- [ ] **Simone Nicoletti**: si cita? Come (direttore SOC, collega, co-autore, Shoulder School)?
- [ ] Non scriviamo �direttore SOC� su Michele � confermato?
- [ ] Shoulder School Fucecchio e screening Peccioli: raccontabili in Chi sono / blog?

### Canali
- [ ] Doctolib resta il bottone �prenota� accanto al telefono?
- [ ] Quali recensioni si possono reimpaginare (screenshot)?
- [ ] URL dei colleghi (D12)?
- [ ] Post LinkedIn: quali sono suoi vs repost? Screenshot o export dei piu lunghi.

### Dominio e periplo clinico
- [ ] Nome dominio nuovo; vecchio dominio (se esiste) ancora suo?
- [ ] Hero = **solo** spalla e arto superiore, oppure anche protesi anca/ginocchio in superficie?
- [ ] Pagina propria anca/ginocchio s�/no?

Dettaglio per nodo: sezioni sotto.

---

## Bloccanti (prima dello scaffold serio)

### D1 � Dominio e nome
Michele vuole **cambiare nome** e non usare il vecchio dominio.
- Qual � il vecchio dominio, se esiste? (in rete **non** risulta un sito personale tipo `michelenovi.it`; c'� il sottodominio `michelenovi.centrosaluteonline.it`.)
- Lo possiede ancora? Se s�: si tiene acceso per 12+ mesi con 301 verso il nuovo.
- Quali nomi dominio candidati? (es. `michelenovi.it`, `dottornovi.it`, `novispalla.it` � da non registrare senza di lui.)
- Casella `info@` sul dominio: s�/no, chi la legge (segreteria)?

### D2 � Elenco sedi **attive oggi**
Online coesistono troppe location, alcune probabilmente vecchie. Tabella da far compilare:

| Sede | Citt� | Indirizzo | Tel prenotazione | Orari | Visita / chirurgia | Ancora attiva? | GBP esiste? | Di chi � la scheda? |
|------|-------|-----------|------------------|-------|--------------------|----------------|-------------|--------|

Civici estratti: `ricerca/2026-09-04_quadro-dottor-novi.md` �3 e checklist sopra.

Senza questa tabella il sito moltiplica la stessa confusione che Michele vuole togliere. Lo scheletro `@04` prevede un hub `/sedi` + una pagina per sede attiva; le altre non si creano.

### D3 � Telefono pubblico unico
Due numeri personali/studio:

- `329 7382673` (CV + CRM � probabilmente personale)
- `348 4331733` (Instagram bio, Doctolib JSON-LD, LinkedIn � **candidato pubblico**)

Pi� i numeri delle strutture (MiniHospital, Santa Croce, You, TrovaOrtopedico 0571 878807).

Quale numero va in header, footer, JSON-LD, WhatsApp? La segreteria (Lun�Gio 15:30�17:30 su LinkedIn) � ancora quella?

### D4 � Google Business Profile
Michele ha �un profilo per ogni studio, circa 4� e vorrebbe **un profilo solo**.
- Elenco URL delle schede attuali (o screenshot).
- Quali sono **sue** (attivit� che pu� verificare) e quali sono delle cliniche?
- Accesso all'account Google con cui sono gestite?

Risposta di principio gi� in [@08](08_Sedi_e_Google_Business.md): un unico pin per quattro indirizzi **non � possibile**. Serve spiegarglielo e proporre il modello �sito unico + N schede o N menzioni sulle schede delle cliniche�.

## Importanti (prima dei testi definitivi)

### D5 � Posizionamento clinico
Il CV e i profili oscillano tra:

- **Core**: spalla / gomito / mano / artroscopia / eco MSK / sport
- **Anche**: protesi anca e ginocchio (CESAT, TrovaOrtopedico, Doctolib)

Per il sito: il hero � �chirurgo della spalla e dell'arto superiore� con protesi anca/ginocchio come secondario, o � un ortopedico generalista di alto livello? Impatta menu, keyword, e se esiste `/patologie/protesi-anca-ginocchio` (@04).

### D6 � Recensioni
- Da quali piattaforme scaricare? (MioDottore: profilo **non trovato** nelle SERP pubbliche di Capannoli; Doctolib non ha restituito recensioni in fetch; LinkedIn no.)
- Consegnare screenshot.
- Consenso a citare nome/piattaforma.
- Nome della sezione sul sito (non �Testimonials�).
- Se al go-live non ci sono: il blocco home **non si mostra**.

### D7 � Blog / nome della sezione
Serve un nome (Journal, Quaderno, Spalla in chiaro, Appunti di sala, Percorsi�). URL proposta: `/articoli`. Michele sta preparando un piano social: chi scrive, che cadenza, chi pubblica su Keystatic (lui, segreteria, Mauro)?

### D8 � Caso Alonso e contenuti �forti�
Citato in telefonata come articolo d'interesse. Athletica Cetilar � legata al fisioterapista di Fernando Alonso. **Non pubblicare** senza:

- consenso del paziente (e della struttura, se serve)
- testo rivisto dal medico
- niente dettagli sanitari identificativi

Chiedere: quali altri casi/pubblicazioni/eventi (Shoulder School Fucecchio, screening Peccioli over 50, Cutting Edge Techniques) sono raccontabili.

### D9 � Foto, video, logo
- Logo esistente? Palette?
- Shooting: quale sede, quante mezze giornate, ritratto + ambienti + eventuale video.
- Materiale gi� in suo possesso (Drive?). In CRM: �importante mettere accessibilit� di ogni struttura, foto, link anche drive�.

### D10 � Prezzi da mostrare
Doctolib JSON-LD: prima visita **120 �**, controllo **80�90 �**, infiltrazione acido ialuronico **80�150 �**. Andarli in chiaro sul sito? (Trasparenza vs flessibilit� tra sedi.)

**Proposta Mauro (@04):** se s�, **solo** in Contatti, con nota che interventi/ricoveri sono un altro listino. Se no, �il costo lo comunica la segreteria�.

### D11 � Lingua inglese
Chi revisiona l'EN? (Mauro / traduttore / Michele, che in CV ha inglese C1.) Target: pazienti internazionali in Toscana / sportivi / Athletica.

### D12 � Colleghi da lui indicati come �buona indicizzazione�
Nella telefonata: link di colleghi con SEO buona e design brutto. **URL non verbalizzati negli appunti.** Chiederli. Ipotesi di ricerca: [simonenicoletti.it](https://www.simonenicoletti.it/) (stesso CESAT) e [drcheccucci.it](https://www.drcheccucci.it/).

### D13 � Come citare il collega (CESAT)
Online Nicoletti risulta direttore della SOC; Michele dirigente / chirurgo. Impatta Chi sono, blog Shoulder School, papers condivisi. Una riga confermata basta; niente pagina �equipe�.

### D14 � Doctolib come canale
Instagram punta ancora l�. Il sito: bottone Prenota + telefono, solo telefono, o �la segreteria ti indica il canale�?

## Non bloccanti

- P. IVA / intestazione dominio / privacy policy titolare
- Assicurazioni convenzionate
- Instagram `michelenovi_md`: da collegare, da non usare come CMS
- LinkedIn da aggiornare (foto, mix IT/EN)
- Correzione job title CRM �Fisioterapista� ? Ortopedico
- Pagina `/pubblicazioni` vs blocco in Chi sono (@04: v1 = blocco)
