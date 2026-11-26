/** Riga autori "come in rivista" → elenco di nomi. */
export function elencoAutori(autori: string | null | undefined): string[] {
  return (autori ?? "")
    .split(",")
    .map((a) => a.trim())
    .filter(Boolean);
}

const esc = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

/**
 * Riconosce il titolare del sito dentro una riga autori, nelle forme in cui le riviste lo scrivono:
 * "Michele Novi", "M. Novi", "M Novi", "Novi M", "Novi M.". Il nome arriva da `profilo.nome`.
 */
export function riconosciTitolare(nomeCompleto: string | null | undefined): (autore: string) => boolean {
  const nome = (nomeCompleto ?? "").trim();
  const parti = nome.split(/\s+/).filter(Boolean);
  if (parti.length < 2) return () => false;
  const cognome = esc(parti[parti.length - 1]);
  const iniziale = esc(parti[0][0]);
  const re = new RegExp(`^(?:${parti.map(esc).join("\\s+")}|${iniziale}\\.?\\s+${cognome}|${cognome}\\s+${iniziale}\\.?)$`, "i");
  return (autore) => re.test(autore.trim());
}
