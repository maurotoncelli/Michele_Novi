/** Inietta JSON-LD generato dai dati. Mai numeri scritti a mano qui. */
export function JsonLd({ data }: { data: unknown | unknown[] | null }) {
  if (!data) return null;
  const list = Array.isArray(data) ? data.filter(Boolean) : [data];
  return (
    <>
      {list.map((d, i) => (
        <script
          key={i}
          type="application/ld+json"
          // JSON.stringify con escaping di "<" per sicurezza
          dangerouslySetInnerHTML={{ __html: JSON.stringify(d).replace(/</g, "\\u003c") }}
        />
      ))}
    </>
  );
}
