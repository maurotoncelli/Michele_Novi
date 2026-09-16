"use client";

import Link from "next/link";
import Script from "next/script";
import { useSyncExternalStore } from "react";

const KEY = "mn_consenso";
const EVENT = "mn-consenso";
type Stato = "si" | "no" | "boot" | "";

function subscribe(cb: () => void) {
  window.addEventListener(EVENT, cb);
  window.addEventListener("storage", cb);
  return () => {
    window.removeEventListener(EVENT, cb);
    window.removeEventListener("storage", cb);
  };
}
const leggi = (): Stato => (window.localStorage.getItem(KEY) as Stato | null) ?? "";
const scegli = (v: "si" | "no") => {
  window.localStorage.setItem(KEY, v);
  window.dispatchEvent(new Event(EVENT));
};

/**
 * Banner cookie + GA4. Si monta solo se NEXT_PUBLIC_GA_ID esiste.
 * GA parte esclusivamente dopo il consenso. Stato letto da localStorage via store esterno
 * (niente setState in effect, niente mismatch di idratazione: sul server è "boot").
 */
export function CookieBanner({ gaId, testo, accetta, rifiuta, cookieHref, cookieLabel }: {
  gaId: string;
  testo: string;
  accetta: string;
  rifiuta: string;
  cookieHref: string;
  cookieLabel: string;
}) {
  const stato = useSyncExternalStore(subscribe, leggi, () => "boot" as Stato);

  return (
    <>
      {stato === "si" && (
        <>
          <Script src={`https://www.googletagmanager.com/gtag/js?id=${gaId}`} strategy="afterInteractive" />
          <Script id="ga4" strategy="afterInteractive">
            {`window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','${gaId}',{anonymize_ip:true});`}
          </Script>
        </>
      )}
      {stato === "" && (
        <div role="dialog" aria-live="polite" aria-label={cookieLabel} className="fixed inset-x-3 bottom-3 z-[70] sm:bottom-5 sm:left-auto sm:right-5 sm:w-[26rem]">
          <div className="vetro osso p-4 sm:p-5">
            <p className="text-sm text-inchiostro">
              {testo}{" "}
              <Link href={cookieHref} className="underline decoration-1 underline-offset-2 hover:text-petrolio">
                {cookieLabel}
              </Link>
            </p>
            <div className="mt-3 flex gap-2">
              <button type="button" onClick={() => scegli("si")} className="btn btn-petrolio !min-h-10 !py-2 text-sm">
                {accetta}
              </button>
              <button type="button" onClick={() => scegli("no")} className="btn btn-osso !min-h-10 !py-2 text-sm">
                {rifiuta}
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}
