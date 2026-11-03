import type { Locale } from "./routing";

/**
 * Informativa Privacy (art. 13 GDPR), Cookie Policy e Condizioni d'uso / Disclaimer sanitario.
 * I dati del titolare arrivano da settings e vengono interpolati: {titolare} {piva} {albo} {pec} {email} {dominio}.
 */
export type Blocco = { h?: string; p: string[] };

const privacy: Record<Locale, Blocco[]> = {
  it: [
    {
      h: "Titolare del trattamento",
      p: [
        "Titolare del trattamento dei dati personali è il {titolare}, Medico Chirurgo specialista in Ortopedia e Traumatologia ({albo}), P. IVA {piva}, domicilio digitale / PEC: {pec}. Per qualsiasi richiesta relativa alla privacy è possibile scrivere a: {email}.",
        "La presente informativa (resa ai sensi dell'art. 13 del Regolamento UE 2016/679 — GDPR) riguarda il sito web {dominio}. Il sito ha natura esclusivamente informativa e non raccoglie né conserva su database dati relativi allo stato di salute: il modulo di contatto richiede unicamente nome, un recapito telefonico o email, la sede preferita e la fascia oraria in cui essere ricontattati.",
      ],
    },
    {
      h: "Tipologie di dati trattati, finalità e base giuridica",
      p: [
        "Dati forniti volontariamente tramite il modulo di contatto (nome e cognome, email o telefono, sede preferita, preferenze di ricontatto): vengono utilizzati esclusivamente dalla segreteria per ricontattare l'interessato e fornire informazioni sulle visite ambulatoriali. Base giuridica: esecuzione di misure precontrattuali adottate su richiesta dell'interessato (art. 6, par. 1, lett. b GDPR) e consenso dell'interessato (art. 6, par. 1, lett. a GDPR). Conservazione: per il solo tempo necessario a evadere la richiesta di contatto.",
        "Dati tecnici di navigazione (indirizzo IP, log tecnici dei sistemi informatici e del provider di hosting): acquisiti automaticamente per garantire il corretto funzionamento e la sicurezza del sito. Base giuridica: legittimo interesse del titolare (art. 6, par. 1, lett. f GDPR).",
        "Dati statistici aggregati (Google Analytics 4, attivato solo previo consenso esplicito tramite il banner cookie e con anonimizzazione dell'indirizzo IP): utilizzati per analizzare in forma aggregata il traffico sulle pagine del sito. Base giuridica: consenso dell'interessato (art. 6, par. 1, lett. a GDPR), liberamente revocabile in qualsiasi momento.",
      ],
    },
    {
      h: "Destinatari e fornitori tecnici",
      p: [
        "Il modulo di contatto recapita la richiesta via posta elettronica alla segreteria tramite il servizio transazionale Resend (Resend, Inc.). L'infrastruttura di hosting e distribuzione è fornita da Vercel Inc. Le statistiche, esclusivamente se accettate dall'utente, sono gestite da Google Ireland Limited. Tali soggetti operano in qualità di responsabili del trattamento o titolari autonomi nel rispetto delle garanzie previste dal GDPR. Nessun dato viene ceduto a terzi per finalità commerciali o di profilazione.",
      ],
    },
    {
      h: "Diritti dell'interessato",
      p: [
        "Ai sensi degli artt. 15–22 del GDPR, l'interessato può chiedere in qualsiasi momento l'accesso ai propri dati personali, la rettifica, la cancellazione, la limitazione o l'opposizione al trattamento, nonché revocare il consenso prestato, inviando una comunicazione a {email}. Resta fermo il diritto di proporre reclamo al Garante per la protezione dei dati personali (www.garanteprivacy.it).",
      ],
    },
    {
      h: "Informazione sanitaria e condizioni d'uso",
      p: [
        "I contenuti pubblicati su questo sito hanno finalità esclusivamente divulgativa e informativa, nel rispetto della Legge n. 145/2018 (art. 1, commi 525 e 536) e degli artt. 55 e 56 del Codice di Deontologia Medica. Le informazioni presenti non costituiscono in alcun caso consulenza medica, diagnosi o prescrizione terapeutica a distanza e non sostituiscono il rapporto diretto tra medico e paziente in sede di visita specialistica.",
        "Le recensioni riportate sono pubbliche su piattaforme terze verificate o pubblicate con il consenso degli autori. Nessun contenuto del sito descrive casi clinici riconducibili a pazienti identificabili.",
      ],
    },
  ],
  en: [
    {
      h: "Data Controller",
      p: [
        "The Data Controller is {titolare}, Consultant Orthopaedic and Trauma Surgeon ({albo}), VAT {piva}, certified email (PEC): {pec}. For any privacy-related request, please write to: {email}.",
        "This notice (provided pursuant to Article 13 of EU Regulation 2016/679 — GDPR) covers the website {dominio}. The website is purely informational and does not collect or store health data on any database: the contact form only asks for your name, a phone number or email address, your preferred clinic location and when you prefer to be called back.",
      ],
    },
    {
      h: "Categories of data, purposes and legal basis",
      p: [
        "Data voluntarily provided through the contact form (full name, email or phone, preferred location, callback preferences): used solely by the office to call you back and arrange an outpatient consultation. Legal basis: pre-contractual steps taken at the data subject's request (Art. 6(1)(b) GDPR) and consent (Art. 6(1)(a) GDPR). Retention: only for the time strictly required to handle the inquiry.",
        "Technical browsing data (IP address, hosting provider security and access logs): collected automatically to ensure the proper functioning and security of the website. Legal basis: legitimate interest of the controller (Art. 6(1)(f) GDPR).",
        "Aggregated statistical data (Google Analytics 4, activated exclusively after your explicit consent via the cookie banner and with IP anonymisation): used to understand aggregate traffic across pages. Legal basis: consent (Art. 6(1)(a) GDPR), which may be withdrawn at any time.",
      ],
    },
    {
      h: "Recipients and technical providers",
      p: [
        "The contact form forwards your inquiry by email to the office through Resend (Resend, Inc.), a transactional email provider. Hosting is provided by Vercel Inc. Analytics, only if accepted by the user, are processed by Google Ireland Limited. These providers act as data processors or independent controllers under GDPR safeguards. No personal data is ever sold or shared for marketing.",
      ],
    },
    {
      h: "Your rights",
      p: [
        "Under Articles 15–22 of the GDPR, you may request access, rectification, erasure, restriction or objection to processing, and withdraw consent at any time, by writing to {email}. You also have the right to lodge a complaint with the Italian Data Protection Authority (Garante per la protezione dei dati personali, www.garanteprivacy.it).",
      ],
    },
    {
      h: "Medical disclaimer and terms of use",
      p: [
        "All content published on this website is provided solely for educational and informational purposes in compliance with Italian healthcare communication regulations (Law 145/2018 and Articles 55–56 of the Italian Code of Medical Ethics). Nothing on this website constitutes remote medical advice, diagnosis or treatment prescription, nor does it replace an in-person clinical examination.",
        "Published patient reviews are either publicly available on verified third-party platforms or shared with the author's consent. No content on this site describes identifiable clinical cases.",
      ],
    },
  ],
};

