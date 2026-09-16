import os

filepath = "/Volumes/Programs/Temporary files/Progetti cursor/Michele_Novi_Website/Proposte HTML/index.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

missing_views = """
        <!-- === DETTAGLI MANCANTI PATOLOGIE === -->
        <section id="view-patologie-sport" class="page-view py-32 px-6 max-w-[50rem] mx-auto observer-trigger">
            <a href="#patologie" class="accent-line text-[10px] font-mono uppercase tracking-widest mb-12 block w-max">← Torna ad Aree di trattamento</a>
            <h1 class="text-fluid-h2 font-serif mb-8">Traumatologia <span class="italic text-medical-accent">sportiva.</span></h1>
            <div class="text-lg font-light leading-relaxed text-medical-text space-y-6">
                <p>La gestione del trauma sportivo richiede non solo la riparazione del danno anatomico, ma una pianificazione precisa per il "Return to Play".</p>
                <ul class="list-disc pl-5 space-y-3 text-base">
                    <li>Lussazioni acromion-claveari e sternoclaveari.</li>
                    <li>Lesioni acute dei tendini della spalla e del bicipite brachiale.</li>
                    <li>Instabilità nel lanciatore (overhead athlete).</li>
                </ul>
            </div>
        </section>

        <section id="view-patologie-artroscopia" class="page-view py-32 px-6 max-w-[50rem] mx-auto observer-trigger">
            <a href="#patologie" class="accent-line text-[10px] font-mono uppercase tracking-widest mb-12 block w-max">← Torna ad Aree di trattamento</a>
            <span class="text-[10px] font-mono uppercase tracking-widest text-medical-accent bg-medical-surface px-2 py-0.5 rounded block w-max mb-4">Filosofia / Metodo</span>
            <h1 class="text-fluid-h2 font-serif mb-8">Chirurgia <span class="italic text-medical-accent">artroscopica.</span></h1>
            <div class="text-lg font-light leading-relaxed text-medical-text space-y-6">
                <p>L'artroscopia rappresenta il varco mini-invasivo per l'esplorazione e il trattamento delle patologie articolari.</p>
                <p>Attraverso incisioni di pochi millimetri, utilizzando ottiche ad altissima definizione, è possibile riparare tendini e legamenti con il minimo impatto sui tessuti sani, garantendo un recupero più rapido e meno doloroso rispetto alle tecniche a cielo aperto tradizionali.</p>
            </div>
        </section>

        <section id="view-patologie-ecografia" class="page-view py-32 px-6 max-w-[50rem] mx-auto observer-trigger">
            <a href="#patologie" class="accent-line text-[10px] font-mono uppercase tracking-widest mb-12 block w-max">← Torna ad Aree di trattamento</a>
            <span class="text-[10px] font-mono uppercase tracking-widest text-medical-accent bg-medical-surface px-2 py-0.5 rounded block w-max mb-4">Filosofia / Metodo</span>
            <h1 class="text-fluid-h2 font-serif mb-8">Ecografia <span class="italic text-medical-accent">muscoloscheletrica.</span></h1>
            <div class="text-lg font-light leading-relaxed text-medical-text space-y-6">
                <p>Essendo in possesso del diploma nazionale SIUMB in ecografia muscoloscheletrica, utilizzo la sonda ecografica come diretta estensione della visita clinica.</p>
                <p>Questo permette non solo una diagnosi immediata e dinamica in ambulatorio, ma anche l'esecuzione di procedure infiltrative mirate (ecoguidate) con precisione millimetrica.</p>
            </div>
        </section>

        <!-- === DETTAGLI MANCANTI SEDI === -->
        <section id="view-sedi-fucecchio" class="page-view py-32 px-6 max-w-[50rem] mx-auto observer-trigger">
            <a href="#sedi" class="accent-line text-[10px] font-mono uppercase tracking-widest mb-12 block w-max">← Torna alle Strutture</a>
            <span class="text-[10px] font-mono uppercase tracking-widest text-medical-accent bg-medical-surface px-2 py-0.5 rounded block w-max mb-4">Polo Ambulatoriale</span>
            <h1 class="text-fluid-h2 font-serif mb-4">Studi Medici <span class="italic text-medical-accent">San Pietro.</span></h1>
            <p class="text-[10px] font-mono text-medical-muted mb-8">Piazza S. Lavagnini 6, Fucecchio (FI)</p>
            <div class="text-lg font-light leading-relaxed text-medical-text space-y-6 border-t border-medical-border pt-8">
                <p>Situati strategicamente di fronte all'Ospedale CESAT, gli Studi Medici San Pietro costituiscono il polo di riferimento per l'attività ambulatoriale a Fucecchio.</p>
                <p>Qui si svolgono le prime visite specialistiche, la pianificazione degli interventi chirurgici, e il follow-up post-operatorio avanzato.</p>
            </div>
        </section>
        
        <section id="view-sedi-peccioli" class="page-view py-32 px-6 max-w-[50rem] mx-auto observer-trigger">
            <a href="#sedi" class="accent-line text-[10px] font-mono uppercase tracking-widest mb-12 block w-max">← Torna alle Strutture</a>
            <span class="text-[10px] font-mono uppercase tracking-widest text-medical-accent bg-medical-surface px-2 py-0.5 rounded block w-max mb-4">Polo Ambulatoriale</span>
            <h1 class="text-fluid-h2 font-serif mb-4">Centro Medico <span class="italic text-medical-accent">San Verano.</span></h1>
            <p class="text-[10px] font-mono text-medical-muted mb-8">Viale Cavour 13, Peccioli (PI)</p>
            <div class="text-lg font-light leading-relaxed text-medical-text space-y-6 border-t border-medical-border pt-8">
                <p>Il Centro San Verano è il punto di riferimento per i pazienti della Valdera. Presso questa struttura vengono erogate visite ortopediche specialistiche con il supporto diretto della diagnostica ecografica in sede.</p>
            </div>
        </section>

        <section id="view-sedi-pisa" class="page-view py-32 px-6 max-w-[50rem] mx-auto observer-trigger">
            <a href="#sedi" class="accent-line text-[10px] font-mono uppercase tracking-widest mb-12 block w-max">← Torna alle Strutture</a>
            <span class="text-[10px] font-mono uppercase tracking-widest text-medical-accent bg-medical-surface px-2 py-0.5 rounded block w-max mb-4">Polo Ambulatoriale</span>
            <h1 class="text-fluid-h2 font-serif mb-4">Centro <span class="italic text-medical-accent">Athletica.</span></h1>
            <p class="text-[10px] font-mono text-medical-muted mb-8">Pisa (PI)</p>
            <div class="text-lg font-light leading-relaxed text-medical-text space-y-6 border-t border-medical-border pt-8">
                <p>Presso il centro Athletica a Pisa, l'attività clinica si concentra prevalentemente sul recupero funzionale dell'atleta e sulla traumatologia sportiva, offrendo percorsi di cura sinergici tra l'ortopedico e l'équipe riabilitativa.</p>
            </div>
        </section>

        <!-- === DETTAGLI MANCANTI NOTE CLINICHE === -->
        <section id="view-note-cuffia" class="page-view py-32 px-6 max-w-[50rem] mx-auto observer-trigger">
            <a href="#note-cliniche" class="accent-line text-[10px] font-mono uppercase tracking-widest mb-12 block w-max">← Torna al Quaderno</a>
            <div class="text-[10px] font-mono uppercase tracking-widest text-medical-muted mb-4 block">Nota su Cuffia dei Rotatori · Data: 01 Set 2026</div>
            <h1 class="text-fluid-h2 font-serif mb-12">Cuffia irreparabile: <span class="italic text-medical-accent">oltre l'illusione della sutura.</span></h1>
            
            <div class="text-lg font-light leading-relaxed text-medical-text space-y-6">
                <p>Una lesione della cuffia dei rotatori viene definita "irreparabile" quando la retrazione del tendine e l'infiltrazione adiposa del muscolo superano un punto di non ritorno biologico e meccanico.</p>
                <p>In passato, l'accanimento chirurgico nel tentare di suturare questi tessuti ha spesso portato a fallimenti strutturali (re-tear) entro i primi 6 mesi.</p>
                
                <h3 class="text-2xl font-serif mt-8 mb-4">Le alternative moderne</h3>
                <p>Oggi la chirurgia della spalla offre soluzioni molto più avanzate e ritagliate sull'età e sulle richieste funzionali del paziente:</p>
                <ul class="list-disc pl-5 space-y-3 text-base">
                    <li><strong>Protesi Inversa di Spalla:</strong> Per i pazienti più anziani in cui coesiste artrosi (artropatia da rottura di cuffia), la protesi inversa inverte la biomeccanica articolare restituendo l'elevazione del braccio, pur senza i tendini naturali.</li>
                    <li><strong>Ricostruzione della Capsula Superiore (SCR):</strong> L'utilizzo di innesti biologici per ripristinare il tetto articolare nei pazienti più giovani senza artrosi.</li>
                    <li><strong>Trasferimenti Tendinei:</strong> Tecniche come il transfer del gran dorsale o del trapezio inferiore per ripristinare le rotazioni perdute.</li>
                </ul>
            </div>
        </section>
"""

new_content = content.replace('</main>', missing_views + '\n    </main>')

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Aggiunte tutte le pagine di dettaglio mancanti.")
