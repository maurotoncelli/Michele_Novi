import { notFound } from "next/navigation";

/** Qualsiasi percorso non previsto sotto /[locale] → 404 con il layout del sito. Rotta dinamica, mai prerenderizzata. */
export const dynamic = "force-dynamic";

export default function CatchAll() {
  notFound();
}
