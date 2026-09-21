import { config, collection, singleton, fields } from "@keystatic/core";

/**
 * Schema dei contenuti. Unica fonte di verità per tutto ciò che appare a schermo
 * (vedi ../bibbia/09_tecnica.md → "Principio: tutto è dato").
 *
 * - Sviluppo: KEYSTATIC_STORAGE=local → scrive su content/.
 * - Produzione: GitHub → ogni salvataggio da /keystatic è un commit, Vercel rideploya.
 *
 * Ogni testo ha campo IT e campo EN affiancati. Il sito non duplica mai file per lingua.
 */

const storage =
  process.env.KEYSTATIC_STORAGE === "github"
    ? ({
        kind: "github",
        repo: {
          owner: process.env.KEYSTATIC_GITHUB_OWNER ?? "",
          name: process.env.KEYSTATIC_GITHUB_REPO ?? "",
        },
        // Il repo contiene anche bibbia/ e fonti/: il sito sta nella sottocartella site/.
        pathPrefix: process.env.KEYSTATIC_PATH_PREFIX ?? "site",
      } as const)
    : ({ kind: "local" } as const);

/** Testo breve bilingue. */
const testo = (label: string, opts?: { multiline?: boolean; description?: string; required?: boolean }) =>
  fields.object(
    {
      it: fields.text({
        label: `${label} (IT)`,
        multiline: opts?.multiline,
        validation: opts?.required ? { isRequired: true } : undefined,
      }),
      en: fields.text({ label: `${label} (EN)`, multiline: opts?.multiline }),
    },
    { label, description: opts?.description },
  );

const seo = fields.object(
  {
    title: testo("Title", { description: "Vuoto = titolo della pagina." }),
    description: testo("Description", { multiline: true }),
    ogImage: fields.image({
      label: "Immagine social",
      directory: "public/images/og",
      publicPath: "/images/og/",
    }),
    noindex: fields.checkbox({ label: "Non indicizzare", defaultValue: false }),
  },
  { label: "SEO", description: "Opzionale. Il sito genera fallback da titolo e lead." },
);

const immagine = (label: string, dir: string) =>
  fields.object(
    {
      src: fields.image({ label, directory: `public/images/${dir}`, publicPath: `/images/${dir}/` }),
      alt: testo("Testo alternativo"),
    },
    { label },
  );

const AREE = [
  { label: "Spalla", value: "spalla" },
  { label: "Arto superiore (gomito, mano)", value: "arto-superiore" },
  { label: "Traumatologia sportiva", value: "sport" },
  { label: "Come si opera", value: "metodo" },
  { label: "Anca e ginocchio", value: "anca-ginocchio" },
] as const;

const SEGNI = [
  "spalla",
  "gomito",
  "mano",
  "sport",
  "artroscopia",
  "anca",
  "ginocchio",
  "eco",
  "ospedale",
  "studio",
  "clinica",
  "protesi",
  "frattura",
  "esercizio",
  "globo",
  "approfondimenti",
  "doc",
  "check",
].map((v) => ({ label: v, value: v }));

