# -*- coding: utf-8 -*-
"""
Script per la generazione del prototipo HTML "Awwwards Masterpiece"
per il Dott. Michele Novi.
Integra in modo profondo e tangibile:
1. IL CONCETTO DEGLI STRATI ("Uno strato sotto l'altro" / Dissezione / Sticky Stacking Layers / Sottostrato Osso)
2. IL CONCETTO DELL'INCASTRO ("Due superfici che combaciano" / Congruenza / Giunti monolitici / Interlocking notches)
3. NOMI PAGINE E ARCHITETTURA RIGOROSAMENTE FEDELI ALLA BIBBIA (Capitolo 04, 11, 16).
"""

import os

html_code = """<!DOCTYPE html>
<html lang="it" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dott. Michele Novi | Chirurgia Ortopedica Spalla e Arto Superiore</title>
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Google Fonts: Newsreader (eleganza clinica), Manrope (chiarezza), JetBrains Mono (precisione da lastra) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600&family=Manrope:wght@300;400;500;600;700;800&family=Newsreader:ital,opsz,wght@0,6..72,200;0,6..72,300;0,6..72,400;0,6..72,500;1,6..72,200;1,6..72,300;1,6..72,400&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        osso: {
                            base: '#F5F5F3',        /* Bianco osso materico / carta cotone */
                            surface: '#EAEBE8',     /* Superficie intermedia */
                            plate: '#DFE0DC',       /* Strato profondo / lastra */
                            line: '#CFD2CC',        /* Linea di raccordo millimetrica */
                            dark: '#0C0D0C',        /* Nero profondo / carboncino */
                            muted: '#5A605B',       /* Testo secondario rigoroso */
                            teal: '#005C66',        /* Luce in cavità: Teal chirurgico puro */
                            tealLight: '#E6F0F2',   /* Velo teal tenue */
                            tealHover: '#00474F'
                        }
                    },
                    fontFamily: {
                        serif: ['Newsreader', 'Georgia', 'serif'],
                        sans: ['Manrope', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace']
                    }
                }
            }
        }
    </script>
    
    <style>
        :root {
            --ease-surgical: cubic-bezier(0.16, 1, 0.3, 1);
            --ease-joint: cubic-bezier(0.65, 0, 0.35, 1);
            --ease-varco: cubic-bezier(0.77, 0, 0.175, 1);
        }

        body {
            background-color: #F5F5F3;
            color: #0C0D0C;
            font-family: 'Manrope', sans-serif;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }

        /* ============================================================
           1. LO STRATO SOTTO: IL SOTTOSTRATO OSSO (SUBSTRATE LAYER)
           La struttura portante e le quote millimetriche sempre visibili
           sotto i livelli superficiali.
           ============================================================ */
        .substrate-grid {
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            pointer-events: none;
            z-index: 0;
            display: grid;
            grid-template-columns: 2rem 1fr 1fr 1fr 1fr 2rem;
            border-left: 1px solid rgba(207, 210, 204, 0.5);
            border-right: 1px solid rgba(207, 210, 204, 0.5);
        }
        @media (max-width: 768px) {
            .substrate-grid {
                grid-template-columns: 1rem 1fr 1fr 1rem;
            }
        }
        .substrate-col {
            border-right: 1px dashed rgba(207, 210, 204, 0.4);
            height: 100%;
            position: relative;
        }
        .substrate-cross {
            position: absolute;
            width: 9px; height: 9px;
            transform: translate(-4px, -4px);
        }
        .substrate-cross::before, .substrate-cross::after {
            content: ''; position: absolute; background: #5A605B; opacity: 0.4;
        }
        .substrate-cross::before { top: 4px; left: 0; width: 9px; height: 1px; }
        .substrate-cross::after { top: 0; left: 4px; width: 1px; height: 9px; }

        /* ============================================================
           2. L'INCASTRO GEOMETRICO (INTERLOCKING JOINTS)
           Giunti a pettine, notch concavi e bordi a contatto perfetto
           ============================================================ */
        .joint-border {
            border: 1px solid #CFD2CC;
        }
        .joint-group {
            display: grid;
            gap: 0;
        }
        .joint-item {
            border: 1px solid #CFD2CC;
            margin-top: -1px;
            margin-left: -1px;
            transition: all 0.4s var(--ease-surgical);
            background: #F5F5F3;
        }
        .joint-item:hover {
            z-index: 10;
            border-color: #005C66;
            background: #FFFFFF;
        }

        /* Angolo a incastro (Notch concavo architettonico) */
        .interlock-tab {
            position: relative;
            background: #0C0D0C;
            color: #F5F5F3;
            clip-path: polygon(0 0, calc(100% - 16px) 0, 100% 16px, 100% 100%, 0 100%);
        }

        /* Incastro articolare interattivo: TESTA e GLENOIDE */
        .joint-socket {
            position: relative;
            overflow: hidden;
            border: 1px solid #CFD2CC;
            background: #FFFFFF;
            transition: border-color 0.5s var(--ease-surgical);
        }
        .joint-socket:hover {
            border-color: #005C66;
        }
        .joint-head {
            transform: translateX(-8px);
            transition: transform 0.6s var(--ease-joint);
        }
        .joint-socket:hover .joint-head {
            transform: translateX(0px); /* L'incastro si chiude: congruenza raggiunta */
        }
        .joint-status-badge {
            transition: background-color 0.4s var(--ease-surgical), color 0.4s;
        }
        .joint-socket:hover .joint-status-badge {
            background-color: #005C66;
            color: #FFFFFF;
        }

        /* ============================================================
           3. STRATI SOVRAPPOSTI (STACKED STRATA / SEZIONI A STRATO)
           Ogni strato sale e si sovrappone a quello precedente
           come le lamine anatomiche durante un accesso chirurgico.
           ============================================================ */
        .stratum-card {
            position: sticky;
            top: 5rem;
            border: 1px solid #CFD2CC;
            background: #F5F5F3;
            box-shadow: 0 -12px 32px rgba(12, 13, 12, 0.05);
            transition: transform 0.3s var(--ease-surgical);
        }
        .stratum-card:nth-child(1) { top: 5.5rem; z-index: 1; }
        .stratum-card:nth-child(2) { top: 7.5rem; z-index: 2; }
        .stratum-card:nth-child(3) { top: 9.5rem; z-index: 3; }
        .stratum-card:nth-child(4) { top: 11.5rem; z-index: 4; }

        /* Effetto Varco Fotografico (Accesso ottico con clip-path a diaframma) */
        .varco-portal {
            position: relative;
            overflow: hidden;
            clip-path: inset(0% 0% 0% 0%);
            transition: clip-path 1.4s var(--ease-varco);
        }
        .varco-image {
            transform: scale(1.08);
            filter: grayscale(85%) contrast(1.1);
            transition: transform 1.6s var(--ease-surgical), filter 1.2s var(--ease-surgical);
        }
        .varco-portal:hover .varco-image, .is-loaded .varco-image {
            transform: scale(1);
            filter: grayscale(10%) contrast(1.05);
        }

        /* Maschera di dissezione interattiva */
        .dissection-layer {
            transition: opacity 0.5s var(--ease-surgical), transform 0.5s var(--ease-surgical);
        }

        /* Bottoni Magnetici con incastro visivo */
        .btn-interlock {
            position: relative;
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
            padding: 0.85rem 1.75rem;
            border: 1px solid #0C0D0C;
            background: transparent;
            color: #0C0D0C;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.75rem;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            overflow: hidden;
            transition: color 0.4s var(--ease-surgical), border-color 0.4s;
        }
        .btn-interlock::before {
            content: '';
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: #0C0D0C;
            transform: translateY(100%);
            transition: transform 0.4s var(--ease-joint);
            z-index: 0;
        }
        .btn-interlock:hover {
            color: #F5F5F3;
        }
        .btn-interlock:hover::before {
            transform: translateY(0);
        }
        .btn-interlock span, .btn-interlock svg {
            position: relative;
            z-index: 1;
        }
        .btn-interlock-teal {
            border-color: #005C66;
            color: #005C66;
        }
        .btn-interlock-teal::before {
            background: #005C66;
        }
        .btn-interlock-teal:hover {
            color: #FFFFFF;
        }

        /* Pagine SPA */
        .page-view {
            display: none;
            opacity: 0;
        }
        .page-view.active-view {
            display: block;
            animation: layerReveal 0.7s var(--ease-surgical) forwards;
        }
        @keyframes layerReveal {
            0% {
                opacity: 0;
                transform: translateY(24px) scale(0.99);
            }
            100% {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }

        /* Indicatori di quota e assi */
        .dimension-line {
            position: relative;
        }
        .dimension-line::before, .dimension-line::after {
            content: '';
            position: absolute;
            background: #CFD2CC;
        }
        .dimension-line-h::before {
            top: 50%; left: 0; width: 100%; height: 1px;
        }
    </style>
</head>
<body class="selection:bg-osso-teal selection:text-white relative">

    <!-- ============================================================
         STRATO ZERO: SOTTOSTRATO OSSO (SUBSTRATE)
         La griglia strutturale millimetrica permanente
         ============================================================ -->
    <div class="substrate-grid" aria-hidden="true">
        <div></div>
        <div class="substrate-col">
            <div class="substrate-cross" style="top: 25%;"></div>
            <div class="substrate-cross" style="top: 75%;"></div>
        </div>
        <div class="substrate-col">
            <div class="substrate-cross" style="top: 50%;"></div>
        </div>
        <div class="substrate-col">
            <div class="substrate-cross" style="top: 25%;"></div>
            <div class="substrate-cross" style="top: 75%;"></div>
        </div>
        <div class="substrate-col"></div>
        <div></div>
    </div>

    <!-- ============================================================
         HEADER TECNICO: ALLINEAMENTO E GIUNTO
         ============================================================ -->
    <header class="fixed top-0 left-0 w-full z-50 bg-[#F5F5F3]/90 backdrop-blur-md border-b border-osso-line" id="main-header">
        <div class="max-w-[88rem] mx-auto px-6 h-20 flex justify-between items-center">
            
            <!-- Marchio a incastro: Persona e Specialità -->
            <a href="#home" class="nav-trigger group flex items-center gap-4 cursor-pointer" data-target="home">
                <div class="w-9 h-9 border border-osso-dark flex items-center justify-center font-mono text-xs font-semibold bg-white group-hover:bg-osso-teal group-hover:text-white transition-colors duration-300">
                    MN
                </div>
                <div class="flex flex-col">
                    <span class="font-serif text-lg tracking-tight text-osso-dark font-medium leading-tight">Dott. Michele Novi</span>
                    <span class="font-mono text-[9px] uppercase tracking-widest text-osso-muted mt-0.5">Spalla e Arto Superiore · CESAT</span>
                </div>
            </a>

            <!-- Navigazione: Scheletro Bibbia esatto -->
            <nav class="hidden lg:flex items-center gap-1 font-mono text-[11px] uppercase tracking-wider text-osso-dark">
                <a href="#chi-sono" class="nav-trigger px-4 py-2 border border-transparent hover:border-osso-line hover:bg-white transition-all" data-target="chi-sono">Chi sono</a>
                <a href="#patologie" class="nav-trigger px-4 py-2 border border-transparent hover:border-osso-line hover:bg-white transition-all" data-target="patologie">Cosa curo</a>
                <a href="#sedi" class="nav-trigger px-4 py-2 border border-transparent hover:border-osso-line hover:bg-white transition-all" data-target="sedi">Dove ricevo</a>
                <a href="#articoli" class="nav-trigger px-4 py-2 border border-transparent hover:border-osso-line hover:bg-white transition-all" data-target="articoli">Note cliniche</a>
                <a href="#contatti" class="nav-trigger px-4 py-2 border border-transparent hover:border-osso-line hover:bg-white transition-all" data-target="contatti">Contatti</a>
            </nav>

            <!-- CTA Segreteria ad aggancio rapido -->
            <div class="flex items-center gap-3">
                <a href="tel:+393484331733" class="hidden sm:inline-flex items-center gap-2 px-3 py-1.5 border border-osso-line bg-white font-mono text-[10px] text-osso-muted uppercase tracking-wider hover:border-osso-dark transition-colors">
                    <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
                    <span>348 4331733</span>
                </a>
                <a href="#contatti" class="nav-trigger btn-interlock btn-interlock-teal !py-2 !px-4" data-target="contatti">
                    <span>Prenota Visita</span>
                    <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                </a>
            </div>
        </div>
    </header>

    <!-- ============================================================
         CONTENUTO PRINCIPALE SPA
         ============================================================ -->
    <main class="relative z-10 pt-20" id="app-root">

        <!-- ========================================================
             VISTA 1: HOME (IL VARCO + ARCHITETTURA A STRATI)
             ======================================================== -->
        <section id="view-home" class="page-view active-view">
            
            <!-- STRATO 01: IL VARCO HERO -->
            <div class="min-h-[calc(100vh-5rem)] max-w-[88rem] mx-auto px-6 py-12 flex flex-col justify-between">
                
                <!-- Barra di stato e coordinate (Osso puro) -->
                <div class="flex flex-wrap justify-between items-center text-[10px] font-mono uppercase tracking-widest text-osso-muted border-b border-osso-line pb-4 pt-2">
                    <div class="flex items-center gap-4">
                        <span class="text-osso-dark font-semibold">REF: DOTT-MICHELE-NOVI</span>
                        <span>·</span>
                        <span>ORDINE MEDICI PISA N. 5988</span>
                    </div>
                    <div class="flex items-center gap-6">
                        <span>ATTIVITÀ CHIRURGICA: CESAT FUCECCHIO</span>
                        <span>·</span>
                        <span class="text-osso-teal font-medium">APPROCCIO ARTROSCOPICO MINI-INVASIVO</span>
                    </div>
                </div>

                <!-- Modulo Master a Incastro: Titolo e Finestra Varco -->
                <div class="grid lg:grid-cols-12 gap-8 my-auto py-8 items-center">
                    
                    <!-- Superficie A: La Voce e il Gesto -->
                    <div class="lg:col-span-7 space-y-8 pr-0 lg:pr-8">
                        <div class="inline-flex items-center gap-2 border border-osso-line bg-white px-3 py-1 text-[10px] font-mono uppercase tracking-widest text-osso-dark">
                            <span class="w-2 h-2 bg-osso-teal"></span>
                            <span>Chirurgia dell'Arto Superiore · Traumatologia</span>
                        </div>

                        <h1 class="text-4xl sm:text-6xl xl:text-7xl font-serif font-light text-osso-dark leading-[1.02] tracking-tight">
                            Rigore chirurgico,<br>
                            <span class="italic text-osso-teal">due superfici</span><br>
                            che tornano a combaciare.
                        </h1>

                        <p class="text-lg sm:text-xl font-light text-osso-muted max-w-xl leading-relaxed">
                            Trattamento della patologia della spalla, del gomito e della mano. 
                            Dalla chirurgia artroscopica e protesica alla medicina dello sport, 
                            con la precisione di chi non forza il movimento ma ne ripristina la stabilità.
                        </p>

                        <!-- Giunto di chiamata rapida -->
                        <div class="flex flex-wrap gap-4 pt-2">
                            <a href="#patologie" class="nav-trigger btn-interlock" data-target="patologie">
                                <span>Esplora Patologie</span>
                                <span class="font-mono text-xs opacity-60">[01]</span>
                            </a>
                            <a href="#sedi" class="nav-trigger btn-interlock btn-interlock-teal" data-target="sedi">
                                <span>Le Sedi in Toscana</span>
                                <span class="font-mono text-xs opacity-60">[02]</span>
                            </a>
                        </div>
                    </div>

                    <!-- Superficie B: Il Varco Ottico (Incastrato con quote da sala) -->
                    <div class="lg:col-span-5">
                        <div class="relative border border-osso-line bg-white p-3 shadow-sm">
                            
                            <!-- Metadati angolari a incastro -->
                            <div class="flex justify-between items-center text-[9px] font-mono uppercase text-osso-muted mb-2 px-1">
                                <span>FIELD: ACCESS-01</span>
                                <span>LATERAL PORTAL · 30° OPTICS</span>
                            </div>

                            <!-- Finestra Varco -->
                            <div class="varco-portal aspect-[4/5] bg-osso-surface relative">
                                <img src="https://images.unsplash.com/photo-1579684385127-1ef15d508118?q=80&w=1000&auto=format&fit=crop" 
                                     alt="Dott. Michele Novi" 
                                     class="varco-image w-full h-full object-cover object-center">
                                
                                <!-- Reticolo ottico (Luce in cavità) -->
                                <div class="absolute inset-0 pointer-events-none border border-white/20 m-6 flex items-center justify-center">
                                    <div class="w-12 h-12 border border-white/40 rounded-full flex items-center justify-center">
                                        <div class="w-1.5 h-1.5 bg-osso-teal rounded-full"></div>
                                    </div>
                                </div>
                            </div>

                            <div class="mt-3 px-1 flex justify-between items-center font-mono text-[10px] text-osso-dark">
                                <span class="font-medium">Dott. Michele Novi</span>
                                <span class="text-osso-muted">Pisa · Fucecchio · Valdera</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Barra inferiore: La costellazione dei tre principi -->
                <div class="grid grid-cols-1 md:grid-cols-3 border-t border-osso-line pt-6 gap-6 text-xs font-mono">
                    <div class="flex items-start gap-3">
                        <span class="text-osso-teal font-bold">01/</span>
                        <div>
                            <strong class="block text-osso-dark uppercase">Il Varco (Accesso Preciso)</strong>
                            <span class="text-osso-muted">Minima invasività: intervenire esattamente dove l'articolazione ha ceduto.</span>
                        </div>
                    </div>
                    <div class="flex items-start gap-3">
                        <span class="text-osso-teal font-bold">02/</span>
                        <div>
                            <strong class="block text-osso-dark uppercase">La Congruenza (L'Incastro)</strong>
                            <span class="text-osso-muted">Stabilità naturale tra testa omerale e glenoide senza sacrificare il movimento.</span>
                        </div>
                    </div>
                    <div class="flex items-start gap-3">
                        <span class="text-osso-teal font-bold">03/</span>
                        <div>
                            <strong class="block text-osso-dark uppercase">L'Osso Sotto (Metodo)</strong>
                            <span class="text-osso-muted">Diagnostica ecografica e clinica accurata prima di ogni decisione chirurgica.</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ========================================================
                 STRATO 02: L'INCASTRO CLINICO (WIDGET INTERATTIVO)
                 Dimostrazione visiva di due superfici che combaciano
                 ======================================================== -->
            <div class="border-t border-osso-line bg-white py-24 px-6">
                <div class="max-w-[88rem] mx-auto">
                    
                    <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 pb-6 border-b border-osso-line gap-6">
                        <div>
                            <span class="font-mono text-xs uppercase tracking-widest text-osso-teal block mb-2">[ MECCANICA ARTICOLARE ]</span>
                            <h2 class="text-3xl sm:text-5xl font-serif text-osso-dark">L'Incastro: stabilità e congruenza.</h2>
                        </div>
                        <p class="text-sm font-mono text-osso-muted max-w-md">
                            Una spalla funziona quando le sue superfici combaciano al millimetro. L'instabilità è il fallimento dell'incastro; la chirurgia è il ripristino del contatto.
                        </p>
                    </div>

                    <!-- Componente Incastro Dimostrativo -->
                    <div class="grid lg:grid-cols-2 gap-8 items-stretch">
                        
                        <!-- Scheda Interattiva Congruenza (Testa e Glenoide) -->
                        <div class="joint-socket p-8 flex flex-col justify-between min-h-[380px]">
                            <div>
                                <div class="flex justify-between items-start mb-8">
                                    <span class="font-mono text-xs text-osso-muted uppercase tracking-widest">PROVA DI CONGRUENZA 01</span>
                                    <span class="joint-status-badge font-mono text-[10px] uppercase tracking-widest px-3 py-1 border border-osso-line bg-osso-base">
                                        Passa col mouse per allineare
                                    </span>
                                </div>

                                <div class="flex items-center justify-center my-12 relative">
                                    <!-- Glenoide (Superficie ricevente / Concava) -->
                                    <div class="w-32 h-44 border-2 border-dashed border-osso-teal/60 rounded-r-full flex items-center justify-start pl-3">
                                        <span class="font-mono text-[9px] uppercase tracking-wider text-osso-teal transform -rotate-90">Glenoide</span>
                                    </div>
                                    <!-- Testa omerale mobile (Superficie convessa) -->
                                    <div class="joint-head w-36 h-36 rounded-full bg-osso-teal/10 border-2 border-osso-teal flex items-center justify-center -ml-12 shadow-sm">
                                        <div class="text-center">
                                            <span class="font-serif italic text-osso-teal text-lg block">Testa</span>
                                            <span class="font-mono text-[8px] uppercase tracking-widest text-osso-dark">Omerale</span>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="border-t border-osso-line pt-4 flex justify-between items-center text-xs font-mono">
                                <span class="text-osso-muted">EFFETTO CLINICO:</span>
                                <span class="text-osso-dark font-medium">Contatto anatomico ristabilito · ROM preservato</span>
                            </div>
                        </div>

                        <!-- Spiegazione Clinica Rigorosa (Dal paper Remplissage) -->
                        <div class="border border-osso-line p-8 flex flex-col justify-between bg-osso-base">
                            <div class="space-y-6">
                                <span class="font-mono text-xs text-osso-teal uppercase tracking-widest block">[ IL DUBBIO CLINICO ]</span>
                                <h3 class="text-2xl font-serif text-osso-dark">Nelle lussazioni recidivanti, l'osso non deve ingranare nel vuoto.</h3>
                                <p class="text-sm text-osso-muted leading-relaxed">
                                    Quando la testa dell'omero perde sostanza ossea (lesione di Hill-Sachs), rischia di "incastrarsi" oltre il bordo della glenoide durante il movimento, provocando la lussazione.
                                </p>
                                <p class="text-sm text-osso-muted leading-relaxed">
                                    Con la procedura di <strong class="text-osso-dark">Remplissage</strong> si riempie il difetto extra-articolare con il tendine dell'infraspinato, trasformando un giunto instabile in una superficie congruente e solida.
                                </p>
                            </div>

                            <div class="pt-6 border-t border-osso-line flex items-center justify-between">
                                <span class="font-mono text-[10px] text-osso-muted">PUBBLICAZIONE: OSTEOLOGY 2022</span>
                                <a href="#articoli-remplissage" class="nav-trigger text-xs font-mono text-osso-teal underline uppercase tracking-wider" data-target="articoli-remplissage">
                                    Leggi la nota clinica →
                                </a>
                            </div>
                        </div>

                    </div>
                </div>
            </div>

            <!-- ========================================================
                 STRATO 03: I QUATTRO LIVELLI ANATOMICI (SEZIONI STACKED)
                 Dimostrazione tangibile di "uno strato sotto l'altro"
                 ======================================================== -->
            <div class="max-w-[88rem] mx-auto px-6 py-28">
                
                <div class="mb-16">
                    <span class="font-mono text-xs uppercase tracking-widest text-osso-teal block mb-2">[ ANATOMIA APPLICATA ]</span>
                    <h2 class="text-3xl sm:text-5xl font-serif text-osso-dark">Uno strato sotto l'altro.</h2>
                    <p class="text-sm font-mono text-osso-muted mt-2 max-w-xl">
                        In chirurgia non esiste una sola superficie: ogni livello ha un ruolo, una biomeccanica e una soluzione terapeutica dedicata.
                    </p>
                </div>

                <!-- Pila a strati fisici (Stacked Cards) -->
                <div class="space-y-8 relative">
                    
                    <!-- STRATO 1: CUTE E ACCESSO MINI-INVASIVO -->
                    <div class="stratum-card p-8 md:p-12">
                        <div class="grid md:grid-cols-12 gap-8 items-center">
                            <div class="md:col-span-3 font-mono">
                                <span class="text-3xl font-serif italic text-osso-teal block">01</span>
                                <span class="text-xs uppercase tracking-widest text-osso-dark font-semibold">Lo Strato di Superficie</span>
                                <span class="text-[10px] text-osso-muted block mt-1">L'Accesso Artroscopico</span>
                            </div>
                            <div class="md:col-span-6 space-y-2">
                                <h4 class="text-xl font-serif text-osso-dark">Incisioni millimetriche, rispetto biologico dei tessuti molli.</h4>
                                <p class="text-sm text-osso-muted leading-relaxed">
                                    Non si seziona la muscolatura. Si entra attraverso portali di 5 mm che guidano l'ottica e gli strumenti dedicati, riducendo dolore post-operatorio e tempi di recupero.
                                </p>
                            </div>
                            <div class="md:col-span-3 font-mono text-right text-xs">
                                <span class="border border-osso-line px-3 py-1 bg-white text-osso-dark uppercase text-[10px]">Strato 01 // Cute</span>
                            </div>
                        </div>
                    </div>

                    <!-- STRATO 2: IL PIANO TENDINEO E LA CUFFIA -->
                    <div class="stratum-card p-8 md:p-12">
                        <div class="grid md:grid-cols-12 gap-8 items-center">
                            <div class="md:col-span-3 font-mono">
                                <span class="text-3xl font-serif italic text-osso-teal block">02</span>
                                <span class="text-xs uppercase tracking-widest text-osso-dark font-semibold">Il Motore Biomeccanico</span>
                                <span class="text-[10px] text-osso-muted block mt-1">Cuffia dei Rotatori</span>
                            </div>
                            <div class="md:col-span-6 space-y-2">
                                <h4 class="text-xl font-serif text-osso-dark">Riparazione tendinea anatomica con ancore riassorbibili.</h4>
                                <p class="text-sm text-osso-muted leading-relaxed">
                                    Diagnosi differenziale tra lesioni riparabili e irreparabili. Scelta mirata tra sutura artroscopica, release capsulare o trattamenti rigenerativi in base all'età biologica del tendine.
                                </p>
                            </div>
                            <div class="md:col-span-3 font-mono text-right text-xs">
                                <span class="border border-osso-line px-3 py-1 bg-white text-osso-teal uppercase text-[10px]">Strato 02 // Tendine</span>
                            </div>
                        </div>
                    </div>

                    <!-- STRATO 3: LA CAPSULA E IL CERCINE GLENOIDEO -->
                    <div class="stratum-card p-8 md:p-12">
                        <div class="grid md:grid-cols-12 gap-8 items-center">
                            <div class="md:col-span-3 font-mono">
                                <span class="text-3xl font-serif italic text-osso-teal block">03</span>
                                <span class="text-xs uppercase tracking-widest text-osso-dark font-semibold">Il Sigillo Articolare</span>
                                <span class="text-[10px] text-osso-muted block mt-1">Capsula e Cercine</span>
                            </div>
                            <div class="md:col-span-6 space-y-2">
                                <h4 class="text-xl font-serif text-osso-dark">Riparazione di Bankart e ritensionamento capsulare.</h4>
                                <p class="text-sm text-osso-muted leading-relaxed">
                                    Il cercine fibrocartilagineo approfondisce la cavità glenoidea. Ripristinarne l'inserzione è indispensabile negli atleti soggetti a instabilità e traumi da contatto.
                                </p>
                            </div>
                            <div class="md:col-span-3 font-mono text-right text-xs">
                                <span class="border border-osso-line px-3 py-1 bg-white text-osso-dark uppercase text-[10px]">Strato 03 // Capsula</span>
                            </div>
                        </div>
                    </div>

                    <!-- STRATO 4: L'OSSO E LA CHIRURGIA PROTESICA -->
                    <div class="stratum-card p-8 md:p-12">
                        <div class="grid md:grid-cols-12 gap-8 items-center">
                            <div class="md:col-span-3 font-mono">
                                <span class="text-3xl font-serif italic text-osso-teal block">04</span>
                                <span class="text-xs uppercase tracking-widest text-osso-dark font-semibold">La Struttura Portante</span>
                                <span class="text-[10px] text-osso-muted block mt-1">Osso e Artroplastica</span>
                            </div>
                            <div class="md:col-span-6 space-y-2">
                                <h4 class="text-xl font-serif text-osso-dark">Chirurgia protesica anatomica e inversa di spalla.</h4>
                                <p class="text-sm text-osso-muted leading-relaxed">
                                    Quando l'artrosi o la rottura massiva della cuffia distruggono il fulcro osseo, la protesi inversa inverte la biomeccanica per restituire l'elevazione dell'arto sfruttando il deltoide.
                                </p>
                            </div>
                            <div class="md:col-span-3 font-mono text-right text-xs">
                                <span class="border border-osso-line px-3 py-1 bg-white text-osso-teal uppercase text-[10px]">Strato 04 // Osso</span>
                            </div>
                        </div>
                    </div>

                </div>
            </div>

            <!-- ANTEPRIMA SEDI CON INCASTRO MONOLITICO -->
            <div class="border-t border-osso-line bg-[#EAEBE8] py-20 px-6">
                <div class="max-w-[88rem] mx-auto">
                    <div class="flex justify-between items-end mb-12">
                        <div>
                            <span class="font-mono text-xs uppercase tracking-widest text-osso-teal block mb-1">COSTELLAZIONE AMBULATORIALE</span>
                            <h3 class="text-2xl sm:text-4xl font-serif text-osso-dark">Punti di contatto sul territorio.</h3>
                        </div>
                        <a href="#sedi" class="nav-trigger text-xs font-mono uppercase tracking-wider text-osso-dark underline hover:text-osso-teal" data-target="sedi">
                            Tutte le sedi →
                        </a>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-3 gap-0 border border-osso-line">
                        <div class="joint-item p-6">
                            <span class="text-[10px] font-mono text-osso-teal uppercase">CHIRURGIA E RICOVERI</span>
                            <h4 class="text-xl font-serif text-osso-dark mt-2 mb-1">CESAT Fucecchio</h4>
                            <p class="text-xs text-osso-muted font-mono">Ospedale San Pietro Igneo · Piazza Lavagnini 5</p>
                        </div>
                        <div class="joint-item p-6">
                            <span class="text-[10px] font-mono text-osso-dark uppercase">AMBULATORIO PRINCIPALE</span>
                            <h4 class="text-xl font-serif text-osso-dark mt-2 mb-1">Studi Medici San Pietro</h4>
                            <p class="text-xs text-osso-muted font-mono">Fucecchio · Piazza Lavagnini 6</p>
                        </div>
                        <div class="joint-item p-6">
                            <span class="text-[10px] font-mono text-osso-muted uppercase">AMBULATORI VALDERA & PISA</span>
                            <h4 class="text-xl font-serif text-osso-dark mt-2 mb-1">Peccioli · Fornacette · Pisa</h4>
                            <p class="text-xs text-osso-muted font-mono">San Verano · Fisiomed · Athletica</p>
                        </div>
                    </div>
                </div>
            </div>

        </section>

        <!-- ========================================================
             VISTA 2: CHI SONO (RIGORE, HARBORVIEW, CESAT, DUE TEMPI)
             ======================================================== -->
        <section id="view-chi-sono" class="page-view max-w-[88rem] mx-auto px-6 py-16">
            
            <a href="#home" class="nav-trigger text-xs font-mono uppercase tracking-widest text-osso-muted hover:text-osso-dark block mb-8" data-target="home">
                ← Torna all'accesso principale
            </a>

            <!-- Header Chi Sono a Incastro -->
            <div class="border-b border-osso-line pb-12 mb-16 grid lg:grid-cols-12 gap-8 items-end">
                <div class="lg:col-span-8">
                    <span class="font-mono text-xs uppercase tracking-widest text-osso-teal block mb-3">[ IDENTITÀ & CLINICA ]</span>
                    <h1 class="text-4xl sm:text-6xl font-serif text-osso-dark font-light leading-tight">
                        Chirurgo ortopedico,<br>
                        <span class="italic text-osso-teal">scienza applicata al movimento.</span>
                    </h1>
                </div>
                <div class="lg:col-span-4 font-mono text-xs text-osso-muted leading-relaxed">
                    «Non separo la sala operatoria dal territorio. Il rigore acquisito nella ricerca internazionale è lo stesso che guida dieci minuti di visita in ambulatorio.»
                </div>
            </div>

            <!-- Due Colonne a Incastro: Il Profilo e la Timeline -->
            <div class="grid lg:grid-cols-12 gap-12 items-start">
                
                <!-- Colonna Sinistra: Ritratto Clinico e Dati Istituzionali -->
                <div class="lg:col-span-5 space-y-8">
                    <div class="border border-osso-line bg-white p-3">
                        <div class="aspect-[3/4] bg-osso-surface overflow-hidden">
                            <img src="https://images.unsplash.com/photo-1622253692010-333f2da6031d?q=80&w=800&auto=format&fit=crop" 
                                 alt="Dott. Michele Novi" 
                                 class="w-full h-full object-cover filter grayscale-[20%]">
                        </div>
                        <div class="p-4 border-t border-osso-line mt-3 font-mono text-xs space-y-1">
                            <div class="text-osso-dark font-semibold">Dott. Michele Novi</div>
                            <div class="text-osso-muted">Specialista in Ortopedia e Traumatologia</div>
                            <div class="text-[10px] text-osso-teal pt-1">Diploma Nazionale Ecografia SIUMB</div>
                        </div>
                    </div>

                    <!-- Scheda Valori della Bibbia: Due Tempi -->
                    <div class="border border-osso-line p-6 bg-white space-y-3 font-mono text-xs">
                        <span class="text-osso-teal font-bold uppercase block">[ DUE TEMPI ]</span>
                        <p class="text-osso-muted leading-relaxed">
                            <strong>La Sala di Volume:</strong> Ospedale CESAT di Fucecchio, centro di riferimento toscano per la chirurgia protesica e artroscopica.
                        </p>
                        <p class="text-osso-muted leading-relaxed">
                            <strong>Il Territorio:</strong> Gli ambulatori della Valdera e dell'Empolese, per la diagnosi precoce, le infiltrazioni e il follow-up continuo.
                        </p>
                    </div>
                </div>

                <!-- Colonna Destra: Curriculum e Tappe Formative -->
                <div class="lg:col-span-7 space-y-12">
                    
                    <div class="prose max-w-none text-osso-dark space-y-6 text-base sm:text-lg font-light leading-relaxed">
                        <p>
                            Mi sono laureato e specializzato con lode presso l'<strong>Università di Pisa</strong>, allievo della scuola del Prof. Porcellini e collaboratore del Dott. Nicoletti. Ho completato il mio percorso con fellowship internazionali dedicate alla traumatologia complessa e alla chirurgia d'avanguardia della spalla e del gomito.
                        </p>
                        <p>
                            La mia esperienza presso l'<strong>Harborview Medical Center di Seattle (USA)</strong> mi ha permesso di approfondire la microchirurgia dei lembi e il trattamento delle lesioni nervose e muscoloscheletriche più severe.
                        </p>
                    </div>

                    <!-- Timeline a Griglia Monolitica -->
                    <div class="border-t border-osso-line pt-8">
                        <span class="font-mono text-xs uppercase tracking-widest text-osso-teal block mb-6">[ FORMAZIONE E FELLOWSHIP ]</span>
                        
                        <div class="space-y-6">
                            <div class="border-l-2 border-osso-teal pl-6 space-y-1">
                                <span class="font-mono text-xs text-osso-muted">2020 – PRESENTE</span>
                                <h4 class="text-lg font-serif font-medium text-osso-dark">Dirigente Medico Ortopedico · Ospedale CESAT Fucecchio</h4>
                                <p class="text-xs font-mono text-osso-muted">Attività chirurgica di elezione e protesica, centro regionale artroplastica.</p>
                            </div>

                            <div class="border-l-2 border-osso-line pl-6 space-y-1">
                                <span class="font-mono text-xs text-osso-muted">FELLOWSHIP USA</span>
                                <h4 class="text-lg font-serif font-medium text-osso-dark">Harborview Medical Center · Seattle (Washington, USA)</h4>
                                <p class="text-xs font-mono text-osso-muted">Traumatologia ad alta energia e microchirurgia ricostruttiva arto superiore.</p>
                            </div>

                            <div class="border-l-2 border-osso-line pl-6 space-y-1">
                                <span class="font-mono text-xs text-osso-muted">FELLOWSHIP UK & GERMANIA</span>
                                <h4 class="text-lg font-serif font-medium text-osso-dark">Londra e Charité Berlino</h4>
                                <p class="text-xs font-mono text-osso-muted">Focus su tecniche artroscopiche mini-invasive e spalla dello sportivo.</p>
                            </div>

                            <div class="border-l-2 border-osso-line pl-6 space-y-1">
                                <span class="font-mono text-xs text-osso-muted">SOCIETÀ SCIENTIFICHE</span>
                                <h4 class="text-lg font-serif font-medium text-osso-dark">Socio Ordinario SIAGASCOT e SICSEG</h4>
                                <p class="text-xs font-mono text-osso-muted">Partecipazione attiva a congressi e pubblicazioni internazionali peer-reviewed.</p>
                            </div>
                        </div>
                    </div>

                </div>

            </div>

        </section>

        <!-- ========================================================
             VISTA 3: PATOLOGIE / COSA CURO (HUB INFORMATIVO)
             ======================================================== -->
        <section id="view-patologie" class="page-view max-w-[88rem] mx-auto px-6 py-16">
            
            <a href="#home" class="nav-trigger text-xs font-mono uppercase tracking-widest text-osso-muted hover:text-osso-dark block mb-8" data-target="home">
                ← Torna all'accesso principale
            </a>

            <div class="border-b border-osso-line pb-8 mb-12 flex flex-col md:flex-row md:items-end justify-between gap-6">
                <div>
                    <span class="font-mono text-xs uppercase tracking-widest text-osso-teal block mb-2">[ AREE DI SPECIALIZZAZIONE ]</span>
                    <h1 class="text-4xl sm:text-6xl font-serif text-osso-dark font-light">Cosa curo.</h1>
                </div>
                <p class="font-mono text-xs text-osso-muted max-w-md">
                    Sei percorsi clinici basati su diagnosi strumentale, indicazione chiara (conservativo vs chirurgico) e recupero funzionale monitorato.
                </p>
            </div>

            <!-- Griglia a Incastro: Le 6 Patologie della Bibbia -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-0 border border-osso-line">
                
                <!-- 1. SPALLA -->
                <a href="#patologie-spalla" class="nav-trigger joint-item p-8 flex flex-col justify-between min-h-[320px] group" data-target="patologie-spalla">
                    <div>
                        <div class="flex justify-between items-center text-xs font-mono text-osso-muted mb-6">
                            <span>AREA 01</span>
                            <span class="text-osso-teal font-semibold group-hover:translate-x-1 transition-transform">Esplora →</span>
                        </div>
                        <h3 class="text-2xl font-serif text-osso-dark group-hover:text-osso-teal transition-colors">Chirurgia della Spalla</h3>
                        <p class="text-xs text-osso-muted font-sans mt-3 leading-relaxed">
                            Cuffia dei rotatori, instabilità e lussazioni recidivanti (Bankart, Remplissage), artrosi e protesi anatomica o inversa.
                        </p>
                    </div>
                    <div class="pt-6 border-t border-osso-line/60 font-mono text-[10px] text-osso-muted uppercase flex justify-between">
                        <span>CORE PRATICA</span>
                        <span>CESAT FUCECCHIO</span>
                    </div>
                </a>

                <!-- 2. GOMITO -->
                <a href="#patologie-gomito" class="nav-trigger joint-item p-8 flex flex-col justify-between min-h-[320px] group" data-target="patologie-gomito">
                    <div>
                        <div class="flex justify-between items-center text-xs font-mono text-osso-muted mb-6">
                            <span>AREA 02</span>
                            <span class="text-osso-teal font-semibold group-hover:translate-x-1 transition-transform">Esplora →</span>
                        </div>
                        <h3 class="text-2xl font-serif text-osso-dark group-hover:text-osso-teal transition-colors">Gomito: Traumi e Artroscopia</h3>
                        <p class="text-xs text-osso-muted font-sans mt-3 leading-relaxed">
                            Epicondilite resistente, fratture del capitello radiale, rotture del tendine distale del bicipite e rigidità post-traumatica.
                        </p>
                    </div>
                    <div class="pt-6 border-t border-osso-line/60 font-mono text-[10px] text-osso-muted uppercase flex justify-between">
                        <span>MINI-INVASIVO</span>
                        <span>ARTROSCOPIA GOMITO</span>
                    </div>
                </a>

                <!-- 3. MANO E POLSO -->
                <a href="#patologie-mano" class="nav-trigger joint-item p-8 flex flex-col justify-between min-h-[320px] group" data-target="patologie-mano">
                    <div>
                        <div class="flex justify-between items-center text-xs font-mono text-osso-muted mb-6">
                            <span>AREA 03</span>
                            <span class="text-osso-teal font-semibold group-hover:translate-x-1 transition-transform">Esplora →</span>
                        </div>
                        <h3 class="text-2xl font-serif text-osso-dark group-hover:text-osso-teal transition-colors">Mano e Polso</h3>
                        <p class="text-xs text-osso-muted font-sans mt-3 leading-relaxed">
                            Tunnel carpale, dito a scatto, rizoartrosi del pollice, lesioni legamentose scafo-lunari e tendiniti di De Quervain.
                        </p>
                    </div>
                    <div class="pt-6 border-t border-osso-line/60 font-mono text-[10px] text-osso-muted uppercase flex justify-between">
                        <span>MICROCHIRURGIA</span>
                        <span>DECOMPRESSIONI NERVOSE</span>
                    </div>
                </a>

                <!-- 4. TRAUMATOLOGIA SPORTIVA -->
                <a href="#patologie-traumatologia-sportiva" class="nav-trigger joint-item p-8 flex flex-col justify-between min-h-[320px] group" data-target="patologie-traumatologia-sportiva">
                    <div>
                        <div class="flex justify-between items-center text-xs font-mono text-osso-muted mb-6">
                            <span>AREA 04</span>
                            <span class="text-osso-teal font-semibold group-hover:translate-x-1 transition-transform">Esplora →</span>
                        </div>
                        <h3 class="text-2xl font-serif text-osso-dark group-hover:text-osso-teal transition-colors">Traumatologia Sportiva</h3>
                        <p class="text-xs text-osso-muted font-sans mt-3 leading-relaxed">
                            Lesioni da contatto, lussazioni acromion-claveari, sovraccarico funzionale negli atleti di lancio, arrampicata, tennis e motorsport.
                        </p>
                    </div>
                    <div class="pt-6 border-t border-osso-line/60 font-mono text-[10px] text-osso-muted uppercase flex justify-between">
                        <span>ATHLETICA PISA</span>
                        <span>RETURN TO PLAY</span>
                    </div>
                </a>

                <!-- 5. CHIRURGIA ARTROSCOPICA (IL METODO) -->
                <a href="#patologie-artroscopia" class="nav-trigger joint-item p-8 flex flex-col justify-between min-h-[320px] group" data-target="patologie-artroscopia">
                    <div>
                        <div class="flex justify-between items-center text-xs font-mono text-osso-muted mb-6">
                            <span>AREA 05</span>
                            <span class="text-osso-teal font-semibold group-hover:translate-x-1 transition-transform">Esplora →</span>
                        </div>
                        <h3 class="text-2xl font-serif text-osso-dark group-hover:text-osso-teal transition-colors">Chirurgia Artroscopica</h3>
                        <p class="text-xs text-osso-muted font-sans mt-3 leading-relaxed">
                            Metodologia mini-invasiva a visione diretta: diagnosi endoscopica ad alta definizione e riparazioni interne senza incisioni a cielo aperto.
                        </p>
                    </div>
                    <div class="pt-6 border-t border-osso-line/60 font-mono text-[10px] text-osso-muted uppercase flex justify-between">
                        <span>TECNICA D'ELEZIONE</span>
                        <span>MINIMA INVASIVITÀ</span>
                    </div>
                </a>

                <!-- 6. ECOGRAFIA MUSCOLOSCHELETRICA -->
                <a href="#patologie-ecografia-muscoloscheletrica" class="nav-trigger joint-item p-8 flex flex-col justify-between min-h-[320px] group" data-target="patologie-ecografia-muscoloscheletrica">
                    <div>
                        <div class="flex justify-between items-center text-xs font-mono text-osso-muted mb-6">
                            <span>AREA 06</span>
                            <span class="text-osso-teal font-semibold group-hover:translate-x-1 transition-transform">Esplora →</span>
                        </div>
                        <h3 class="text-2xl font-serif text-osso-dark group-hover:text-osso-teal transition-colors">Ecografia Muscoloscheletrica</h3>
                        <p class="text-xs text-osso-muted font-sans mt-3 leading-relaxed">
                            Diagnostica "al letto del paziente" con ecografo dedicato e infiltrazioni eco-guidate per la massima precisione anatomica dell'infiltrato.
                        </p>
                    </div>
                    <div class="pt-6 border-t border-osso-line/60 font-mono text-[10px] text-osso-muted uppercase flex justify-between">
                        <span>SIUMB</span>
                        <span>TERAPIA INFILTRATIVA</span>
                    </div>
                </a>

            </div>

        </section>

        <!-- ========================================================
             SOTTO-VISTA: DETTAGLIO PATOLOGIA SPALLA
             ======================================================== -->
        <section id="view-patologie-spalla" class="page-view max-w-[70rem] mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger text-xs font-mono uppercase tracking-widest text-osso-muted hover:text-osso-dark block mb-8" data-target="patologie">
                ← Torna a tutte le patologie
            </a>
            
            <span class="font-mono text-xs uppercase tracking-widest text-osso-teal block mb-2">[ AREA CLINICA 01 ]</span>
            <h1 class="text-4xl sm:text-6xl font-serif text-osso-dark font-light mb-8">Chirurgia della spalla.</h1>
            
            <div class="space-y-8 text-base sm:text-lg font-light text-osso-dark leading-relaxed">
                <p>
                    La spalla è l'articolazione più mobile del corpo umano e proprio per questa sua escursione è la più soggetta a perdite di congruenza, usura tendinea e instabilità. Il mio approccio privilegia sempre una diagnosi differenziale rigorosa tra trattamento conservativo (fisioterapia mirata, infiltrazioni ecoguidate) e indicazione chirurgica artroscopica.
                </p>

                <div class="grid md:grid-cols-3 gap-6 my-12 not-prose font-mono text-xs">
                    <div class="border border-osso-line p-6 bg-white space-y-2">
                        <strong class="text-osso-teal block uppercase">Cuffia dei Rotatori</strong>
                        <p class="text-osso-muted text-[11px]">Riparazione artroscopica lesioni sovraspinato, sottoscapolare e infraspinato.</p>
                    </div>
                    <div class="border border-osso-line p-6 bg-white space-y-2">
                        <strong class="text-osso-teal block uppercase">Instabilità e Lussazioni</strong>
                        <p class="text-osso-muted text-[11px]">Procedura di Bankart e Remplissage per atleti e lesioni ossee di Hill-Sachs.</p>
                    </div>
                    <div class="border border-osso-line p-6 bg-white space-y-2">
                        <strong class="text-osso-teal block uppercase">Chirurgia Protesica</strong>
                        <p class="text-osso-muted text-[11px]">Artroplastica anatomica e inversa di spalla per artrosi primaria o fratture complesse.</p>
                    </div>
                </div>

                <h3 class="text-2xl font-serif text-osso-dark pt-6">Quando operare e quando attendere</h3>
                <p>
                    Non tutte le rotture tendinee richiedono la sala operatoria. L'indicazione dipende dall'età biologica, dalla sintomatologia dolorosa notturna e dalla richiesta funzionale del paziente. Se la forza residua e la qualità del tessuto lo consentono, un percorso riabilitativo coordinato con i fisioterapisti sul territorio è sempre la prima scelta.
                </p>
            </div>

            <div class="border-t border-osso-line mt-12 pt-8 flex justify-between items-center">
                <span class="font-mono text-xs text-osso-muted">Visite a Fucecchio, Peccioli, Fornacette, Pisa</span>
                <a href="#contatti" class="nav-trigger btn-interlock btn-interlock-teal" data-target="contatti">
                    <span>Prenota Visita per la Spalla</span>
                </a>
            </div>
        </section>

        <!-- SOTTO-VISTA: GOMITO -->
        <section id="view-patologie-gomito" class="page-view max-w-[70rem] mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger text-xs font-mono uppercase tracking-widest text-osso-muted hover:text-osso-dark block mb-8" data-target="patologie">
                ← Torna a tutte le patologie
            </a>
            <span class="font-mono text-xs uppercase tracking-widest text-osso-teal block mb-2">[ AREA CLINICA 02 ]</span>
            <h1 class="text-4xl sm:text-6xl font-serif text-osso-dark font-light mb-8">Gomito: traumatologia e artroscopia.</h1>
            <p class="text-lg font-light text-osso-dark leading-relaxed">
                Trattamento di epicondilite, rigidità articolare post-traumatica e lesioni del bicipite distale. Il gomito richiede tolleranza chirurgica zero: anche pochi gradi di perdita di estensione impattano sulla vita quotidiana.
            </p>
        </section>

        <!-- SOTTO-VISTA: MANO -->
        <section id="view-patologie-mano" class="page-view max-w-[70rem] mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger text-xs font-mono uppercase tracking-widest text-osso-muted hover:text-osso-dark block mb-8" data-target="patologie">
                ← Torna a tutte le patologie
            </a>
            <span class="font-mono text-xs uppercase tracking-widest text-osso-teal block mb-2">[ AREA CLINICA 03 ]</span>
            <h1 class="text-4xl sm:text-6xl font-serif text-osso-dark font-light mb-8">Mano e polso.</h1>
            <p class="text-lg font-light text-osso-dark leading-relaxed">
                Formazione microchirurgica applicata alle patologie compressive nervose (tunnel carpale), tenosinoviti stenosanti (dito a scatto, De Quervain) e artrosi trapezio-metacarpale (rizoartrosi).
            </p>
        </section>

        <!-- SOTTO-VISTA: TRAUMATOLOGIA SPORTIVA -->
        <section id="view-patologie-traumatologia-sportiva" class="page-view max-w-[70rem] mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger text-xs font-mono uppercase tracking-widest text-osso-muted hover:text-osso-dark block mb-8" data-target="patologie">
                ← Torna a tutte le patologie
            </a>
            <span class="font-mono text-xs uppercase tracking-widest text-osso-teal block mb-2">[ AREA CLINICA 04 ]</span>
            <h1 class="text-4xl sm:text-6xl font-serif text-osso-dark font-light mb-8">Traumatologia sportiva.</h1>
            <p class="text-lg font-light text-osso-dark leading-relaxed">
                Consulenza e recupero per atleti amatoriali e professionisti. Collaborazione attiva con centri di medicina dello sport a Pisa (Athletica) per accelerare il return-to-play senza forzare i tempi biologici di guarigione legamentosa.
            </p>
        </section>

        <!-- SOTTO-VISTA: ARTROSCOPIA -->
        <section id="view-patologie-artroscopia" class="page-view max-w-[70rem] mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger text-xs font-mono uppercase tracking-widest text-osso-muted hover:text-osso-dark block mb-8" data-target="patologie">
                ← Torna a tutte le patologie
            </a>
            <span class="font-mono text-xs uppercase tracking-widest text-osso-teal block mb-2">[ AREA CLINICA 05 ]</span>
            <h1 class="text-4xl sm:text-6xl font-serif text-osso-dark font-light mb-8">Chirurgia artroscopica.</h1>
            <p class="text-lg font-light text-osso-dark leading-relaxed">
                La tecnica mini-invasiva di riferimento: attraverso piccole vie d'accesso ottiche si esegue la diagnosi palpatoria diretta dei tessuti e la loro fissazione millimetrica sotto controllo visivo continuo.
            </p>
        </section>

        <!-- SOTTO-VISTA: ECOGRAFIA -->
        <section id="view-patologie-ecografia-muscoloscheletrica" class="page-view max-w-[70rem] mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger text-xs font-mono uppercase tracking-widest text-osso-muted hover:text-osso-dark block mb-8" data-target="patologie">
                ← Torna a tutte le patologie
            </a>
            <span class="font-mono text-xs uppercase tracking-widest text-osso-teal block mb-2">[ AREA CLINICA 06 ]</span>
            <h1 class="text-4xl sm:text-6xl font-serif text-osso-dark font-light mb-8">Ecografia muscoloscheletrica.</h1>
            <p class="text-lg font-light text-osso-dark leading-relaxed">
                Certificazione nazionale SIUMB. L'ecografo in sede di visita consente di valutare dinamicamente il movimento dei tendini durante l'abduzione e di eseguire infiltrazioni mirate nel punto esatto dell'infiammazione.
            </p>
        </section>

        <!-- ========================================================
             VISTA 4: DOVE RICEVO (LE SEDI - COSTELLAZIONE REALE)
             ======================================================== -->
        <section id="view-sedi" class="page-view max-w-[88rem] mx-auto px-6 py-16">
            
            <a href="#home" class="nav-trigger text-xs font-mono uppercase tracking-widest text-osso-muted hover:text-osso-dark block mb-8" data-target="home">
                ← Torna all'accesso principale
            </a>

            <div class="border-b border-osso-line pb-8 mb-12 flex flex-col md:flex-row md:items-end justify-between gap-6">
                <div>
                    <span class="font-mono text-xs uppercase tracking-widest text-osso-teal block mb-2">[ COSTELLAZIONE SUL TERRITORIO ]</span>
                    <h1 class="text-4xl sm:text-6xl font-serif text-osso-dark font-light">Dove ricevo.</h1>
                </div>
                <p class="font-mono text-xs text-osso-muted max-w-md">
                    Una sola segreteria centrale, più sedi attive tra Valdera, Empolese e Pisa per essere vicini al paziente.
                </p>
            </div>

            <!-- Griglia Schede Sede a Incastro -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                
                <!-- SEDE 1: CESAT OSPEDALE FUCECCHIO (CHIRURGIA) -->
                <div class="border border-osso-line bg-white p-8 space-y-6">
                    <div class="flex justify-between items-start">
                        <span class="interlock-tab px-3 py-1 font-mono text-[9px] uppercase tracking-widest">
                            POLO CHIRURGICO D'ECCELLENZA
                        </span>
                        <span class="font-mono text-xs text-osso-muted">FUCECCHIO (FI)</span>
                    </div>

                    <div>
                        <h3 class="text-2xl font-serif text-osso-dark">CESAT · Ospedale San Pietro Igneo</h3>
                        <p class="text-xs font-mono text-osso-teal mt-1">Centro di Eccellenza Sostituzioni Articolari Toscana</p>
                    </div>

                    <div class="space-y-2 text-xs font-mono text-osso-muted border-t border-osso-line pt-4">
                        <div><strong>INDIRIZZO:</strong> Piazza Lavagnini, 5 · 50054 Fucecchio (FI)</div>
                        <div><strong>ATTIVITÀ:</strong> Interventi chirurgici in ricovero e day-surgery, artroscopia e protesica.</div>
                        <div><strong>PRENOTAZIONE SSN:</strong> Tramite CUP regionale o segreteria dedicata.</div>
                    </div>

                    <div class="pt-4 border-t border-osso-line flex items-center justify-between">
                        <span class="text-[10px] font-mono text-osso-muted">ACCESSIBILITÀ GARANTITA</span>
                        <a href="tel:+393484331733" class="btn-interlock !py-2 !px-4 text-[10px]">Info Ricoveri</a>
                    </div>
                </div>

                <!-- SEDE 2: STUDI MEDICI SAN PIETRO (AMBULATORIO LIBERA PROFESSIONE) -->
                <div class="border border-osso-line bg-white p-8 space-y-6">
                    <div class="flex justify-between items-start">
                        <span class="px-3 py-1 font-mono text-[9px] uppercase tracking-widest bg-osso-teal text-white">
                            AMBULATORIO PRINCIPALE
                        </span>
                        <span class="font-mono text-xs text-osso-muted">FUCECCHIO (FI)</span>
                    </div>

                    <div>
                        <h3 class="text-2xl font-serif text-osso-dark">Studi Medici San Pietro</h3>
                        <p class="text-xs font-mono text-osso-muted mt-1">Visite specialistiche, ecografie muscoloscheletriche e infiltrazioni</p>
                    </div>

                    <div class="space-y-2 text-xs font-mono text-osso-muted border-t border-osso-line pt-4">
                        <div><strong>INDIRIZZO:</strong> Piazza Lavagnini, 6 · 50054 Fucecchio (FI)</div>
                        <div><strong>ORARI:</strong> Su appuntamento tramite segreteria (Lunedì – Giovedì)</div>
                        <div><strong>TELEFONO:</strong> 348 4331733 (Segreteria diretta Dott. Novi)</div>
                    </div>

                    <div class="pt-4 border-t border-osso-line flex items-center justify-between">
                        <span class="text-[10px] font-mono text-osso-muted">PARCHEGGIO ADIACENTE</span>
                        <a href="#contatti" class="nav-trigger btn-interlock btn-interlock-teal !py-2 !px-4 text-[10px]" data-target="contatti">Prenota a Fucecchio</a>
                    </div>
                </div>

                <!-- SEDE 3: VALDERA (SAN VERANO PECCIOLI) -->
                <div class="border border-osso-line bg-white p-8 space-y-6">
                    <div class="flex justify-between items-start">
                        <span class="border border-osso-line px-3 py-1 font-mono text-[9px] uppercase tracking-widest text-osso-dark">
                            AMBULATORIO VALDERA
                        </span>
                        <span class="font-mono text-xs text-osso-muted">PECCIOLI (PI)</span>
                    </div>

                    <div>
                        <h3 class="text-2xl font-serif text-osso-dark">Polo San Verano</h3>
                        <p class="text-xs font-mono text-osso-muted mt-1">Visite ortopediche per l'alta Valdera e screening articolare</p>
                    </div>

                    <div class="space-y-2 text-xs font-mono text-osso-muted border-t border-osso-line pt-4">
                        <div><strong>INDIRIZZO:</strong> Località San Verano · Peccioli (PI)</div>
                        <div><strong>SERVIZI:</strong> Visita specialistica spalla/arto superiore, ecografia di supporto</div>
                    </div>

                    <div class="pt-4 border-t border-osso-line flex items-center justify-between">
                        <span class="text-[10px] font-mono text-osso-muted">TERRITORIO VALDERA</span>
                        <a href="#contatti" class="nav-trigger btn-interlock !py-2 !px-4 text-[10px]" data-target="contatti">Prenota a Peccioli</a>
                    </div>
                </div>

                <!-- SEDE 4: PISA (ATHLETICA / FISIOMED) -->
                <div class="border border-osso-line bg-white p-8 space-y-6">
                    <div class="flex justify-between items-start">
                        <span class="border border-osso-line px-3 py-1 font-mono text-[9px] uppercase tracking-widest text-osso-dark">
                            SPORT & TRAUMATOLOGIA
                        </span>
                        <span class="font-mono text-xs text-osso-muted">PISA & FORNACETTE</span>
                    </div>

                    <div>
                        <h3 class="text-2xl font-serif text-osso-dark">Athletica Pisa & Fisiomed</h3>
                        <p class="text-xs font-mono text-osso-muted mt-1">Medicina dello sport, atleti agonistici e riabilitazione</p>
                    </div>

                    <div class="space-y-2 text-xs font-mono text-osso-muted border-t border-osso-line pt-4">
                        <div><strong>SEDI:</strong> Pisa centro e Fornacette (Calcinaia)</div>
                        <div><strong>FOCUS:</strong> Valutazione ritorno allo sport, lesioni da impatto e overuse</div>
                    </div>

                    <div class="pt-4 border-t border-osso-line flex items-center justify-between">
                        <span class="text-[10px] font-mono text-osso-muted">ATLETI & SPORT</span>
                        <a href="#contatti" class="nav-trigger btn-interlock !py-2 !px-4 text-[10px]" data-target="contatti">Prenota a Pisa</a>
                    </div>
                </div>

            </div>

        </section>

        <!-- ========================================================
             VISTA 5: NOTE CLINICHE / IL QUADERNO (ARTICOLI DA PAPER)
             ======================================================== -->
        <section id="view-articoli" class="page-view max-w-[88rem] mx-auto px-6 py-16">
            
            <a href="#home" class="nav-trigger text-xs font-mono uppercase tracking-widest text-osso-muted hover:text-osso-dark block mb-8" data-target="home">
                ← Torna all'accesso principale
            </a>

            <div class="border-b border-osso-line pb-8 mb-12 flex flex-col md:flex-row md:items-end justify-between gap-6">
                <div>
                    <span class="font-mono text-xs uppercase tracking-widest text-osso-teal block mb-2">[ RIGORE E RICERCA ]</span>
                    <h1 class="text-4xl sm:text-6xl font-serif text-osso-dark font-light">Note cliniche.</h1>
                </div>
                <p class="font-mono text-xs text-osso-muted max-w-md">
                    Non articoli da blog per i motori di ricerca, ma riflessioni tratte dalla pratica chirurgica e dai paper scientifici pubblicati.
                </p>
            </div>

            <!-- Lista Tipografica a Incastro: Il Quaderno -->
            <div class="space-y-6">
                
                <!-- ARTICOLO 1: REMPLISSAGE -->
                <a href="#articoli-remplissage" class="nav-trigger block border border-osso-line p-8 md:p-10 bg-white hover:border-osso-teal transition-all group" data-target="articoli-remplissage">
                    <div class="flex flex-wrap justify-between items-start gap-4 mb-4 font-mono text-xs">
                        <span class="text-osso-teal font-semibold">[ SPALLA & INSTABILITÀ ]</span>
                        <span class="text-osso-muted">PUBBLICAZIONE: OSTEOLOGY 2022 · CESAT</span>
                    </div>
                    
                    <h2 class="text-2xl sm:text-3xl font-serif text-osso-dark group-hover:text-osso-teal transition-colors mb-3">
                        Il dubbio nel remplissage: quando la stabilità rischia di sacrificare il movimento.
                    </h2>
                    
                    <p class="text-sm font-light text-osso-muted leading-relaxed max-w-3xl">
                        Nelle lussazioni recidivanti con difetto osseo della testa omerale (Hill-Sachs), la sutura dell'infraspinato previene l'ingranamento glenoideo. Lo studio multicentrico sui risultati a medio termine e il ROM post-operatorio.
                    </p>
                    
                    <div class="mt-6 pt-4 border-t border-osso-line/60 flex items-center justify-between font-mono text-xs text-osso-dark">
                        <span>Autore: Dott. Michele Novi et al.</span>
                        <span class="text-osso-teal font-medium group-hover:translate-x-1 transition-transform">Leggi la nota completa →</span>
                    </div>
                </a>

                <!-- ARTICOLO 2 (PREVIEW) -->
                <div class="border border-osso-line p-8 bg-osso-base opacity-75">
                    <div class="flex justify-between items-start mb-2 font-mono text-xs text-osso-muted">
                        <span>[ IN PREPARAZIONE ]</span>
                        <span>LINEA EDITORIALE CESAT</span>
                    </div>
                    <h3 class="text-xl font-serif text-osso-dark">
                        La cuffia dei rotatori nell'over 60: riparazione biologica vs protesi inversa.
                    </h3>
                    <p class="text-xs text-osso-muted font-mono mt-2">
                        Analisi dei criteri decisionali basati sulla retrazione tendinea di Patte e sull'infiltrazione adiposa di Goutallier.
                    </p>
                </div>

            </div>

        </section>

        <!-- SOTTO-VISTA: DETTAGLIO ARTICOLO REMPLISSAGE -->
        <section id="view-articoli-remplissage" class="page-view max-w-[55rem] mx-auto px-6 py-16">
            <a href="#articoli" class="nav-trigger text-xs font-mono uppercase tracking-widest text-osso-muted hover:text-osso-dark block mb-8" data-target="articoli">
                ← Torna alle Note cliniche
            </a>

            <div class="border-b border-osso-line pb-6 mb-8 font-mono text-xs text-osso-muted flex justify-between">
                <span>NOTA CLINICA // 01</span>
                <span>OSTEOLOGY 2022 · DOI: 10.3390/osteology2040021</span>
            </div>

            <h1 class="text-3xl sm:text-5xl font-serif text-osso-dark font-light leading-tight mb-8">
                Il dubbio nel remplissage: conciliare stabilità e mobilità nella spalla dello sportivo.
            </h1>

            <div class="space-y-6 text-base sm:text-lg font-light text-osso-dark leading-relaxed">
                <p class="font-normal text-osso-muted border-l-2 border-osso-teal pl-4 italic">
                    «Il chirurgo che affronta una lussazione anteriore di spalla ha un timore costante: riparare troppo poco e vedere l'omero uscire di nuovo, o serrare troppo e privare l'atleta della rotazione esterna.»
                </p>
                
                <p>
                    Nelle lussazioni recidivanti anteriori, la combinazione tra lesione labrale (Bankart) e lesione da compressione ossea posterolaterale sulla testa omerale (Hill-Sachs) crea un ingranaggio pericoloso. Durante il movimento di abduzione ed extrarotazione — tipico del lancio o della caduta nello sport — la lesione di Hill-Sachs può incastrarsi sul bordo anteriore della glenoide, agendo come una leva che scardina l'articolazione.
                </p>

                <h3 class="text-2xl font-serif text-osso-dark pt-4">La procedura: colmare il vuoto</h3>
                <p>
                    Il <em>Remplissage</em> (dal francese "riempimento") risolve questo problema fissando la capsula articolare posteriore e il tendine dell'infraspinato direttamente dentro la lesione ossea. L'obiettivo biomeccanico è rendere il difetto osseo "extra-articolare", impedendone l'ingranamento glenoideo.
                </p>

                <h3 class="text-2xl font-serif text-osso-dark pt-4">I risultati del nostro studio</h3>
                <p>
                    Nel paper condotto in collaborazione con l'équipe del CESAT, abbiamo valutato il ritorno allo sport e la misurazione goniometrica del ROM in pazienti atleti a un follow-up minimo di due anni. I dati confermano una perdita media di extrarotazione inferiore a 4 gradi, clinicamente impercettibile per la maggior parte delle attività sportive, a fronte di un tasso di recidiva dell'instabilità azzerato.
                </p>
            </div>

            <div class="border-t border-osso-line mt-12 pt-8 flex justify-between items-center text-xs font-mono">
                <span class="text-osso-muted">Dott. Michele Novi · Ortopedia e Traumatologia</span>
                <a href="#contatti" class="nav-trigger btn-interlock btn-interlock-teal" data-target="contatti">
                    <span>Richiedi una Valutazione Clinica</span>
                </a>
            </div>
        </section>

        <!-- ========================================================
             VISTA 6: CONTATTI E PRENOTAZIONI
             ======================================================== -->
        <section id="view-contatti" class="page-view max-w-[88rem] mx-auto px-6 py-16">
            
            <a href="#home" class="nav-trigger text-xs font-mono uppercase tracking-widest text-osso-muted hover:text-osso-dark block mb-8" data-target="home">
                ← Torna all'accesso principale
            </a>

            <div class="border-b border-osso-line pb-8 mb-12 flex flex-col md:flex-row md:items-end justify-between gap-6">
                <div>
                    <span class="font-mono text-xs uppercase tracking-widest text-osso-teal block mb-2">[ ACCESSO DIRETTO ALLA SEGRETERIA ]</span>
                    <h1 class="text-4xl sm:text-6xl font-serif text-osso-dark font-light">Contatti e prenotazioni.</h1>
                </div>
                <p class="font-mono text-xs text-osso-muted max-w-md">
                    Un solo numero dedicato per tutte le visite in libera professione e informazioni su ricoveri chirurgici.
                </p>
            </div>

            <div class="grid lg:grid-cols-12 gap-12 items-start">
                
                <!-- Colonna Recapiti e Regole Chiare -->
                <div class="lg:col-span-5 space-y-8">
                    
                    <div class="border border-osso-line bg-white p-8 space-y-6">
                        <span class="font-mono text-xs uppercase text-osso-teal font-semibold block">[ RECAPITO SEGRETERIA ]</span>
                        
                        <div>
                            <div class="font-mono text-xs text-osso-muted uppercase mb-1">Telefono Chiamate & WhatsApp</div>
                            <a href="tel:+393484331733" class="text-3xl sm:text-4xl font-mono font-bold text-osso-dark hover:text-osso-teal transition-colors">
                                348 4331733
                            </a>
                        </div>

                        <div class="space-y-2 font-mono text-xs text-osso-muted border-t border-osso-line pt-4">
                            <div><strong>FASCE ORARIE:</strong> Lunedì – Giovedì · 15:30 – 17:30</div>
                            <div><strong>MESSAGGI WHATSAPP:</strong> Attivi per richieste disponibilità visite</div>
                            <div><strong>EMAIL AMMINISTRATIVA:</strong> segreteria@michelenovi.it</div>
                        </div>

                        <div class="p-4 bg-osso-surface border border-osso-line font-mono text-[11px] text-osso-muted leading-relaxed">
                            <strong class="text-osso-dark block mb-1">Cosa comunicare:</strong>
                            Nome, recapito, motivo sintetico della visita (es. "dolore spalla destra") e sede preferita (Fucecchio, Peccioli, Fornacette, Pisa). Non inviare referti o immagini diagnostiche pesanti via messaggio prima della visita.
                        </div>
                    </div>

                    <div class="border border-osso-line p-6 bg-[#EAEBE8] font-mono text-xs space-y-2 text-osso-muted">
                        <strong class="text-osso-dark block uppercase">Interventi Ospedalieri SSN:</strong>
                        <p>Le prestazioni chirurgiche in convenzione presso l'Ospedale CESAT di Fucecchio seguono i percorsi di lista d'attesa regionale stabiliti durante la visita preliminare.</p>
                    </div>

                </div>

                <!-- Colonna Form Essenziale (Niente Dati Clinici Sensibili) -->
                <div class="lg:col-span-7 border border-osso-line bg-white p-8 md:p-12">
                    
                    <div class="mb-8">
                        <span class="font-mono text-xs uppercase tracking-widest text-osso-teal block mb-1">[ MODULO DI RICHIESTA ]</span>
                        <h3 class="text-2xl font-serif text-osso-dark">Invia una richiesta di contatto.</h3>
                        <p class="text-xs font-mono text-osso-muted mt-1">La segreteria ricontatterà telefonicamente entro 24-48 ore lavorative.</p>
                    </div>

                    <form onsubmit="event.preventDefault(); alert('Grazie. La segreteria del Dott. Michele Novi ti ricontatterà al recapito indicato.');" class="space-y-6">
                        
                        <div class="grid sm:grid-cols-2 gap-6">
                            <div>
                                <label class="block font-mono text-[10px] uppercase text-osso-dark mb-2 font-semibold">Nome e Cognome *</label>
                                <input type="text" required class="w-full border border-osso-line p-3 font-mono text-xs bg-osso-base focus:outline-none focus:border-osso-teal" placeholder="Mario Rossi">
                            </div>
                            <div>
                                <label class="block font-mono text-[10px] uppercase text-osso-dark mb-2 font-semibold">Recapito Telefonico *</label>
                                <input type="tel" required class="w-full border border-osso-line p-3 font-mono text-xs bg-osso-base focus:outline-none focus:border-osso-teal" placeholder="340 0000000">
                            </div>
                        </div>

                        <div class="grid sm:grid-cols-2 gap-6">
                            <div>
                                <label class="block font-mono text-[10px] uppercase text-osso-dark mb-2 font-semibold">Sede Desiderata</label>
                                <select class="w-full border border-osso-line p-3 font-mono text-xs bg-osso-base focus:outline-none focus:border-osso-teal">
                                    <option>Fucecchio (Studi San Pietro)</option>
                                    <option>Peccioli (Polo San Verano)</option>
                                    <option>Fornacette (Fisiomed)</option>
                                    <option>Pisa (Athletica)</option>
                                </select>
                            </div>
                            <div>
                                <label class="block font-mono text-[10px] uppercase text-osso-dark mb-2 font-semibold">Articolazione Interessata</label>
                                <select class="w-full border border-osso-line p-3 font-mono text-xs bg-osso-base focus:outline-none focus:border-osso-teal">
                                    <option>Spalla</option>
                                    <option>Gomito</option>
                                    <option>Mano o Polso</option>
                                    <option>Traumatologia dello Sport</option>
                                </select>
                            </div>
                        </div>

                        <div>
                            <label class="block font-mono text-[10px] uppercase text-osso-dark mb-2 font-semibold">Messaggio per la segreteria (Non clinico)</label>
                            <textarea rows="4" class="w-full border border-osso-line p-3 font-mono text-xs bg-osso-base focus:outline-none focus:border-osso-teal" placeholder="Desidero richiedere disponibilità per una prima visita specialistica..."></textarea>
                        </div>

                        <div class="flex items-start gap-3">
                            <input type="checkbox" required id="privacy" class="mt-1">
                            <label for="privacy" class="text-[11px] font-mono text-osso-muted leading-tight">
                                Ho letto e accetto l'informativa sul trattamento dei dati personali ai sensi del GDPR. I dati forniti saranno utilizzati esclusivamente per ricontattarmi in merito alla visita.
                            </label>
                        </div>

                        <button type="submit" class="btn-interlock btn-interlock-teal w-full justify-center !py-3.5">
                            <span>Invia Richiesta alla Segreteria</span>
                            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M5 12h14M12 5l7 7-7 7"/>
                            </svg>
                        </button>

                    </form>

                </div>

            </div>

        </section>

    </main>

    <!-- ============================================================
         FOOTER OSSO: NAP UNIFICATO E CONGRUENZA FINALE
         ============================================================ -->
    <footer class="border-t border-osso-line bg-white mt-32 py-16 px-6 relative z-10">
        <div class="max-w-[88rem] mx-auto grid grid-cols-1 md:grid-cols-4 gap-12 font-mono text-xs">
            
            <div class="space-y-3">
                <div class="font-serif text-lg text-osso-dark font-medium">Dott. Michele Novi</div>
                <p class="text-osso-muted text-[11px] leading-relaxed">
                    Specialista in Ortopedia e Traumatologia.<br>
                    Chirurgia della Spalla e dell'Arto Superiore.<br>
                    Dirigente Medico Ospedale CESAT Fucecchio.
                </p>
                <div class="text-[10px] text-osso-muted">P. IVA: In definizione · Ordine Medici Pisa 5988</div>
            </div>

            <div class="space-y-2">
                <strong class="text-osso-dark uppercase text-[10px] block mb-2">Navigazione Rapida</strong>
                <div><a href="#chi-sono" class="nav-trigger text-osso-muted hover:text-osso-teal" data-target="chi-sono">Chi sono</a></div>
                <div><a href="#patologie" class="nav-trigger text-osso-muted hover:text-osso-teal" data-target="patologie">Cosa curo (Patologie)</a></div>
                <div><a href="#sedi" class="nav-trigger text-osso-muted hover:text-osso-teal" data-target="sedi">Dove ricevo (Sedi)</a></div>
                <div><a href="#articoli" class="nav-trigger text-osso-muted hover:text-osso-teal" data-target="articoli">Note cliniche (Il Quaderno)</a></div>
                <div><a href="#contatti" class="nav-trigger text-osso-muted hover:text-osso-teal" data-target="contatti">Contatti e Prenotazioni</a></div>
            </div>

            <div class="space-y-2">
                <strong class="text-osso-dark uppercase text-[10px] block mb-2">Polo Chirurgico & Sedi</strong>
                <p class="text-osso-muted text-[11px]">
                    <strong>CESAT Fucecchio:</strong> Ospedale San Pietro Igneo (Piazza Lavagnini 5)<br>
                    <strong>Studi San Pietro:</strong> Piazza Lavagnini 6<br>
                    <strong>Valdera & Pisa:</strong> Peccioli, Fornacette, Pisa
                </p>
            </div>

            <div class="space-y-3">
                <strong class="text-osso-dark uppercase text-[10px] block mb-2">Recapito Unificato</strong>
                <a href="tel:+393484331733" class="text-base font-bold text-osso-teal block">
                    348 4331733
                </a>
                <p class="text-[10px] text-osso-muted leading-relaxed">
                    Segreteria attiva Lunedì – Giovedì 15:30 – 17:30.<br>
                    WhatsApp sempre disponibile per richieste visite.
                </p>
            </div>

        </div>

        <div class="max-w-[88rem] mx-auto mt-12 pt-6 border-t border-osso-line flex flex-col sm:flex-row justify-between items-center text-[10px] font-mono text-osso-muted gap-4">
            <div>© 2026 Dott. Michele Novi. Tutti i diritti riservati.</div>
            <div class="flex gap-6">
                <span>Informativa Privacy</span>
                <span>Cookie Policy</span>
                <span class="text-osso-teal">Conforme Linee Guida Pubblicità Sanitaria FNOMCeO</span>
            </div>
        </div>
    </footer>

    <!-- ============================================================
         JS ROUTER SPA NATIVO E INTERAZIONI DI STRATO
         ============================================================ -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Router SPA
            const navTriggers = document.querySelectorAll('.nav-trigger');
            const pageViews = document.querySelectorAll('.page-view');

            function switchView(targetId) {
                const targetEl = document.getElementById('view-' + targetId);
                if (!targetEl) return;

                pageViews.forEach(view => {
                    view.classList.remove('active-view');
                });
                
                targetEl.classList.add('active-view');
                window.scrollTo({ top: 0, behavior: 'instant' });
                
                // Aggiorna URL hash senza reload
                history.pushState(null, '', '#' + targetId);
            }

            navTriggers.forEach(trigger => {
                trigger.addEventListener('click', (e) => {
                    e.preventDefault();
                    const target = trigger.getAttribute('data-target');
                    if (target) {
                        switchView(target);
                    }
                });
            });

            // Gestione diretta dell'hash da URL (deep-linking)
            if (window.location.hash) {
                const hashId = window.location.hash.replace('#', '');
                switchView(hashId);
            }

            // Animazione ingresso Varco
            setTimeout(() => {
                document.body.classList.add('is-loaded');
            }, 100);
        });
    </script>

</body>
</html>
"""

# Scrittura del file principale
target_path = "/Volumes/Programs/Temporary files/Progetti cursor/Michele_Novi_Website/handoff_sito.html"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_code)

# Copia anche in Proposte HTML per coerenza
proposte_path = "/Volumes/Programs/Temporary files/Progetti cursor/Michele_Novi_Website/Proposte HTML/index.html"
with open(proposte_path, "w", encoding="utf-8") as f:
    f.write(html_code)

print("Prototipo Awwwards con concetti di STRATO e INCASTRO generato con successo!")