const cookie: Record<Locale, Blocco[]> = {
  it: [
    {
      h: "Cosa sono i cookie e come li usiamo",
      p: [
        "Questo sito utilizza cookie tecnici strettamente necessari al funzionamento (per ricordare la lingua di navigazione e la scelta espressa nel banner cookie). Per questi strumenti non è richiesto il consenso preventivo.",
        "Esclusivamente se clicchi su «Accetta» nel banner, viene attivato Google Analytics 4 (con IP anonimizzato) per raccogliere statistiche aggregate e anonime sulle pagine visitate. Se scegli «Solo tecnici» o chiudi il banner senza accettare, nessuno script statistico di terze parti viene caricato.",
      ],
    },
    {
      h: "Elenco degli strumenti utilizzati",
      p: [
        "mn_lang — cookie tecnico di prima parte (durata: 12 mesi) — memorizza la lingua preferita (IT / EN).",
        "mn_consenso — archiviazione locale tecnica (localStorage) — memorizza la tua preferenza sui cookie statistici («si» oppure «no»).",
        "_ga, _ga_* — cookie statistici di terza parte (Google Ireland Ltd., durata: fino a 24 mesi) — installati esclusivamente dopo il tuo consenso esplicito per statistiche aggregate su Google Analytics 4.",
        "Eventuali contenuti video incorporati da YouTube utilizzano la modalità di privacy avanzata (youtube-nocookie.com), che non installa cookie di tracciamento all'apertura della pagina.",
      ],
    },
    {
      h: "Come modificare o revocare il consenso",
      p: [
        "Puoi modificare o revocare in qualsiasi momento la tua scelta cliccando sul pulsante qui sotto per riaprire il banner dei cookie, oppure cancellando i dati di navigazione dal tuo browser.",
      ],
    },
  ],
  en: [
    {
      h: "What cookies are and how we use them",
      p: [
        "This website uses strictly necessary technical cookies required for basic operation (remembering your chosen language and your cookie banner preference). These do not require prior consent.",
        "Only if you click 'Accept' on the banner is Google Analytics 4 (with anonymised IP) activated to collect anonymous, aggregated statistics on visited pages. If you choose 'Technical only', no third-party analytics scripts are loaded.",
      ],
    },
    {
      h: "List of cookies and local storage items",
      p: [
        "mn_lang — first-party technical cookie (duration: 12 months) — remembers your preferred language (IT / EN).",
        "mn_consenso — technical localStorage item — stores your preference regarding analytics cookies ('si' or 'no').",
        "_ga, _ga_* — third-party analytics cookies (Google Ireland Ltd., duration: up to 24 months) — set exclusively after your explicit consent for Google Analytics 4.",
        "Where YouTube videos are embedded, they use enhanced privacy mode (youtube-nocookie.com), which sets no tracking cookies when the page loads.",
      ],
    },
    {
      h: "How to change or withdraw your consent",
      p: [
        "You can review or withdraw your consent at any time by clicking the button below to reopen the cookie banner, or by clearing site data in your browser settings.",
      ],
    },
  ],
};

export const legale = { privacy, cookie };
