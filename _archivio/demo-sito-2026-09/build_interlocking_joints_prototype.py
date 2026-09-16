# -*- coding: utf-8 -*-
"""
Script per la generazione del prototipo HTML "Interlocking Joints & Articular Transitions"
per il Dott. Michele Novi.

Implementa i 5 concetti concordati:
1. IL GIUNTO MORFICO TRA SEZIONI (Scroll Seam con profilo anatomico condilo/fossa)
2. CARD A DUE METÀ CONGRUENTI (Diagnosi e Trattamento che si incastrano magneticamente all'hover)
3. TAB A RACCORDO INVERSO (Inverted Fillet Joints organici che uniscono tab e contenuto)
4. TRANSIZIONE VARCO ARTICOLARE (Apertura e ricomposizione fluida al cambio pagina)
5. MICRO-INCASTRO DELLE SEDI (Selettore interattivo con tassello che va a dockare nell'alloggiamento)
"""

import os

html_content = """<!DOCTYPE html>
<html lang="it" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dott. Michele Novi | Chirurgia Ortopedica Spalla e Arto Superiore</title>
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Google Fonts: Newsreader (classe clinica) + Plus Jakarta Sans (freschezza e calore) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,300;1,6..72,400;1,6..72,500&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        caldo: {
                            bg: '#FAF8F5',
                            surface: '#FFFFFF',
                            border: '#EBE6DE',
                            borderSoft: 'rgba(235, 230, 222, 0.75)',
                            text: '#162122',
                            muted: '#5A6667',
                            
                            teal: '#0C535C',
                            tealLight: '#E8F3F4',
                            tealSoft: '#F2F8F8',
                            
                            coral: '#DC6D48',
                            coralLight: '#FDF2ED',
                            coralSoft: '#FFF7F3',
                            
                            salvia: '#437A55',
                            salviaLight: '#EDF5F0',
                            
                            gold: '#C58C46',
                            goldLight: '#FDF7EE'
                        }
                    },
                    fontFamily: {
                        serif: ['Newsreader', 'Georgia', 'serif'],
                        sans: ['Plus Jakarta Sans', 'system-ui', 'sans-serif']
                    }
                }
            }
        }
    </script>
    
    <style>
        :root {
            --ease-silk: cubic-bezier(0.16, 1, 0.3, 1);
            --ease-joint: cubic-bezier(0.34, 1.56, 0.64, 1);
            --ease-snap: cubic-bezier(0.68, -0.6, 0.32, 1.6);
        }

        body {
            background-color: #FAF8F5;
            color: #162122;
            font-family: 'Plus Jakarta Sans', sans-serif;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }

        /* 1. AMBIENT MESH GRADIENTS */
        .ambient-mesh {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            pointer-events: none; z-index: 0;
            background: 
                radial-gradient(ellipse 60% 50% at 12% 18%, rgba(232, 243, 244, 0.75) 0%, transparent 60%),
                radial-gradient(ellipse 55% 45% at 88% 22%, rgba(253, 242, 237, 0.6) 0%, transparent 60%),
                radial-gradient(ellipse 65% 55% at 50% 85%, rgba(237, 245, 240, 0.5) 0%, transparent 70%);
            filter: blur(40px);
            opacity: 0.9;
        }

        /* 2. GIUNTO MORFICO TRA LE SEZIONI (Scroll Seam) */
        .joint-seam {
            position: relative;
            width: 100%;
            height: 48px;
            overflow: hidden;
            pointer-events: none;
            z-index: 10;
        }
        .joint-seam-curve {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 100%;
            fill: #FFFFFF;
            transition: transform 0.6s var(--ease-silk);
        }

        /* 3. CARD A DUE METÀ CONGRUENTI (INCASTRO CALDO) */
        .congruent-card-wrapper {
            position: relative;
            display: grid;
            grid-template-columns: 1fr;
            transition: all 0.5s var(--ease-silk);
        }
        @media (min-width: 768px) {
            .congruent-card-wrapper {
                grid-template-columns: 1fr 1fr;
            }
        }
        
        .congruent-half-left {
            background: linear-gradient(135deg, #FFFFFF 0%, #FAF8F5 100%);
            border: 1px solid #EBE6DE;
            border-radius: 28px 28px 0 0;
            transition: transform 0.55s var(--ease-silk), border-color 0.4s, box-shadow 0.4s;
            position: relative;
            z-index: 1;
        }
        @media (min-width: 768px) {
            .congruent-half-left {
                border-radius: 28px 0 0 28px;
                border-right: none;
                transform: translateX(-6px);
            }
        }

        .congruent-half-right {
            background: linear-gradient(135deg, #FAF8F5 0%, #FFFFFF 100%);
            border: 1px solid #EBE6DE;
            border-radius: 0 0 28px 28px;
            transition: transform 0.55s var(--ease-silk), border-color 0.4s, box-shadow 0.4s, background 0.4s;
            position: relative;
            z-index: 2;
        }
        @media (min-width: 768px) {
            .congruent-half-right {
                border-radius: 0 28px 28px 0;
                border-left: 1px dashed rgba(220, 109, 72, 0.4);
                transform: translateX(6px);
            }
        }

        /* Stato Hover / Incastro Magnetico */
        .congruent-card-wrapper:hover .congruent-half-left {
            transform: translateX(0);
            border-color: #0C535C;
            box-shadow: 0 16px 36px -10px rgba(12, 83, 92, 0.12);
        }
        .congruent-card-wrapper:hover .congruent-half-right {
            transform: translateX(0);
            border-color: #0C535C;
            background: linear-gradient(135deg, #F0F7F8 0%, #FFFFFF 100%);
            box-shadow: 0 16px 36px -10px rgba(12, 83, 92, 0.12);
        }
        
        .joint-snap-badge {
            transition: all 0.4s var(--ease-silk);
        }
        .congruent-card-wrapper:hover .joint-snap-badge {
            background-color: #0C535C;
            color: #FFFFFF;
            transform: scale(1.05);
        }

        /* 4. TAB CON RACCORDO INVERSO (Inverted Fillet Joint) */
        .joint-tab-btn {
            position: relative;
            transition: all 0.35s var(--ease-silk);
            border-radius: 20px 20px 0 0;
        }
        .joint-tab-btn.active-tab {
            background: #FFFFFF;
            color: #0C535C;
            font-weight: 700;
            box-shadow: 0 -4px 16px rgba(12, 83, 92, 0.05);
        }
        
        /* 5. MICRO-INCASTRO PER LE SEDI (Docking Component) */
        .clinic-dock-socket {
            background: #FAF8F5;
            border: 2px dashed rgba(12, 83, 92, 0.25);
            border-radius: 28px;
            transition: all 0.45s var(--ease-silk);
        }
        .clinic-dock-socket.is-docked {
            background: #FFFFFF;
            border-style: solid;
            border-color: #0C535C;
            box-shadow: 0 20px 40px -12px rgba(12, 83, 92, 0.12);
        }
        
        .dock-indicator {
            transition: transform 0.5s var(--ease-joint);
        }

        /* 6. TRANSIZIONE VARCO ARTICOLARE SPA */
        .page-view {
            display: none;
            opacity: 0;
            transform: scale(0.985) translateY(12px);
            transition: opacity 0.45s var(--ease-silk), transform 0.45s var(--ease-silk);
        }
        .page-view.active-view {
            display: block;
            opacity: 1;
            transform: scale(1) translateY(0);
        }

        /* Transizione ad otturatore articolare durante il cambio pagina */
        #articular-curtain {
            position: fixed;
            inset: 0;
            background: linear-gradient(135deg, rgba(232, 243, 244, 0.85) 0%, rgba(253, 242, 237, 0.85) 100%);
            backdrop-filter: blur(12px);
            z-index: 100;
            pointer-events: none;
            opacity: 0;
            clip-path: polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%);
            transition: opacity 0.35s var(--ease-silk), clip-path 0.5s var(--ease-silk);
        }
        #articular-curtain.curtain-close {
            opacity: 1;
            clip-path: polygon(0% 0%, 100% 0%, 100% 50%, 0% 50%);
        }
        #articular-curtain.curtain-open {
            opacity: 0;
            clip-path: polygon(0% 0%, 100% 0%, 100% 0%, 0% 0%);
        }

        /* Effetto Reveal Soft */
        .reveal-soft {
            opacity: 0;
            transform: translateY(20px);
            filter: blur(6px);
            transition: opacity 1.1s var(--ease-silk), transform 1.1s var(--ease-silk), filter 1.1s var(--ease-silk);
        }
        .reveal-soft.is-visible {
            opacity: 1;
            transform: translateY(0);
            filter: blur(0);
        }

        /* Bottoni Fluidi */
        .btn-fluid-primary {
            background: linear-gradient(135deg, #0C535C 0%, #17717D 100%);
            color: #FFFFFF;
            border-radius: 9999px;
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
            transition: all 0.35s var(--ease-silk);
            box-shadow: 0 8px 20px -4px rgba(12, 83, 92, 0.28);
        }
        .btn-fluid-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 14px 28px -4px rgba(12, 83, 92, 0.38);
        }

        .btn-fluid-coral {
            background: linear-gradient(135deg, #DC6D48 0%, #E87E5C 100%);
            color: #FFFFFF;
            border-radius: 9999px;
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
            transition: all 0.35s var(--ease-silk);
            box-shadow: 0 8px 20px -4px rgba(220, 109, 72, 0.28);
        }
        .btn-fluid-coral:hover {
            transform: translateY(-2px);
            box-shadow: 0 14px 28px -4px rgba(220, 109, 72, 0.4);
        }
    </style>
</head>
<body class="selection:bg-caldo-tealLight selection:text-caldo-teal relative">

    <!-- Schermo per transizione varco articolare -->
    <div id="articular-curtain" aria-hidden="true"></div>

    <!-- Gradienti d'ambiente sfumati in background -->
    <div class="ambient-mesh" aria-hidden="true"></div>

    <!-- ============================================================
         HEADER CON LOGO TIPOGRAFICO PURO (NO QUADRATO)
         ============================================================ -->
    <header class="fixed top-0 left-0 w-full z-50 bg-[#FAF8F5]/85 backdrop-blur-md border-b border-caldo-borderSoft transition-all duration-300" id="main-header">
        <div class="max-w-7xl mx-auto px-6 h-20 flex justify-between items-center">
            
            <!-- Logo Tipografico: Il Nome del Medico -->
            <a href="#home" class="nav-trigger group flex flex-col cursor-pointer" data-target="home">
                <span class="font-serif text-2xl sm:text-[26px] tracking-tight text-caldo-text font-normal leading-tight group-hover:text-caldo-teal transition-colors duration-300">
                    Dott. Michele Novi
                </span>
                <span class="text-[11px] font-medium text-caldo-muted group-hover:text-caldo-teal transition-colors flex items-center gap-1.5 mt-0.5">
                    <span class="w-1.5 h-1.5 rounded-full bg-caldo-coral"></span>
                    <span>Ortopedia & Chirurgia Arto Superiore · CESAT Fucecchio</span>
                </span>
            </a>

            <!-- Navigazione Principale -->
            <nav class="hidden lg:flex items-center gap-1 text-sm font-medium text-caldo-text">
                <a href="#chi-sono" class="nav-trigger px-4 py-2 rounded-full hover:bg-white/80 hover:text-caldo-teal transition-all" data-target="chi-sono">Chi sono</a>
                <a href="#patologie" class="nav-trigger px-4 py-2 rounded-full hover:bg-white/80 hover:text-caldo-teal transition-all" data-target="patologie">Cosa curo</a>
                <a href="#sedi" class="nav-trigger px-4 py-2 rounded-full hover:bg-white/80 hover:text-caldo-teal transition-all" data-target="sedi">Dove ricevo</a>
                <a href="#articoli" class="nav-trigger px-4 py-2 rounded-full hover:bg-white/80 hover:text-caldo-teal transition-all" data-target="articoli">Note cliniche</a>
                <a href="#contatti" class="nav-trigger px-4 py-2 rounded-full hover:bg-white/80 hover:text-caldo-teal transition-all" data-target="contatti">Contatti</a>
            </nav>

            <!-- Recapito e Prenotazione -->
            <div class="flex items-center gap-3">
                <a href="tel:+393484331733" class="hidden sm:inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/90 border border-caldo-border text-caldo-teal text-xs font-semibold hover:border-caldo-teal transition-all shadow-sm">
                    <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                    <span>348 4331733</span>
                </a>
                
                <a href="#contatti" class="nav-trigger btn-fluid-coral px-5 py-2.5 text-xs font-semibold" data-target="contatti">
                    <span>Prenota Visita</span>
                    <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                        <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                </a>
            </div>
        </div>
    </header>

    <!-- ============================================================
         MAIN CONTAINER
         ============================================================ -->
    <main class="relative z-10 pt-20" id="app-root">

        <!-- ========================================================
             VISTA 1: HOME (CON TUTTI I 5 MECCANISMI D'INCASTRO)
             ======================================================== -->
        <section id="view-home" class="page-view active-view">
            
            <!-- HERO SECTION CON GRADIENTI E RITRATTO -->
            <div class="max-w-7xl mx-auto px-6 pt-12 pb-20">
                
                <div class="reveal-soft inline-flex items-center gap-2 bg-gradient-to-r from-caldo-tealLight/80 to-caldo-coralLight/80 border border-white px-4 py-1.5 rounded-full shadow-sm mb-8">
                    <span class="w-2 h-2 rounded-full bg-caldo-coral"></span>
                    <span class="text-xs font-semibold text-caldo-teal">Polo Ospedaliero CESAT Fucecchio</span>
                    <span class="text-caldo-muted text-xs">· Sedi a Fucecchio, Peccioli, Fornacette, Pisa</span>
                </div>

                <div class="grid lg:grid-cols-12 gap-12 items-center">
                    
                    <div class="lg:col-span-7 space-y-6">
                        <h1 class="reveal-soft text-4xl sm:text-6xl xl:text-7xl font-serif text-caldo-text font-normal leading-[1.07] tracking-tight">
                            Ritrovare il movimento,<br>
                            con la precisione di <br>
                            <span class="italic text-caldo-teal bg-gradient-to-r from-caldo-teal to-caldo-coral bg-clip-text text-transparent font-medium">due superfici che combaciano.</span>
                        </h1>

                        <p class="reveal-soft text-lg sm:text-xl text-caldo-muted font-light leading-relaxed max-w-xl">
                            Specialista della spalla, del gomito e della mano. 
                            Dalla chirurgia artroscopica mini-invasiva alle protesi articolari, 
                            con l'ascolto e la vicinanza di un medico del territorio.
                        </p>

                        <!-- Punti di forza con icone dedicate -->
                        <div class="reveal-soft grid sm:grid-cols-3 gap-3.5 pt-2">
                            <div class="flex items-center gap-3 p-3.5 rounded-2xl bg-white/80 border border-caldo-borderSoft shadow-sm">
                                <div class="w-10 h-10 rounded-xl bg-caldo-tealLight text-caldo-teal flex items-center justify-center flex-shrink-0">
                                    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                                        <circle cx="12" cy="12" r="9"/>
                                        <path d="M12 7v5l3 3"/>
                                    </svg>
                                </div>
                                <div class="text-xs">
                                    <strong class="block text-caldo-text font-semibold">Spalla & Arto</strong>
                                    <span class="text-caldo-muted text-[11px]">Core clinico</span>
                                </div>
                            </div>

                            <div class="flex items-center gap-3 p-3.5 rounded-2xl bg-white/80 border border-caldo-borderSoft shadow-sm">
                                <div class="w-10 h-10 rounded-xl bg-caldo-coralLight text-caldo-coral flex items-center justify-center flex-shrink-0">
                                    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                                        <path d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"/>
                                        <path d="M12 3v2M12 19v2M3 12h2M19 12h2"/>
                                    </svg>
                                </div>
                                <div class="text-xs">
                                    <strong class="block text-caldo-text font-semibold">Artroscopia</strong>
                                    <span class="text-caldo-muted text-[11px]">Mini-invasiva</span>
                                </div>
                            </div>

                            <div class="flex items-center gap-3 p-3.5 rounded-2xl bg-white/80 border border-caldo-borderSoft shadow-sm">
                                <div class="w-10 h-10 rounded-xl bg-caldo-salviaLight text-caldo-salvia flex items-center justify-center flex-shrink-0">
                                    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                                        <path d="M3 21h18M5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16"/>
                                        <path d="M9 10h6M12 7v6"/>
                                    </svg>
                                </div>
                                <div class="text-xs">
                                    <strong class="block text-caldo-text font-semibold">Polo CESAT</strong>
                                    <span class="text-caldo-muted text-[11px]">Chirurgia & Protesi</span>
                                </div>
                            </div>
                        </div>

                        <div class="reveal-soft flex flex-wrap gap-4 pt-3">
                            <a href="#contatti" class="nav-trigger btn-fluid-primary px-8 py-4 text-sm font-semibold" data-target="contatti">
                                <span>Richiedi una Visita</span>
                                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                                    <path d="M5 12h14M12 5l7 7-7 7"/>
                                </svg>
                            </a>
                            <a href="#patologie" class="nav-trigger px-7 py-4 rounded-full bg-white border border-caldo-border text-caldo-teal text-sm font-semibold hover:border-caldo-teal transition-all" data-target="patologie">
                                <span>Scopri le Patologie</span>
                                <span class="ml-1">→</span>
                            </a>
                        </div>
                    </div>

                    <!-- Ritratto con Cornice Armonica -->
                    <div class="lg:col-span-5 relative reveal-soft">
                        <div class="relative z-10 p-3.5 rounded-[36px] bg-gradient-to-br from-white via-white/90 to-caldo-coralLight/40 border border-white shadow-xl shadow-caldo-teal/5">
                            <div class="aspect-[4/5] rounded-[28px] overflow-hidden relative bg-gradient-to-tr from-caldo-tealLight to-caldo-coralLight">
                                <img src="https://images.unsplash.com/photo-1622253692010-333f2da6031d?q=80&w=1000&auto=format&fit=crop" 
                                     alt="Dott. Michele Novi" 
                                     class="w-full h-full object-cover object-center filter contrast-[1.02]">
                                <div class="absolute inset-0 bg-gradient-to-t from-caldo-teal/70 via-transparent to-transparent opacity-60"></div>
                                <div class="absolute bottom-5 left-5 right-5 bg-white/95 backdrop-blur-md p-4 rounded-2xl border border-white/80 shadow-md flex items-center justify-between">
                                    <div>
                                        <span class="text-sm font-serif font-semibold text-caldo-text block">Dott. Michele Novi</span>
                                        <span class="text-[11px] text-caldo-teal font-medium">Dirigente Medico Ospedale CESAT</span>
                                    </div>
                                    <div class="w-8 h-8 rounded-full bg-caldo-tealLight text-caldo-teal flex items-center justify-center">
                                        <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                                        </svg>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>

            <!-- ========================================================
                 APPLICAZIONE 1: IL GIUNTO MORFICO (SCROLL SEAM)
                 Transizione anatomica tra Hero e la Sezione Incastro
                 ======================================================== -->
            <div class="joint-seam">
                <svg class="joint-seam-curve" viewBox="0 0 1440 48" preserveAspectRatio="none">
                    <!-- Profilo di un condilo e cavità glenoidea morbida -->
                    <path d="M0,0 C320,0 480,48 720,48 C960,48 1120,0 1440,0 L1440,48 L0,48 Z"/>
                </svg>
            </div>

            <!-- ========================================================
                 APPLICAZIONE 2: CARD A DUE METÀ CONGRUENTI (INCASTRO)
                 Dimostrazione interattiva del Remplissage e della stabilità
                 ======================================================== -->
            <div class="bg-white py-24 px-6 border-b border-caldo-borderSoft">
                <div class="max-w-7xl mx-auto">
                    
                    <div class="max-w-2xl mb-16 space-y-3">
                        <span class="inline-flex items-center gap-2 text-xs font-semibold text-caldo-coral bg-caldo-coralLight px-3.5 py-1 rounded-full">
                            <span class="w-1.5 h-1.5 rounded-full bg-caldo-coral"></span>
                            Principio dell'Incastro Anatomico
                        </span>
                        <h2 class="text-3xl sm:text-5xl font-serif text-caldo-text leading-tight">
                            Le due metà che combaciano: la stabilità della spalla.
                        </h2>
                        <p class="text-base text-caldo-muted font-light leading-relaxed">
                            Passa con il mouse sulle card sottostanti: vedrai come la diagnosi del problema (metà sinistra) e la soluzione chirurgica (metà destra) <strong>si attraggono e si uniscono al millimetro</strong>, ristabilendo la continuità.
                        </p>
                    </div>

                    <!-- Card a Incastro Awwwards: SPALLA & REMPLISSAGE -->
                    <div class="congruent-card-wrapper max-w-5xl mx-auto group cursor-pointer">
                        
                        <!-- Metà Sinistra: Il Problema / La Cavità di Hill-Sachs -->
                        <div class="congruent-half-left p-8 sm:p-10 space-y-4">
                            <div class="flex justify-between items-center">
                                <span class="text-xs font-bold text-caldo-coral uppercase tracking-wider">
                                    01. La Lesione Ossea
                                </span>
                                <span class="text-[11px] font-mono text-caldo-muted">TESTA OMERALE</span>
                            </div>

                            <h3 class="text-2xl font-serif text-caldo-text font-semibold">
                                La nicchia di Hill-Sachs che scardina l'articolazione.
                            </h3>

                            <p class="text-sm text-caldo-muted font-light leading-relaxed">
                                Nelle lussazioni recidivanti, l'impatto ripetuto scava una tacca nell'osso. Durante la rotazione del braccio, questa lesione <em>si incastra sul ciglio della glenoide</em>, facendo uscire la spalla dalla sua sede naturale.
                            </p>

                            <div class="pt-4 flex items-center gap-2 text-xs text-caldo-coral font-medium">
                                <span class="w-2 h-2 rounded-full bg-caldo-coral animate-ping"></span>
                                <span>Stato: Instabilità e rischio lussazione</span>
                            </div>
                        </div>

                        <!-- Metà Destra: La Soluzione / Il Remplissage che chiude il vano -->
                        <div class="congruent-half-right p-8 sm:p-10 space-y-4">
                            <div class="flex justify-between items-center">
                                <span class="text-xs font-bold text-caldo-teal uppercase tracking-wider">
                                    02. L'Incastro Ripristinato
                                </span>
                                <span class="joint-snap-badge text-[11px] font-medium bg-caldo-tealLight text-caldo-teal px-3 py-1 rounded-full">
                                    Avvicina per innestare
                                </span>
                            </div>

                            <h3 class="text-2xl font-serif text-caldo-text font-semibold">
                                Procedura di Remplissage: colmare il vuoto per scivolare.
                            </h3>

                            <p class="text-sm text-caldo-muted font-light leading-relaxed">
                                Inseriamo e suturiamo il tendine dell'infraspinato nel difetto osseo: la nicchia viene riempita ed esclusa dal giunto. Le due superfici tornano lisce e la spalla ruota liberamente senza incepparsi.
                            </p>

                            <div class="pt-4 flex items-center justify-between text-xs">
                                <span class="text-caldo-teal font-semibold">Risultato: Stabilità 100% · ROM preservato</span>
                                <span class="text-caldo-muted font-mono">Paper CESAT 2022 →</span>
                            </div>
                        </div>

                    </div>

                </div>
            </div>

            <!-- ========================================================
                 APPLICAZIONE 3: I TAB CON RACCORDO INVERSO
                 Navigatore rapido delle 6 Patologie
                 ======================================================== -->
            <div class="max-w-7xl mx-auto px-6 py-28">
                
                <div class="max-w-2xl mb-12 space-y-3">
                    <span class="inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal bg-caldo-tealLight px-3.5 py-1 rounded-full">
                        <span class="w-1.5 h-1.5 rounded-full bg-caldo-teal"></span>
                        Aree di Trattamento
                    </span>
                    <h2 class="text-3xl sm:text-5xl font-serif text-caldo-text leading-tight">
                        Cosa curo: esplorazione per distretto.
                    </h2>
                    <p class="text-base text-caldo-muted font-light leading-relaxed">
                        Seleziona un'articolazione per osservare come il riquadro del contenuto si raccorda in modo continuo al selettore.
                    </p>
                </div>

                <!-- Barra dei Tab con Raccordo Inverso -->
                <div class="flex flex-wrap gap-2 border-b border-caldo-border">
                    <button class="joint-tab-btn active-tab px-6 py-3.5 text-xs font-medium tracking-wide transition-all" onclick="selectJointTab(this, 'tab-spalla')">
                        Chirurgia della Spalla
                    </button>
                    <button class="joint-tab-btn px-6 py-3.5 text-xs font-medium text-caldo-muted hover:text-caldo-teal transition-all" onclick="selectJointTab(this, 'tab-gomito')">
                        Gomito e Traumi
                    </button>
                    <button class="joint-tab-btn px-6 py-3.5 text-xs font-medium text-caldo-muted hover:text-caldo-teal transition-all" onclick="selectJointTab(this, 'tab-mano')">
                        Mano e Polso
                    </button>
                    <button class="joint-tab-btn px-6 py-3.5 text-xs font-medium text-caldo-muted hover:text-caldo-teal transition-all" onclick="selectJointTab(this, 'tab-sport')">
                        Traumatologia Sportiva
                    </button>
                    <button class="joint-tab-btn px-6 py-3.5 text-xs font-medium text-caldo-muted hover:text-caldo-teal transition-all" onclick="selectJointTab(this, 'tab-artroscopia')">
                        Chirurgia Artroscopica
                    </button>
                    <button class="joint-tab-btn px-6 py-3.5 text-xs font-medium text-caldo-muted hover:text-caldo-teal transition-all" onclick="selectJointTab(this, 'tab-eco')">
                        Ecografia Muscoloscheletrica
                    </button>
                </div>

                <!-- Box Contenuto Raccordato Inversamente -->
                <div class="bg-white p-8 sm:p-12 rounded-b-3xl rounded-tr-3xl border-x border-b border-caldo-border shadow-sm min-h-[260px] flex flex-col justify-between" id="joint-tab-content">
                    <div class="grid md:grid-cols-12 gap-8 items-center">
                        <div class="md:col-span-8 space-y-4">
                            <span class="text-xs font-bold text-caldo-teal uppercase tracking-wider">Focus Patologia Selezionata</span>
                            <h3 class="text-2xl sm:text-3xl font-serif text-caldo-text" id="tab-title">Chirurgia della Spalla</h3>
                            <p class="text-sm text-caldo-muted font-light leading-relaxed" id="tab-desc">
                                Riparazione artroscopica della cuffia dei rotatori con micro-ancore riassorbibili, trattamento dell'instabilità scapolo-omerale e chirurgia protesica anatomica o inversa nel centro regionale CESAT.
                            </p>
                        </div>
                        <div class="md:col-span-4 text-right">
                            <a href="#patologie-spalla" class="nav-trigger btn-fluid-primary px-6 py-3 text-xs font-semibold" id="tab-link" data-target="patologie-spalla">
                                Scheda approfondita spalla →
                            </a>
                        </div>
                    </div>
                </div>

            </div>

            <!-- ========================================================
                 APPLICAZIONE 5: IL MICRO-INCASTRO DELLE SEDI (DOCKING)
                 Seleziona una sede e osserva il tassello che entra nel vano
                 ======================================================== -->
            <div class="bg-white py-24 px-6 border-t border-caldo-borderSoft">
                <div class="max-w-7xl mx-auto">
                    
                    <div class="max-w-2xl mb-16 space-y-3">
                        <span class="inline-flex items-center gap-2 text-xs font-semibold text-caldo-coral bg-caldo-coralLight px-3.5 py-1 rounded-full">
                            <span class="w-1.5 h-1.5 rounded-full bg-caldo-coral"></span>
                            Incastro Prenotazione Sedi
                        </span>
                        <h2 class="text-3xl sm:text-5xl font-serif text-caldo-text leading-tight">
                            Dove desideri farti visitare?
                        </h2>
                        <p class="text-base text-caldo-muted font-light leading-relaxed">
                            Seleziona una delle strutture: la scheda della visita <strong>scivola e si incastra al millimetro nell'alloggiamento</strong>, rivelando recapiti e orari dedicati.
                        </p>
                    </div>

                    <!-- Pulsanti di Selezione Sede -->
                    <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
                        <button class="p-4 rounded-2xl border border-caldo-border bg-caldo-bg text-left hover:border-caldo-teal transition-all flex items-center justify-between group" onclick="dockClinic('cesat', this)">
                            <div>
                                <strong class="block text-sm text-caldo-text group-hover:text-caldo-teal">CESAT Fucecchio</strong>
                                <span class="text-xs text-caldo-muted">Polo Ospedaliero</span>
                            </div>
                            <span class="w-6 h-6 rounded-full bg-white text-caldo-teal flex items-center justify-center font-bold text-xs shadow-sm">1</span>
                        </button>

                        <button class="p-4 rounded-2xl border-2 border-caldo-coral bg-caldo-coralLight text-left transition-all flex items-center justify-between group shadow-sm" onclick="dockClinic('fucecchio', this)">
                            <div>
                                <strong class="block text-sm text-caldo-text">Studi San Pietro</strong>
                                <span class="text-xs text-caldo-muted">Fucecchio (Ambulatorio)</span>
                            </div>
                            <span class="w-6 h-6 rounded-full bg-caldo-coral text-white flex items-center justify-center font-bold text-xs shadow-sm">✓</span>
                        </button>

                        <button class="p-4 rounded-2xl border border-caldo-border bg-caldo-bg text-left hover:border-caldo-teal transition-all flex items-center justify-between group" onclick="dockClinic('peccioli', this)">
                            <div>
                                <strong class="block text-sm text-caldo-text group-hover:text-caldo-teal">Polo San Verano</strong>
                                <span class="text-xs text-caldo-muted">Alta Valdera (Peccioli)</span>
                            </div>
                            <span class="w-6 h-6 rounded-full bg-white text-caldo-salvia flex items-center justify-center font-bold text-xs shadow-sm">3</span>
                        </button>

                        <button class="p-4 rounded-2xl border border-caldo-border bg-caldo-bg text-left hover:border-caldo-teal transition-all flex items-center justify-between group" onclick="dockClinic('pisa', this)">
                            <div>
                                <strong class="block text-sm text-caldo-text group-hover:text-caldo-teal">Pisa & Fornacette</strong>
                                <span class="text-xs text-caldo-muted">Sport & Fisiomed</span>
                            </div>
                            <span class="w-6 h-6 rounded-full bg-white text-caldo-gold flex items-center justify-center font-bold text-xs shadow-sm">4</span>
                        </button>
                    </div>

                    <!-- Il "Socket" (Alloggiamento a Incastro Dinamico) -->
                    <div class="clinic-dock-socket is-docked p-8 sm:p-12 relative overflow-hidden" id="clinic-dock-target">
                        <div class="grid lg:grid-cols-12 gap-8 items-center">
                            
                            <div class="lg:col-span-8 space-y-3">
                                <div class="inline-flex items-center gap-2 text-xs font-bold text-caldo-coral uppercase tracking-wider">
                                    <span class="w-2 h-2 rounded-full bg-caldo-coral animate-ping"></span>
                                    <span id="dock-tag">Sede Selezionata: Fucecchio Ambulatorio</span>
                                </div>
                                <h3 class="text-2xl sm:text-4xl font-serif text-caldo-text" id="dock-name">
                                    Studi Medici San Pietro · Fucecchio
                                </h3>
                                <p class="text-sm text-caldo-muted font-light leading-relaxed" id="dock-address">
                                    Piazza Lavagnini, 6 (Adiacente all'Ospedale CESAT). Prime visite specialistiche, infiltrazioni ecoguidate e controlli.
                                </p>
                                <div class="pt-2 flex flex-wrap gap-4 text-xs font-medium text-caldo-muted" id="dock-extra">
                                    <span>🕒 Orari: Lunedì – Giovedì su appuntamento</span>
                                    <span>·</span>
                                    <span>🅿️ Parcheggio comodo antistante</span>
                                </div>
                            </div>

                            <div class="lg:col-span-4 flex flex-col gap-3 justify-center items-start lg:items-end">
                                <a href="tel:+393484331733" class="btn-fluid-primary px-6 py-3 text-xs font-semibold w-full sm:w-auto justify-center">
                                    <span>Chiama la Segreteria</span>
                                    <span>348 4331733</span>
                                </a>
                                <a href="https://wa.me/393484331733" target="_blank" class="px-6 py-3 rounded-full bg-[#25D366] text-white text-xs font-semibold w-full sm:w-auto justify-center inline-flex items-center gap-2 hover:opacity-90 transition-opacity">
                                    <span>Scrivi su WhatsApp</span>
                                </a>
                            </div>

                        </div>
                    </div>

                </div>
            </div>

        </section>

        <!-- ========================================================
             VISTA 2: CHI SONO (PROFILO & HARBORVIEW)
             ======================================================== -->
        <section id="view-chi-sono" class="page-view max-w-6xl mx-auto px-6 py-16">
            <a href="#home" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal hover:text-caldo-coral mb-8 transition-colors" data-target="home">
                <span>← Torna alla Home</span>
            </a>
            <div class="max-w-3xl mb-12 space-y-3">
                <span class="text-xs font-semibold text-caldo-teal bg-caldo-tealLight px-3 py-1 rounded-full inline-block">Profilo</span>
                <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text">Dott. Michele Novi</h1>
                <p class="text-lg text-caldo-muted font-light leading-relaxed">
                    Dirigente Medico Ortopedico presso il centro di eccellenza CESAT di Fucecchio. Fellowship presso l'Harborview Medical Center di Seattle (USA) in traumatologia complessa e microchirurgia.
                </p>
            </div>
            <div class="grid md:grid-cols-2 gap-8">
                <div class="p-8 rounded-3xl bg-white border border-caldo-border space-y-3">
                    <strong class="text-sm text-caldo-teal font-bold uppercase block">La Scuola e la Ricerca</strong>
                    <p class="text-xs text-caldo-muted font-light leading-relaxed">
                        Cresciuto nella scuola del Prof. Porcellini e allievo del Dott. Nicoletti, socio ordinario SIAGASCOT e SICSEG con oltre 15 pubblicazioni internazionali su riviste ad alto impatto.
                    </p>
                </div>
                <div class="p-8 rounded-3xl bg-white border border-caldo-border space-y-3">
                    <strong class="text-sm text-caldo-coral font-bold uppercase block">I Due Tempi</strong>
                    <p class="text-xs text-caldo-muted font-light leading-relaxed">
                        L'alto volume della sala operatoria al CESAT si unisce all'ascolto attento negli ambulatori del territorio, spiegando sempre con calma ogni indicazione terapeutica.
                    </p>
                </div>
            </div>
        </section>

        <!-- ========================================================
             VISTA 3: PATOLOGIE (HUB)
             ======================================================== -->
        <section id="view-patologie" class="page-view max-w-7xl mx-auto px-6 py-16">
            <a href="#home" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal hover:text-caldo-coral mb-8 transition-colors" data-target="home">
                <span>← Torna alla Home</span>
            </a>
            <div class="max-w-3xl mb-12 space-y-3">
                <span class="text-xs font-semibold text-caldo-teal bg-caldo-tealLight px-3 py-1 rounded-full inline-block">Aree Cliniche</span>
                <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text">Cosa curo.</h1>
                <p class="text-base text-caldo-muted font-light">Le 6 specializzazioni canoniche per la cura dell'arto superiore.</p>
            </div>
            <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
                <a href="#patologie-spalla" class="nav-trigger p-8 rounded-3xl bg-white border border-caldo-border hover:border-caldo-teal transition-all group" data-target="patologie-spalla">
                    <h3 class="text-xl font-serif text-caldo-text group-hover:text-caldo-teal font-semibold mb-2">Chirurgia della Spalla</h3>
                    <p class="text-xs text-caldo-muted font-light leading-relaxed mb-4">Cuffia dei rotatori, instabilità articolare, protesi inversa.</p>
                    <span class="text-xs text-caldo-teal font-semibold">Dettaglio spalla →</span>
                </a>
                <a href="#patologie-gomito" class="nav-trigger p-8 rounded-3xl bg-white border border-caldo-border hover:border-caldo-coral transition-all group" data-target="patologie-gomito">
                    <h3 class="text-xl font-serif text-caldo-text group-hover:text-caldo-coral font-semibold mb-2">Gomito e Traumi</h3>
                    <p class="text-xs text-caldo-muted font-light leading-relaxed mb-4">Epicondilite resistente e riparazione bicipite distale.</p>
                    <span class="text-xs text-caldo-coral font-semibold">Dettaglio gomito →</span>
                </a>
                <a href="#patologie-mano" class="nav-trigger p-8 rounded-3xl bg-white border border-caldo-border hover:border-caldo-salvia transition-all group" data-target="patologie-mano">
                    <h3 class="text-xl font-serif text-caldo-text group-hover:text-caldo-salvia font-semibold mb-2">Mano e Polso</h3>
                    <p class="text-xs text-caldo-muted font-light leading-relaxed mb-4">Tunnel carpale, dito a scatto, rizoartrosi pollice.</p>
                    <span class="text-xs text-caldo-salvia font-semibold">Dettaglio mano →</span>
                </a>
                <a href="#patologie-traumatologia-sportiva" class="nav-trigger p-8 rounded-3xl bg-white border border-caldo-border hover:border-caldo-gold transition-all group" data-target="patologie-traumatologia-sportiva">
                    <h3 class="text-xl font-serif text-caldo-text group-hover:text-caldo-gold font-semibold mb-2">Traumatologia Sportiva</h3>
                    <p class="text-xs text-caldo-muted font-light leading-relaxed mb-4">Lussazioni acromion-claveari e ritorno allo sport.</p>
                    <span class="text-xs text-caldo-gold font-semibold">Dettaglio sport →</span>
                </a>
                <a href="#patologie-artroscopia" class="nav-trigger p-8 rounded-3xl bg-white border border-caldo-border hover:border-caldo-teal transition-all group" data-target="patologie-artroscopia">
                    <h3 class="text-xl font-serif text-caldo-text group-hover:text-caldo-teal font-semibold mb-2">Chirurgia Artroscopica</h3>
                    <p class="text-xs text-caldo-muted font-light leading-relaxed mb-4">La visione ottica mini-invasiva diretta.</p>
                    <span class="text-xs text-caldo-teal font-semibold">Dettaglio artroscopia →</span>
                </a>
                <a href="#patologie-ecografia-muscoloscheletrica" class="nav-trigger p-8 rounded-3xl bg-white border border-caldo-border hover:border-caldo-coral transition-all group" data-target="patologie-ecografia-muscoloscheletrica">
                    <h3 class="text-xl font-serif text-caldo-text group-hover:text-caldo-coral font-semibold mb-2">Ecografia Muscoloscheletrica</h3>
                    <p class="text-xs text-caldo-muted font-light leading-relaxed mb-4">Diploma SIUMB e infiltrazioni eco-guidate.</p>
                    <span class="text-xs text-caldo-coral font-semibold">Dettaglio ecografia →</span>
                </a>
            </div>
        </section>

        <!-- SOTTO-VISTA SPALLA -->
        <section id="view-patologie-spalla" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal mb-8" data-target="patologie">← Tutte le patologie</a>
            <h1 class="text-4xl font-serif text-caldo-text mb-4">Chirurgia della Spalla</h1>
            <p class="text-caldo-muted leading-relaxed font-light mb-6">Trattamento specialistico della cuffia dei rotatori, instabilità articolare e chirurgia protesica al CESAT.</p>
            <a href="#contatti" class="nav-trigger btn-fluid-coral px-6 py-3 text-xs font-semibold" data-target="contatti">Prenota visita spalla</a>
        </section>
        <section id="view-patologie-gomito" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal mb-8" data-target="patologie">← Indietro</a>
            <h1 class="text-4xl font-serif text-caldo-text mb-4">Gomito: traumatologia e artroscopia</h1>
            <p class="text-caldo-muted">Rigidità ed epicondilite resistente.</p>
        </section>
        <section id="view-patologie-mano" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal mb-8" data-target="patologie">← Indietro</a>
            <h1 class="text-4xl font-serif text-caldo-text mb-4">Mano e Polso</h1>
            <p class="text-caldo-muted">Tunnel carpale, dito a scatto e rizoartrosi.</p>
        </section>
        <section id="view-patologie-traumatologia-sportiva" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal mb-8" data-target="patologie">← Indietro</a>
            <h1 class="text-4xl font-serif text-caldo-text mb-4">Traumatologia Sportiva</h1>
            <p class="text-caldo-muted">Supporto completo ad atleti agonistici e amatoriali.</p>
        </section>
        <section id="view-patologie-artroscopia" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal mb-8" data-target="patologie">← Indietro</a>
            <h1 class="text-4xl font-serif text-caldo-text mb-4">Chirurgia Artroscopica</h1>
            <p class="text-caldo-muted">Tecnica mini-invasiva a visione ottica diretta.</p>
        </section>
        <section id="view-patologie-ecografia-muscoloscheletrica" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal mb-8" data-target="patologie">← Indietro</a>
            <h1 class="text-4xl font-serif text-caldo-text mb-4">Ecografia Muscoloscheletrica</h1>
            <p class="text-caldo-muted">Diagnosi dinamica in ambulatorio e infiltrazioni eco-guidate.</p>
        </section>

        <!-- ========================================================
             VISTA 4: DOVE RICEVO (LE SEDI)
             ======================================================== -->
        <section id="view-sedi" class="page-view max-w-7xl mx-auto px-6 py-16">
            <a href="#home" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal mb-8" data-target="home">← Torna alla Home</a>
            <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text mb-8">Dove ricevo: le strutture in Toscana</h1>
            <div class="grid md:grid-cols-2 gap-8">
                <div class="p-8 rounded-3xl bg-white border border-caldo-border space-y-4">
                    <span class="bg-caldo-teal text-white text-xs font-semibold px-3 py-1 rounded-full">Polo Ospedaliero</span>
                    <h3 class="text-2xl font-serif text-caldo-text">Ospedale CESAT Fucecchio</h3>
                    <p class="text-xs text-caldo-muted">Piazza Lavagnini 5 · Fucecchio (Chirurgia e Ricoveri)</p>
                </div>
                <div class="p-8 rounded-3xl bg-white border border-caldo-border space-y-4">
                    <span class="bg-caldo-coral text-white text-xs font-semibold px-3 py-1 rounded-full">Ambulatorio Visite</span>
                    <h3 class="text-2xl font-serif text-caldo-text">Studi Medici San Pietro</h3>
                    <p class="text-xs text-caldo-muted">Piazza Lavagnini 6 · Fucecchio (Visite ed ecografie)</p>
                </div>
            </div>
        </section>

        <!-- ========================================================
             VISTA 5: NOTE CLINICHE (IL QUADERNO SCIENTIFICO)
             ======================================================== -->
        <section id="view-articoli" class="page-view max-w-5xl mx-auto px-6 py-16">
            <a href="#home" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal mb-8" data-target="home">← Torna alla Home</a>
            <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text mb-8">Note cliniche</h1>
            <a href="#articoli-remplissage" class="nav-trigger block p-8 rounded-3xl bg-white border border-caldo-border hover:border-caldo-teal transition-all group" data-target="articoli-remplissage">
                <span class="text-xs font-semibold text-caldo-coral block mb-2">Paper Osteology 2022 · CESAT</span>
                <h2 class="text-2xl font-serif text-caldo-text group-hover:text-caldo-teal mb-2">Il dubbio nel remplissage: stabilità e movimento</h2>
                <p class="text-xs text-caldo-muted font-light leading-relaxed">Studio sul ritorno allo sport e mantenimento della rotazione esterna negli atleti.</p>
            </a>
        </section>

        <section id="view-articoli-remplissage" class="page-view max-w-3xl mx-auto px-6 py-16">
            <a href="#articoli" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal mb-8" data-target="articoli">← Note cliniche</a>
            <h1 class="text-3xl sm:text-4xl font-serif text-caldo-text mb-6">Il dubbio nel remplissage</h1>
            <p class="text-sm text-caldo-muted leading-relaxed font-light mb-6">
                Riempire il difetto osseo della testa omerale con il tendine dell'infraspinato previene l'ingranamento glenoideo e garantisce stabilità senza sacrificare la mobilità articolare.
            </p>
        </section>

        <!-- ========================================================
             VISTA 6: CONTATTI E PRENOTAZIONI
             ======================================================== -->
        <section id="view-contatti" class="page-view max-w-5xl mx-auto px-6 py-16">
            <a href="#home" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal mb-8" data-target="home">← Torna alla Home</a>
            <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text mb-8">Contatti e Segreteria</h1>
            <div class="grid md:grid-cols-2 gap-8">
                <div class="p-8 rounded-3xl bg-white border border-caldo-border space-y-4">
                    <strong class="text-sm text-caldo-teal uppercase font-bold block">Segreteria Telefonica</strong>
                    <a href="tel:+393484331733" class="text-3xl font-serif text-caldo-teal block">348 4331733</a>
                    <p class="text-xs text-caldo-muted">Lunedì – Giovedì 15:30 – 17:30</p>
                    <a href="https://wa.me/393484331733" target="_blank" class="inline-block py-2.5 px-5 rounded-full bg-[#25D366] text-white text-xs font-semibold">
                        Scrivi su WhatsApp
                    </a>
                </div>
                <div class="p-8 rounded-3xl bg-white border border-caldo-border space-y-4">
                    <strong class="text-sm text-caldo-coral uppercase font-bold block">Richiesta Online</strong>
                    <p class="text-xs text-caldo-muted">La segreteria ricontatta entro 24 ore per confermare la data e la sede più comoda.</p>
                </div>
            </div>
        </section>

    </main>

    <!-- FOOTER ELEGANTE -->
    <footer class="bg-white border-t border-caldo-border mt-32 py-16 px-6">
        <div class="max-w-7xl mx-auto flex flex-col sm:flex-row justify-between items-center gap-4 text-xs text-caldo-muted">
            <div class="font-serif text-lg text-caldo-text font-normal">Dott. Michele Novi</div>
            <div>© 2026 · Specialista in Ortopedia e Traumatologia · CESAT Fucecchio</div>
        </div>
    </footer>

    <!-- ============================================================
         SCRIPT JS: GESTIONE INCASTRI, DOCKING E TRANSIZIONI ARTICOLARI
         ============================================================ -->
    <script>
        // 1. GESTIONE TAB A RACCORDO INVERSO
        const tabData = {
            'tab-spalla': {
                title: 'Chirurgia della Spalla',
                desc: 'Riparazione artroscopica della cuffia dei rotatori con micro-ancore riassorbibili, trattamento dell\\'instabilità scapolo-omerale e chirurgia protesica anatomica o inversa nel centro regionale CESAT.',
                link: '#patologie-spalla',
                target: 'patologie-spalla'
            },
            'tab-gomito': {
                title: 'Gomito: Traumatologia e Artroscopia',
                desc: 'Riparazione del tendine distale del bicipite brachiale, trattamento dell\\'epicondilite resistente e release artroscopico per il recupero dell\\'estensione completa del braccio.',
                link: '#patologie-gomito',
                target: 'patologie-gomito'
            },
            'tab-mano': {
                title: 'Mano e Polso',
                desc: 'Decompressione del tunnel carpale con tecnica mininvasiva, risoluzione del dito a scatto, tendinite di De Quervain e cura conservativa o protesica della rizoartrosi del pollice.',
                link: '#patologie-mano',
                target: 'patologie-mano'
            },
            'tab-sport': {
                title: 'Traumatologia dello Sport',
                desc: 'Assistenza ad atleti professionisti e amatoriali (tennis, moto, arrampicata, corsa). Trattamento lussazioni acromion-claveari e protocolli rapidi di return-to-play sicuro.',
                link: '#patologie-traumatologia-sportiva',
                target: 'patologie-traumatologia-sportiva'
            },
            'tab-artroscopia': {
                title: 'Chirurgia Artroscopica',
                desc: 'Il metodo d\\'eccellenza mini-invasivo: telecamera ottica miniaturizzata ad alta definizione per operare dentro l\\'articolazione senza incidere i tessuti muscolari sani.',
                link: '#patologie-artroscopia',
                target: 'patologie-artroscopia'
            },
            'tab-eco': {
                title: 'Ecografia Muscoloscheletrica',
                desc: 'Certificazione SIUMB: diagnosi immediata al letto del paziente durante la visita ed esecuzione di infiltrazioni ecoguidate mirate con acido ialuronico ad alto peso molecolare.',
                link: '#patologie-ecografia-muscoloscheletrica',
                target: 'patologie-ecografia-muscoloscheletrica'
            }
        };

        function selectJointTab(btn, tabKey) {
            document.querySelectorAll('.joint-tab-btn').forEach(b => {
                b.classList.remove('active-tab');
                b.classList.remove('text-caldo-teal');
                b.classList.add('text-caldo-muted');
            });
            btn.classList.add('active-tab');
            btn.classList.remove('text-caldo-muted');
            btn.classList.add('text-caldo-teal');

            const data = tabData[tabKey];
            if (data) {
                const titleEl = document.getElementById('tab-title');
                const descEl = document.getElementById('tab-desc');
                const linkEl = document.getElementById('tab-link');
                
                titleEl.style.opacity = '0';
                descEl.style.opacity = '0';
                setTimeout(() => {
                    titleEl.innerText = data.title;
                    descEl.innerText = data.desc;
                    linkEl.setAttribute('href', data.link);
                    linkEl.setAttribute('data-target', data.target);
                    titleEl.style.opacity = '1';
                    descEl.style.opacity = '1';
                }, 180);
            }
        }

        // 2. GESTIONE MICRO-INCASTRO DELLE SEDI (DOCKING)
        const clinicData = {
            'cesat': {
                tag: 'Sede Selezionata: Polo Ospedaliero di Eccellenza',
                name: 'CESAT · Ospedale San Pietro Igneo',
                address: 'Piazza Lavagnini, 5 · 50054 Fucecchio (FI). Ricoveri chirurgici, protesi spalla/arto e interventi in day-surgery.',
                extra: '🏥 Ricoveri Ospedalieri SSN & Convenzionati · Equipe CESAT'
            },
            'fucecchio': {
                tag: 'Sede Selezionata: Ambulatorio Principale Fucecchio',
                name: 'Studi Medici San Pietro · Fucecchio',
                address: 'Piazza Lavagnini, 6 (Adiacente all\\'Ospedale CESAT). Prime visite specialistiche, infiltrazioni ecoguidate e controlli.',
                extra: '🕒 Lunedì – Giovedì su appuntamento · 🅿️ Parcheggio adiacente'
            },
            'peccioli': {
                tag: 'Sede Selezionata: Alta Valdera',
                name: 'Polo San Verano · Peccioli (PI)',
                address: 'Località San Verano · Peccioli (PI). Visite specialistiche ortopediche per l\\'Alta Valdera con ecografo dedicato.',
                extra: '🌿 Comodo accesso al piano terra senza barriere'
            },
            'pisa': {
                tag: 'Sede Selezionata: Sport & Territorio',
                name: 'Athletica Pisa & Centro Fisiomed',
                address: 'Pisa centro e Fornacette (Calcinaia). Valutazione funzionale per sportivi e medicina rigenerativa.',
                extra: '🏃 Test funzionali per il ritorno allo sport'
            }
        };

        function dockClinic(key, btn) {
            const socket = document.getElementById('clinic-dock-target');
            socket.classList.remove('is-docked');
            
            // Highlight button
            const allBtns = btn.parentElement.querySelectorAll('button');
            allBtns.forEach(b => {
                b.className = "p-4 rounded-2xl border border-caldo-border bg-caldo-bg text-left hover:border-caldo-teal transition-all flex items-center justify-between group";
                b.querySelector('span:last-child').className = "w-6 h-6 rounded-full bg-white text-caldo-teal flex items-center justify-center font-bold text-xs shadow-sm";
                b.querySelector('span:last-child').innerText = "○";
            });

            btn.className = "p-4 rounded-2xl border-2 border-caldo-coral bg-caldo-coralLight text-left transition-all flex items-center justify-between group shadow-sm";
            btn.querySelector('span:last-child').className = "w-6 h-6 rounded-full bg-caldo-coral text-white flex items-center justify-center font-bold text-xs shadow-sm";
            btn.querySelector('span:last-child').innerText = "✓";

            // Snap data into socket
            setTimeout(() => {
                const info = clinicData[key];
                if (info) {
                    document.getElementById('dock-tag').innerText = info.tag;
                    document.getElementById('dock-name').innerText = info.name;
                    document.getElementById('dock-address').innerText = info.address;
                    document.getElementById('dock-extra').innerHTML = `<span>${info.extra}</span>`;
                }
                socket.classList.add('is-docked');
            }, 160);
        }

        // 3. TRANSIZIONE DI PAGINA VARCO ARTICOLARE
        document.addEventListener('DOMContentLoaded', () => {
            const curtain = document.getElementById('articular-curtain');
            const navTriggers = document.querySelectorAll('.nav-trigger');
            const pageViews = document.querySelectorAll('.page-view');

            function switchViewWithJointTransition(targetId) {
                const targetEl = document.getElementById('view-' + targetId);
                if (!targetEl) return;

                // Animazione apertura varco (curtain)
                curtain.classList.add('curtain-close');

                setTimeout(() => {
                    pageViews.forEach(view => view.classList.remove('active-view'));
                    targetEl.classList.add('active-view');
                    window.scrollTo({ top: 0, behavior: 'instant' });
                    history.pushState(null, '', '#' + targetId);

                    curtain.classList.remove('curtain-close');
                    curtain.classList.add('curtain-open');

                    setTimeout(() => {
                        curtain.classList.remove('curtain-open');
                    }, 400);
                }, 280);
            }

            document.body.addEventListener('click', (e) => {
                const trigger = e.target.closest('.nav-trigger');
                if (trigger) {
                    e.preventDefault();
                    const target = trigger.getAttribute('data-target');
                    if (target) {
                        switchViewWithJointTransition(target);
                    }
                }
            });

            if (window.location.hash) {
                const hashId = window.location.hash.replace('#', '');
                const targetEl = document.getElementById('view-' + hashId);
                if (targetEl) {
                    pageViews.forEach(view => view.classList.remove('active-view'));
                    targetEl.classList.add('active-view');
                }
            }

            // Scroll reveal
            const revealElements = document.querySelectorAll('.reveal-soft');
            const revealObserver = new IntersectionObserver((entries) => {
                entries.forEach((entry, idx) => {
                    if (entry.isIntersecting) {
                        setTimeout(() => entry.target.classList.add('is-visible'), idx * 70);
                    }
                });
            }, { threshold: 0.1 });
            revealElements.forEach(el => revealObserver.observe(el));
        });
    </script>

</body>
</html>
"""

# Salva su handoff_sito.html
target_path = "/Volumes/Programs/Temporary files/Progetti cursor/Michele_Novi_Website/handoff_sito.html"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_content)

# Salva copia sincronizzata in Proposte HTML
proposte_path = "/Volumes/Programs/Temporary files/Progetti cursor/Michele_Novi_Website/Proposte HTML/index.html"
with open(proposte_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Prototipo con TUTTI I 5 MECCANISMI D'INCASTRO E TRANSIZIONI generato con successo!")
