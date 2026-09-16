import type { Locale } from "./routing";

/**
 * Testi legali in bozza (Mauro redige, non è consulenza legale — bibbia/09_tecnica.md).
 * I dati del titolare arrivano da settings e vengono interpolati: {titolare} {piva} {pec} {email} {dominio}.
 */
export type Blocco = { h?: string; p: string[] };

const privacy: Record<Locale, Blocco[]> = {
  it: [
    {
      p: [
        "Titolare del trattamento: {titolare}, P. IVA {piva}, PEC {pec}. Per qualsiasi richiesta: {email}.",
        "Questa informativa riguarda il sito {dominio}. Il sito non raccoglie dati sanitari: il modulo di contatto chiede solo nome, un recapito, la sede preferita e come richiamarti.",
      ],
    },
    {
      h: "Quali dati e perché",
      p: [
        "Dati del modulo di contatto (nome, email o telefono, sede preferita, messaggio): servono a richiamarti per fissare una visita. Base giuridica: il tuo consenso e l'esecuzione di misure precontrattuali. Conservazione: il tempo necessario a gestire la richiesta, poi cancellati.",
        "Dati di navigazione (indirizzo IP, log tecnici del provider di hosting): necessari al funzionamento e alla sicurezza del sito. Base giuridica: legittimo interesse.",
        "Statistiche (Google Analytics 4, solo dopo il tuo consenso, con IP anonimizzato): servono a capire come viene usato il sito. Puoi rifiutarle senza alcuna conseguenza.",
      ],
    },
    {
      h: "A chi vengono comunicati",
      p: [
        "Il modulo invia un'email alla segreteria tramite un fornitore di email transazionali. L'hosting è fornito da Vercel Inc. Le statistiche, se accettate, sono trattate da Google Ireland Ltd. Questi fornitori agiscono come responsabili del trattamento o titolari autonomi nei limiti delle rispettive policy. Nessun dato viene venduto o ceduto per marketing.",
      ],
    },
    {
      h: "I tuoi diritti",
      p: [
        "Puoi chiedere accesso, rettifica, cancellazione, limitazione, opposizione e portabilità dei tuoi dati, e revocare il consenso in ogni momento, scrivendo a {email}. Puoi anche proporre reclamo al Garante per la protezione dei dati personali.",
      ],
    },
    {
      h: "Recensioni e contenuti",
      p: [
        "Le recensioni pubblicate sono riportate con il consenso di chi le ha scritte o sono già pubbliche su piattaforme terze. Nessun contenuto del sito descrive casi clinici identificabili.",
      ],
    },
  ],
  en: [
    {
      p: [
        "Data controller: {titolare}, VAT {piva}, certified email {pec}. For any request: {email}.",
        "This notice covers the website {dominio}. The site does not collect health data: the contact form only asks for your name, a way to reach you, your preferred location and how to call you back.",
      ],
    },
    {
      h: "Which data and why",
      p: [
        "Contact form data (name, email or phone, preferred location, message): used to call you back and book a visit. Legal basis: your consent and pre-contractual steps. Retention: as long as needed to handle the request, then deleted.",
        "Browsing data (IP address, hosting provider technical logs): needed for the site to work and stay secure. Legal basis: legitimate interest.",
        "Statistics (Google Analytics 4, only after your consent, with anonymised IP): used to understand how the site is used. You may refuse with no consequence.",
      ],
    },
    {
      h: "Who receives them",
      p: [
        "The form sends an email to the office through a transactional email provider. Hosting is provided by Vercel Inc. Statistics, if accepted, are processed by Google Ireland Ltd. These providers act as processors or independent controllers within their own policies. No data is sold or shared for marketing.",
      ],
    },
    {
      h: "Your rights",
      p: [
        "You may request access, rectification, erasure, restriction, objection and portability of your data, and withdraw consent at any time, by writing to {email}. You may also lodge a complaint with the Italian Data Protection Authority.",
      ],
    },
    {
      h: "Reviews and content",
      p: ["Published reviews are shown with the consent of their authors or are already public on third-party platforms. No content on this site describes identifiable clinical cases."],
    },
  ],
};

const cookie: Record<Locale, Blocco[]> = {
  it: [
    {
      p: [
        "Il sito usa cookie tecnici, necessari al funzionamento (ricordare la lingua scelta e la tua scelta sui cookie). Non richiedono consenso.",
        "Solo se accetti, viene attivato Google Analytics 4 per statistiche anonime sull'uso del sito. Puoi cambiare idea in qualsiasi momento cancellando i dati del sito dal browser: alla visita successiva il banner ricompare.",
      ],
    },
    {
      h: "Elenco",
      p: [
        "mn_lang — tecnico, 12 mesi — ricorda la lingua.",
        "mn_consenso (localStorage) — tecnico — ricorda la tua scelta sui cookie.",
        "_ga, _ga_* — statistico, solo dopo consenso, fino a 24 mesi — Google Analytics 4.",
        "I video YouTube, se presenti, sono caricati in modalità privacy avanzata (youtube-nocookie.com).",
      ],
    },
  ],
  en: [
    {
      p: [
        "The site uses technical cookies needed for it to work (remembering your language and your cookie choice). They do not require consent.",
        "Only if you accept, Google Analytics 4 is activated for anonymous statistics on site usage. You can change your mind at any time by clearing site data in your browser: the banner will appear again on your next visit.",
      ],
    },
    {
      h: "List",
      p: [
        "mn_lang — technical, 12 months — remembers your language.",
        "mn_consenso (localStorage) — technical — remembers your cookie choice.",
        "_ga, _ga_* — statistics, only after consent, up to 24 months — Google Analytics 4.",
        "YouTube videos, where present, are loaded in enhanced privacy mode (youtube-nocookie.com).",
      ],
    },
  ],
};

export const legale = { privacy, cookie };