export default config({
  storage,
  ui: {
    brand: { name: "Michele Novi — Sito" },
    navigation: {
      Sito: ["settings", "home", "profilo", "disegni"],
      Contenuti: ["patologie", "sedi", "approfondimenti", "pubblicazioni", "faq", "recensioni"],
    },
  },

  singletons: {
    settings: singleton({
      label: "Impostazioni",
      path: "content/settings",
      format: { data: "yaml" },
      schema: {
        nome: fields.text({ label: "Nome pubblico", defaultValue: "Dott. Michele Novi" }),
        ruolo: testo("Ruolo (una riga)"),
        dominio: fields.url({ label: "Dominio (https://…)", description: "Senza slash finale." }),
        telefono: fields.text({
          label: "Telefono segreteria",
          description:
            "Formato internazionale, es. +39 348 0000000. VUOTO finché le due cifre non coincidono (bibbia/APERTI). Se vuoto, il sito non mostra nessun bottone Chiama.",
        }),
        whatsapp: fields.text({
          label: "WhatsApp (solo cifre, es. 39348…)",
          description: "Vuoto = nessun bottone WhatsApp.",
        }),
        whatsappTesto: testo("Testo precompilato WhatsApp", {
          description: "Non clinico. Es. «Vorrei informazioni per una visita».",
        }),
        email: fields.text({ label: "Email pubblica (info@…)" }),
        emailDestinazioneForm: fields.text({
          label: "Email che riceve il form",
          description: "Non è mostrata. Se vuota si usa quella pubblica.",
        }),
        orari: testo("Orari segreteria", {
          multiline: true,
          description: "Vuoto finché la segreteria non li conferma.",
        }),
        instagram: fields.url({ label: "Instagram" }),
        linkedin: fields.url({ label: "LinkedIn" }),
        youtube: fields.url({ label: "YouTube" }),
        piva: fields.text({ label: "P. IVA" }),
        albo: fields.text({ label: "Albo (es. OMCeO Pisa n. 5749)" }),
        pec: fields.text({ label: "PEC" }),
        disclaimer: testo("Disclaimer sanitario (breve)", { multiline: true }),
      },
    }),

    profilo: singleton({
      label: "Chi sono",
      path: "content/profilo",
      format: { data: "yaml" },
      schema: {
        nome: fields.text({ label: "Nome e cognome", defaultValue: "Michele Novi" }),
        titolo: testo("Titolo professionale"),
        apertura: testo("Apertura (2–3 frasi)", { multiline: true }),
        ritratto: immagine("Ritratto", "profilo"),
        inEvidenza: fields.array(
          fields.object({
            anno: fields.text({ label: "Anno" }),
            titolo: testo("Titolo"),
            testo: testo("Una riga", { multiline: true }),
          }),
          { label: "In evidenza (fellowship, incarichi)", itemLabel: (p) => `${p.fields.anno.value} — ${p.fields.titolo.fields.it.value}` },
        ),
        timeline: fields.array(
          fields.object({
            periodo: fields.text({ label: "Periodo" }),
            tipo: fields.select({
              label: "Barra",
              options: [
                { label: "Esperienze lavorative", value: "lavoro" },
                { label: "Fellowship internazionali", value: "fellowship" },
                { label: "Formazione", value: "formazione" },
              ],
              defaultValue: "formazione",
            }),
            titolo: testo("Cosa"),
            luogo: fields.text({ label: "Dove" }),
          }),
          { label: "Percorso (barre in Chi sono)", itemLabel: (p) => `${p.fields.periodo.value} · ${p.fields.tipo.value} — ${p.fields.titolo.fields.it.value}` },
        ),
        docenza: fields.array(
          fields.object({ periodo: fields.text({ label: "Periodo" }), testo: testo("Cosa") }),
          { label: "Docenza e società", itemLabel: (p) => p.fields.testo.fields.it.value },
        ),
        societa: fields.array(fields.text({ label: "Società scientifica" }), {
          label: "Società scientifiche",
          itemLabel: (p) => p.value,
        }),
        comeValuto: testo("Come valuto (paragrafo)", { multiline: true }),
        comeValutoPassi: fields.array(
          fields.object({
            titolo: testo("Titolo"),
            testo: testo("Una riga", { multiline: true }),
          }),
          { label: "Come valuto: i passi della visita (tre)", itemLabel: (p) => p.fields.titolo.fields.it.value },
        ),
        territorio: testo("Territorio e didattica (paragrafo)", { multiline: true }),
        lingue: fields.array(fields.text({ label: "Lingua" }), { label: "Lingue", itemLabel: (p) => p.value }),
        seo,
      },
    }),

    home: singleton({
      label: "Home",
      path: "content/home",
      format: { data: "yaml" },
      schema: {
        eyebrow: testo("Riga sopra il titolo"),
        titolo: testo("Titolo (H1)", { required: true }),
        sottotitolo: testo("Sottotitolo", { multiline: true }),
        ritratto: immagine("Ritratto hero", "home"),
        lavoro: fields.object(
          {
            foto: immagine("Foto del lavoro (ambulatorio, sala, ecografo)", "home"),
            video: fields.text({
              label: "Video breve (opzionale)",
              description: "File in public/videos, es. «sala.mp4». Muto, in loop, 8–10 secondi. Se vuoto si usa la foto.",
            }),
          },
          { label: "Fascia Percorso: lastra a sinistra" },
        ),
        fiducia: fields.array(
          fields.object({ testo: testo("Voce"), segno: fields.select({ label: "Segno", options: SEGNI, defaultValue: "ospedale" }) }),
          { label: "Perché fidarsi (4–5 voci)", itemLabel: (p) => p.fields.testo.fields.it.value },
        ),
        fasce: fields.array(
          fields.object({
            tipo: fields.select({
              label: "Fascia",
              options: [
                { label: "Cosa curo", value: "patologie" },
                { label: "Dove", value: "sedi" },
                { label: "Perché fidarsi", value: "fiducia" },
                { label: "Recensioni", value: "recensioni" },
                { label: "Approfondimenti", value: "approfondimenti" },
                { label: "Contatto", value: "contatto" },
              ],
              defaultValue: "patologie",
            }),
            attiva: fields.checkbox({ label: "Attiva", defaultValue: true }),
          }),
          { label: "Ordine delle fasce", itemLabel: (p) => `${p.fields.tipo.value}${p.fields.attiva.value ? "" : " (off)"}` },
        ),
        seo,
      },
    }),

    disegni: singleton({
      label: "Disegni",
      path: "content/disegni",
      format: { data: "yaml" },
      schema: {
        voci: fields.array(
          fields.object({
            id: fields.select({ label: "Segno", options: SEGNI, defaultValue: "spalla" }),
            file: fields.image({
              label: "Disegno",
              directory: "public/images/disegni",
              publicPath: "/images/disegni/",
            }),
            alt: testo("Testo alternativo"),
          }),
          { label: "Catalogo", description: "Una voce per segno. I file stanno in public/images/disegni/. Se una patologia ha una Immagine propria, quella vince.", itemLabel: (p) => p.fields.id.value },
        ),
      },
    }),
  },

  collections: {
    patologie: collection({
      label: "Cosa curo",
      slugField: "slug",
      path: "content/patologie/*/",
      format: { contentField: "corpo" },
      entryLayout: "content",
      schema: {
        slug: fields.slug({ name: { label: "Slug IT" } }),
        slugEn: fields.text({ label: "Slug EN", description: "Es. shoulder" }),
        titolo: testo("Titolo", { required: true }),
        area: fields.select({ label: "Area", options: AREE, defaultValue: "spalla" }),
        segno: fields.select({ label: "Segno", options: SEGNI, defaultValue: "spalla" }),
        peso: fields.integer({ label: "Ordine (1 = primo)", defaultValue: 10 }),
        principale: fields.checkbox({ label: "Card grande in home", defaultValue: false }),
        secondaria: fields.checkbox({ label: "Secondaria (riga, non card)", defaultValue: false }),
        lead: testo("Lead", { multiline: true }),
        corpo: fields.markdoc({ label: "Corpo (IT)" }),
        corpoEn: fields.markdoc({ label: "Corpo (EN)" }),
        faq: fields.array(
          fields.object({ domanda: testo("Domanda"), risposta: testo("Risposta", { multiline: true }) }),
          { label: "FAQ", itemLabel: (p) => p.fields.domanda.fields.it.value },
        ),
        sedi: fields.array(fields.relationship({ label: "Sede", collection: "sedi" }), {
          label: "Dove si tratta",
          itemLabel: (p) => p.value ?? "",
        }),
        correlate: fields.array(fields.relationship({ label: "Pagina", collection: "patologie" }), {
          label: "Pagine correlate",
          itemLabel: (p) => p.value ?? "",
        }),
        pubblicazioni: fields.array(fields.relationship({ label: "Paper", collection: "pubblicazioni" }), {
          label: "Pubblicazioni correlate",
          itemLabel: (p) => p.value ?? "",
        }),
        immagine: immagine("Immagine", "patologie"),
        seo,
      },
    }),

    sedi: collection({
      label: "Dove",
      slugField: "slug",
      path: "content/sedi/*",
      format: { data: "yaml" },
      schema: {
        slug: fields.slug({ name: { label: "Slug" } }),
        nome: fields.text({ label: "Nome struttura", validation: { isRequired: true } }),
        citta: fields.text({ label: "Città" }),
        provincia: fields.text({ label: "Provincia (sigla)" }),
        indirizzo: fields.text({ label: "Indirizzo (via e civico)" }),
        cap: fields.text({ label: "CAP" }),
        coordinate: fields.object({
          lat: fields.number({ label: "Latitudine" }),
          lng: fields.number({ label: "Longitudine" }),
        }, { label: "Coordinate" }),
        tipo: fields.select({
          label: "Tipo",
          options: [
            { label: "Ospedale pubblico", value: "ospedale" },
            { label: "Casa di cura", value: "clinica" },
            { label: "Studio / centro medico", value: "studio" },
          ],
          defaultValue: "clinica",
        }),
        propria: fields.checkbox({
          label: "Sede propria (LocalBusiness in JSON-LD)",
          description: "Solo per la sede in cui il titolare è Michele. Non si ostenta nel testo.",
          defaultValue: false,
        }),
        visite: fields.checkbox({ label: "Visite", defaultValue: true }),
        chirurgia: fields.checkbox({ label: "Chirurgia", defaultValue: false }),
        infiltrazioni: fields.checkbox({ label: "Infiltrazioni", defaultValue: true }),
        ecografo: fields.checkbox({ label: "Ecografo in sede (strumento della visita)", defaultValue: false }),
        regime: testo("Regime (una riga)", { description: "Es. «Ricovero e chirurgia in SSN» / «Libera professione»." }),
        ruolo: testo("Cosa faccio qui (paragrafo)", { multiline: true }),
        comeArrivare: testo("Come arrivare", { multiline: true }),
        accessibilita: testo("Accessibilità e parcheggio", { multiline: true }),
        orari: testo("Orari in questa sede", { description: "Vuoto = «su appuntamento»." }),
        peso: fields.integer({ label: "Ordine", defaultValue: 10 }),
        mapsUrl: fields.url({ label: "Link Google Maps" }),
        gbpUrl: fields.url({ label: "Scheda Google (struttura o propria)" }),
        sitoStruttura: fields.url({ label: "Sito della struttura" }),
        foto: fields.array(immagine("Foto", "sedi"), { label: "Foto", itemLabel: (p) => p.fields.alt.fields.it.value || "foto" }),
        patologie: fields.array(fields.relationship({ label: "Pagina", collection: "patologie" }), {
          label: "Patologie tipiche qui",
          itemLabel: (p) => p.value ?? "",
        }),
        seo,
      },
    }),

    pubblicazioni: collection({
      label: "Pubblicazioni",
      slugField: "slug",
      path: "content/pubblicazioni/*",
      format: { data: "yaml" },
      schema: {
        slug: fields.slug({ name: { label: "Slug" } }),
        titolo: fields.text({ label: "Titolo originale", validation: { isRequired: true } }),
        titoloBreve: testo("Titolo breve per il sito"),
        autori: fields.text({ label: "Autori (come in rivista)" }),
        rivista: fields.text({ label: "Rivista" }),
        anno: fields.integer({ label: "Anno", validation: { isRequired: true } }),
        volume: fields.text({ label: "Volume / pagine" }),
        doi: fields.text({ label: "DOI (solo il codice, es. 10.3390/…)" }),
        pubmedId: fields.text({ label: "PubMed ID" }),
        url: fields.url({ label: "Link alternativo alla fonte" }),
        pdf: fields.file({ label: "PDF (solo se lecito)", directory: "public/paper", publicPath: "/paper/" }),
        abstract: fields.text({ label: "Abstract (originale, EN)", multiline: true }),
        riassunto: testo("Riassunto per pazienti", { multiline: true }),
        tag: fields.array(fields.text({ label: "Tag" }), { label: "Tag", itemLabel: (p) => p.value }),
        principale: fields.checkbox({ label: "Tra le principali (CV)", defaultValue: false }),
        patologie: fields.array(fields.relationship({ label: "Pagina", collection: "patologie" }), {
          label: "Patologie correlate",
          itemLabel: (p) => p.value ?? "",
        }),
        pubblicato: fields.checkbox({ label: "Pubblicato", defaultValue: true }),
      },
    }),

    approfondimenti: collection({
      label: "Approfondimenti — Dal lavoro",
      slugField: "slug",
      path: "content/approfondimenti/*/",
      format: { contentField: "corpo" },
      entryLayout: "content",
      schema: {
        slug: fields.slug({ name: { label: "Slug IT" } }),
        slugEn: fields.text({ label: "Slug EN" }),
        titolo: testo("Titolo", { required: true }),
        data: fields.date({ label: "Data", validation: { isRequired: true } }),
        aggiornato: fields.date({ label: "Aggiornato il" }),
        lead: testo("Lead", { multiline: true }),
        copertina: immagine("Immagine in anteprima", "approfondimenti"),
        corpo: fields.markdoc({ label: "Corpo (IT)" }),
        corpoEn: fields.markdoc({ label: "Corpo (EN)" }),
        tag: fields.array(fields.text({ label: "Tag" }), { label: "Tag", itemLabel: (p) => p.value }),
        video: fields.file({
          label: "Video (file)",
          description: "MP4 o WebM. Se c'è anche YouTube, il file ha la precedenza.",
          directory: "public/video/approfondimenti",
          publicPath: "/video/approfondimenti/",
        }),
        youtube: fields.text({
          label: "YouTube",
          description: "URL completo (watch, youtu.be, shorts) oppure solo l'ID del video.",
        }),
        patologie: fields.array(fields.relationship({ label: "Pagina", collection: "patologie" }), {
          label: "Patologie correlate",
          itemLabel: (p) => p.value ?? "",
        }),
        pubblicazioni: fields.array(fields.relationship({ label: "Paper", collection: "pubblicazioni" }), {
          label: "Pubblicazioni correlate",
          itemLabel: (p) => p.value ?? "",
        }),
        pubblicato: fields.checkbox({ label: "Pubblicato", defaultValue: false }),
        seo,
      },
    }),

    faq: collection({
      label: "FAQ generali",
      slugField: "slug",
      path: "content/faq/*",
      format: { data: "yaml" },
      schema: {
        slug: fields.slug({ name: { label: "Slug" } }),
        domanda: testo("Domanda", { required: true }),
        risposta: testo("Risposta", { multiline: true }),
        contesto: fields.select({
          label: "Dove appare",
          options: [
            { label: "Contatti / prima visita", value: "contatti" },
            { label: "Home", value: "home" },
          ],
          defaultValue: "contatti",
        }),
        peso: fields.integer({ label: "Ordine", defaultValue: 10 }),
      },
    }),

    recensioni: collection({
      label: "Recensioni",
      slugField: "slug",
      path: "content/recensioni/*",
      format: { data: "yaml" },
      schema: {
        slug: fields.slug({ name: { label: "Slug" } }),
        nome: fields.text({ label: "Nome e cognome", validation: { isRequired: true } }),
        testo: testo("Testo", { multiline: true }),
        piattaforma: fields.text({ label: "Piattaforma (Google, Doctolib, …)" }),
        stelle: fields.integer({ label: "Stelle (1–5)", defaultValue: 5, validation: { min: 1, max: 5 } }),
        data: fields.date({ label: "Data" }),
        sede: fields.relationship({ label: "Sede", collection: "sedi" }),
        peso: fields.integer({ label: "Ordine in home (più basso = prima)", defaultValue: 10 }),
        mostra: fields.checkbox({ label: "Mostra sul sito", defaultValue: false }),
      },
    }),
  },
});
