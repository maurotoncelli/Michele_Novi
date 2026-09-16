# -*- coding: utf-8 -*-
"""
Script per applicare i moduli di incastro magnetico estremo a TUTTE le sezioni
mantenendo al 100% tutti i testi originali della Bibbia.
"""

with open('handoff_sito.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. VIEW-CHI-SONO: MODULO DUE TEMPI INTERATTIVO
chi_search = """<div class="bg-gradient-to-br from-caldo-coralLight to-caldo-goldLight/40 p-6 rounded-3xl border border-caldo-coral/20 space-y-3">
                        <span class="text-xs font-bold text-caldo-coral uppercase tracking-wider block">Due Tempi, Un Medico Solo</span>
                        <p class="text-xs text-caldo-muted leading-relaxed font-light">
                            <strong>La Sala di Volume:</strong> Al CESAT di Fucecchio affronto quotidianamente la chirurgia protesica e artroscopica complessa, forte di una casistica operatoria di rilievo.
                        </p>
                        <p class="text-xs text-caldo-muted leading-relaxed font-light">
                            <strong>Il Territorio:</strong> Negli ambulatori della Valdera e di Pisa ascolto le storie dei pazienti, imposto il percorso e seguo la guarigione passo dopo passo senza intermediari.
                        </p>
                    </div>"""

chi_replace = """<div class="bg-gradient-to-br from-caldo-coralLight to-caldo-goldLight/40 p-6 rounded-3xl border border-caldo-coral/20 space-y-3">
                        <span class="text-xs font-bold text-caldo-coral uppercase tracking-wider block">Due Tempi, Un Medico Solo</span>
                        <p class="text-xs text-caldo-muted leading-relaxed font-light">
                            <strong>La Sala di Volume:</strong> Al CESAT di Fucecchio affronto quotidianamente la chirurgia protesica e artroscopica complessa, forte di una casistica operatoria di rilievo.
                        </p>
                        <p class="text-xs text-caldo-muted leading-relaxed font-light">
                            <strong>Il Territorio:</strong> Negli ambulatori della Valdera e di Pisa ascolto le storie dei pazienti, imposto il percorso e seguo la guarigione passo dopo passo senza intermediari.
                        </p>
                    </div>

                    <!-- MODULO D'INCASTRO BIOLOGICO DEI DUE TEMPI -->
                    <div class="card-soft-gradient p-6 rounded-3xl border border-caldo-borderSoft space-y-4" id="two-tempi-container">
                        <div class="flex items-center justify-between">
                            <span class="text-[11px] font-bold uppercase tracking-wider text-caldo-teal">Sinergia Biomeccanica dei Due Tempi</span>
                            <button type="button" id="btn-toggle-two-tempi" class="text-xs font-semibold px-3 py-1.5 rounded-lg bg-caldo-teal text-white hover:opacity-90 transition-opacity">
                                Sincronizza i Due Tempi
                            </button>
                        </div>
                        <div class="grid sm:grid-cols-2 gap-4 pt-2">
                            <div class="gear-lobe-left bg-white p-5 rounded-2xl border border-caldo-borderSoft space-y-2 relative overflow-hidden">
                                <div class="w-8 h-8 rounded-xl bg-caldo-tealLight text-caldo-teal flex items-center justify-center text-xs font-bold font-mono">01</div>
                                <h4 class="font-serif text-base text-caldo-text font-semibold">Volume Chirurgico Ospedaliero</h4>
                                <p class="text-xs text-caldo-muted font-light leading-relaxed">
                                    Oltre centinaia di interventi/anno al CESAT Fucecchio. Precisione millimetrica su protesica anatomica/inversa e ricostruzioni artroscopiche.
                                </p>
                                <span class="text-[10px] text-caldo-teal font-medium block pt-1">● Presidio di Continuità Operatoria SSN</span>
                            </div>
                            <div class="gear-lobe-right bg-white p-5 rounded-2xl border border-caldo-borderSoft space-y-2 relative overflow-hidden">
                                <div class="w-8 h-8 rounded-xl bg-caldo-coralLight text-caldo-coral flex items-center justify-center text-xs font-bold font-mono">02</div>
                                <h4 class="font-serif text-base text-caldo-text font-semibold">Ascolto & Diagnostica Diffusa</h4>
                                <p class="text-xs text-caldo-muted font-light leading-relaxed">
                                    Presenza a Fucecchio, Peccioli, Fornacette e Pisa. Ecografia muscoloscheletrica SIUMB immediata e tempo dedicato ad ogni paziente.
                                </p>
                                <span class="text-[10px] text-caldo-coral font-medium block pt-1">● Presidio di Prossimità Territoriale</span>
                            </div>
                        </div>
                        <div class="text-center pt-2">
                            <span id="two-tempi-status" class="text-[11px] font-medium text-emerald-700 bg-emerald-50 px-3 py-1 rounded-full border border-emerald-200/60 inline-block">
                                ✓ Incastro Perfetto: La sala operatoria protegge la competenza clinica; l'ambulatorio custodisce la fiducia.
                            </span>
                        </div>
                    </div>"""

if chi_search in text:
    text = text.replace(chi_search, chi_replace)
    print("1. Chi Sono aggiornato")
else:
    print("1. Chi Sono search non trovato")

# 2. VIEW-PATOLOGIE: BIVIO TERAPEUTICO AD INCASTRO
pat_search = """<div class="max-w-3xl mb-16 space-y-4">
                <span class="text-xs font-semibold text-caldo-teal bg-caldo-tealLight px-3.5 py-1.5 rounded-full inline-block">Aree Cliniche</span>
                <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text leading-tight">Cosa curo: 6 percorsi specialistici.</h1>
                <p class="text-base text-caldo-muted font-light leading-relaxed">
                    Dalla diagnosi palpatoria ed ecografica alla chirurgia d'avanguardia: ogni articolazione viene trattata con l'obiettivo del massimo recupero funzionale.
                </p>
            </div>"""

pat_replace = pat_search + """

            <!-- WIDGET BIVIO TERAPEUTICO AD INCASTRO MAGNETICO -->
            <div class="max-w-5xl mx-auto mb-16 p-6 sm:p-8 rounded-3xl card-soft-gradient border border-caldo-borderSoft space-y-6">
                <div class="flex flex-wrap items-center justify-between gap-4">
                    <div>
                        <span class="text-[10px] font-bold uppercase tracking-wider text-caldo-coral block">Metodologia Decisionale</span>
                        <h3 class="font-serif text-2xl text-caldo-text font-semibold">Il Bivio Terapeutico: Criteri di Incastro Clinico</h3>
                        <p class="text-xs text-caldo-muted font-light mt-1">Confronta i parametri che determinano la scelta tra recupero funzionale e intervento chirurgico:</p>
                    </div>
                    <div class="inline-flex p-1 rounded-xl bg-white border border-caldo-borderSoft">
                        <button type="button" id="btn-tab-conservativo" class="px-4 py-2 rounded-lg text-xs font-semibold bg-caldo-teal text-white shadow-xs transition-all">Approccio Conservativo</button>
                        <button type="button" id="btn-tab-chirurgico" class="px-4 py-2 rounded-lg text-xs font-semibold text-caldo-muted hover:text-caldo-text transition-all">Approccio Chirurgico</button>
                    </div>
                </div>

                <div id="bivio-content-box" class="bg-white/90 p-6 rounded-2xl border border-caldo-borderSoft space-y-3">
                    <div class="flex items-center gap-2 text-caldo-teal font-semibold text-sm">
                        <span class="w-2.5 h-2.5 rounded-full bg-caldo-teal"></span>
                        <h4 id="bivio-title">Indicazioni al Trattamento Conservativo</h4>
                    </div>
                    <p id="bivio-desc" class="text-xs text-caldo-muted font-light leading-relaxed">
                        Lesioni parziali della cuffia, primo episodio di instabilità senza difetto osseo critico, artrosi iniziale responsiva a viscosuppletivazione con acido ialuronico ed epicondiliti in fase acuta. Il percorso integra ecografia dinamica, infiltrazioni eco-guidate mirate e fisioterapia personalizzata.
                    </p>
                </div>
            </div>"""

if pat_search in text:
    text = text.replace(pat_search, pat_replace)
    print("2. Patologie Hub aggiornato")
else:
    print("2. Patologie Hub search non trovato")

# 3. VIEW-PATOLOGIE-SPALLA: SIMULATORE FOOTPRINT & CUFFIA
spalla_search = """<h3 class="text-2xl font-serif text-caldo-text font-semibold pt-4">Conservativo vs Chirurgico</h3>"""
spalla_replace = """<!-- SIMULATORE INTERATTIVO DI SUTURA ARTROSCOPICA SUL FOOTPRINT -->
                <div class="bg-white/90 p-6 rounded-3xl border border-caldo-borderSoft space-y-4 my-6" id="cuff-sim-wrapper">
                    <div class="flex flex-wrap items-center justify-between gap-3">
                        <div>
                            <span class="text-[10px] font-bold uppercase tracking-wider text-caldo-coral block">Dimostrazione Biomeccanica</span>
                            <h4 class="font-serif text-base text-caldo-text font-semibold">Riancoraggio del Tendine sul Footprint Osseo</h4>
                        </div>
                        <button type="button" id="btn-toggle-cuff-repair" class="px-3.5 py-1.5 rounded-xl bg-caldo-teal text-white font-medium text-xs shadow-sm hover:opacity-90 transition-all">
                            Esegui Trazione & Sutura
                        </button>
                    </div>

                    <div class="relative bg-caldo-bg p-5 rounded-2xl border border-caldo-borderSoft overflow-hidden">
                        <div class="flex justify-between text-[11px] font-mono text-caldo-muted mb-3">
                            <span>[TESTA OMERALE / FOOTPRINT]</span>
                            <span>[TENDINE SOVRASPINATO]</span>
                        </div>

                        <div class="flex items-center justify-between h-14 relative px-4 bg-white/70 rounded-xl border border-caldo-borderSoft">
                            <!-- Footprint con alloggiamento ancore -->
                            <div class="flex items-center gap-3">
                                <div class="w-8 h-8 rounded-lg bg-caldo-borderSoft flex items-center justify-center suture-anchor-point" title="Ancora riassorbibile mediale">
                                    <div class="w-2 h-2 rounded-full bg-caldo-coral"></div>
                                </div>
                                <div class="w-8 h-8 rounded-lg bg-caldo-borderSoft flex items-center justify-center suture-anchor-point" title="Ancora riassorbibile laterale">
                                    <div class="w-2 h-2 rounded-full bg-caldo-coral"></div>
                                </div>
                                <span class="text-[11px] font-semibold text-caldo-text">Footprint Denudato</span>
                            </div>

                            <!-- Tendine mobile -->
                            <div class="tendon-strip px-4 py-2 rounded-lg bg-caldo-coral text-white text-xs font-semibold shadow-sm flex items-center gap-2 cursor-pointer">
                                <span>Tendine Sovraspinato</span>
                                <span class="text-[10px] opacity-80 font-mono">→</span>
                            </div>
                        </div>

                        <div class="flex items-center justify-between pt-3 text-[11px] text-caldo-muted">
                            <span id="cuff-sim-stat">Stato lesione: <strong>Retrazione tendinea Patte 2 (Spazio libero 12mm)</strong></span>
                            <span class="text-caldo-teal font-medium">Tecnica: SpeedBridge™ suture bridge</span>
                        </div>
                    </div>
                </div>

                <h3 class="text-2xl font-serif text-caldo-text font-semibold pt-4">Conservativo vs Chirurgico</h3>"""

if spalla_search in text:
    text = text.replace(spalla_search, spalla_replace)
    print("3. Spalla aggiornata")
else:
    print("3. Spalla search non trovato")

# 4. VIEW-PATOLOGIE-GOMITO: CERNIERA A COMPASSO
gomito_search = """<div class="p-6 rounded-3xl bg-white border border-caldo-border space-y-3 text-sm">
                    <p><strong>Epicondilite resistente:</strong> trattamento conservativo con infiltrazioni ecoguidate e, nei casi cronici ribelli, release mininvasivo.</p>
                    <p><strong>Fratture del capitello radiale:</strong> sintesi con micro-viti o sostituzione con endoprotesi nei traumi comminuti.</p>
                    <p><strong>Rottura del bicipite distale:</strong> reinserzione anatomica del tendine con bottoni di sospensione corticali e viti a interferenza.</p>
                    <p><strong>Rigidità articolare:</strong> artrolisi artroscopica per asportare osteofiti o corpi mobili e restituire l'escursione articolare.</p>
                </div>"""

gomito_replace = gomito_search + """

                <!-- WIDGET CERNIERA BIOMECCANICA DEL GOMITO -->
                <div class="card-soft-gradient p-6 sm:p-8 rounded-3xl border border-caldo-borderSoft space-y-4 my-6">
                    <div class="flex flex-wrap items-center justify-between gap-4">
                        <div>
                            <span class="text-[10px] font-bold uppercase tracking-wider text-caldo-teal block">Cinematica Articolare del Gomito</span>
                            <h4 class="font-serif text-xl text-caldo-text font-semibold">La Cerniera a Compasso (Troclea e Capitello)</h4>
                        </div>
                        <div class="flex items-center gap-2">
                            <label for="elbow-angle-slider" class="text-xs text-caldo-muted font-light">Angolo:</label>
                            <span id="elbow-angle-value" class="text-xs font-mono font-bold text-caldo-teal bg-white px-2 py-1 rounded border border-caldo-borderSoft">90° (Posizione Funzionale)</span>
                        </div>
                    </div>

                    <div class="bg-white/80 p-5 rounded-2xl border border-caldo-borderSoft space-y-3">
                        <input type="range" id="elbow-angle-slider" min="0" max="145" value="90" class="w-full accent-caldo-teal cursor-pointer">
                        <div class="flex justify-between text-[11px] text-caldo-muted font-light">
                            <span>0° Estensione Totale (Olecrano in fossa)</span>
                            <span>90° Punto di Congruenza Ideale</span>
                            <span>145° Flessione Completa (Recesso anteriore)</span>
                        </div>
                        <p id="elbow-kinetic-desc" class="text-xs text-caldo-muted font-light pt-2 border-t border-caldo-borderSoft/60">
                            A 90°, l'omero e l'ulna formano il perfetto angolo di riposo per i flessori ed estensori dell'avambraccio.
                        </p>
                    </div>
                </div>"""

if gomito_search in text:
    text = text.replace(gomito_search, gomito_replace)
    print("4. Gomito aggiornato")
else:
    print("4. Gomito search non trovato")

# 5. VIEW-PATOLOGIE-MANO: DECOMPRESSIONE TUNNEL CARPALE
mano_search = """<div class="p-6 rounded-3xl bg-white border border-caldo-border space-y-3 text-sm">
                    <p><strong>Sindrome del Tunnel Carpale:</strong> neurolisi e sezione del legamento trasverso del carpo in anestesia locale con immediata scomparsa del formicolio notturno.</p>
                    <p><strong>Dito a scatto e Morbo di De Quervain:</strong> puleggiotomia mininvasiva o tenolisi per liberare i tendini intrappolati nelle guaine fibrose.</p>
                    <p><strong>Rizoartrosi (artrosi del pollice):</strong> trapeziectomia e tenosospensione biologica o impianto di protesi trapezio-metacarpale per ripristinare la presa e la pinza.</p>
                </div>"""

mano_replace = mano_search + """

                <!-- SEZIONE ANATOMICA INTERATTIVA TUNNEL CARPALE -->
                <div class="card-soft-gradient p-6 sm:p-8 rounded-3xl border border-caldo-borderSoft space-y-4 my-6" id="carpal-decompression-wrapper">
                    <div class="flex flex-wrap items-center justify-between gap-3">
                        <div>
                            <span class="text-[10px] font-bold uppercase tracking-wider text-caldo-coral block">Microchirurgia Mininvasiva</span>
                            <h4 class="font-serif text-xl text-caldo-text font-semibold">Sezione Anatomica della Decompressione del Nervo Mediano</h4>
                        </div>
                        <button type="button" id="btn-toggle-carpal" class="px-3.5 py-1.5 rounded-xl bg-caldo-coral text-white font-medium text-xs shadow-sm hover:opacity-90 transition-all">
                            Simula Decompressione Mininvasiva
                        </button>
                    </div>

                    <div class="bg-white/90 p-5 rounded-2xl border border-caldo-borderSoft space-y-4">
                        <div class="h-24 relative flex items-center justify-center bg-caldo-bg rounded-xl border border-caldo-borderSoft overflow-hidden">
                            <!-- Legamento trasverso del carpo sopra -->
                            <div class="transverse-ligament absolute top-2 w-3/4 h-3 rounded-full bg-caldo-coral border border-caldo-coral flex items-center justify-center text-[9px] text-white font-semibold">
                                Legamento Trasverso del Carpo
                            </div>
                            <!-- Nervo mediano al centro -->
                            <div class="carpal-nerve-expanded w-16 h-8 rounded-full bg-amber-200 border border-amber-400 flex items-center justify-center text-[10px] font-bold text-amber-900 shadow-sm">
                                Nervo Mediano
                            </div>
                            <!-- Base dell'arco carpale sotto -->
                            <div class="absolute bottom-2 w-5/6 h-2 rounded-full bg-caldo-borderSoft"></div>
                        </div>
                        <div class="flex items-center justify-between text-xs text-caldo-muted font-light">
                            <span id="carpal-status-text">Stato canale: <strong>Compressione ischemica del nervo mediano (Formicolio notturno)</strong></span>
                            <span class="text-caldo-teal font-medium">Incisione: 1.5 cm nel solco palmare</span>
                        </div>
                    </div>
                </div>"""

if mano_search in text:
    text = text.replace(mano_search, mano_replace)
    print("5. Mano aggiornata")
else:
    print("5. Mano search non trovato")

# 6. VIEW-PATOLOGIE-SPORT: COCKPIT RETURN TO PLAY
sport_search = """<div class="p-6 rounded-3xl bg-white border border-caldo-border space-y-3 text-sm">
                    <p><strong>Lussazioni acromion-claveari:</strong> stabilizzazione biologica con legamenti sintetici o ancore nei traumi da caduta in bici, moto o sci.</p>
                    <p><strong>Spalla del lanciatore e dello scalatore:</strong> diagnosi di lesioni SLAP (cercine superiore) e impingement interno postero-superiore.</p>
                    <p><strong>Return to play test:</strong> protocolli condivisi con i fisioterapisti per misurare forza, stabilità e assenza di apprensione prima della ripresa agonistica.</p>
                </div>"""

sport_replace = sport_search + """

                <!-- COCKPIT DI CONGRUENZA RETURN TO PLAY -->
                <div class="card-soft-gradient p-6 sm:p-8 rounded-3xl border border-caldo-borderSoft space-y-4 my-6" id="rtp-cockpit">
                    <div class="flex flex-wrap items-center justify-between gap-3">
                        <div>
                            <span class="text-[10px] font-bold uppercase tracking-wider text-caldo-teal block">Protocollo Athletica Pisa</span>
                            <h4 class="font-serif text-xl text-caldo-text font-semibold">Cockpit di Congruenza Return-to-Play</h4>
                            <p class="text-xs text-caldo-muted font-light mt-1">Clicca sui 3 requisiti per verificare l'incastro dei criteri di idoneità agonistica:</p>
                        </div>
                        <span id="rtp-final-status" class="px-3 py-1.5 rounded-full text-xs font-semibold bg-amber-50 text-amber-800 border border-amber-200">
                            In attesa di validazione (0/3)
                        </span>
                    </div>

                    <div class="grid sm:grid-cols-3 gap-4">
                        <button type="button" class="rtp-checkpoint-btn p-4 rounded-2xl bg-white border border-caldo-borderSoft text-left space-y-2 hover:border-caldo-teal transition-all" data-criterion="1">
                            <div class="flex justify-between items-center">
                                <span class="text-xs font-mono font-bold text-caldo-teal">01. MOBILITÀ</span>
                                <span class="rtp-chk-icon text-xs text-caldo-muted">○</span>
                            </div>
                            <h5 class="font-serif text-sm text-caldo-text font-semibold">ROM Attivo Completo</h5>
                            <p class="text-[11px] text-caldo-muted font-light leading-relaxed">Elevazione e rotazione esterna > 95% rispetto al controlaterale sano.</p>
                        </button>

                        <button type="button" class="rtp-checkpoint-btn p-4 rounded-2xl bg-white border border-caldo-borderSoft text-left space-y-2 hover:border-caldo-teal transition-all" data-criterion="2">
                            <div class="flex justify-between items-center">
                                <span class="text-xs font-mono font-bold text-caldo-teal">02. FORZA</span>
                                <span class="rtp-chk-icon text-xs text-caldo-muted">○</span>
                            </div>
                            <h5 class="font-serif text-sm text-caldo-text font-semibold">Simmetria Isocinetica</h5>
                            <p class="text-[11px] text-caldo-muted font-light leading-relaxed">Deficit di forza inferiore al 10% nei test dinamometrici selettivi.</p>
                        </button>

                        <button type="button" class="rtp-checkpoint-btn p-4 rounded-2xl bg-white border border-caldo-borderSoft text-left space-y-2 hover:border-caldo-teal transition-all" data-criterion="3">
                            <div class="flex justify-between items-center">
                                <span class="text-xs font-mono font-bold text-caldo-teal">03. GESTO</span>
                                <span class="rtp-chk-icon text-xs text-caldo-muted">○</span>
                            </div>
                            <h5 class="font-serif text-sm text-caldo-text font-semibold">Test Gesto Specifico</h5>
                            <p class="text-[11px] text-caldo-muted font-light leading-relaxed">Assenza di apprensione nel gesto di lancio o impatto in caduta.</p>
                        </button>
                    </div>
                </div>"""

if sport_search in text:
    text = text.replace(sport_search, sport_replace)
    print("6. Traumatologia Sportiva aggiornata")
else:
    print("6. Traumatologia Sportiva search non trovato")

# 7. VIEW-PATOLOGIE-ARTROSCOPIA: VARCO OTTICO
artro_search = """<div class="p-6 rounded-3xl bg-white border border-caldo-border space-y-3 text-sm">
                    <p><strong>Visione diretta ingrandita:</strong> permette di rilevare lesioni cartilaginee o tendinee non sempre evidenti nemmeno con la risonanza magnetica.</p>
                    <p><strong>Rispetto anatomico totale:</strong> i muscoli circostanti non vengono sezionati o staccati dall'osso, riducendo drasticamente il dolore post-operatorio.</p>
                    <p><strong>Recupero accelerato:</strong> dimissione tipicamente in day-hospital o con una sola notte di degenza, con inizio precoce della fisioterapia passiva.</p>
                </div>"""

artro_replace = artro_search + """

                <!-- VARCO OTTICO ARTROSCOPICO DEI DUE PORTALI -->
                <div class="card-soft-gradient p-6 rounded-3xl border border-caldo-borderSoft space-y-4 my-6">
                    <div class="flex justify-between items-center">
                        <span class="text-[10px] font-bold uppercase tracking-wider text-caldo-teal">Triangolazione Artroscopica a 2 Portali</span>
                        <span class="text-xs font-mono text-caldo-coral font-medium">Accessi Minimi da 4 mm</span>
                    </div>
                    <div class="bg-white/90 p-5 rounded-2xl border border-caldo-borderSoft flex items-center justify-around text-center">
                        <div class="space-y-1">
                            <div class="w-10 h-10 mx-auto rounded-full bg-caldo-tealLight text-caldo-teal flex items-center justify-center font-bold text-sm">👁️</div>
                            <strong class="text-xs text-caldo-text block">Portale Posteriore</strong>
                            <span class="text-[10px] text-caldo-muted block">Ottica 30° Full HD 4K</span>
                        </div>
                        <div class="text-xs text-caldo-coral font-mono px-3 py-1 rounded-full bg-caldo-coralLight border border-caldo-coral/30">
                            Convergenza a 45° sul Cercine
                        </div>
                        <div class="space-y-1">
                            <div class="w-10 h-10 mx-auto rounded-full bg-caldo-coralLight text-caldo-coral flex items-center justify-center font-bold text-sm">🛠️</div>
                            <strong class="text-xs text-caldo-text block">Portale Anteriore</strong>
                            <span class="text-[10px] text-caldo-muted block">Sonde a Radiofrequenza e Ancore</span>
                        </div>
                    </div>
                    <p class="text-xs text-caldo-muted font-light text-center">
                        La triangolazione dei due portali evita qualsiasi incisione dei ventri muscolari del deltoide, consentendo l'immediata mobilitazione post-operatoria.
                    </p>
                </div>"""

if artro_search in text:
    text = text.replace(artro_search, artro_replace)
    print("7. Artroscopia aggiornata")
else:
    print("7. Artroscopia search non trovato")

# 8. VIEW-PATOLOGIE-ECOGRAFIA: SONDA DINAMICA
eco_search = """<div class="p-6 rounded-3xl bg-white border border-caldo-border space-y-3 text-sm">
                    <p><strong>Diagnostica dinamica in tempo reale:</strong> possiamo osservare i tendini mentre il paziente muove la spalla o il gomito, individuando conflitti o scatti che le immagini statiche non possono mostrare.</p>
                    <p><strong>Infiltrazioni eco-guidate:</strong> l'ago viene visualizzato sullo schermo in ogni istante, garantendo che l'acido ialuronico, il cortisonico o i derivati biologici vengano depositati esattamente all'interno della borsa o dello spazio articolare bersaglio.</p>
                    <p><strong>Nessuna attesa:</strong> ecografia eseguita contestualmente alla visita specialistica negli ambulatori provvisti di strumentazione dedicata.</p>
                </div>"""

eco_replace = eco_search + """

                <!-- FINESTRA DINAMICA CUTE / SONDA ECOGRAFICA SIUMB -->
                <div class="card-soft-gradient p-6 rounded-3xl border border-caldo-borderSoft space-y-4 my-6">
                    <div class="flex justify-between items-center">
                        <span class="text-[10px] font-bold uppercase tracking-wider text-caldo-coral">Diagnostica Dinamica SIUMB in Studio</span>
                        <span class="text-xs font-semibold text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-full border border-emerald-200">Visione Strato per Strato</span>
                    </div>
                    <div class="grid sm:grid-cols-3 gap-3 text-xs">
                        <div class="bg-white p-4 rounded-xl border border-caldo-borderSoft space-y-1">
                            <strong class="text-caldo-text block">1. Cute & Sottocute</strong>
                            <p class="text-[11px] text-caldo-muted font-light">Contatto diretto della sonda lineare ad alta frequenza (12-18 MHz).</p>
                        </div>
                        <div class="bg-white p-4 rounded-xl border border-caldo-borderSoft space-y-1">
                            <strong class="text-caldo-coral block">2. Borsa Sottoacromiale</strong>
                            <p class="text-[11px] text-caldo-muted font-light">Spazio virtuale di scorrimento: sede elettiva per infiltrazione antinfiammatoria.</p>
                        </div>
                        <div class="bg-white p-4 rounded-xl border border-caldo-borderSoft space-y-1">
                            <strong class="text-caldo-teal block">3. Tendine Sovraspinato</strong>
                            <p class="text-[11px] text-caldo-muted font-light">Ecotessitura fibrillare parallela: verifica immediata di fessurazioni o calcificazioni.</p>
                        </div>
                    </div>
                </div>"""

if eco_search in text:
    text = text.replace(eco_search, eco_replace)
    print("8. Ecografia aggiornata")
else:
    print("8. Ecografia search non trovato")

# 9. VIEW-SEDI: DOCKING TERRITORIALE
sedi_search = """<div class="max-w-3xl mb-16 space-y-4">
                <span class="text-xs font-semibold text-caldo-teal bg-caldo-tealLight px-3.5 py-1.5 rounded-full inline-block">Presidio Sanitario in Toscana</span>
                <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text leading-tight">Dove ricevo: le strutture attive.</h1>
                <p class="text-base text-caldo-muted font-light leading-relaxed">
                    Tutti gli interventi chirurgici e i ricoveri ospedalieri si svolgono presso l'Ospedale CESAT di Fucecchio. Le prime visite, i controlli e le infiltrazioni sono distribuiti su 4 sedi territoriali.
                </p>
            </div>"""

sedi_replace = sedi_search + """

            <!-- CONSOLE INTERATTIVA DOCKING DELLE STRUTTURE -->
            <div class="mb-12 p-6 rounded-3xl bg-white/90 border border-caldo-borderSoft shadow-sm flex flex-wrap items-center justify-between gap-4">
                <div class="flex items-center gap-3">
                    <span class="w-3 h-3 rounded-full bg-emerald-500 animate-pulse"></span>
                    <span class="text-xs font-semibold text-caldo-text">Navigazione Rapida Sedi sul Territorio:</span>
                    <span class="text-xs text-caldo-muted font-light">Seleziona per focalizzare la scheda operativa</span>
                </div>
                <div class="flex flex-wrap gap-2">
                    <a href="#view-sedi" onclick="document.querySelectorAll('.card-soft-gradient')[0].scrollIntoView({behavior:'smooth'});" class="px-3 py-1.5 rounded-xl bg-caldo-tealLight text-caldo-teal font-semibold text-xs border border-caldo-teal/20 hover:bg-caldo-teal hover:text-white transition-all">CESAT Ospedale (Chirurgia SSN)</a>
                    <a href="#view-sedi" onclick="document.querySelectorAll('.card-soft-gradient')[1].scrollIntoView({behavior:'smooth'});" class="px-3 py-1.5 rounded-xl bg-caldo-tealLight text-caldo-teal font-semibold text-xs border border-caldo-teal/20 hover:bg-caldo-teal hover:text-white transition-all">Studi San Pietro (Ambulatorio)</a>
                    <a href="#view-sedi" onclick="document.querySelectorAll('.card-soft-gradient')[2].scrollIntoView({behavior:'smooth'});" class="px-3 py-1.5 rounded-xl bg-caldo-coralLight text-caldo-coral font-semibold text-xs border border-caldo-coral/20 hover:bg-caldo-coral hover:text-white transition-all">Polo San Verano (Peccioli)</a>
                    <a href="#view-sedi" onclick="document.querySelectorAll('.card-soft-gradient')[3].scrollIntoView({behavior:'smooth'});" class="px-3 py-1.5 rounded-xl bg-caldo-salviaLight text-caldo-salvia font-semibold text-xs border border-caldo-salvia/20 hover:bg-caldo-salvia hover:text-white transition-all">Pisa & Fornacette</a>
                </div>
            </div>"""

if sedi_search in text:
    text = text.replace(sedi_search, sedi_replace)
    print("9. Sedi aggiornate")
else:
    print("9. Sedi search non trovato")

# 10. JS HANDLER AGGIUNTIVO PER IL BIVIO TERAPEUTICO IN PATOLOGIE
extra_bivio_js = """
        // GESTIONE BIVIO TERAPEUTICO IN PATOLOGIE
        const btnConservativo = document.getElementById('btn-tab-conservativo');
        const btnChirurgico = document.getElementById('btn-tab-chirurgico');
        const bivioTitle = document.getElementById('bivio-title');
        const bivioDesc = document.getElementById('bivio-desc');

        if (btnConservativo && btnChirurgico && bivioTitle && bivioDesc) {
            btnConservativo.addEventListener('click', () => {
                btnConservativo.className = 'px-4 py-2 rounded-lg text-xs font-semibold bg-caldo-teal text-white shadow-xs transition-all';
                btnChirurgico.className = 'px-4 py-2 rounded-lg text-xs font-semibold text-caldo-muted hover:text-caldo-text transition-all';
                bivioTitle.textContent = 'Indicazioni al Trattamento Conservativo';
                bivioDesc.textContent = 'Lesioni parziali della cuffia, primo episodio di instabilità senza difetto osseo critico, artrosi iniziale responsiva a viscosuppletivazione con acido ialuronico ed epicondiliti in fase acuta. Il percorso integra ecografia dinamica, infiltrazioni eco-guidate mirate e fisioterapia personalizzata.';
            });
            btnChirurgico.addEventListener('click', () => {
                btnChirurgico.className = 'px-4 py-2 rounded-lg text-xs font-semibold bg-caldo-coral text-white shadow-xs transition-all';
                btnConservativo.className = 'px-4 py-2 rounded-lg text-xs font-semibold text-caldo-muted hover:text-caldo-text transition-all';
                bivioTitle.textContent = 'Indicazioni al Trattamento Chirurgico Mininvasivo';
                bivioDesc.textContent = 'Lesioni a tutto spessore retratte con deficit funzionale resistente, instabilità con lesione di Hill-Sachs / Bankart recidivante, artrosi eccentrica severa candidata a protesi inversa al CESAT, e compressioni nervose con deficit motorio (tunnel carpale avanzato).';
            });
        }
"""

if "GESTIONE BIVIO TERAPEUTICO IN PATOLOGIE" not in text:
    text = text.replace("</script>\n</body>", extra_bivio_js + "\n    </script>\n</body>")
    print("10. JS Bivio inserito")

# Scrittura su file
with open('handoff_sito.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('Proposte HTML/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Scrittura completata con successo su entrambi i file HTML!")
