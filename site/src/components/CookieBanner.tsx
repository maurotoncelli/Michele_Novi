"use client";

import Link from "next/link";
import Script from "next/script";
import { useEffect, useSyncExternalStore } from "react";

const KEY = "mn_consenso";
const EVENT = "mn-consenso";
type Stato = "si" | "no" | "boot" | "";

declare global {
  interface Window {
    dataLayer?: unknown[];
    gtag?: (...args: unknown[]) => void;
  }
}

function subscribe(cb: () => void) {
  window.addEventListener(EVENT, cb);
  window.addEventListener("storage", cb);
  return () => {
    window.removeEventListener(EVENT, cb);
    window.removeEventListener("storage", cb);
  };
}
const leggi = (): Stato => (window.localStorage.getItem(KEY) as Stato | null) ?? "";
export const scegliConsensoCookie = (v: "si" | "no" | "") => {
  if (v === "") {
    window.localStorage.removeItem(KEY);
  } else {
    window.localStorage.setItem(KEY, v);
  }
  window.dispatchEvent(new Event(EVENT));
};

/** Invia un evento a GA4 solo se l'utente ha espresso il consenso statistico e gtag è attivo. */
export function tracciaEvento(nome: string, params?: Record<string, string | number | boolean>) {
  if (typeof window === "undefined") return;
  if (window.localStorage.getItem(KEY) !== "si") return;
  window.gtag?.("event", nome, params ?? {});
}

/** Pulsante da inserire nella Cookie Policy per riaprire il banner e modificare/revocare il consenso. */
export function BottonePreferenzeCookie({ label }: { label: string }) {
  return (
    <button
      type="button"
      onClick={() => scegliConsensoCookie("")}
      className="btn btn-osso mt-6 !min-h-10 !py-2 text-sm"
    >
      {label}
    </button>
  );
}

/**
 * Banner cookie + GA4 + tracciamento conversioni (`click_call`, `click_whatsapp`, `click_maps`, `form_submit`).
 * GA4 parte esclusivamente dopo il consenso (`stato === "si"`) e se `gaId` (`NEXT_PUBLIC_GA_ID`) è configurato.
 */
export function CookieBanner({
  gaId,
  testo,
  accetta,
  rifiuta,
  cookieHref,
  cookieLabel,
}: {
  gaId?: string;
  testo: string;
  accetta: string;
  rifiuta: string;
  cookieHref: string;
  cookieLabel: string;
}) {
  const stato = useSyncExternalStore(subscribe, leggi, () => "boot" as Stato);

  useEffect(() => {
    if (stato !== "si" || !gaId) return;
    const onClick = (e: MouseEvent) => {
      const a = (e.target as HTMLElement | null)?.closest?.("a");
      if (!a) return;
      const h = a.getAttribute("href") ?? "";
      if (h.startsWith("tel:")) {
        tracciaEvento("click_call", { link_url: h });
      } else if (h.includes("wa.me") || h.includes("whatsapp.com")) {
        tracciaEvento("click_whatsapp", { link_url: h });
      } else if (h.includes("google.com/maps")) {
        tracciaEvento("click_maps", { link_url: h });
      }
    };
    document.addEventListener("click", onClick);
    return () => document.removeEventListener("click", onClick);
  }, [stato, gaId]);

  return (
    <>
      {stato === "si" && gaId && (
        <>
          <Script src={`https://www.googletagmanager.com/gtag/js?id=${gaId}`} strategy="afterInteractive" />
          <Script id="ga4" strategy="afterInteractive">
            {`window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}window.gtag=gtag;gtag('js',new Date());gtag('config','${gaId}',{anonymize_ip:true});`}
          </Script>
        </>
      )}
      {stato === "" && (
        <div
          role="dialog"
          aria-live="polite"
          aria-label={cookieLabel}
          className="fixed inset-x-3 bottom-3 z-[70] sm:bottom-5 sm:left-auto sm:right-5 sm:w-[27rem]"
        >
          <div className="border border-linea bg-osso p-5 shadow-osso sm:p-6">
            <p className="text-[0.92rem] leading-relaxed text-inchiostro">
              {testo}{" "}
              <Link href={cookieHref} className="text-petrolio underline decoration-1 underline-offset-3 hover:text-profondo">
                {cookieLabel}
              </Link>
            </p>
            <div className="mt-4 flex flex-wrap gap-2">
              <button type="button" onClick={() => scegliConsensoCookie("si")} className="btn btn-petrolio !min-h-10 !px-4 !py-2 text-sm">
                {accetta}
              </button>
              <button type="button" onClick={() => scegliConsensoCookie("no")} className="btn btn-osso !min-h-10 !px-4 !py-2 text-sm">
                {rifiuta}
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}
