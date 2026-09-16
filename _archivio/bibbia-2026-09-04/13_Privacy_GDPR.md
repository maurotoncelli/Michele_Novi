# 13. Privacy, GDPR e deontologia

> Parte della Bibbia. Indice: [00_README_Master_Index.md](00_README_Master_Index.md).

## Metadati
- ID: CAP-13
- Stato: Bozza
- Ultimo aggiornamento: 2026-09-04
- Dipendenze: @05_Stack, @09_Recensioni, @10_Blog
- Owner: Mauro (testi) · titolare del trattamento: Michele / studio (da confermare)

## Sintesi
I dati sulla salute sono **categorie particolari** (art. 9 GDPR). Il sito è disegnato per **non raccoglierli**. Privacy policy e cookie banner ci sono; il form chiede recapiti. Casi clinici e VIP (Alonso) restano fuori finché non c’è consenso esplicito.

## Stato attuale del progetto

### Principio già venduto nel piano tecnico
- Form: nome + recapito + consenso. Il problema clinico si racconta in studio o al telefono.
- Cookie banner: analytics solo dopo consenso.
- Policy redatte per attività sanitaria (non un template e-commerce).
- Niente database pazienti sul sito.

### Titolare
Da confermare: persona fisica Dott. Michele Novi vs eventuale studio associato. Indirizzo (CV: Lungarno Gambacorti 36, Pisa — può essere residenza, **non** pubblicare come sede visita se non lo è). Email privacy: sul dominio nuovo.

### Form e email
- Minimizzazione: niente «descrivi i sintomi», niente upload referti in v1.
- Informativa sotto il form, checkbox consenso al trattamento per ricontatto.
- Marketing (newsletter): non in v1; se arriva, checkbox separata.
- Conservazione lead: quanto basta per ricontattare, poi cancellazione. Definire mesi.

### Cookie / GA4
Consent Mode o non caricare GA4 prima del sì. GSC non richiede cookie lato utente.

### Recensioni
Pubblicare un nome e un testo è diffusione di dati. Preferire iniziali o nome di battesimo + consenso. Non copiare recensioni da MioDottore violando i ToS se lo vietano: parafrasi breve + attribuzione piattaforma, o citazione autorizzata.

### Contenuti sanitari
- Disclaimer in articoli e pagine patologia.
- Niente diagnosi online.
- Casi reali: anonimizzazione vera (non “paziente famoso ovvio”).
- **Alonso / personaggi pubblici:** il fatto che Athletica ruoti intorno al motorsport non autorizza a scrivere «ho operato X». Segreto professionale + GDPR. Se Michele vuole quel pezzo: consenso scritto, testo approvato, possibilmente senza dettagli sanitari.

### Foto shooting
Liberatoria ritratti (Michele). Se compaiono altri (segreteria, pazienti in sala d’attesa): liberatoria o crop. Niente volti pazienti.

### Keystatic / git
I contenuti del blog sono pubblici. Non committare elenchi pazienti, screenshot recensioni con email, Drive clinici.

## Idee future
- DPA con Vercel / Resend / Google se un legale lo chiede.
- Se nascerà il gestionale: altro capitolo, altro DPIA. Non mescolare.

## Nodi da sciogliere
- Titolare, P.IVA, pec, OMCeO.
- Chi è il DPO (probabilmente nessuno, titolare piccolo).
- Testo policy: Mauro redige bozza, non è consulenza legale.

## Passi successivi
Bozze `/privacy` e `/cookie` in IT+EN quando il dominio e il titolare sono noti.

## Decisioni congelate (lock-in)
- Zero dati clinici nel form.
- Zero casi identificativi senza consenso.
- Analytics dopo consenso.
- Policy dedicate, non copiate da un ristorante.

## Rischi / Compliance & Riferimenti
- Reg. UE 2016/679.
- Codice di deontologia medica (pubblicità informativa).
- Piano tecnico, sezione Privacy e GDPR.
