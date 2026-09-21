"use client";

import Link from "next/link";
import { useState, type FormEvent } from "react";
import { Segno } from "./ui/Segno";

export type ContactFormLabels = {
  nome: string;
  recapito: string;
  sede: string;
  sedeQualsiasi: string;
  messaggio: string;
  consenso: string;
  invia: string;
  invio: string;
  grazie: string;
  errore: string;
  obbligatorio: string;
  privacy: string;
};

export function ContactForm({
  locale,
  sedi,
  labels,
  privacyHref,
}: {
  locale: string;
  sedi: { slug: string; nome: string; citta: string }[];
  labels: ContactFormLabels;
  privacyHref: string;
}) {
  const [stato, setStato] = useState<"idle" | "busy" | "ok" | "err">("idle");

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const form = e.currentTarget;
    if (!form.reportValidity()) return;
    setStato("busy");
    const fd = new FormData(form);
    fd.set("locale", locale);
    try {
      const res = await fetch("/api/contatto", { method: "POST", body: fd });
      if (!res.ok) throw new Error(String(res.status));
      setStato("ok");
      form.reset();
    } catch {
      setStato("err");
    }
  }

  if (stato === "ok") {
    return (
      <div role="status" className="osso flex items-start gap-3 p-6">
        <span className="incavo grid h-10 w-10 shrink-0 place-items-center text-petrolio">
          <Segno nome="check" size={20} />
        </span>
        <p className="pt-2 text-[1.05rem]">{labels.grazie}</p>
      </div>
    );
  }

  const campo = "w-full border border-linea bg-osso px-4 py-3 text-[0.98rem] placeholder:text-nebbia focus:border-petrolio";

  return (
    <form onSubmit={onSubmit} noValidate className="space-y-4" aria-busy={stato === "busy"}>
      {/* honeypot */}
      <div className="absolute -left-[9999px] top-auto h-px w-px overflow-hidden" aria-hidden="true">
        <label>
          Sito web <input type="text" name="sito" tabIndex={-1} autoComplete="off" />
        </label>
      </div>
      <div className="grid gap-4 sm:grid-cols-2">
        <label className="block">
          <span className="mb-1.5 block text-sm font-medium">{labels.nome}</span>
          <input name="nome" required autoComplete="name" className={campo} />
        </label>
        <label className="block">
          <span className="mb-1.5 block text-sm font-medium">{labels.recapito}</span>
          <input name="recapito" required autoComplete="email tel" className={campo} />
        </label>
      </div>
      <label className="block">
        <span className="mb-1.5 block text-sm font-medium">{labels.sede}</span>
        <select name="sede" className={campo} defaultValue="">
          <option value="">{labels.sedeQualsiasi}</option>
          {sedi.map((s) => (
            <option key={s.slug} value={s.slug}>
              {s.citta} — {s.nome}
            </option>
          ))}
        </select>
      </label>
      <label className="block">
        <span className="mb-1.5 block text-sm font-medium">{labels.messaggio}</span>
        <textarea name="messaggio" rows={3} maxLength={600} className={campo} />
      </label>
      <label className="flex items-start gap-3 text-sm text-grafite">
        <input type="checkbox" name="consenso" required className="mt-1 h-4 w-4 accent-petrolio" />
        <span>
          {labels.consenso}{" "}
          <Link href={privacyHref} className="underline underline-offset-2 hover:text-petrolio">
            {labels.privacy}
          </Link>
        </span>
      </label>
      <div className="flex flex-wrap items-center gap-3">
        <button type="submit" disabled={stato === "busy"} className="btn btn-petrolio disabled:opacity-60">
          <Segno nome="mail" size={18} />
          {stato === "busy" ? labels.invio : labels.invia}
        </button>
        {stato === "err" && (
          <p role="alert" className="text-sm text-rame">
            {labels.errore}
          </p>
        )}
      </div>
    </form>
  );
}
