# -*- coding: utf-8 -*-
import os

html_content = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dott. Michele Novi | Ortopedico spalla e arto superiore in Toscana</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500&family=Manrope:wght@300;400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,200;0,6..72,300;0,6..72,400;0,6..72,500;1,6..72,200;1,6..72,300;1,6..72,400&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        medical: {
                            bg: '#FFFFFF',          /* Puro bianco - Osso */
                            surface: '#F8F9FA',     /* Grigio neutro leggerissimo */
                            border: '#EAEAEA',      /* Linee nette e discrete */
                            text: '#111111',        /* Nero profondo */
                            muted: '#6B7280',       /* Grigio tipografico */
                            accent: '#006775',      /* Luce in cavità: Teal chirurgico intenso */
                            accentHover: '#004c57',
                        }
                    },
                    fontFamily: {
                        serif: ['Newsreader', 'serif'],
                        sans: ['Manrope', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace']
                    }
                }
            }
        }
    </script>
    
    <style>
        :root {
            /* Timing rigorosi (Gesto: slide corti, non acrobatici) */
            --ease-out: cubic-bezier(0.215, 0.61, 0.355, 1);
            --ease-in-out: cubic-bezier(0.645, 0.045, 0.355, 1);
            --ease-varco: cubic-bezier(0.77, 0, 0.175, 1);
        }

        body {
            background-color: #FFFFFF;
            color: #111111;
            font-family: 'Manrope', sans-serif;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            overflow-x: hidden;
        }

        /* 
         * OSSO VISIBILE: Griglia strutturale di sfondo
         * Sottilissime linee verticali che danno ritmo e rigore (Congruenza)
         * Nessuna ombra: solo bordi e margini veri.
         */
        .grid-osso {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            pointer-events: none;
            z-index: -1;
            display: flex;
            justify-content: center;
        }
        .grid-osso-inner {
            width: 100%;
            max-width: 80rem;
            height: 100%;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            border-left: 1px solid var(--medical-border);
            border-right: 1px solid var(--medical-border);
            opacity: 0.4;
        }
        .grid-osso-inner div {
            border-right: 1px solid var(--medical-border);
        }
        .grid-osso-inner div:last-child {
            border-right: none;
        }

        /* 
         * IL VARCO (Hero Animation)
         * "Un foro preciso. Dietro profondità"
         */
        .varco-mask {
            clip-path: inset(35% 25% 35% 25%);
            transition: clip-path 1.8s var(--ease-varco);
            will-change: clip-path;
        }
        .varco-img {
            transform: scale(1.4);
            filter: grayscale(100%) contrast(1.1);
            transition: transform 2.5s var(--ease-out), filter 2s var(--ease-out);
            will-change: transform, filter;
        }
        
        .is-loaded .varco-mask {
            clip-path: inset(0% 0% 0% 0%);
        }
        .is-loaded .varco-img {
            transform: scale(1);
            filter: grayscale(15%) contrast(1.05); /* Lieve desaturazione clinica */
        }

        /*
         * ANIMAZIONI TESTO & SCROLL REVEAL (Gesto pulito)
         */
        .mask-text {
            overflow: hidden;
            display: block;
        }
        .mask-text-inner {
            display: inline-block;
            transform: translateY(110%);
            transition: transform 1s var(--ease-out);
            will-change: transform;
        }
        .reveal-fade {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 1s var(--ease-out), transform 1s var(--ease-out);
        }

        .is-visible .mask-text-inner { transform: translateY(0); }
        .is-visible.reveal-fade, .is-visible .reveal-fade { opacity: 1; transform: translateY(0); }

        .d-1 { transition-delay: 0.1s; }
        .d-2 { transition-delay: 0.2s; }
        .d-3 { transition-delay: 0.3s; }

        /* 
         * HOVER STATES (Congruenza & Luce)
         */
        .card-congruenza {
            transition: border-color 0.4s var(--ease-out);
        }
        .card-congruenza .card-img-wrap {
            overflow: hidden;
            clip-path: inset(0 0 0 0);
            transition: clip-path 0.6s var(--ease-out);
        }
        .card-congruenza img {
            transition: transform 0.8s var(--ease-out), filter 0.8s var(--ease-out);
            filter: grayscale(100%);
        }
        .card-congruenza:hover {
            border-color: var(--medical-accent);
        }
        .card-congruenza:hover .card-img-wrap {
            clip-path: inset(2% 2% 2% 2%); 
        }
        .card-congruenza:hover img {
            transform: scale(1.05);
            filter: grayscale(0%);
        }

        /* Row Articoli (Quaderno) - Un foglio di lavoro pulito */
        .row-quaderno {
            position: relative;
            transition: padding-left 0.4s var(--ease-out);
        }
        .row-quaderno::before {
            content: '';
            position: absolute;
            left: -20px; top: 0; width: 0%; height: 100%;
            background: var(--medical-surface);
            z-index: -1;
            transition: width 0.5s var(--ease-varco), left 0.5s var(--ease-varco);
        }
        .row-quaderno:hover {
            padding-left: 20px;
        }
        .row-quaderno:hover::before {
            left: 0;
            width: 100%;
        }
        .row-quaderno .titolo-articolo {
            transition: color 0.4s var(--ease-out);
        }
        .row-quaderno:hover .titolo-articolo {
            color: var(--medical-accent);
            font-style: italic;
        }

        /* Pulsante CTA (Luce chirurgica) */
        .btn-mag {
            position: relative;
            overflow: hidden;
            border: 1px solid var(--medical-accent);
            color: var(--medical-accent);
            background: transparent;
            transition: color 0.4s var(--ease-out);
            z-index: 1;
        }
        .btn-mag::after {
            content: '';
            position: absolute;
            bottom: 0; left: 0; width: 100%; height: 0%;
            background: var(--medical-accent);
            z-index: -1;
            transition: height 0.4s var(--ease-varco);
        }
        .btn-mag:hover {
            color: #fff;
        }
        .btn-mag:hover::after {
            height: 100%;
        }

        .btn-mag-solid {
            background: var(--medical-accent);
            color: #fff;
        }
        .btn-mag-solid::after {
            background: #111111;
        }

        /* ROUTER PAGE TRANSITIONS */
        .page-view {
            display: none;
            opacity: 0;
        }
        .page-view.active-view {
            display: block;
            animation: viewEnter 0.8s var(--ease-varco) forwards;
        }
        @keyframes viewEnter {
            0% { opacity: 0; transform: translateY(30px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        /* Tipografia fluida */
        .text-fluid-hero { font-size: clamp(3rem, 7vw, 7rem); line-height: 0.95; letter-spacing: -0.02em; }
        .text-fluid-h2 { font-size: clamp(2.5rem, 5vw, 4.5rem); line-height: 1; letter-spacing: -0.01em; }
        .text-fluid-h3 { font-size: clamp(1.5rem, 3vw, 2.5rem); line-height: 1.1; }
        
        /* Nav Line */
        .nav-link { position: relative; }
        .nav-link::after {
            content: ''; position: absolute; bottom: 0; left: 0; width: 0%; height: 1px;
            background: currentColor; transition: width 0.3s var(--ease-out);
        }
        .nav-link:hover::after, .nav-link.active-link::after { width: 100%; }
        
        /* Accent Text Line (Il filetto della luce) */
        .accent-line {
            display: inline-block;
            border-bottom: 1px solid var(--medical-accent);
            color: var(--medical-text);
            transition: color 0.3s var(--ease-out);
        }
        .accent-line:hover {
            color: var(--medical-accent);
        }
    </style>
</head>
<body class="selection:bg-medical-accent selection:text-white">

    <!-- L'OSSO SOTTO: Griglia strutturale visibile (calma, precisa) -->
    <div class="grid-osso hidden md:flex">
        <div class="grid-osso-inner">
            <div></div><div></div><div></div><div></div>
        </div>
    </div>

    <!-- Header -->
    <header class="fixed top-0 w-full z-50 bg-white/90 backdrop-blur-md border-b border-medical-border transition-transform duration-500" id="main-header">
        <div class="max-w-[80rem] mx-auto px-6 h-20 flex justify-between items-center">
            <a href="#home" class="group flex flex-col cursor-pointer overflow-hidden">
                <span class="text-xl font-serif tracking-tight text-medical-text transition-colors">Dott. Michele Novi</span>
                <span class="text-[10px] uppercase tracking-widest text-medical-muted font-mono mt-0.5">Ortopedico Spalla e Arto Superiore</span>
            </a>

            <nav class="hidden lg:flex items-center gap-10 text-[11px] font-mono uppercase tracking-widest text-medical-text">
                <a href="#chi-sono" class="nav-link py-2" data-route="chi-sono">Chi sono</a>
                <a href="#patologie" class="nav-link py-2" data-route="patologie">Cosa curo</a>
                <a href="#sedi" class="nav-link py-2" data-route="sedi">Dove ricevo</a>
                <a href="#note-cliniche" class="nav-link py-2" data-route="note-cliniche">Note Cliniche</a>
            </nav>

            <div class="hidden sm:flex items-center gap-4">
                <a href="#contatti" class="btn-mag-solid px-6 py-2.5 rounded-full text-[11px] font-mono uppercase tracking-widest transition-all">
                    Chiama
                </a>
            </div>

            <button id="mobile-menu-btn" class="lg:hidden p-2 text-medical-text">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 6h16M4 12h16M4 18h16"></path></svg>
            </button>
        </div>
    </header>

    <main id="app" class="pt-20">

        <!-- ========================================== -->
        <!-- 1. VIEW: HOME                              -->
        <!-- ========================================== -->
        <section id="view-home" class="page-view active-view">
            <!-- HERO: IL VARCO -->
            <div class="relative min-h-[calc(100vh-5rem)] flex flex-col justify-center px-6 max-w-[80rem] mx-auto pt-10 pb-20">
                <div class="grid lg:grid-cols-12 gap-12 items-center h-full">
                    
                    <div class="lg:col-span-7 z-10 space-y-8 observer-trigger">
                        <div class="mask-text">
                            <span class="mask-text-inner text-[10px] font-mono uppercase tracking-widest text-medical-text border border-medical-border px-3 py-1 rounded-full">
                                Ospedale CESAT Fucecchio · Studi in Toscana
                            </span>
                        </div>
                        <h1 class="text-fluid-hero font-serif text-medical-text">
                            <div class="mask-text"><span class="mask-text-inner">Chirurgo</span></div>
                            <div class="mask-text"><span class="mask-text-inner d-1 italic text-medical-accent">ortopedico.</span></div>
                            <div class="mask-text"><span class="mask-text-inner d-2">Spalla e</span></div>
                            <div class="mask-text"><span class="mask-text-inner d-3 text-medical-muted">arto superiore.</span></div>
                        </h1>
                        <div class="mask-text">
                            <p class="mask-text-inner d-3 text-base md:text-lg font-light leading-relaxed text-medical-text max-w-md">
                                Ortopedico traumatologo, chirurgia della spalla e dell'arto superiore, artroscopica e protesica.
                            </p>
                        </div>
                        <div class="reveal-fade d-3 flex gap-4 pt-4">
                            <a href="#contatti" class="btn-mag px-8 py-3.5 rounded-full text-[11px] font-mono uppercase tracking-widest text-center">
                                Contatta la segreteria
                            </a>
                            <a href="#sedi" class="btn-mag px-8 py-3.5 rounded-full text-[11px] font-mono uppercase tracking-widest text-center !border-medical-border !text-medical-text hover:!text-white hover:!border-medical-text before:!bg-medical-text">
                                Dove ricevo
                            </a>
                        </div>
                    </div>

                    <div class="lg:col-span-5 h-[60vh] lg:h-[80vh] relative observer-trigger">
                        <!-- IL VARCO VISIVO -->
                        <div class="w-full h-full varco-mask overflow-hidden absolute inset-0 bg-medical-surface">
                            <img src="https://images.unsplash.com/photo-1551076805-e1869043e560?q=80&w=1200&auto=format&fit=crop" class="w-full h-full object-cover object-center varco-img" alt="Chirurgia spalla artroscopica">
                        </div>
                    </div>
                </div>
            </div>

            <!-- CREDENZIALI (Perché fidarsi - L'Osso) -->
            <div class="border-y border-medical-border px-6 observer-trigger">
                <div class="max-w-[80rem] mx-auto grid grid-cols-2 md:grid-cols-4 divide-x divide-medical-border">
                    <div class="py-10 px-4 reveal-fade">
                        <div class="text-fluid-h3 font-serif text-medical-text">CESAT Fucecchio</div>
                        <div class="text-[10px] font-mono uppercase tracking-widest text-medical-muted mt-2">Polo Chirurgico d'Eccellenza</div>
                    </div>
                    <div class="py-10 px-6 reveal-fade d-1">
                        <div class="text-fluid-h3 font-serif text-medical-text">Formazione</div>
                        <div class="text-[10px] font-mono uppercase tracking-widest text-medical-muted mt-2">Università di Pisa</div>
                    </div>
                    <div class="py-10 px-6 reveal-fade d-2">
                        <div class="text-fluid-h3 font-serif text-medical-text">Fellowship</div>
                        <div class="text-[10px] font-mono uppercase tracking-widest text-medical-muted mt-2">Londra · Seattle · Berlino</div>
                    </div>
                    <div class="py-10 px-6 reveal-fade d-3">
                        <div class="text-fluid-h3 font-serif text-medical-text">Porcellini</div>
                        <div class="text-[10px] font-mono uppercase tracking-widest text-medical-muted mt-2">Scuola di specializzazione</div>
                    </div>
                </div>
            </div>

            <!-- PATOLOGIE (Congruenza) -->
            <section class="py-32 px-6 max-w-[80rem] mx-auto observer-trigger">
                <div class="flex flex-col md:flex-row md:items-end justify-between mb-20">
                    <div>
                        <div class="mask-text"><span class="mask-text-inner text-[10px] font-mono uppercase tracking-widest text-medical-muted mb-4 block">Cosa curo</span></div>
                        <h2 class="text-fluid-h2 font-serif">
                            <div class="mask-text"><span class="mask-text-inner d-1">Aree di</span></div>
                            <div class="mask-text"><span class="mask-text-inner d-2 italic text-medical-accent">trattamento.</span></div>
                        </h2>
                    </div>
                    <a href="#patologie" class="reveal-fade d-3 accent-line text-[11px] font-mono uppercase tracking-widest pb-1 mt-6 md:mt-0">
                        Vedi tutte le aree
                    </a>
                </div>

                <div class="grid md:grid-cols-2 gap-6">
                    <a href="#patologie/spalla" class="card-congruenza block border border-medical-border p-8 reveal-fade group bg-white">
                        <h3 class="text-2xl font-serif mb-3">Spalla</h3>
                        <p class="text-sm font-light text-medical-muted leading-relaxed">Cuffia dei rotatori, instabilità, lussazioni, protesica anatomica e inversa.</p>
                        <div class="mt-6 pt-4 border-t border-medical-border text-[10px] font-mono text-medical-accent opacity-0 transform translate-y-2 group-hover:opacity-100 group-hover:translate-y-0 transition-all duration-500">
                            ESPLORA SCHEDA →
                        </div>
                    </a>
                    <a href="#patologie/gomito-mano" class="card-congruenza block border border-medical-border p-8 reveal-fade d-1 group bg-white">
                        <h3 class="text-2xl font-serif mb-3">Gomito, Mano e Polso</h3>
                        <p class="text-sm font-light text-medical-muted leading-relaxed">Epicondilite, tunnel carpale, rizoartrosi, dita a scatto, traumatologia complessa.</p>
                        <div class="mt-6 pt-4 border-t border-medical-border text-[10px] font-mono text-medical-accent opacity-0 transform translate-y-2 group-hover:opacity-100 group-hover:translate-y-0 transition-all duration-500">
                            ESPLORA SCHEDA →
                        </div>
                    </a>
                    <a href="#patologie/traumatologia-sportiva" class="card-congruenza block border border-medical-border p-8 reveal-fade d-2 group bg-white">
                        <h3 class="text-2xl font-serif mb-3">Traumatologia Sportiva</h3>
                        <p class="text-sm font-light text-medical-muted leading-relaxed">Return to sport, lussazioni acromion-claveari, traumi overhead.</p>
                        <div class="mt-6 pt-4 border-t border-medical-border text-[10px] font-mono text-medical-accent opacity-0 transform translate-y-2 group-hover:opacity-100 group-hover:translate-y-0 transition-all duration-500">
                            ESPLORA SCHEDA →
                        </div>
                    </a>
                    
                    <div class="grid grid-cols-2 gap-6 reveal-fade d-3">
                        <a href="#patologie/artroscopia" class="card-congruenza block border border-medical-border p-8 group bg-medical-surface">
                            <span class="text-[10px] font-mono uppercase tracking-widest text-medical-accent mb-2 block">Metodo</span>
                            <h3 class="text-xl font-serif mb-3">Artroscopia</h3>
                            <p class="text-xs font-light text-medical-muted leading-relaxed">Chirurgia mini-invasiva.</p>
                        </a>
                        <a href="#patologie/ecografia" class="card-congruenza block border border-medical-border p-8 group bg-medical-surface">
                            <span class="text-[10px] font-mono uppercase tracking-widest text-medical-accent mb-2 block">Metodo</span>
                            <h3 class="text-xl font-serif mb-3">Eco MSK</h3>
                            <p class="text-xs font-light text-medical-muted leading-relaxed">Ecografia in ambulatorio.</p>
                        </a>
                    </div>
                </div>
            </section>

            <!-- SEDI -->
            <section class="py-32 px-6 border-t border-medical-border bg-medical-surface observer-trigger">
                <div class="max-w-[80rem] mx-auto grid lg:grid-cols-12 gap-16 items-start">
                    <div class="lg:col-span-5 sticky top-32">
                        <div class="mask-text"><span class="mask-text-inner text-[10px] font-mono uppercase tracking-widest text-medical-muted mb-4 block">Dove ricevo</span></div>
                        <h2 class="text-fluid-h2 font-serif mb-6">
                            <div class="mask-text"><span class="mask-text-inner">Le sedi</span></div>
                            <div class="mask-text"><span class="mask-text-inner italic text-medical-accent">confermate.</span></div>
                        </h2>
                        <div class="reveal-fade">
                            <p class="text-base font-light text-medical-text leading-relaxed mb-8">
                                Ambulatori di libera professione per le prime visite e la diagnostica sul territorio. Chirurgia ad alto volume presso l'Ospedale CESAT.
                            </p>
                            <a href="#sedi" class="btn-mag px-6 py-3 rounded-full text-[11px] font-mono uppercase tracking-widest inline-block">
                                Dettagli e Mappa
                            </a>
                        </div>
                    </div>
                    
                    <div class="lg:col-span-7 space-y-4 reveal-fade d-1">
                        <!-- Sede: CESAT (Ospedale) -->
                        <a href="#sedi/cesat-fucecchio" class="group flex flex-col sm:flex-row justify-between items-start sm:items-center p-6 bg-white border border-medical-border hover:border-medical-accent transition-colors">
                            <div>
                                <span class="text-[10px] font-mono uppercase tracking-widest text-white bg-medical-text px-2 py-0.5 rounded block w-max mb-3">Chirurgia & Ricoveri</span>
                                <h3 class="text-2xl font-serif text-medical-text group-hover:text-medical-accent transition-colors">CESAT Ospedale Fucecchio</h3>
                                <p class="text-xs font-mono text-medical-muted mt-2">Piazza Spartaco Lavagnini 5</p>
                            </div>
                            <span class="hidden sm:block text-medical-border group-hover:text-medical-accent transition-colors">→</span>
                        </a>
                        
                        <!-- Sede: Fucecchio Studio -->
                        <a href="#sedi/fucecchio-san-pietro" class="group flex flex-col sm:flex-row justify-between items-start sm:items-center p-6 bg-white border border-medical-border hover:border-medical-accent transition-colors">
                            <div>
                                <span class="text-[10px] font-mono uppercase tracking-widest text-medical-accent mb-3 block">Visite Ambulatoriali</span>
                                <h3 class="text-2xl font-serif text-medical-text group-hover:text-medical-accent transition-colors">Studi Medici San Pietro</h3>
                                <p class="text-xs font-mono text-medical-muted mt-2">Fucecchio (FI) · Piazza S. Lavagnini 6</p>
                            </div>
                            <span class="hidden sm:block text-medical-border group-hover:text-medical-accent transition-colors">→</span>
                        </a>

                        <!-- Sede: Peccioli -->
                        <a href="#sedi/peccioli-san-verano" class="group flex flex-col sm:flex-row justify-between items-start sm:items-center p-6 bg-white border border-medical-border hover:border-medical-accent transition-colors">
                            <div>
                                <span class="text-[10px] font-mono uppercase tracking-widest text-medical-accent mb-3 block">Visite & Ecografia</span>
                                <h3 class="text-2xl font-serif text-medical-text group-hover:text-medical-accent transition-colors">Centro Medico San Verano</h3>
                                <p class="text-xs font-mono text-medical-muted mt-2">Peccioli (PI) · Viale Cavour 13</p>
                            </div>
                            <span class="hidden sm:block text-medical-border group-hover:text-medical-accent transition-colors">→</span>
                        </a>

                        <!-- Sede: Pisa -->
                        <a href="#sedi/pisa-athletica" class="group flex flex-col sm:flex-row justify-between items-start sm:items-center p-6 bg-white border border-medical-border hover:border-medical-accent transition-colors">
                            <div>
                                <span class="text-[10px] font-mono uppercase tracking-widest text-medical-accent mb-3 block">Visite</span>
                                <h3 class="text-2xl font-serif text-medical-text group-hover:text-medical-accent transition-colors">Athletica</h3>
                                <p class="text-xs font-mono text-medical-muted mt-2">Pisa</p>
                            </div>
                            <span class="hidden sm:block text-medical-border group-hover:text-medical-accent transition-colors">→</span>
                        </a>
                    </div>
                </div>
            </section>

            <!-- QUADERNO / NOTE CLINICHE -->
            <section class="py-32 px-6 max-w-[80rem] mx-auto observer-trigger border-t border-medical-border">
                <div class="text-center mb-20">
                    <div class="mask-text"><span class="mask-text-inner text-[10px] font-mono uppercase tracking-widest text-medical-muted mb-4 block">Ricerca & Divulgazione</span></div>
                    <h2 class="text-fluid-h2 font-serif mx-auto">
                        <div class="mask-text"><span class="mask-text-inner">Note <span class="italic text-medical-accent">cliniche.</span></span></div>
                    </h2>
                </div>

                <div class="border-t border-medical-border">
                    <a href="#note-cliniche/remplissage" class="row-quaderno block border-b border-medical-border py-10 px-4 reveal-fade">
                        <div class="grid md:grid-cols-12 gap-6 items-center">
                            <div class="md:col-span-3 text-[10px] font-mono text-medical-muted">12 NOV 2026 · INSTABILITÀ</div>
                            <div class="md:col-span-7">
                                <h3 class="titolo-articolo text-3xl font-serif text-medical-text">Il dubbio nel remplissage: stabilità e movimento.</h3>
                            </div>
                            <div class="md:col-span-2 text-right hidden md:block text-[10px] font-mono text-medical-muted">LEGGI NOTA →</div>
                        </div>
                    </a>
                    <a href="#note-cliniche/cuffia-irreparabile" class="row-quaderno block border-b border-medical-border py-10 px-4 reveal-fade d-1">
                        <div class="grid md:grid-cols-12 gap-6 items-center">
                            <div class="md:col-span-3 text-[10px] font-mono text-medical-muted">04 OTT 2026 · CUFFIA ROTATORI</div>
                            <div class="md:col-span-7">
                                <h3 class="titolo-articolo text-3xl font-serif text-medical-text">Cuffia irreparabile: oltre l'illusione della sutura.</h3>
                            </div>
                            <div class="md:col-span-2 text-right hidden md:block text-[10px] font-mono text-medical-muted">LEGGI NOTA →</div>
                        </div>
                    </a>
                </div>
                <div class="text-center mt-12 reveal-fade d-2">
                    <a href="#note-cliniche" class="accent-line text-[11px] font-mono uppercase tracking-widest pb-1">
                        Archivio Completo Note Cliniche
                    </a>
                </div>
            </section>
        </section>

        <!-- VISTA CONTATTI (Clean, Osso style, no Dati Sanitari) -->
        <section id="view-contatti" class="page-view py-32 px-6 max-w-[80rem] mx-auto observer-trigger">
            <div class="grid lg:grid-cols-2 gap-16">
                <div class="reveal-fade">
                    <h1 class="text-fluid-h2 font-serif mb-8">Contatti e <span class="italic text-medical-accent">prenotazioni.</span></h1>
                    <p class="text-base font-light text-medical-text leading-relaxed mb-12">Una singola segreteria coordina gli appuntamenti per tutte le sedi ambulatoriali della Toscana. Utilizza i recapiti o il form per essere ricontattato.</p>
                    
                    <div class="border-t border-medical-border py-8">
                        <span class="text-[10px] font-mono uppercase tracking-widest text-medical-accent">Segreteria Telefonica</span>
                        <div class="text-4xl font-serif text-medical-text my-4">+39 348 4331733</div>
                        <p class="text-sm font-light text-medical-muted">Lunedì – Giovedì · 15:30 – 17:30</p>
                    </div>
                </div>
                
                <div class="border border-medical-border p-8 reveal-fade d-1 bg-medical-surface">
                    <form id="booking-form" class="space-y-6" onsubmit="event.preventDefault(); document.getElementById('form-success-message').style.display='block';">
                        <div class="grid grid-cols-2 gap-4">
                            <input type="text" placeholder="Nome *" class="w-full bg-transparent border-b border-medical-border px-0 py-3 text-sm focus:outline-none focus:border-medical-accent rounded-none font-light" required>
                            <input type="text" placeholder="Cognome *" class="w-full bg-transparent border-b border-medical-border px-0 py-3 text-sm focus:outline-none focus:border-medical-accent rounded-none font-light" required>
                        </div>
                        <input type="tel" placeholder="Telefono *" class="w-full bg-transparent border-b border-medical-border px-0 py-3 text-sm focus:outline-none focus:border-medical-accent rounded-none font-light" required>
                        <select class="w-full bg-transparent border-b border-medical-border px-0 py-3 text-sm focus:outline-none focus:border-medical-accent rounded-none font-light text-medical-muted" required>
                            <option value="" disabled selected>Sede di preferenza *</option>
                            <option>Fucecchio (Studi San Pietro)</option>
                            <option>Peccioli (Centro San Verano)</option>
                            <option>Pisa (Athletica)</option>
                        </select>
                        
                        <p class="text-[10px] text-medical-muted font-light leading-relaxed">
                            Nota: Il modulo raccoglie solo i dati di contatto. Non inserire diagnosi o referti sensibili, il form non raccoglie il quadro clinico.
                        </p>

                        <button type="submit" class="btn-mag-solid w-full py-4 text-[11px] font-mono uppercase tracking-widest mt-8">
                            Invia richiesta
                        </button>
                    </form>
                    <div id="form-success-message" class="hidden mt-6 text-sm font-light text-medical-accent border border-medical-accent p-4">
                        Richiesta inoltrata alla segreteria. Verrai ricontattato a breve.
                    </div>
                </div>
            </div>
        </section>

    </main>

    <!-- FOOTER "OSSO" -->
    <footer class="border-t border-medical-border py-16 px-6 mt-20 bg-white">
        <div class="max-w-[80rem] mx-auto grid md:grid-cols-4 gap-12 text-sm font-light text-medical-text">
            <div class="md:col-span-2">
                <div class="text-2xl font-serif text-medical-text mb-4">Dott. Michele Novi</div>
                <p class="text-medical-muted">Ortopedico Traumatologo, Chirurgia Spalla e Arto Superiore<br>Ospedale CESAT Fucecchio</p>
            </div>
            <div>
                <div class="text-[10px] font-mono uppercase tracking-widest text-medical-accent mb-4">Dove visito</div>
                <ul class="space-y-2 text-medical-muted">
                    <li>Fucecchio (San Pietro)</li>
                    <li>Peccioli (San Verano)</li>
                    <li>Pisa (Athletica)</li>
                </ul>
            </div>
            <div>
                <div class="text-[10px] font-mono uppercase tracking-widest text-medical-accent mb-4">Segreteria</div>
                <ul class="space-y-2 text-medical-muted font-mono text-xs">
                    <li>+39 348 4331733</li>
                    <li>Lun - Gio 15:30 - 17:30</li>
                </ul>
            </div>
        </div>
    </footer>

    <!-- LOGICA GSAP-like con VANILLA JS -->
    <script>
        window.addEventListener('load', () => {
            document.body.classList.add('is-loaded');
        });

        const observerOptions = { root: null, rootMargin: '0px 0px -10% 0px', threshold: 0.1 };
        const scrollObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                }
            });
        }, observerOptions);

        document.querySelectorAll('.observer-trigger').forEach(trigger => {
            scrollObserver.observe(trigger);
        });

        const routes = {
            '': 'view-home',
            'home': 'view-home',
            'contatti': 'view-contatti'
        };

        function navigate() {
            const rawHash = window.location.hash.replace('#', '').trim();
            const targetViewId = routes[rawHash] || 'view-home';

            if (targetViewId === 'view-home') {
                document.body.classList.remove('is-loaded');
                setTimeout(() => document.body.classList.add('is-loaded'), 50);
            }

            document.querySelectorAll('.page-view').forEach(view => {
                if (view.id === targetViewId) {
                    view.classList.add('active-view');
                    view.querySelectorAll('.observer-trigger').forEach(t => t.classList.remove('is-visible'));
                } else {
                    view.classList.remove('active-view');
                }
            });
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        window.addEventListener('hashchange', navigate);
        
        window.addEventListener('scroll', () => {
            const header = document.getElementById('main-header');
            if (window.scrollY > 50) {
                header.classList.add('shadow-sm');
                header.style.paddingTop = '0.5rem';
                header.style.paddingBottom = '0.5rem';
            } else {
                header.classList.remove('shadow-sm');
                header.style.paddingTop = '1rem';
                header.style.paddingBottom = '1rem';
            }
        });
    </script>
</body>
</html>
"""

output_path = "/Volumes/Programs/Temporary files/Progetti cursor/Michele_Novi_Website/Proposte HTML/index.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("File sincronizzato con l'Architettura dell'Informazione e la palette corretta.")
