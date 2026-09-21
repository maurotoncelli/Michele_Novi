/** Stelle piene/vuote a filo dell'eyebrow. Il numero lo dice lo screen reader, non le icone. */
export function Stelle({ n, su = 5, label, className = "" }: { n: number; su?: number; label: string; className?: string }) {
  const piene = Math.max(0, Math.min(su, Math.round(n)));
  return (
    <span role="img" aria-label={label} className={`inline-flex items-center gap-[2px] align-[-1px] ${className}`}>
      {Array.from({ length: su }, (_, i) => (
        <svg key={i} width="11" height="11" viewBox="0 0 24 24" aria-hidden="true" fill={i < piene ? "currentColor" : "none"} stroke="currentColor" strokeWidth="1.6" strokeLinejoin="round">
          <path d="M12 2.8l2.9 6 6.5.9-4.7 4.5 1.2 6.5L12 17.6l-5.9 3.1 1.2-6.5L2.6 9.7l6.5-.9z" />
        </svg>
      ))}
    </span>
  );
}
