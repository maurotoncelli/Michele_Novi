out_dir = '/Volumes/Programs/Temporary files/Progetti cursor/Michele_Novi_Website/Proposte HTML'
# -*- coding: utf-8 -*-
import os

html_head = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dott. Michele Novi | Ortopedico spalla e arto superiore</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500&family=Manrope:wght@300;400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,200;0,6..72,300;0,6..72,400;0,6..72,500;1,6..72,200;1,6..72,300;1,6..72,400&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        medical: { bg: '#FFFFFF', surface: '#F8F9FA', border: '#EAEAEA', text: '#111111', muted: '#6B7280', accent: '#006775' }
                    },
                    fontFamily: { serif: ['Newsreader', 'serif'], sans: ['Manrope', 'sans-serif'], mono: ['JetBrains Mono', 'monospace'] }
                }
            }
        }
    </script>
    <style>
        :root { --ease-out: cubic-bezier(0.215, 0.61, 0.355, 1); --ease-varco: cubic-bezier(0.77, 0, 0.175, 1); }
        body { background-color: #FFFFFF; color: #111111; font-family: 'Manrope', sans-serif; overflow-x: hidden; scroll-behavior: smooth; }
        .grid-osso { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: -1; display: flex; justify-content: center; }
        .grid-osso-inner { width: 100%; max-width: 80rem; height: 100%; display: grid; grid-template-columns: repeat(4, 1fr); border-left: 1px solid var(--medical-border); border-right: 1px solid var(--medical-border); opacity: 0.4; }
        .grid-osso-inner div { border-right: 1px solid var(--medical-border); }
        .grid-osso-inner div:last-child { border-right: none; }
        
        .varco-mask { clip-path: inset(35% 25% 35% 25%); transition: clip-path 1.8s var(--ease-varco); will-change: clip-path; }
        .varco-img { transform: scale(1.4); filter: grayscale(100%) contrast(1.1); transition: transform 2.5s var(--ease-out), filter 2s var(--ease-out); will-change: transform, filter; }
        .is-loaded .varco-mask { clip-path: inset(0% 0% 0% 0%); }
        .is-loaded .varco-img { transform: scale(1); filter: grayscale(15%) contrast(1.05); }
        
        .mask-text { overflow: hidden; display: block; }
        .mask-text-inner { display: inline-block; transform: translateY(110%); transition: transform 1s var(--ease-out); will-change: transform; }
        .reveal-fade { opacity: 0; transform: translateY(20px); transition: opacity 1s var(--ease-out), transform 1s var(--ease-out); }
        .is-visible .mask-text-inner { transform: translateY(0); }
        .is-visible.reveal-fade, .is-visible .reveal-fade { opacity: 1; transform: translateY(0); }
        .d-1 { transition-delay: 0.1s; } .d-2 { transition-delay: 0.2s; } .d-3 { transition-delay: 0.3s; }
        
        .card-congruenza { transition: border-color 0.4s var(--ease-out); }
        .card-congruenza:hover { border-color: var(--medical-accent); }
        
        .btn-mag { position: relative; overflow: hidden; border: 1px solid var(--medical-accent); color: var(--medical-accent); background: transparent; transition: color 0.4s var(--ease-out); z-index: 1; display: inline-block; text-align: center; }
        .btn-mag::after { content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 0%; background: var(--medical-accent); z-index: -1; transition: height 0.4s var(--ease-varco); }
        .btn-mag:hover { color: #fff; } .btn-mag:hover::after { height: 100%; }
        .btn-mag-solid { background: var(--medical-accent); color: #fff; }
        .btn-mag-solid::after { background: #111111; }
        
        .text-fluid-hero { font-size: clamp(3rem, 7vw, 7rem); line-height: 0.95; letter-spacing: -0.02em; }
        .text-fluid-h2 { font-size: clamp(2.5rem, 5vw, 4.5rem); line-height: 1; letter-spacing: -0.01em; }
        .text-fluid-h3 { font-size: clamp(1.5rem, 3vw, 2.5rem); line-height: 1.1; }
        
        .nav-link { position: relative; }
        .nav-link::after { content: ''; position: absolute; bottom: 0; left: 0; width: 0%; height: 1px; background: currentColor; transition: width 0.3s var(--ease-out); }
        .nav-link:hover::after, .nav-link.active-link::after { width: 100%; }
        .accent-line { display: inline-block; border-bottom: 1px solid var(--medical-accent); color: var(--medical-text); transition: color 0.3s var(--ease-out); }
        .accent-line:hover { color: var(--medical-accent); }
        
        /* Layout Quaderno per Articoli */
        .row-quaderno { position: relative; transition: padding-left 0.4s var(--ease-out); }
        .row-quaderno::before { content: ''; position: absolute; left: -20px; top: 0; width: 0%; height: 100%; background: var(--medical-surface); z-index: -1; transition: width 0.5s var(--ease-varco), left 0.5s var(--ease-varco); }
        .row-quaderno:hover { padding-left: 20px; }
        .row-quaderno:hover::before { left: 0; width: 100%; }
        .row-quaderno .titolo-articolo { transition: color 0.4s var(--ease-out); }
        .row-quaderno:hover .titolo-articolo { color: var(--medical-accent); font-style: italic; }

        .page-view { display: none; opacity: 0; }
        .page-view.active-view { display: block; animation: viewEnter 0.6s var(--ease-varco) forwards; }
        @keyframes viewEnter { 0% { opacity: 0; transform: translateY(20px); } 100% { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body class="selection:bg-medical-accent selection:text-white">

    <div class="grid-osso hidden md:flex"><div class="grid-osso-inner"><div></div><div></div><div></div><div></div></div></div>

    <header class="fixed top-0 w-full z-50 bg-white/90 backdrop-blur-md border-b border-medical-border transition-transform duration-500" id="main-header">
        <div class="max-w-[80rem] mx-auto px-6 h-20 flex justify-between items-center">
            <a href="#home" class="group flex flex-col cursor-pointer overflow-hidden nav-target" data-target="home">
                <span class="text-xl font-serif tracking-tight text-medical-text transition-colors">Dott. Michele Novi</span>
                <span class="text-[10px] uppercase tracking-widest text-medical-muted font-mono mt-0.5">Ortopedico Spalla e Arto Superiore</span>
            </a>
            <nav class="hidden lg:flex items-center gap-10 text-[11px] font-mono uppercase tracking-widest text-medical-text">
                <a href="#chi-sono" class="nav-link py-2 nav-target" data-target="chi-sono">Chi sono</a>
                <a href="#patologie" class="nav-link py-2 nav-target" data-target="patologie">Cosa curo</a>
                <a href="#sedi" class="nav-link py-2 nav-target" data-target="sedi">Dove ricevo</a>
                <a href="#note-cliniche" class="nav-link py-2 nav-target" data-target="note-cliniche">Note cliniche</a>
            </nav>
            <div class="hidden sm:flex items-center gap-4">
                <a href="#contatti" class="btn-mag-solid px-6 py-2.5 rounded-full text-[11px] font-mono uppercase tracking-widest transition-all nav-target" data-target="contatti">Chiama</a>
            </div>
        </div>
    </header>

    <main class="pt-20" id="app-root">
"""

html_views = """
        <!-- ================= HOME ================= -->
        <section id="view-home" class="page-view active-view">
            <div class="relative min-h-[calc(100vh-5rem)] flex flex-col justify-center px-6 max-w-[80rem] mx-auto pt-10 pb-20">
                <div class="grid lg:grid-cols-12 gap-12 items-center h-full">
                    <div class="lg:col-span-7 z-10 space-y-8 observer-trigger">
                        <div class="mask-text"><span class="mask-text-inner text-[10px] font-mono uppercase tracking-widest text-medical-text border border-medical-border px-3 py-1 rounded-full">Ospedale CESAT Fucecchio · Studi in Toscana</span></div>
                        <h1 class="text-fluid-hero font-serif text-medical-text">
                            <div class="mask-text"><span class="mask-text-inner">Chirurgo</span></div>
                            <div class="mask-text"><span class="mask-text-inner d-1 italic text-medical-accent">ortopedico.</span></div>
                            <div class="mask-text"><span class="mask-text-inner d-2">Spalla e</span></div>
                            <div class="mask-text"><span class="mask-text-inner d-3 text-medical-muted">arto superiore.</span></div>
                        </h1>
                        <div class="mask-text">
                            <p class="mask-text-inner d-3 text-base md:text-lg font-light leading-relaxed text-medical-text max-w-md">Ortopedico traumatologo, chirurgia della spalla e dell'arto superiore, artroscopica e protesica.</p>
                        </div>
                        <div class="reveal-fade d-3 flex gap-4 pt-4">
                            <a href="#contatti" class="btn-mag px-8 py-3.5 rounded-full text-[11px] font-mono uppercase tracking-widest text-center">Contatta la segreteria</a>
                            <a href="#sedi" class="btn-mag px-8 py-3.5 rounded-full text-[11px] font-mono uppercase tracking-widest text-center !border-medical-border !text-medical-text hover:!text-white hover:!border-medical-text before:!bg-medical-text">Dove ricevo</a>
                        </div>
                    </div>
                    <div class="lg:col-span-5 h-[60vh] lg:h-[80vh] relative observer-trigger">
                        <div class="w-full h-full varco-mask overflow-hidden absolute inset-0 bg-medical-surface">
                            <img src="https://images.unsplash.com/photo-1551076805-e1869043e560?q=80&w=1200&auto=format&fit=crop" class="w-full h-full object-cover object-center varco-img" alt="Chirurgia spalla artroscopica">
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="border-y border-medical-border px-6 observer-trigger">
                <div class="max-w-[80rem] mx-auto grid grid-cols-2 md:grid-cols-4 divide-x divide-medical-border">
                    <div class="py-10 px-4 reveal-fade"><div class="text-fluid-h3 font-serif text-medical-text">CESAT Fucecchio</div><div class="text-[10px] font-mono uppercase tracking-widest text-medical-muted mt-2">Polo Chirurgico d'Eccellenza</div></div>
                    <div class="py-10 px-6 reveal-fade d-1"><div class="text-fluid-h3 font-serif text-medical-text">Formazione</div><div class="text-[10px] font-mono uppercase tracking-widest text-medical-muted mt-2">Università di Pisa</div></div>
                    <div class="py-10 px-6 reveal-fade d-2"><div class="text-fluid-h3 font-serif text-medical-text">Fellowship</div><div class="text-[10px] font-mono uppercase tracking-widest text-medical-muted mt-2">Londra · Seattle · Berlino</div></div>
                    <div class="py-10 px-6 reveal-fade d-3"><div class="text-fluid-h3 font-serif text-medical-text">Porcellini</div><div class="text-[10px] font-mono uppercase tracking-widest text-medical-muted mt-2">Scuola di specializzazione</div></div>
                </div>
            </div>
            
            <section class="py-32 px-6 max-w-[80rem] mx-auto observer-trigger text-center">
                <h2 class="text-fluid-h2 font-serif mb-12">Percorsi <span class="italic text-medical-accent">clinici.</span></h2>
                <div class="flex flex-col sm:flex-row justify-center gap-8 reveal-fade">
                    <a href="#patologie" class="accent-line text-[11px] font-mono uppercase tracking-widest pb-1">Esplora le Patologie</a>
                    <a href="#sedi" class="accent-line text-[11px] font-mono uppercase tracking-widest pb-1">Scopri le Strutture</a>
                    <a href="#note-cliniche" class="accent-line text-[11px] font-mono uppercase tracking-widest pb-1">Leggi il Quaderno</a>
                </div>
            </section>
        </section>

        <!-- ================= CHI SONO ================= -->
        <section id="view-chi-sono" class="page-view py-32 px-6 max-w-[80rem] mx-auto observer-trigger">
            <div class="grid lg:grid-cols-12 gap-16 items-start">
                <div class="lg:col-span-4 reveal-fade">
                    <div class="aspect-[3/4] overflow-hidden border border-medical-border bg-medical-surface relative">
                        <img src="https://images.unsplash.com/photo-1622253692010-333f2da6031d?q=80&w=800&auto=format&fit=crop" class="w-full h-full object-cover filter grayscale-[15%]" alt="Dott. Michele Novi">
                    </div>
                    <div class="mt-6">
                        <h2 class="text-2xl font-serif text-medical-text">Dott. Michele Novi</h2>
                        <p class="text-[10px] font-mono text-medical-muted mt-2">Ordine dei Medici di Pisa n. 5988</p>
                    </div>
                </div>
                <div class="lg:col-span-8 space-y-16">
                    <div class="reveal-fade d-1">
                        <div class="mask-text"><span class="mask-text-inner text-[10px] font-mono uppercase tracking-widest text-medical-muted mb-4 block">Profilo Clinico</span></div>
                        <h1 class="text-fluid-h2 font-serif mb-8">Rigore clinico,<br><span class="italic text-medical-accent">precisione chirurgica.</span></h1>
                        <div class="text-lg font-light leading-relaxed text-medical-text space-y-6">
                            <p>Sono un chirurgo ortopedico specializzato esclusivamente nella patologia della spalla e dell'arto superiore. La mia pratica clinica si divide tra l'attività ambulatoriale sul territorio (Pisa, Fucecchio, Peccioli) e la chirurgia di alto volume presso il CESAT (Centro di Eccellenza per la Sostituzione Articolare) dell'Ospedale San Pietro Igneo di Fucecchio.</p>
                            <p>Il mio approccio unisce il massimo rispetto biologico dei tessuti, garantito dalla chirurgia artroscopica mini-invasiva, al recupero funzionale completo tramite la chirurgia protesica avanzata.</p>
                        </div>
                    </div>
                    <div class="border-t border-medical-border pt-12 reveal-fade d-2">
                        <h3 class="text-2xl font-serif text-medical-text mb-8">Esperienza e Formazione</h3>
                        <div class="space-y-8">
                            <div class="grid md:grid-cols-4 gap-4"><div class="text-[10px] font-mono text-medical-muted">2021 — OGGI</div><div class="md:col-span-3"><h4 class="text-lg font-serif text-medical-text">Chirurgo Ortopedico</h4><p class="text-sm font-light text-medical-muted mt-1">CESAT – Ospedale San Pietro Igneo, Fucecchio.</p></div></div>
                            <div class="grid md:grid-cols-4 gap-4"><div class="text-[10px] font-mono text-medical-muted">2020 — 2021</div><div class="md:col-span-3"><h4 class="text-lg font-serif text-medical-text">Research Fellow (Spalla e Arto Superiore)</h4><p class="text-sm font-light text-medical-muted mt-1">UNIMORE / AOU Modena – Scuola Prof. Porcellini e Catani.</p></div></div>
                            <div class="grid md:grid-cols-4 gap-4"><div class="text-[10px] font-mono text-medical-muted">2013 — 2018</div><div class="md:col-span-3"><h4 class="text-lg font-serif text-medical-text">Specializzazione in Ortopedia e Traumatologia</h4><p class="text-sm font-light text-medical-muted mt-1">Università di Pisa. Voto: 110/110 e Lode. Tesi sulle ancorette all-suture nella lesione di Bankart.</p></div></div>
                        </div>
                    </div>
                    <div class="border-t border-medical-border pt-12 reveal-fade d-3">
                        <h3 class="text-2xl font-serif text-medical-text mb-8">Fellowship Internazionali</h3>
                        <ul class="space-y-4 text-sm font-light text-medical-text">
                            <li class="flex items-start gap-4"><span class="text-medical-accent font-mono mt-1">→</span><div><strong>Charité, Berlino (2017)</strong> – Chirurgia spalla e gomito (Prof. Scheibel).</div></li>
                            <li class="flex items-start gap-4"><span class="text-medical-accent font-mono mt-1">→</span><div><strong>University of Washington / Harborview, Seattle (2015)</strong> – Chirurgia mano e microchirurgia.</div></li>
                            <li class="flex items-start gap-4"><span class="text-medical-accent font-mono mt-1">→</span><div><strong>RNOH Stanmore, Londra (2011)</strong> – Chirurgia del nervo periferico.</div></li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- ================= HUB PATOLOGIE ================= -->
        <section id="view-patologie" class="page-view py-32 px-6 max-w-[80rem] mx-auto observer-trigger">
            <div class="text-center mb-20 reveal-fade">
                <div class="mask-text"><span class="mask-text-inner text-[10px] font-mono uppercase tracking-widest text-medical-muted mb-4 block">Aree di trattamento</span></div>
                <h1 class="text-fluid-h2 font-serif">Cosa <span class="italic text-medical-accent">curo.</span></h1>
            </div>
            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                <a href="#patologie-spalla" class="card-congruenza block border border-medical-border p-8 reveal-fade bg-white group">
                    <h3 class="text-2xl font-serif mb-3">Spalla</h3><p class="text-sm font-light text-medical-muted leading-relaxed">Cuffia dei rotatori, instabilità, lussazioni, protesica.</p>
                </a>
                <a href="#patologie-gomito-mano" class="card-congruenza block border border-medical-border p-8 reveal-fade d-1 bg-white group">
                    <h3 class="text-2xl font-serif mb-3">Gomito, Mano e Polso</h3><p class="text-sm font-light text-medical-muted leading-relaxed">Epicondilite, tunnel carpale, rizoartrosi, dita a scatto.</p>
                </a>
                <a href="#patologie-sport" class="card-congruenza block border border-medical-border p-8 reveal-fade d-2 bg-white group">
                    <h3 class="text-2xl font-serif mb-3">Traumatologia Sportiva</h3><p class="text-sm font-light text-medical-muted leading-relaxed">Lesioni legamentose, return to sport, lussazioni.</p>
                </a>
                <a href="#patologie-artroscopia" class="card-congruenza block border border-medical-border p-8 reveal-fade bg-medical-surface group">
                    <span class="text-[10px] font-mono uppercase tracking-widest text-medical-accent mb-2 block">Metodo</span><h3 class="text-2xl font-serif mb-3">Artroscopia</h3><p class="text-sm font-light text-medical-muted leading-relaxed">Il varco mini-invasivo e il rispetto biologico.</p>
                </a>
                <a href="#patologie-ecografia" class="card-congruenza block border border-medical-border p-8 reveal-fade d-1 bg-medical-surface group">
                    <span class="text-[10px] font-mono uppercase tracking-widest text-medical-accent mb-2 block">Metodo</span><h3 class="text-2xl font-serif mb-3">Ecografia MSK</h3><p class="text-sm font-light text-medical-muted leading-relaxed">Diagnostica e interventistica in ambulatorio.</p>
                </a>
            </div>
        </section>

        <!-- === DETTAGLI PATOLOGIE === -->
        <section id="view-patologie-spalla" class="page-view py-32 px-6 max-w-[50rem] mx-auto observer-trigger">
            <a href="#patologie" class="accent-line text-[10px] font-mono uppercase tracking-widest mb-12 block w-max">← Torna ad Aree di trattamento</a>
            <h1 class="text-fluid-h2 font-serif mb-8">Chirurgia della <span class="italic text-medical-accent">spalla.</span></h1>
            <div class="text-lg font-light leading-relaxed text-medical-text space-y-6">
                <p>La chirurgia della spalla è il core della mia pratica clinica. Tratto quotidianamente la patologia degenerativa e traumatica di questa articolazione, cercando di bilanciare le migliori opzioni conservative e chirurgiche per restituire la funzionalità perduta.</p>
                <h3 class="text-2xl font-serif mt-12 mb-4">Aree principali di intervento</h3>
                <ul class="list-disc pl-5 space-y-3 text-base">
                    <li><strong>Lesioni della Cuffia dei Rotatori:</strong> Dalla riparazione artroscopica biologica alla gestione delle lesioni irreparabili.</li>
                    <li><strong>Instabilità e Lussazioni:</strong> Tecniche di stabilizzazione (Bankart, Latarjet, Remplissage) per atleti e pazienti attivi.</li>
                    <li><strong>Protesica di spalla:</strong> Sostituzione articolare anatomica e inversa per l'artrosi primaria e le fratture complesse, con approcci computer-assistiti.</li>
                    <li><strong>Patologia calcifica e capsulite adesiva:</strong> Gestione conservativa, ecoguidata e chirurgica.</li>
                </ul>
            </div>
            <div class="mt-16"><a href="#contatti" class="btn-mag px-6 py-3 rounded-full text-[11px] font-mono uppercase tracking-widest">Richiedi un consulto</a></div>
        </section>

        <section id="view-patologie-gomito-mano" class="page-view py-32 px-6 max-w-[50rem] mx-auto observer-trigger">
            <a href="#patologie" class="accent-line text-[10px] font-mono uppercase tracking-widest mb-12 block w-max">← Torna ad Aree di trattamento</a>
            <h1 class="text-fluid-h2 font-serif mb-8">Gomito, mano <span class="italic text-medical-accent">e polso.</span></h1>
            <div class="text-lg font-light leading-relaxed text-medical-text space-y-6">
                <p>Oltre alla spalla, mi dedico alla diagnosi e al trattamento chirurgico e conservativo delle principali patologie dell'arto superiore distale.</p>
                <h3 class="text-2xl font-serif mt-12 mb-4">Trattamenti comuni</h3>
                <ul class="list-disc pl-5 space-y-3 text-base">
                    <li><strong>Gomito:</strong> Epicondilite ed epitrocleite, rigidità articolare, instabilità.</li>
                    <li><strong>Mano e Polso:</strong> Sindrome del tunnel carpale, dita a scatto, malattia di De Quervain, rizoartrosi (artrosi del pollice).</li>
                    <li><strong>Traumatologia complessa:</strong> Fratture dell'arto superiore trattate chirurgicamente.</li>
                </ul>
            </div>
            <div class="mt-16"><a href="#contatti" class="btn-mag px-6 py-3 rounded-full text-[11px] font-mono uppercase tracking-widest">Richiedi un consulto</a></div>
        </section>

        <!-- ================= HUB SEDI ================= -->
        <section id="view-sedi" class="page-view py-32 px-6 max-w-[80rem] mx-auto observer-trigger">
            <div class="text-center mb-20 reveal-fade">
                <div class="mask-text"><span class="mask-text-inner text-[10px] font-mono uppercase tracking-widest text-medical-muted mb-4 block">Le Strutture</span></div>
                <h1 class="text-fluid-h2 font-serif">Dove <span class="italic text-medical-accent">ricevo.</span></h1>
            </div>
            <div class="grid lg:grid-cols-2 gap-6 reveal-fade">
                <a href="#sedi-cesat" class="block border border-medical-border p-8 bg-white hover:border-medical-accent transition-colors group">
                    <span class="text-[10px] font-mono uppercase tracking-widest text-white bg-medical-text px-2 py-0.5 rounded block w-max mb-4">Chirurgia & Ricoveri</span>
                    <h3 class="text-3xl font-serif text-medical-text mb-2 group-hover:text-medical-accent">CESAT Ospedale Fucecchio</h3>
                    <p class="text-sm font-light text-medical-muted mb-6">Polo d'eccellenza per la chirurgia protesica e artroscopica.</p>
                    <div class="text-xs font-mono text-medical-text border-t border-medical-border pt-4">Piazza Spartaco Lavagnini 5, Fucecchio (FI)</div>
                </a>
                <a href="#sedi-fucecchio" class="block border border-medical-border p-8 bg-white hover:border-medical-accent transition-colors group">
                    <span class="text-[10px] font-mono uppercase tracking-widest text-medical-accent mb-4 block">Visite Ambulatoriali</span>
                    <h3 class="text-3xl font-serif text-medical-text mb-2 group-hover:text-medical-accent">Studi Medici San Pietro</h3>
                    <p class="text-sm font-light text-medical-muted mb-6">Attività ambulatoriale per prime visite e controlli.</p>
                    <div class="text-xs font-mono text-medical-text border-t border-medical-border pt-4">Piazza S. Lavagnini 6, Fucecchio (FI)</div>
                </a>
                <a href="#sedi-peccioli" class="block border border-medical-border p-8 bg-white hover:border-medical-accent transition-colors group">
                    <span class="text-[10px] font-mono uppercase tracking-widest text-medical-accent mb-4 block">Visite & Ecografia</span>
                    <h3 class="text-3xl font-serif text-medical-text mb-2 group-hover:text-medical-accent">Centro Medico San Verano</h3>
                    <p class="text-sm font-light text-medical-muted mb-6">Polo ambulatoriale territoriale per visite e screening.</p>
                    <div class="text-xs font-mono text-medical-text border-t border-medical-border pt-4">Viale Cavour 13, Peccioli (PI)</div>
                </a>
                <a href="#sedi-pisa" class="block border border-medical-border p-8 bg-white hover:border-medical-accent transition-colors group">
                    <span class="text-[10px] font-mono uppercase tracking-widest text-medical-accent mb-4 block">Visite</span>
                    <h3 class="text-3xl font-serif text-medical-text mb-2 group-hover:text-medical-accent">Athletica</h3>
                    <p class="text-sm font-light text-medical-muted mb-6">Polo per le visite in libera professione sulla città di Pisa.</p>
                    <div class="text-xs font-mono text-medical-text border-t border-medical-border pt-4">Pisa</div>
                </a>
            </div>
        </section>

        <!-- === DETTAGLI SEDI === -->
        <section id="view-sedi-cesat" class="page-view py-32 px-6 max-w-[50rem] mx-auto observer-trigger">
            <a href="#sedi" class="accent-line text-[10px] font-mono uppercase tracking-widest mb-12 block w-max">← Torna alle Strutture</a>
            <span class="text-[10px] font-mono uppercase tracking-widest text-white bg-medical-text px-2 py-0.5 rounded block w-max mb-4">Ospedale</span>
            <h1 class="text-fluid-h2 font-serif mb-4">CESAT <span class="italic text-medical-accent">Fucecchio.</span></h1>
            <p class="text-[10px] font-mono text-medical-muted mb-8">Piazza Spartaco Lavagnini 5, Fucecchio (FI)</p>
            <div class="text-lg font-light leading-relaxed text-medical-text space-y-6 border-t border-medical-border pt-8">
                <p>Il Centro di Eccellenza per la Sostituzione Articolare (CESAT) fa parte dell'Ospedale San Pietro Igneo di Fucecchio.</p>
                <p>È la sede in cui svolgo la mia attività chirurgica principale di alto volume, sia in regime SSN che in regime di intramoenia, per interventi di protesica (spalla, anca, ginocchio) e artroscopia avanzata.</p>
                <div class="mt-8 p-6 bg-medical-surface border border-medical-border">
                    <strong class="block text-sm font-serif mb-2">Nota sulla prenotazione</strong>
                    <p class="text-sm text-medical-muted">Per la prenotazione chirurgica presso questa struttura, fare riferimento alle indicazioni rilasciate durante la prima visita in ambulatorio.</p>
                </div>
            </div>
        </section>

        <!-- ================= HUB NOTE CLINICHE ================= -->
        <section id="view-note-cliniche" class="page-view py-32 px-6 max-w-[80rem] mx-auto observer-trigger">
            <div class="text-center mb-20">
                <div class="mask-text"><span class="mask-text-inner text-[10px] font-mono uppercase tracking-widest text-medical-muted mb-4 block">Ricerca & Divulgazione</span></div>
                <h1 class="text-fluid-h2 font-serif mx-auto">Note <span class="italic text-medical-accent">cliniche.</span></h1>
            </div>
            <div class="border-t border-medical-border">
                <a href="#note-remplissage" class="row-quaderno block border-b border-medical-border py-10 px-4 reveal-fade">
                    <div class="grid md:grid-cols-12 gap-6 items-center">
                        <div class="md:col-span-3 text-[10px] font-mono text-medical-muted">INSTABILITÀ · 2026</div>
                        <div class="md:col-span-7"><h3 class="titolo-articolo text-3xl font-serif text-medical-text">Il dubbio nel remplissage: stabilità e movimento negli atleti.</h3></div>
                        <div class="md:col-span-2 text-right hidden md:block text-[10px] font-mono text-medical-muted">LEGGI NOTA →</div>
                    </div>
                </a>
                <a href="#note-cuffia" class="row-quaderno block border-b border-medical-border py-10 px-4 reveal-fade d-1">
                    <div class="grid md:grid-cols-12 gap-6 items-center">
                        <div class="md:col-span-3 text-[10px] font-mono text-medical-muted">CUFFIA ROTATORI · 2026</div>
                        <div class="md:col-span-7"><h3 class="titolo-articolo text-3xl font-serif text-medical-text">Cuffia irreparabile: oltre l'illusione della sutura.</h3></div>
                        <div class="md:col-span-2 text-right hidden md:block text-[10px] font-mono text-medical-muted">LEGGI NOTA →</div>
                    </div>
                </a>
            </div>
        </section>

        <!-- === DETTAGLIO NOTA CLINICA === -->
        <section id="view-note-remplissage" class="page-view py-32 px-6 max-w-[50rem] mx-auto observer-trigger">
            <a href="#note-cliniche" class="accent-line text-[10px] font-mono uppercase tracking-widest mb-12 block w-max">← Torna al Quaderno</a>
            <div class="text-[10px] font-mono uppercase tracking-widest text-medical-muted mb-4 block">Nota su Instabilità · Data: 12 Nov 2026</div>
            <h1 class="text-fluid-h2 font-serif mb-12">Il dubbio nel remplissage: <span class="italic text-medical-accent">stabilità e movimento.</span></h1>
            
            <div class="text-lg font-light leading-relaxed text-medical-text space-y-6">
                <p>Nelle lussazioni anteriori recidivanti di spalla, specialmente in pazienti giovani e atleti competitivi, la semplice riparazione artroscopica del cercine (intervento di Bankart) può talvolta fallire.</p>
                <p>In presenza di un'ampia lesione ossea sulla testa omerale (la cosiddetta <em>lesione di Hill-Sachs</em>), la testa dell'omero può letteralmente "incastrarsi" sul bordo glenoideo durante la rotazione esterna e l'abduzione, causando una nuova lussazione.</p>
                
                <h3 class="text-2xl font-serif mt-8 mb-4">La procedura di Remplissage</h3>
                <p>Il <strong>Remplissage</strong> ("riempimento" in francese) consiste nel suturare la porzione posteriore della capsula articolare e il tendine dell'infraspinato direttamente dentro la lesione di Hill-Sachs. Trasforma la lesione ossea in uno spazio "extra-articolare", impedendo l'incastro.</p>
                <p>Il dubbio clinico verte sempre sul range of motion (ROM): il paziente perderà rotazione esterna post-operatoria? I nostri studi, e in particolare il paper pubblicato su <em>Osteology</em> in collaborazione con il CESAT, dimostrano che in atleti selezionati questa riduzione è minima e il tasso di ritorno allo sport è estremamente incoraggiante, offrendo un'eccellente stabilità senza i rischi neurologici della procedura di Latarjet a cielo aperto.</p>
            </div>
            
            <div class="border-t border-medical-border mt-16 pt-8 text-sm text-medical-muted">
                <strong class="font-mono text-medical-text block mb-2">Riferimento bibliografico</strong>
                Novi M., Nicoletti S., et al. "The Remplissage Technique for Hill-Sachs Lesions in Competitive Athletes." Osteology (2022).
            </div>
        </section>

        <!-- ================= CONTATTI ================= -->
        <section id="view-contatti" class="page-view py-32 px-6 max-w-[80rem] mx-auto observer-trigger">
            <div class="grid lg:grid-cols-2 gap-16">
                <div class="reveal-fade">
                    <h1 class="text-fluid-h2 font-serif mb-8">Contatti e <span class="italic text-medical-accent">prenotazioni.</span></h1>
                    <p class="text-base font-light text-medical-text leading-relaxed mb-12">Una singola segreteria coordina gli appuntamenti per tutte le sedi ambulatoriali della Toscana.</p>
                    <div class="border-t border-medical-border py-8">
                        <span class="text-[10px] font-mono uppercase tracking-widest text-medical-accent">Segreteria Telefonica</span>
                        <div class="text-4xl font-serif text-medical-text my-4">+39 348 4331733</div>
                        <p class="text-sm font-light text-medical-muted">Lunedì – Giovedì · 15:30 – 17:30</p>
                    </div>
                </div>
                <div class="border border-medical-border p-8 reveal-fade d-1 bg-medical-surface">
                    <form onsubmit="event.preventDefault(); alert('Inoltrato con successo!');">
                        <div class="grid grid-cols-2 gap-4 mb-4">
                            <input type="text" placeholder="Nome *" class="w-full bg-transparent border-b border-medical-border px-0 py-3 text-sm focus:outline-none focus:border-medical-accent rounded-none font-light" required>
                            <input type="text" placeholder="Cognome *" class="w-full bg-transparent border-b border-medical-border px-0 py-3 text-sm focus:outline-none focus:border-medical-accent rounded-none font-light" required>
                        </div>
                        <input type="tel" placeholder="Telefono *" class="w-full bg-transparent border-b border-medical-border px-0 py-3 text-sm mb-4 focus:outline-none focus:border-medical-accent rounded-none font-light" required>
                        <select class="w-full bg-transparent border-b border-medical-border px-0 py-3 text-sm mb-6 focus:outline-none focus:border-medical-accent rounded-none font-light text-medical-muted" required>
                            <option value="" disabled selected>Sede di preferenza *</option>
                            <option>Fucecchio (Studi San Pietro)</option>
                            <option>Peccioli (Centro San Verano)</option>
                            <option>Pisa (Athletica)</option>
                        </select>
                        <p class="text-[10px] text-medical-muted font-light leading-relaxed mb-6">Nota: Il modulo raccoglie solo i dati di contatto. Non inserire diagnosi o referti sensibili, il form non raccoglie il quadro clinico.</p>
                        <button type="submit" class="btn-mag-solid w-full py-4 text-[11px] font-mono uppercase tracking-widest">Invia richiesta</button>
                    </form>
                </div>
            </div>
        </section>

    </main>
    
    <footer class="border-t border-medical-border py-16 px-6 mt-20 bg-white">
        <div class="max-w-[80rem] mx-auto grid md:grid-cols-4 gap-12 text-sm font-light text-medical-text">
            <div class="md:col-span-2">
                <div class="text-2xl font-serif text-medical-text mb-4">Dott. Michele Novi</div>
                <p class="text-medical-muted">Ortopedico Traumatologo<br>Ospedale CESAT Fucecchio</p>
            </div>
            <div>
                <div class="text-[10px] font-mono uppercase tracking-widest text-medical-accent mb-4">Dove visito</div>
                <ul class="space-y-2 text-medical-muted"><li>Fucecchio</li><li>Peccioli</li><li>Pisa</li></ul>
            </div>
        </div>
    </footer>

    <!-- JS SPA ROUTER -->
    <script>
        window.addEventListener('load', () => document.body.classList.add('is-loaded'));
        
        const observerOptions = { root: null, rootMargin: '0px 0px -10% 0px', threshold: 0.1 };
        const scrollObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add('is-visible'); });
        }, observerOptions);
        
        function observeAll() {
            document.querySelectorAll('.observer-trigger').forEach(t => scrollObserver.observe(t));
        }
        observeAll();

        function navigate() {
            let hash = window.location.hash.replace('#', '').trim();
            if (!hash) hash = 'home';
            
            const targetViewId = 'view-' + hash;
            const targetView = document.getElementById(targetViewId);
            
            if (!targetView) {
                window.location.hash = 'home';
                return;
            }

            document.querySelectorAll('.page-view').forEach(view => {
                if (view.id === targetViewId) {
                    view.style.display = 'block';
                    setTimeout(() => {
                        view.classList.add('active-view');
                        view.querySelectorAll('.observer-trigger').forEach(t => t.classList.remove('is-visible'));
                    }, 50);
                } else {
                    view.style.display = 'none';
                    view.classList.remove('active-view');
                }
            });

            document.querySelectorAll('.nav-link').forEach(link => {
                if (link.getAttribute('data-target') === hash) link.classList.add('active-link');
                else link.classList.remove('active-link');
            });

            if (hash === 'home') {
                document.body.classList.remove('is-loaded');
                setTimeout(() => document.body.classList.add('is-loaded'), 50);
            }
            
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        window.addEventListener('hashchange', navigate);
        
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                const target = this.getAttribute('href');
                if (target === window.location.hash) {
                    e.preventDefault();
                }
            });
        });

        navigate();

        window.addEventListener('scroll', () => {
            const header = document.getElementById('main-header');
            if (window.scrollY > 50) {
                header.classList.add('shadow-sm');
                header.style.paddingTop = '0.5rem'; header.style.paddingBottom = '0.5rem';
            } else {
                header.classList.remove('shadow-sm');
                header.style.paddingTop = '1rem'; header.style.paddingBottom = '1rem';
            }
        });
    </script>
</body>
</html>
"""

with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_head + html_views)

print("Scrittura completata: Contenuti massicci reintegrati e mappati nel router SPA.")
