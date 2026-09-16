# 08. Sedi e Google Business Profile

> Parte della Bibbia. Indice: [00_README_Master_Index.md](00_README_Master_Index.md).
> Tabella completa (indirizzi, telefoni, evidenza): [`../ricerca/2026-09-04_quadro-dottor-novi.md`](../ricerca/2026-09-04_quadro-dottor-novi.md) §3.

## Metadati
- ID: CAP-08
- Stato: Bozza
- Ultimo aggiornamento: 2026-09-04 (estrazione civici dai siti)
- Dipendenze: @04_IA, @06_SEO, @07_Presenza
- Owner: Mauro

## Sintesi
La domanda di Michele («posso avere un solo profilo Google per tutti gli studi?») ha risposta **no**, se intende un solo pin in mappa. Può avere **un solo sito** e, se le schede sono sue, **un account** che ne gestisce diverse. Molte «sedi» sono ambulatori di terzi: lì la scheda è della clinica, non del medico.

Due civici facili da confondere: a Fucecchio **Piazza Lavagnini 5** è l'ospedale CESAT; **n. 6** sono gli Studi Medici San Pietro (Doctolib).

## Stato attuale del progetto

### Regola Google (2026)
- Un indirizzo fisico verificabile ? **una** scheda GBP.
- Più specialità nello stesso indirizzo ? **non** si clonano schede.
- Più sedi dello stesso titolare ? N schede, gestibili da un **Location Group** / Account di sedi.
- Medico che visita in una clinica: di norma è un **professionista ospitato**. Creare una seconda scheda sullo stesso civico, a nome del medico, viola le policy e viene fusa o sospesa.

Quello che Michele ricorda come «4 profili» è probabilmente già il modello corretto (o un mix di schede clinica + schede sue). Va ispezionato da dentro l'account, non da fuori.

### Cosa proporgli
1. **Sito = profilo unico** percepito dal paziente.
2. Pagine `/sedi/[slug]` con mappa e bottone «Indicazioni» / «Scheda Google della struttura».
3. GBP:
   - se esiste uno **studio proprio** (es. San Verano?): scheda a suo nome, categoria Ortopedico, sito, foto shooting, recensioni spinte lì;
   - per MiniHospital, Athletica, Santa Croce, Fisiomed, San Paolo: chiedere di comparire nello staff e che il sito ufficiale sia in bio dove possibile;
   - schede duplicate o abbandonate: unione/chiusura.
4. Non promettere un pin solo che copre Peccioli+Fucecchio+Pisa: Google mostra la distanza. Un pin a Peccioli **non** posiziona a Pisa.

### Elenco sedi da validare (estratto 4/09/2026)

**Alta evidenza 2025–26** (candidati nucleo sito, da spuntare):

| Sede | Indirizzo pubblico | Tel | Evidenza |
|------|-------------------|-----|----------|
| CESAT / Osp. San Pietro Igneo | Piazza Spartaco Lavagnini **5**, Fucecchio | CUP USL, non la sua segreteria | LinkedIn dal mag 2021, bio Doctolib, Quinews |
| Studi Medici San Pietro | Piazza Lavagnini **6**, Fucecchio | **348 4331733** | Doctolib default; mer 16–18 |
| Centro Medico San Verano | Viale Cavour **13**, Peccioli (Reteimprese cita anche Piazza del Carmine 6) | 348… | LinkedIn; Instagram struttura lo tagga **apr–mag 2026** |
| Fisiomed | Via Tosco Romagnola Ovest **210**, Fornacette | 0587 420853 (struttura) | Doctolib; LinkedIn |
| Kinetic Center | Via G. Impastato **3**, Pisa | — | Doctolib; LinkedIn |
| Athletica Cetilar | Via delle Lenze **216/B**, Pisa | Doctolib | Staff sito; 1 recensione 5/5 in snippet |
| MiniHospital S. Pertini | Via Antonio Gramsci **29**, Capannoli | 0587 609134 | Scheda medico + CV; Q&A MioDottore «Capannoli» |

**Da confermare (citati, evidenza più debole):**

- Santa Croce Medical Center, Piazza F.lli Cervi 11, Santa Croce sull'Arno — pagina nome-only
- Casa di Cura San Paolo, Via Bonellina 199, Pistoia — bio copy-paste
- Villa Donatello, Sesto Fiorentino — asterisco **solo ricovero**, non ambulatorio

**Storico / da non pubblicare:**

- Studi Medici You — Facebook 15/11/2021, tel 0587 734714
- CentroSaluteOnline — shell di prenotazione, non una sede
- Reteimprese / Localshop24 — directory inesatte

Doctolib elenca **4 civici** in listing Pisa: Lavagnini 6, Tosco Romagnola 210, Impastato 3, Lenze 216. Peccioli è nel title ma non nella riga `address`. MiniHospital non è su Doctolib.

Per il lancio: meglio **3–6 sedi vere** che 11 fantasma. CRM: «importante mettere accessibilità di ogni struttura, foto, link anche drive».

### Campi da raccogliere per ogni sede attiva
Vedi modello dati in @04. In più: parcheggio, barriere architettoniche, presenza ecografo, come si prenota (segreteria Michele vs CUP vs Doctolib vs centralino clinica).

### Orari
LinkedIn: segreteria Lun–Gio 15:30–17:30. Instagram: «da Lun a Giov» senza fascia. Doctolib: solo uno slot mercoledì 16–18 a Fucecchio. Troppo poco per il sito: servono orari veri per sede, o la formula «su appuntamento, chiama la segreteria» **uguale ovunque**.

## Idee future
- Icona/logo per sede.
- Filtro «visita vicino a me» se le sedi restano molte.
- Quando ci sarà l'agenda: disponibilità per sede.

## Nodi da sciogliere
D2, D3, D4. Senza accesso GBP si può solo teorizzare. Civico San Verano (Cavour 13 vs Carmine 6) da chiudere.

## Passi successivi
1. Call: elenco sedi sì/no sulla tabella del quadro.
2. Screenshot delle 4 schede Google.
3. Decidere quali pagine `/sedi/` esistono al lancio.

## Decisioni congelate (lock-in)
- Niente scheda Google unica multi-indirizzo.
- Niente GBP clonata sul civico di una clinica.
- Ogni sede pubblica sul sito deve essere confermata da Michele.
- CESAT si comunica come ospedale («operante presso»), non come studio privato.

## Rischi / Compliance & Riferimenti
- Policy Google Business Profile (name, address, category).
- Libera professione in ospedale: rispettare regole USL su pubblicità e recapiti.
- Guide: PublyMedica SEO locale; Docplanner help GBP medici.
