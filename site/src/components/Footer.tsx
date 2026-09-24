import Link from "next/link";
import { href, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import { getSedi, getSettings, telHref } from "@/lib/content";
import { Segno } from "./ui/Segno";
import { Telefono } from "./ui/Telefono";

export async function Footer({ locale }: { locale: Locale }) {
  const [s, sedi] = await Promise.all([getSettings(), getSedi()]);
  const m = getMessages(locale);
  const tel = telHref(s.telefono);
  const social = [
    { nome: "instagram" as const, url: s.instagram, label: "Instagram" },
    { nome: "linkedin" as const, url: s.linkedin, label: "LinkedIn" },
    { nome: "youtube" as const, url: s.youtube, label: "YouTube" },
  ].filter((x) => x.url);
  const orari = pick(s.orari, locale);

  return (
    <footer className="fascia-scura relative border-t border-[var(--color-linea-chiara)]">
      <div className="contenitore grid gap-10 py-14 md:grid-cols-12">
        <div className="md:col-span-5">
          <p className="serif text-2xl">{s.nome}</p>
          <p className="mt-1 text-sm text-osso/60">{pick(s.ruolo, locale)}</p>
          <ul className="mt-6 space-y-2 text-[0.95rem]">
            {tel && (
              <li>
                <a href={tel} className="inline-flex items-center gap-2 hover:text-[var(--color-petrolio-chiaro)]">
                  <Segno nome="telefono" size={18} className="text-osso/45" />
                  <Telefono numero={s.telefono ?? ""} />
                </a>
              </li>
            )}
            {s.email && (
              <li>
                <a href={`mailto:${s.email}`} className="inline-flex items-center gap-2 hover:text-[var(--color-petrolio-chiaro)]">
                  <Segno nome="mail" size={18} className="text-osso/45" />
                  {s.email}
                </a>
              </li>
            )}
            {orari && (
              <li className="flex items-start gap-2 text-osso/60">
                <Segno nome="orologio" size={18} className="mt-0.5 shrink-0 text-osso/45" />
                <span className="whitespace-pre-line">{orari}</span>
              </li>
            )}
          </ul>
          {social.length > 0 && (
            <div className="mt-6">
              <p className="eyebrow">{m.footer.seguimi}</p>
              <ul className="mt-2 flex gap-2">
                {social.map((x) => (
                  <li key={x.nome}>
                    <a
                      href={x.url!}
                      target="_blank"
                      rel="noopener noreferrer me"
                      aria-label={x.label}
                      className="grid h-10 w-10 place-items-center bg-white/[0.06] text-osso/70 transition hover:text-[var(--color-petrolio-chiaro)]"
                    >
                      <Segno nome={x.nome} size={20} />
                    </a>
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>

        <div className="md:col-span-4">
          <p className="eyebrow">{m.footer.sedi}</p>
          <ul className="mt-3 space-y-2">
            {sedi.map((sede) => (
              <li key={sede.slug}>
                <Link href={href(locale, { kind: "dove", slug: sede.slug })} className="group inline-flex items-baseline gap-2 hover:text-[var(--color-petrolio-chiaro)]">
                  <span className="font-medium">{sede.citta}</span>
                  <span className="text-sm text-osso/55 group-hover:text-[var(--color-petrolio-chiaro)]">{sede.nome}</span>
                </Link>
              </li>
            ))}
          </ul>
        </div>

        <div className="md:col-span-3">
          <p className="eyebrow">{m.footer.legale}</p>
          <ul className="mt-3 space-y-2 text-[0.95rem]">
            <li>
              <Link href={href(locale, { kind: "privacy" })} className="hover:text-[var(--color-petrolio-chiaro)]">
                {m.footer.privacy}
              </Link>
            </li>
            <li>
              <Link href={href(locale, { kind: "cookie" })} className="hover:text-[var(--color-petrolio-chiaro)]">
                {m.footer.cookie}
              </Link>
            </li>
          </ul>
          <dl className="mt-6 space-y-1 text-xs text-osso/55">
            {s.piva && (
              <div className="flex gap-2">
                <dt>{m.footer.piva}</dt>
                <dd>{s.piva}</dd>
              </div>
            )}
            {s.albo && (
              <div className="flex gap-2">
                <dt>{m.footer.albo}</dt>
                <dd>{s.albo}</dd>
              </div>
            )}
          </dl>
        </div>
      </div>
      <div className="border-t border-[var(--color-linea-chiara)]">
        <div className="contenitore flex flex-col gap-2 py-5 text-xs text-osso/45 sm:flex-row sm:items-center sm:justify-between">
          <p>
            {`© ${new Date().getFullYear()} ${s.nome}. ${m.footer.diritti}`}
          </p>
          {pick(s.disclaimer, locale) && <p className="max-w-xl sm:text-right">{pick(s.disclaimer, locale)}</p>}
        </div>
      </div>
    </footer>
  );
}
