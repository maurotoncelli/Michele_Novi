import { NextResponse, type NextRequest } from "next/server";
import { Resend } from "resend";
import { getSede, getSettings } from "@/lib/content";

/**
 * Form contatti → email alla segreteria. Nessun dato salvato.
 * Honeypot + rate limit in memoria (best effort; Vercel è stateless).
 */
const finestre = new Map<string, number[]>();
const LIMITE = 5;
const FINESTRA_MS = 10 * 60 * 1000;

function troppi(ip: string) {
  const ora = Date.now();
  const arr = (finestre.get(ip) ?? []).filter((t) => ora - t < FINESTRA_MS);
  arr.push(ora);
  finestre.set(ip, arr);
  return arr.length > LIMITE;
}

const pulisci = (v: FormDataEntryValue | null, max = 500) =>
  typeof v === "string" ? v.replace(/[\r\n]+/g, " ").trim().slice(0, max) : "";

export async function POST(req: NextRequest) {
  const ip = req.headers.get("x-forwarded-for")?.split(",")[0]?.trim() ?? "anon";
  if (troppi(ip)) return NextResponse.json({ ok: false }, { status: 429 });

  const fd = await req.formData();
  if (pulisci(fd.get("sito"))) return NextResponse.json({ ok: true }); // bot: fingiamo successo

  const nome = pulisci(fd.get("nome"), 120);
  const recapito = pulisci(fd.get("recapito"), 160);
  const sedeSlug = pulisci(fd.get("sede"), 60);
  const messaggio = typeof fd.get("messaggio") === "string" ? String(fd.get("messaggio")).trim().slice(0, 600) : "";
  const consenso = fd.get("consenso") === "on";
  const locale = pulisci(fd.get("locale"), 2) || "it";

  if (!nome || !recapito || !consenso) return NextResponse.json({ ok: false }, { status: 400 });

  const settings = await getSettings();
  const sede = sedeSlug ? await getSede(sedeSlug) : null;
  const to = settings.emailDestinazioneForm || settings.email;
  const key = process.env.RESEND_API_KEY;

  const righe = [
    `Nome: ${nome}`,
    `Recapito: ${recapito}`,
    `Sede preferita: ${sede ? `${sede.nome} (${sede.citta})` : "qualsiasi"}`,
    `Lingua: ${locale}`,
    "",
    messaggio ? `Messaggio:\n${messaggio}` : "(nessun messaggio)",
    "",
    `Consenso privacy: sì — ${new Date().toISOString()}`,
  ].join("\n");

  if (!to || !key) {
    // Ambiente senza email configurata: non perdere la richiesta nei log di build/dev
    console.info("[contatto] email non configurata, richiesta:\n" + righe);
    return NextResponse.json({ ok: true, inviato: false });
  }

  try {
    const resend = new Resend(key);
    await resend.emails.send({
      from: process.env.RESEND_FROM ?? "Sito <onboarding@resend.dev>",
      to,
      replyTo: recapito.includes("@") ? recapito : undefined,
      subject: `Richiesta di contatto dal sito — ${nome}`,
      text: righe,
    });
    return NextResponse.json({ ok: true, inviato: true });
  } catch (e) {
    console.error("[contatto] invio fallito", e);
    return NextResponse.json({ ok: false }, { status: 502 });
  }
}
