# -*- coding: utf-8 -*-
"""
Script per reintegrare TUTTO il contenuto clinico, biografico e informativo
proveniente dalla Bibbia di progetto (04_Architettura_Informazione.md, 08_Sedi, 15_CV, ecc.),
mantenendo al 100%:
- I 5 meccanismi d'incastro articolare e transizioni fluide
- Gradienti leggeri e caldi
- Logo puramente tipografico (nessun box quadrato)
- Iconografia medica raffinata
- Le schede approfondite per tutte le 6 patologie, le sedi dettagliate, le note cliniche estese e il form completo.
"""

import os

html_content = """<!DOCTYPE html>
<html lang="it" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dott. Michele Novi | Chirurgo Ortopedico Spalla e Arto Superiore</title>
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Google Fonts: Newsreader (eleganza clinica) + Plus Jakarta Sans (calore e leggibilità) -->
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
        }

        body {
            background-color: #FAF8F5;
            color: #162122;
            font-family: 'Plus Jakarta Sans', sans-serif;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }

        /* 1. MESH D'AMBIENTE CON SFUMATURE SOFFUSE */
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

        /* 2. GIUNTO MORFICO (SCROLL SEAM) */
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
        }

        /* 3. CARD A DUE METÀ CONGRUENTI */
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

        /* 4. TAB CON RACCORDO INVERSO */
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
        
        /* 5. STRATI SOVRAPPOSTI (STICKY STRATA) */
        .strata-card-soft {
            position: sticky;
            border-radius: 32px;
            background: linear-gradient(180deg, #FFFFFF 0%, #FCFBF9 100%);
            border: 1px solid #EBE7DF;
            box-shadow: 0 -8px 28px rgba(22, 33, 34, 0.03);
            transition: transform 0.4s var(--ease-silk);
        }
        .strata-card-soft:nth-child(1) { top: 6rem; z-index: 10; }
        .strata-card-soft:nth-child(2) { top: 8.5rem; z-index: 20; }
        .strata-card-soft:nth-child(3) { top: 11rem; z-index: 30; }
        .strata-card-soft:nth-child(4) { top: 13.5rem; z-index: 40; }

        /* 6. DOCKING DELLE SEDI */
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

        /* 7. TRANSIZIONE VARCO ARTICOLARE */
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

        /* Card traslucide e bottoni fluidi */
        .card-soft-gradient {
            background: linear-gradient(180deg, rgba(255, 255, 255, 0.95) 0%, rgba(250, 248, 245, 0.85) 100%);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(235, 231, 223, 0.85);
            transition: all 0.45s var(--ease-silk);
        }
        .card-soft-gradient:hover {
            transform: translateY(-4px);
            border-color: rgba(12, 83, 92, 0.35);
            box-shadow: 0 20px 40px -15px rgba(12, 83, 92, 0.08);
        }

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

    <div id="articular-curtain" aria-hidden="true"></div>
    <div class="ambient-mesh" aria-hidden="true"></div>

    <!-- ============================================================
         HEADER: LOGO TIPOGRAFICO PURO (NESSUN BOX QUADRATO)
         ============================================================ -->
    <header class="fixed top-0 left-0 w-full z-50 bg-[#FAF8F5]/90 backdrop-blur-md border-b border-caldo-borderSoft transition-all duration-300" id="main-header">
        <div class="max-w-7xl mx-auto px-6 h-20 flex justify-between items-center">
            
            <a href="#home" class="nav-trigger group flex flex-col cursor-pointer" data-target="home">
                <span class="font-serif text-2xl sm:text-[26px] tracking-tight text-caldo-text font-normal leading-tight group-hover:text-caldo-teal transition-colors duration-300">
                    Dott. Michele Novi
                </span>
                <span class="text-[11px] font-medium text-caldo-muted group-hover:text-caldo-teal transition-colors flex items-center gap-1.5 mt-0.5">
                    <span class="w-1.5 h-1.5 rounded-full bg-caldo-coral"></span>
                    <span>Ortopedia & Chirurgia Arto Superiore · CESAT Fucecchio</span>
                </span>
            </a>

            <nav class="hidden lg:flex items-center gap-1 text-sm font-medium text-caldo-text">
                <a href="#chi-sono" class="nav-trigger px-4 py-2 rounded-full hover:bg-white/80 hover:text-caldo-teal transition-all" data-target="chi-sono">Chi sono</a>
                <a href="#patologie" class="nav-trigger px-4 py-2 rounded-full hover:bg-white/80 hover:text-caldo-teal transition-all" data-target="patologie">Cosa curo</a>
                <a href="#sedi" class="nav-trigger px-4 py-2 rounded-full hover:bg-white/80 hover:text-caldo-teal transition-all" data-target="sedi">Dove ricevo</a>
                <a href="#articoli" class="nav-trigger px-4 py-2 rounded-full hover:bg-white/80 hover:text-caldo-teal transition-all" data-target="articoli">Note cliniche</a>
                <a href="#contatti" class="nav-trigger px-4 py-2 rounded-full hover:bg-white/80 hover:text-caldo-teal transition-all" data-target="contatti">Contatti</a>
            </nav>

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

    <main class="relative z-10 pt-20" id="app-root">

        <!-- ========================================================
             VISTA 1: HOME COMPLETA
             ======================================================== -->
        <section id="view-home" class="page-view active-view">
            
            <div class="max-w-7xl mx-auto px-6 pt-12 pb-20">
                <div class="inline-flex items-center gap-2 bg-gradient-to-r from-caldo-tealLight/80 to-caldo-coralLight/80 border border-white px-4 py-1.5 rounded-full shadow-sm mb-8">
                    <span class="w-2 h-2 rounded-full bg-caldo-coral"></span>
                    <span class="text-xs font-semibold text-caldo-teal">Polo Ospedaliero CESAT Fucecchio</span>
                    <span class="text-caldo-muted text-xs">· Sedi tra Valdera, Empolese e Pisa</span>
                </div>

                <div class="grid lg:grid-cols-12 gap-12 items-center">
                    <div class="lg:col-span-7 space-y-6">
                        <h1 class="text-4xl sm:text-6xl xl:text-7xl font-serif text-caldo-text font-normal leading-[1.07] tracking-tight">
                            Ritrovare il movimento,<br>
                            con la precisione di <br>
                            <span class="italic text-caldo-teal bg-gradient-to-r from-caldo-teal to-caldo-coral bg-clip-text text-transparent font-medium">due superfici che combaciano.</span>
                        </h1>

                        <p class="text-lg sm:text-xl text-caldo-muted font-light leading-relaxed max-w-xl">
                            Specialista della spalla, del gomito e della mano. Dalla chirurgia artroscopica mini-invasiva alle protesi articolari avanzate, con l'ascolto e la dedizione di un medico del territorio.
                        </p>

                        <div class="grid sm:grid-cols-3 gap-3.5 pt-2">
                            <div class="flex items-center gap-3 p-3.5 rounded-2xl bg-white/80 border border-caldo-borderSoft shadow-sm">
                                <div class="w-10 h-10 rounded-xl bg-caldo-tealLight text-caldo-teal flex items-center justify-center flex-shrink-0">
                                    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>
                                </div>
                                <div class="text-xs">
                                    <strong class="block text-caldo-text font-semibold">Spalla & Arto</strong>
                                    <span class="text-caldo-muted text-[11px]">Core specialistico</span>
                                </div>
                            </div>
                            <div class="flex items-center gap-3 p-3.5 rounded-2xl bg-white/80 border border-caldo-borderSoft shadow-sm">
                                <div class="w-10 h-10 rounded-xl bg-caldo-coralLight text-caldo-coral flex items-center justify-center flex-shrink-0">
                                    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"/><path d="M12 3v2M12 19v2M3 12h2M19 12h2"/></svg>
                                </div>
                                <div class="text-xs">
                                    <strong class="block text-caldo-text font-semibold">Artroscopia</strong>
                                    <span class="text-caldo-muted text-[11px]">Visione mini-invasiva</span>
                                </div>
                            </div>
                            <div class="flex items-center gap-3 p-3.5 rounded-2xl bg-white/80 border border-caldo-borderSoft shadow-sm">
                                <div class="w-10 h-10 rounded-xl bg-caldo-salviaLight text-caldo-salvia flex items-center justify-center flex-shrink-0">
                                    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 21h18M5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16"/><path d="M9 10h6M12 7v6"/></svg>
                                </div>
                                <div class="text-xs">
                                    <strong class="block text-caldo-text font-semibold">Polo CESAT</strong>
                                    <span class="text-caldo-muted text-[11px]">Centro regionale protesi</span>
                                </div>
                            </div>
                        </div>

                        <div class="flex flex-wrap gap-4 pt-3">
                            <a href="#contatti" class="nav-trigger btn-fluid-primary px-8 py-4 text-sm font-semibold" data-target="contatti">
                                <span>Richiedi una Visita</span>
                                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                            </a>
                            <a href="#patologie" class="nav-trigger px-7 py-4 rounded-full bg-white border border-caldo-border text-caldo-teal text-sm font-semibold hover:border-caldo-teal transition-all" data-target="patologie">
                                <span>Esplora le Patologie</span>
                                <span class="ml-1">→</span>
                            </a>
                        </div>
                    </div>

                    <div class="lg:col-span-5 relative">
                        <div class="relative z-10 p-3.5 rounded-[36px] bg-gradient-to-br from-white via-white/90 to-caldo-coralLight/40 border border-white shadow-xl shadow-caldo-teal/5">
                            <div class="aspect-[4/5] rounded-[28px] overflow-hidden relative bg-gradient-to-tr from-caldo-tealLight to-caldo-coralLight">
                                <img src="https://images.unsplash.com/photo-1622253692010-333f2da6031d?q=80&w=1000&auto=format&fit=crop" 
                                     alt="Dott. Michele Novi" 
                                     class="w-full h-full object-cover object-center filter contrast-[1.02]">
                                <div class="absolute inset-0 bg-gradient-to-t from-caldo-teal/70 via-transparent to-transparent opacity-60"></div>
                                <div class="absolute bottom-5 left-5 right-5 bg-white/95 backdrop-blur-md p-4 rounded-2xl border border-white/80 shadow-md flex items-center justify-between">
                                    <div>
                                        <span class="text-sm font-serif font-semibold text-caldo-text block">Dott. Michele Novi</span>
                                        <span class="text-[11px] text-caldo-teal font-medium">Dirigente Medico Ospedale CESAT Fucecchio</span>
                                    </div>
                                    <div class="w-8 h-8 rounded-full bg-caldo-tealLight text-caldo-teal flex items-center justify-center">
                                        <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- IL GIUNTO MORFICO -->
            <div class="joint-seam">
                <svg class="joint-seam-curve" viewBox="0 0 1440 48" preserveAspectRatio="none">
                    <path d="M0,0 C320,0 480,48 720,48 C960,48 1120,0 1440,0 L1440,48 L0,48 Z"/>
                </svg>
            </div>

            <!-- CARD A DUE METÀ CONGRUENTI (HILL-SACHS E REMPLISSAGE) -->
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
                            Passa con il mouse sulla card sottostante: vedrai come la diagnosi del problema e la soluzione chirurgica si attraggono e si uniscono al millimetro, ristabilendo la congruenza articolare naturale.
                        </p>
                    </div>

                    <div class="congruent-card-wrapper max-w-5xl mx-auto group cursor-pointer">
                        <div class="congruent-half-left p-8 sm:p-10 space-y-4">
                            <div class="flex justify-between items-center">
                                <span class="text-xs font-bold text-caldo-coral uppercase tracking-wider">01. La Lesione Ossea</span>
                                <span class="text-[11px] font-mono text-caldo-muted">TESTA OMERALE</span>
                            </div>
                            <h3 class="text-2xl font-serif text-caldo-text font-semibold">
                                La nicchia di Hill-Sachs che scardina l'articolazione.
                            </h3>
                            <p class="text-sm text-caldo-muted font-light leading-relaxed">
                                Nelle lussazioni recidivanti, l'impatto ripetuto contro il bordo glenoideo scava una lesione nell'osso. Durante la rotazione del braccio, questa fessura <em>si incastra sul ciglio della glenoide</em>, facendo uscire la spalla dalla sua sede.
                            </p>
                            <div class="pt-4 flex items-center gap-2 text-xs text-caldo-coral font-medium">
                                <span class="w-2 h-2 rounded-full bg-caldo-coral animate-ping"></span>
                                <span>Stato: Instabilità e rischio lussazione</span>
                            </div>
                        </div>

                        <div class="congruent-half-right p-8 sm:p-10 space-y-4">
                            <div class="flex justify-between items-center">
                                <span class="text-xs font-bold text-caldo-teal uppercase tracking-wider">02. L'Incastro Ripristinato</span>
                                <span class="joint-snap-badge text-[11px] font-medium bg-caldo-tealLight text-caldo-teal px-3 py-1 rounded-full">
                                    Avvicina per innestare
                                </span>
                            </div>
                            <h3 class="text-2xl font-serif text-caldo-text font-semibold">
                                Procedura di Remplissage: colmare il vuoto per scivolare.
                            </h3>
                            <p class="text-sm text-caldo-muted font-light leading-relaxed">
                                Fissiamo il tendine dell'infraspinato direttamente all'interno della lesione ossea: la nicchia viene riempita ed esclusa dalla cavità. Le superfici tornano perfettamente lisce e la spalla ruota senza blocchi.
                            </p>
                            <div class="pt-4 flex items-center justify-between text-xs">
                                <span class="text-caldo-teal font-semibold">Risultato: Stabilità 100% · ROM preservato</span>
                                <span class="text-caldo-muted font-mono">Paper CESAT 2022 →</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- I TAB A RACCORDO INVERSO DELLE 6 PATOLOGIE -->
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
                        Seleziona un'articolazione per osservare come il riquadro del contenuto si raccorda con continuità al selettore.
                    </p>
                </div>

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

            <!-- SEZIONE STRATI ANATOMICI SOVRAPPOSTI (UNO STRATO SOTTO L'ALTRO) -->
            <div class="max-w-7xl mx-auto px-6 py-28 border-t border-caldo-borderSoft">
                <div class="max-w-2xl mb-16 space-y-3">
                    <span class="inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal bg-caldo-tealLight px-3.5 py-1 rounded-full">
                        <span class="w-1.5 h-1.5 rounded-full bg-caldo-teal"></span>
                        Dissezione & Anatomia Funzionale
                    </span>
                    <h2 class="text-3xl sm:text-5xl font-serif text-caldo-text leading-tight">
                        Uno strato sotto l'altro: il rispetto biologico dei tessuti.
                    </h2>
                    <p class="text-base text-caldo-muted font-light leading-relaxed">
                        In chirurgia non si aggredisce il corpo: si attraversano con delicatezza i diversi strati tessutali per raggiungere l'origine esatta del dolore.
                    </p>
                </div>

                <div class="space-y-8 relative">
                    <div class="strata-card-soft p-8 md:p-12">
                        <div class="grid md:grid-cols-12 gap-6 items-center">
                            <div class="md:col-span-2 flex md:flex-col items-center gap-2">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-caldo-tealLight to-white text-caldo-teal flex items-center justify-center shadow-sm">
                                    <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 2v20M2 12h20M7 7l10 10M7 17l10-10"/></svg>
                                </div>
                                <span class="text-xs font-bold text-caldo-teal tracking-wider uppercase">Strato 01</span>
                            </div>
                            <div class="md:col-span-7 space-y-1.5">
                                <h3 class="text-2xl font-serif text-caldo-text">L'Accesso Mini-Invasivo</h3>
                                <p class="text-sm text-caldo-muted leading-relaxed font-light">
                                    Attraverso micro-portali ottici da 5 millimetri preserviamo i muscoli di superficie, minimizzando il dolore post-operatorio e garantendo una cicatrizzazione rapida.
                                </p>
                            </div>
                            <div class="md:col-span-3 text-right">
                                <span class="inline-block bg-caldo-tealLight text-caldo-teal text-xs font-semibold px-4 py-1.5 rounded-full">Artroscopia Avanzata</span>
                            </div>
                        </div>
                    </div>

                    <div class="strata-card-soft p-8 md:p-12">
                        <div class="grid md:grid-cols-12 gap-6 items-center">
                            <div class="md:col-span-2 flex md:flex-col items-center gap-2">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-caldo-coralLight to-white text-caldo-coral flex items-center justify-center shadow-sm">
                                    <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M18 8h1a4 4 0 0 1 0 8h-1M6 8H5a4 4 0 0 0 0 8h1M2 12h20"/></svg>
                                </div>
                                <span class="text-xs font-bold text-caldo-coral tracking-wider uppercase">Strato 02</span>
                            </div>
                            <div class="md:col-span-7 space-y-1.5">
                                <h3 class="text-2xl font-serif text-caldo-text">I Tendini della Cuffia dei Rotatori</h3>
                                <p class="text-sm text-caldo-muted leading-relaxed font-light">
                                    Il motore della spalla. Ripariamo le lesioni con suture anatomiche su micro-ancore biologiche riassorbibili, valutando sempre con attenzione quando è preferibile il percorso conservativo con fisioterapia mirata.
                                </p>
                            </div>
                            <div class="md:col-span-3 text-right">
                                <span class="inline-block bg-caldo-coralLight text-caldo-coral text-xs font-semibold px-4 py-1.5 rounded-full">Riparazione Tendinea</span>
                            </div>
                        </div>
                    </div>

                    <div class="strata-card-soft p-8 md:p-12">
                        <div class="grid md:grid-cols-12 gap-6 items-center">
                            <div class="md:col-span-2 flex md:flex-col items-center gap-2">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-caldo-goldLight to-white text-caldo-gold flex items-center justify-center shadow-sm">
                                    <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                                </div>
                                <span class="text-xs font-bold text-caldo-gold tracking-wider uppercase">Strato 03</span>
                            </div>
                            <div class="md:col-span-7 space-y-1.5">
                                <h3 class="text-2xl font-serif text-caldo-text">Il Cercine e la Capsula Articolare</h3>
                                <p class="text-sm text-caldo-muted leading-relaxed font-light">
                                    La guarnizione legamentosa che stabilizza la testa dell'omero. La ricostruzione di Bankart ripristina la sicurezza nei giovani sportivi e nei lavoratori soggetti a sforzi ripetuti.
                                </p>
                            </div>
                            <div class="md:col-span-3 text-right">
                                <span class="inline-block bg-caldo-goldLight text-caldo-gold text-xs font-semibold px-4 py-1.5 rounded-full">Stabilità Articolare</span>
                            </div>
                        </div>
                    </div>

                    <div class="strata-card-soft p-8 md:p-12">
                        <div class="grid md:grid-cols-12 gap-6 items-center">
                            <div class="md:col-span-2 flex md:flex-col items-center gap-2">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-caldo-salviaLight to-white text-caldo-salvia flex items-center justify-center shadow-sm">
                                    <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><line x1="6" y1="9" x2="6" y2="15"/><circle cx="18" cy="6" r="3"/><circle cx="18" cy="18" r="3"/><line x1="18" y1="9" x2="18" y2="15"/><line x1="9" y1="12" x2="15" y2="12"/></svg>
                                </div>
                                <span class="text-xs font-bold text-caldo-salvia tracking-wider uppercase">Strato 04</span>
                            </div>
                            <div class="md:col-span-7 space-y-1.5">
                                <h3 class="text-2xl font-serif text-caldo-text">La Struttura Ossea e la Protesica</h3>
                                <p class="text-sm text-caldo-muted leading-relaxed font-light">
                                    Nel polo ospedaliero CESAT di Fucecchio trattiamo l'artrosi avanzata con impianti protesici anatomici o inversi, restituendo completa autonomia e sonno sereno senza dolore.
                                </p>
                            </div>
                            <div class="md:col-span-3 text-right">
                                <span class="inline-block bg-caldo-salviaLight text-caldo-salvia text-xs font-semibold px-4 py-1.5 rounded-full">Protesica d'Eccellenza</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- IL DOCKING INTERATTIVO DELLE SEDI -->
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
             VISTA 2: CHI SONO (PROFILO COMPLETO DELLA BIBBIA)
             ======================================================== -->
        <section id="view-chi-sono" class="page-view max-w-6xl mx-auto px-6 py-16">
            <a href="#home" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal hover:text-caldo-coral mb-8 transition-colors" data-target="home">
                <span>← Torna alla Home</span>
            </a>

            <div class="max-w-3xl mb-16 space-y-4">
                <span class="text-xs font-semibold text-caldo-teal bg-caldo-tealLight px-3.5 py-1.5 rounded-full inline-block">
                    Identità e Visione Clinica
                </span>
                <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text leading-tight">
                    Chirurgia di precisione,<br>
                    <span class="italic text-caldo-teal font-medium">vicinanza alla persona.</span>
                </h1>
                <p class="text-lg text-caldo-muted font-light leading-relaxed">
                    «Operare bene è un dovere tecnico; guidare il paziente con parole chiare, senza fretta e concordando la strategia migliore è una scelta di rispetto umano.»
                </p>
            </div>

            <div class="grid lg:grid-cols-12 gap-12 items-start">
                <div class="lg:col-span-5 space-y-6">
                    <div class="bg-white p-4 rounded-3xl border border-caldo-border shadow-md">
                        <div class="aspect-[3/4] rounded-2xl overflow-hidden bg-caldo-tealLight mb-4">
                            <img src="https://images.unsplash.com/photo-1622253692010-333f2da6031d?q=80&w=800&auto=format&fit=crop" 
                                 alt="Dott. Michele Novi" 
                                 class="w-full h-full object-cover">
                        </div>
                        <div class="p-2 space-y-1">
                            <h3 class="text-lg font-serif font-bold text-caldo-text">Dott. Michele Novi</h3>
                            <p class="text-xs text-caldo-muted">Dirigente Medico Ortopedico · Ospedale CESAT Fucecchio</p>
                            <p class="text-xs text-caldo-teal font-medium">Iscritto all'Ordine dei Medici di Pisa n. 5988</p>
                        </div>
                    </div>

                    <div class="bg-gradient-to-br from-caldo-coralLight to-caldo-goldLight/40 p-6 rounded-3xl border border-caldo-coral/20 space-y-3">
                        <span class="text-xs font-bold text-caldo-coral uppercase tracking-wider block">Due Tempi, Un Medico Solo</span>
                        <p class="text-xs text-caldo-muted leading-relaxed font-light">
                            <strong>La Sala di Volume:</strong> Al CESAT di Fucecchio affronto quotidianamente la chirurgia protesica e artroscopica complessa, forte di una casistica operatoria di rilievo.
                        </p>
                        <p class="text-xs text-caldo-muted leading-relaxed font-light">
                            <strong>Il Territorio:</strong> Negli ambulatori della Valdera e di Pisa ascolto le storie dei pazienti, imposto il percorso e seguo la guarigione passo dopo passo senza intermediari.
                        </p>
                    </div>
                </div>

                <div class="lg:col-span-7 space-y-8">
                    <div class="space-y-6 text-base text-caldo-muted font-light leading-relaxed">
                        <p>
                            Mi sono laureato e specializzato con lode presso l'<strong>Università di Pisa</strong>, allievo della scuola del Prof. Porcellini e stretto collaboratore del Dott. Nicoletti. Fin dagli anni della formazione, ho concentrato la mia attenzione sulle patologie dell'arto superiore e sul trattamento del trauma sportivo.
                        </p>
                        <p>
                            Credo che l'aggiornamento internazionale sia fondamentale per un chirurgo. Per questo ho completato un'intensa fellowship presso il celebre <strong>Harborview Medical Center di Seattle (USA)</strong>, punto di riferimento mondiale per la traumatologia ad alta energia e la microchirurgia ricostruttiva dei nervi periferici, integrando poi la mia esperienza a Londra e presso la Charité di Berlino.
                        </p>
                        <p>
                            Sono socio ordinario delle maggiori società scientifiche del settore (<strong>SIAGASCOT</strong> e <strong>SICSEG</strong>) e autore di oltre 15 pubblicazioni su riviste internazionali peer-reviewed, con particolare focus sulla stabilità della spalla e sulle tecniche di salvataggio articolare.
                        </p>
                    </div>

                    <div class="border-t border-caldo-border pt-8 space-y-4">
                        <h4 class="text-xl font-serif text-caldo-text font-semibold">Tappe Salienti della Formazione</h4>

                        <div class="flex items-start gap-4 p-4 rounded-2xl bg-white border border-caldo-border shadow-sm">
                            <div class="w-10 h-10 rounded-xl bg-caldo-tealLight text-caldo-teal flex items-center justify-center font-bold text-base flex-shrink-0">🏥</div>
                            <div>
                                <span class="text-xs font-bold text-caldo-teal block">2020 – Presente</span>
                                <strong class="text-sm text-caldo-text block">Dirigente Medico Ortopedico · Ospedale CESAT Fucecchio</strong>
                                <p class="text-xs text-caldo-muted mt-0.5">Centro regionale di eccellenza per le sostituzioni articolari e chirurgia artroscopica.</p>
                            </div>
                        </div>

                        <div class="flex items-start gap-4 p-4 rounded-2xl bg-white border border-caldo-border shadow-sm">
                            <div class="w-10 h-10 rounded-xl bg-caldo-coralLight text-caldo-coral flex items-center justify-center font-bold text-base flex-shrink-0">🇺🇸</div>
                            <div>
                                <span class="text-xs font-bold text-caldo-coral block">Fellowship Internazionale</span>
                                <strong class="text-sm text-caldo-text block">Harborview Medical Center · Seattle (USA)</strong>
                                <p class="text-xs text-caldo-muted mt-0.5">Microchirurgia dei lembi, riparazioni nervose e traumatologia complessa.</p>
                            </div>
                        </div>

                        <div class="flex items-start gap-4 p-4 rounded-2xl bg-white border border-caldo-border shadow-sm">
                            <div class="w-10 h-10 rounded-xl bg-caldo-salviaLight text-caldo-salvia flex items-center justify-center font-bold text-base flex-shrink-0">🔬</div>
                            <div>
                                <span class="text-xs font-bold text-caldo-salvia block">Certificazione SIUMB</span>
                                <strong class="text-sm text-caldo-text block">Diploma Nazionale in Ecografia Muscoloscheletrica</strong>
                                <p class="text-xs text-caldo-muted mt-0.5">Valutazione ecografica immediata in studio e infiltrazioni eco-guidate.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ========================================================
             VISTA 3: PATOLOGIE (HUB COMPLETO)
             ======================================================== -->
        <section id="view-patologie" class="page-view max-w-7xl mx-auto px-6 py-16">
            <a href="#home" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal hover:text-caldo-coral mb-8 transition-colors" data-target="home">
                <span>← Torna alla Home</span>
            </a>
            <div class="max-w-3xl mb-16 space-y-4">
                <span class="text-xs font-semibold text-caldo-teal bg-caldo-tealLight px-3.5 py-1.5 rounded-full inline-block">Aree Cliniche</span>
                <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text leading-tight">Cosa curo: 6 percorsi specialistici.</h1>
                <p class="text-base text-caldo-muted font-light leading-relaxed">
                    Dalla diagnosi palpatoria ed ecografica alla chirurgia d'avanguardia: ogni articolazione viene trattata con l'obiettivo del massimo recupero funzionale.
                </p>
            </div>

            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Spalla -->
                <div class="card-soft-gradient p-8 rounded-3xl flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-caldo-tealLight text-caldo-teal flex items-center justify-center mb-6">
                            <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>
                        </div>
                        <h3 class="text-2xl font-serif text-caldo-text mb-3">Chirurgia della Spalla</h3>
                        <p class="text-xs text-caldo-muted leading-relaxed font-light mb-6">
                            Rotture della cuffia dei rotatori, instabilità e lussazioni recidivanti (Bankart, Remplissage), artrosi e protesi anatomica o inversa.
                        </p>
                    </div>
                    <a href="#patologie-spalla" class="nav-trigger btn-fluid-primary !py-2.5 !px-5 text-xs justify-center" data-target="patologie-spalla">Scheda Spalla →</a>
                </div>

                <!-- Gomito -->
                <div class="card-soft-gradient p-8 rounded-3xl flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-caldo-coralLight text-caldo-coral flex items-center justify-center mb-6">
                            <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M18 10h-4a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h4a2 2 0 0 0 2-2v-8a2 2 0 0 0-2-2Z"/><path d="M6 4h4a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2Z"/></svg>
                        </div>
                        <h3 class="text-2xl font-serif text-caldo-text mb-3">Gomito e Traumatologia</h3>
                        <p class="text-xs text-caldo-muted leading-relaxed font-light mb-6">
                            Rigidità post-traumatica, epicondilite resistente (gomito del tennista) e reinserzione del tendine distale del bicipite brachiale.
                        </p>
                    </div>
                    <a href="#patologie-gomito" class="nav-trigger btn-fluid-primary !py-2.5 !px-5 text-xs justify-center" data-target="patologie-gomito">Scheda Gomito →</a>
                </div>

                <!-- Mano -->
                <div class="card-soft-gradient p-8 rounded-3xl flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-caldo-salviaLight text-caldo-salvia flex items-center justify-center mb-6">
                            <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M18 11V6a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v0"/><path d="M14 10V4a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v2"/><path d="M10 10.5V6a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v8"/></svg>
                        </div>
                        <h3 class="text-2xl font-serif text-caldo-text mb-3">Mano e Polso</h3>
                        <p class="text-xs text-caldo-muted leading-relaxed font-light mb-6">
                            Tunnel carpale con tecnica mini-invasiva, dito a scatto, morbo di De Quervain e rizoartrosi con impianti o chirurgia conservativa.
                        </p>
                    </div>
                    <a href="#patologie-mano" class="nav-trigger btn-fluid-primary !py-2.5 !px-5 text-xs justify-center" data-target="patologie-mano">Scheda Mano e Polso →</a>
                </div>

                <!-- Sport -->
                <div class="card-soft-gradient p-8 rounded-3xl flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-caldo-goldLight text-caldo-gold flex items-center justify-center mb-6">
                            <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/><path d="M4 22h16"/></svg>
                        </div>
                        <h3 class="text-2xl font-serif text-caldo-text mb-3">Traumatologia Sportiva</h3>
                        <p class="text-xs text-caldo-muted leading-relaxed font-light mb-6">
                            Collaborazione con Athletica Pisa: lesioni da contatto, lussazioni acromion-claveari e protocolli per il ritorno allo sport in sicurezza.
                        </p>
                    </div>
                    <a href="#patologie-traumatologia-sportiva" class="nav-trigger btn-fluid-primary !py-2.5 !px-5 text-xs justify-center" data-target="patologie-traumatologia-sportiva">Scheda Sport →</a>
                </div>

                <!-- Artroscopia -->
                <div class="card-soft-gradient p-8 rounded-3xl flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-caldo-tealLight text-caldo-teal flex items-center justify-center mb-6">
                            <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="3"/><path d="M3 7V5a2 2 0 0 1 2-2h2M17 3h2a2 2 0 0 1 2 2v2M21 17v2a2 2 0 0 1-2 2h-2M7 21H5a2 2 0 0 1-2-2v-2"/></svg>
                        </div>
                        <h3 class="text-2xl font-serif text-caldo-text mb-3">Chirurgia Artroscopica</h3>
                        <p class="text-xs text-caldo-muted leading-relaxed font-light mb-6">
                            La metodologia mini-invasiva a visione ottica diretta ad alta definizione per riparazioni interne senza incisioni a cielo aperto.
                        </p>
                    </div>
                    <a href="#patologie-artroscopia" class="nav-trigger btn-fluid-primary !py-2.5 !px-5 text-xs justify-center" data-target="patologie-artroscopia">Scheda Artroscopia →</a>
                </div>

                <!-- Ecografia -->
                <div class="card-soft-gradient p-8 rounded-3xl flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-caldo-coralLight text-caldo-coral flex items-center justify-center mb-6">
                            <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M2 12h5l3 8 4-16 3 8h5"/></svg>
                        </div>
                        <h3 class="text-2xl font-serif text-caldo-text mb-3">Ecografia Muscoloscheletrica</h3>
                        <p class="text-xs text-caldo-muted leading-relaxed font-light mb-6">
                            Diploma SIUMB: valutazione dinamica dei tendini in ambulatorio e infiltrazioni eco-guidate per una precisione anatomica assoluta.
                        </p>
                    </div>
                    <a href="#patologie-ecografia-muscoloscheletrica" class="nav-trigger btn-fluid-primary !py-2.5 !px-5 text-xs justify-center" data-target="patologie-ecografia-muscoloscheletrica">Scheda Ecografia →</a>
                </div>
            </div>
        </section>

        <!-- SOTTO-VISTE SPECIFICHE DELLE 6 PATOLOGIE (TESTO INTEGRATO DALLA BIBBIA) -->
        
        <!-- 1. DETTAGLIO SPALLA -->
        <section id="view-patologie-spalla" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal hover:text-caldo-coral mb-8" data-target="patologie">← Torna alle Patologie</a>
            <span class="text-xs font-semibold text-caldo-teal bg-caldo-tealLight px-3.5 py-1.5 rounded-full inline-block mb-3">Area Specialistica 01</span>
            <h1 class="text-4xl sm:text-5xl font-serif text-caldo-text mb-6">Chirurgia della spalla.</h1>
            <div class="space-y-6 text-base text-caldo-muted font-light leading-relaxed">
                <p>
                    La chirurgia della spalla rappresenta il cuore della mia pratica clinica quotidiana al CESAT di Fucecchio. Tratto sia la patologia degenerativa dell'adulto e dell'anziano, sia i traumi da sport e da impatto nei giovani atleti.
                </p>
                <div class="my-6 p-6 rounded-3xl bg-white border border-caldo-border space-y-4">
                    <h3 class="text-xl font-serif font-bold text-caldo-text">Percorsi principali di trattamento:</h3>
                    <ul class="space-y-3 text-sm">
                        <li class="flex items-start gap-3">
                            <span class="w-5 h-5 rounded-full bg-caldo-tealLight text-caldo-teal flex items-center justify-center font-bold text-xs flex-shrink-0">✓</span>
                            <span><strong>Cuffia dei Rotatori:</strong> sutura artroscopica anatomica di sovraspinato, sottoscapolare e infraspinato con ancore riassorbibili. Gestione avanzata delle lesioni massive e irreparabili.</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <span class="w-5 h-5 rounded-full bg-caldo-coralLight text-caldo-coral flex items-center justify-center font-bold text-xs flex-shrink-0">✓</span>
                            <span><strong>Instabilità e Lussazioni:</strong> riparazione del cercine glenoideo (Bankart) e procedura di Remplissage per escludere il difetto di Hill-Sachs.</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <span class="w-5 h-5 rounded-full bg-caldo-salviaLight text-caldo-salvia flex items-center justify-center font-bold text-xs flex-shrink-0">✓</span>
                            <span><strong>Protesica di Spalla:</strong> artroplastica anatomica (per preservare la cuffia) e protesi inversa (per artrosi con rottura massiva della cuffia, sfruttando la forza del deltoide).</span>
                        </li>
                    </ul>
                </div>
                <h3 class="text-2xl font-serif text-caldo-text font-semibold pt-4">Conservativo vs Chirurgico</h3>
                <p>
                    Non tutte le rotture tendinee richiedono la sala operatoria. Se la forza residua e la qualità biologica del tessuto lo consentono, impostiamo percorsi conservativi con infiltrazioni mirate di acido ialuronico e fisioterapia guidata. Quando l'intervento è indispensabile, l'artroscopia permette un recupero sereno e rapido.
                </p>
            </div>
            <div class="mt-12 pt-8 border-t border-caldo-border flex justify-between items-center">
                <span class="text-xs text-caldo-muted">Visite a Fucecchio, Peccioli, Pisa</span>
                <a href="#contatti" class="nav-trigger btn-fluid-coral px-6 py-3 text-xs font-semibold" data-target="contatti">Prenota visita spalla</a>
            </div>
        </section>

        <!-- 2. DETTAGLIO GOMITO -->
        <section id="view-patologie-gomito" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal hover:text-caldo-coral mb-8" data-target="patologie">← Torna alle Patologie</a>
            <span class="text-xs font-semibold text-caldo-coral bg-caldo-coralLight px-3.5 py-1.5 rounded-full inline-block mb-3">Area Specialistica 02</span>
            <h1 class="text-4xl sm:text-5xl font-serif text-caldo-text mb-6">Gomito: traumatologia e artroscopia.</h1>
            <div class="space-y-6 text-base text-caldo-muted font-light leading-relaxed">
                <p>
                    Il gomito è un'articolazione che richiede tolleranza millimetrica: anche una perdita di pochi gradi di estensione può compromettere le normali attività quotidiane o la pratica sportiva.
                </p>
                <div class="p-6 rounded-3xl bg-white border border-caldo-border space-y-3 text-sm">
                    <p><strong>Epicondilite resistente:</strong> trattamento conservativo con infiltrazioni ecoguidate e, nei casi cronici ribelli, release mininvasivo.</p>
                    <p><strong>Fratture del capitello radiale:</strong> sintesi con micro-viti o sostituzione con endoprotesi nei traumi comminuti.</p>
                    <p><strong>Rottura del bicipite distale:</strong> reinserzione anatomica del tendine con bottoni di sospensione corticali e viti a interferenza.</p>
                    <p><strong>Rigidità articolare:</strong> artrolisi artroscopica per asportare osteofiti o corpi mobili e restituire l'escursione articolare.</p>
                </div>
            </div>
            <div class="mt-12 pt-8 border-t border-caldo-border flex justify-between items-center">
                <span class="text-xs text-caldo-muted">Specialista arto superiore</span>
                <a href="#contatti" class="nav-trigger btn-fluid-primary px-6 py-3 text-xs font-semibold" data-target="contatti">Richiedi visita gomito</a>
            </div>
        </section>

        <!-- 3. DETTAGLIO MANO E POLSO -->
        <section id="view-patologie-mano" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal hover:text-caldo-coral mb-8" data-target="patologie">← Torna alle Patologie</a>
            <span class="text-xs font-semibold text-caldo-salvia bg-caldo-salviaLight px-3.5 py-1.5 rounded-full inline-block mb-3">Area Specialistica 03</span>
            <h1 class="text-4xl sm:text-5xl font-serif text-caldo-text mb-6">Mano e polso.</h1>
            <div class="space-y-6 text-base text-caldo-muted font-light leading-relaxed">
                <p>
                    Grazie alla fellowship specialistica presso l'Harborview Medical Center di Seattle (USA), applico tecniche microchirurgiche e mininvasive a tutte le affezioni nervose e tendinee della mano.
                </p>
                <div class="p-6 rounded-3xl bg-white border border-caldo-border space-y-3 text-sm">
                    <p><strong>Sindrome del Tunnel Carpale:</strong> neurolisi e sezione del legamento trasverso del carpo in anestesia locale con immediata scomparsa del formicolio notturno.</p>
                    <p><strong>Dito a scatto e Morbo di De Quervain:</strong> liberazione della puleggia o del primo compartimento estensore con recupero immediato della fluidità di movimento.</p>
                    <p><strong>Rizoartrosi (artrosi del pollice):</strong> dalle infiltrazioni rigenerative alla trapezectomia con sospensivoplastica o protesi trapezio-metacarpale.</p>
                </div>
            </div>
            <div class="mt-12 pt-8 border-t border-caldo-border flex justify-between items-center">
                <span class="text-xs text-caldo-muted">Microchirurgia della mano</span>
                <a href="#contatti" class="nav-trigger btn-fluid-primary px-6 py-3 text-xs font-semibold" data-target="contatti">Richiedi visita mano</a>
            </div>
        </section>

        <!-- 4. DETTAGLIO TRAUMATOLOGIA SPORTIVA -->
        <section id="view-patologie-traumatologia-sportiva" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal hover:text-caldo-coral mb-8" data-target="patologie">← Torna alle Patologie</a>
            <span class="text-xs font-semibold text-caldo-gold bg-caldo-goldLight px-3.5 py-1.5 rounded-full inline-block mb-3">Area Specialistica 04</span>
            <h1 class="text-4xl sm:text-5xl font-serif text-caldo-text mb-6">Traumatologia sportiva.</h1>
            <div class="space-y-6 text-base text-caldo-muted font-light leading-relaxed">
                <p>
                    Come appassionato di sport (tennis, motociclismo, arrampicata) e consulente presso centri di medicina dello sport a Pisa (Athletica), conosco la necessità dell'atleta di tornare in campo rapidamente ma senza forzare i tempi biologici di guarigione.
                </p>
                <div class="p-6 rounded-3xl bg-white border border-caldo-border space-y-3 text-sm">
                    <p><strong>Lussazioni acromion-claveari:</strong> stabilizzazione biologica con legamenti sintetici o ancore nei traumi da caduta in bici, moto o sci.</p>
                    <p><strong>Spalla del lanciatore e dello scalatore:</strong> diagnosi di lesioni SLAP (cercine superiore) e impingement interno postero-superiore.</p>
                    <p><strong>Return to play test:</strong> protocolli condivisi con i fisioterapisti per misurare forza, stabilità e assenza di apprensione prima della ripresa agonistica.</p>
                </div>
            </div>
            <div class="mt-12 pt-8 border-t border-caldo-border flex justify-between items-center">
                <span class="text-xs text-caldo-muted">Ambulatorio atleti Pisa</span>
                <a href="#contatti" class="nav-trigger btn-fluid-coral px-6 py-3 text-xs font-semibold" data-target="contatti">Prenota valutazione sportiva</a>
            </div>
        </section>

        <!-- 5. DETTAGLIO CHIRURGIA ARTROSCOPICA -->
        <section id="view-patologie-artroscopia" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal hover:text-caldo-coral mb-8" data-target="patologie">← Torna alle Patologie</a>
            <span class="text-xs font-semibold text-caldo-teal bg-caldo-tealLight px-3.5 py-1.5 rounded-full inline-block mb-3">Area Specialistica 05</span>
            <h1 class="text-4xl sm:text-5xl font-serif text-caldo-text mb-6">Chirurgia artroscopica: il metodo.</h1>
            <div class="space-y-6 text-base text-caldo-muted font-light leading-relaxed">
                <p>
                    L'artroscopia non è una cura, ma una straordinaria metodologia: attraverso una telecamera millimetrica ad altissima definizione e strumenti dedicati, entriamo all'interno dell'articolazione attraverso piccoli fori di 5 millimetri.
                </p>
                <div class="p-6 rounded-3xl bg-white border border-caldo-border space-y-3 text-sm">
                    <p><strong>Visione diretta ingrandita:</strong> permette di rilevare lesioni cartilaginee o tendinee non sempre evidenti nemmeno con la risonanza magnetica.</p>
                    <p><strong>Rispetto anatomico totale:</strong> i muscoli circostanti non vengono sezionati o staccati dall'osso, riducendo drasticamente il dolore post-operatorio.</p>
                    <p><strong>Recupero accelerato:</strong> dimissione tipicamente in day-hospital o con una sola notte di degenza, con inizio precoce della fisioterapia passiva.</p>
                </div>
            </div>
            <div class="mt-12 pt-8 border-t border-caldo-border flex justify-between items-center">
                <span class="text-xs text-caldo-muted">Minima invasività al CESAT</span>
                <a href="#contatti" class="nav-trigger btn-fluid-primary px-6 py-3 text-xs font-semibold" data-target="contatti">Richiedi valutazione clinica</a>
            </div>
        </section>

        <!-- 6. DETTAGLIO ECOGRAFIA MUSCOLOSCHELETRICA -->
        <section id="view-patologie-ecografia-muscoloscheletrica" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal hover:text-caldo-coral mb-8" data-target="patologie">← Torna alle Patologie</a>
            <span class="text-xs font-semibold text-caldo-coral bg-caldo-coralLight px-3.5 py-1.5 rounded-full inline-block mb-3">Area Specialistica 06</span>
            <h1 class="text-4xl sm:text-5xl font-serif text-caldo-text mb-6">Ecografia muscoloscheletrica.</h1>
            <div class="space-y-6 text-base text-caldo-muted font-light leading-relaxed">
                <p>
                    Ho conseguito il <strong>Diploma Nazionale SIUMB</strong> (Società Italiana di Ultrasonologia in Medicina e Biologia) perché considero l'ecografo il naturale prolungamento delle mani del chirurgo durante la visita in studio.
                </p>
                <div class="p-6 rounded-3xl bg-white border border-caldo-border space-y-3 text-sm">
                    <p><strong>Diagnostica dinamica in tempo reale:</strong> possiamo osservare i tendini mentre il paziente muove la spalla o il gomito, individuando conflitti o scatti che le immagini statiche non possono mostrare.</p>
                    <p><strong>Infiltrazioni eco-guidate:</strong> l'ago viene visualizzato sullo schermo in ogni istante, garantendo che l'acido ialuronico, il cortisonico o i derivati biologici vengano depositati esattamente all'interno della borsa o dello spazio articolare bersaglio.</p>
                    <p><strong>Nessuna attesa:</strong> ecografia eseguita contestualmente alla visita specialistica negli ambulatori provvisti di strumentazione dedicata.</p>
                </div>
            </div>
            <div class="mt-12 pt-8 border-t border-caldo-border flex justify-between items-center">
                <span class="text-xs text-caldo-muted">Certificazione SIUMB</span>
                <a href="#contatti" class="nav-trigger btn-fluid-coral px-6 py-3 text-xs font-semibold" data-target="contatti">Prenota ecografia e visita</a>
            </div>
        </section>

        <!-- ========================================================
             VISTA 4: DOVE RICEVO (LE SEDI CON DETTAGLI COMPLETI)
             ======================================================== -->
        <section id="view-sedi" class="page-view max-w-7xl mx-auto px-6 py-16">
            <a href="#home" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal hover:text-caldo-coral mb-8 transition-colors" data-target="home">
                <span>← Torna alla Home</span>
            </a>

            <div class="max-w-3xl mb-16 space-y-4">
                <span class="text-xs font-semibold text-caldo-teal bg-caldo-tealLight px-3.5 py-1.5 rounded-full inline-block">Presidio Sanitario in Toscana</span>
                <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text leading-tight">Dove ricevo: le strutture attive.</h1>
                <p class="text-base text-caldo-muted font-light leading-relaxed">
                    Tutti gli interventi chirurgici e i ricoveri ospedalieri si svolgono presso l'Ospedale CESAT di Fucecchio. Le prime visite, i controlli e le infiltrazioni sono distribuiti su 4 sedi territoriali.
                </p>
            </div>

            <div class="grid md:grid-cols-2 gap-8">
                <!-- CESAT FUCECCHIO -->
                <div class="card-soft-gradient p-8 md:p-10 rounded-3xl space-y-6">
                    <div class="flex justify-between items-start">
                        <span class="bg-caldo-teal text-white text-[11px] font-semibold uppercase tracking-wider px-3.5 py-1.5 rounded-full">Polo Ospedaliero di Eccellenza</span>
                        <span class="text-xs text-caldo-muted">Fucecchio (FI)</span>
                    </div>
                    <div>
                        <h3 class="text-2xl font-serif text-caldo-text font-semibold">CESAT · Ospedale San Pietro Igneo</h3>
                        <p class="text-xs text-caldo-teal font-medium mt-1">Centro di Eccellenza Sostituzioni Articolari Toscana</p>
                    </div>
                    <div class="space-y-2 text-xs text-caldo-muted border-t border-caldo-borderSoft pt-4 font-light">
                        <p><strong>Indirizzo:</strong> Piazza Lavagnini, 5 · 50054 Fucecchio (FI)</p>
                        <p><strong>Attività:</strong> Interventi chirurgici di protesi spalla/arto superiore, chirurgia artroscopica in regime di ricovero ordinario e day-surgery.</p>
                        <p><strong>Accesso:</strong> Prestazioni chirurgiche in convenzione con il Servizio Sanitario Regionale (SSN).</p>
                    </div>
                    <div class="pt-4 border-t border-caldo-borderSoft flex justify-between items-center">
                        <span class="text-xs text-caldo-muted">Ricoveri Ospedalieri</span>
                        <a href="tel:+393484331733" class="btn-fluid-primary !py-2 !px-4 text-xs font-semibold">Info Ricoveri</a>
                    </div>
                </div>

                <!-- STUDI SAN PIETRO FUCECCHIO -->
                <div class="card-soft-gradient p-8 md:p-10 rounded-3xl space-y-6">
                    <div class="flex justify-between items-start">
                        <span class="bg-caldo-coral text-white text-[11px] font-semibold uppercase tracking-wider px-3.5 py-1.5 rounded-full">Ambulatorio Principale</span>
                        <span class="text-xs text-caldo-muted">Fucecchio (FI)</span>
                    </div>
                    <div>
                        <h3 class="text-2xl font-serif text-caldo-text font-semibold">Studi Medici San Pietro</h3>
                        <p class="text-xs text-caldo-muted mt-1">Prime visite ortopediche in libera professione, ecografie e infiltrazioni</p>
                    </div>
                    <div class="space-y-2 text-xs text-caldo-muted border-t border-caldo-borderSoft pt-4 font-light">
                        <p><strong>Indirizzo:</strong> Piazza Lavagnini, 6 · 50054 Fucecchio (a pochi passi dall'Ospedale)</p>
                        <p><strong>Orari visite:</strong> Lunedì – Giovedì pomeriggio su appuntamento.</p>
                        <p><strong>Servizi:</strong> Ambulatorio diagnostico, infiltrazioni ecoguidate, medicazioni post-operatorie.</p>
                    </div>
                    <div class="pt-4 border-t border-caldo-borderSoft flex justify-between items-center">
                        <span class="text-xs text-caldo-muted">Prenotazione diretta</span>
                        <a href="#contatti" class="nav-trigger btn-fluid-coral !py-2 !px-4 text-xs font-semibold" data-target="contatti">Prenota a Fucecchio</a>
                    </div>
                </div>

                <!-- POLO SAN VERANO PECCIOLI -->
                <div class="card-soft-gradient p-8 md:p-10 rounded-3xl space-y-6">
                    <div class="flex justify-between items-start">
                        <span class="bg-caldo-salvia text-white text-[11px] font-semibold uppercase tracking-wider px-3.5 py-1.5 rounded-full">Presidio Alta Valdera</span>
                        <span class="text-xs text-caldo-muted">Peccioli (PI)</span>
                    </div>
                    <div>
                        <h3 class="text-2xl font-serif text-caldo-text font-semibold">Polo San Verano · Peccioli</h3>
                        <p class="text-xs text-caldo-muted mt-1">Visite specialistiche e screening per i residenti del territorio</p>
                    </div>
                    <div class="space-y-2 text-xs text-caldo-muted border-t border-caldo-borderSoft pt-4 font-light">
                        <p><strong>Indirizzo:</strong> Località San Verano · Peccioli (PI)</p>
                        <p><strong>Accessibilità:</strong> Struttura al piano terra senza barriere architettoniche, ampio parcheggio riservato.</p>
                        <p><strong>Attività:</strong> Valutazione clinica dell'articolazione, ecografia di supporto, impostazione terapia medica e riabilitativa.</p>
                    </div>
                    <div class="pt-4 border-t border-caldo-borderSoft flex justify-between items-center">
                        <span class="text-xs text-caldo-muted">Territorio Valdera</span>
                        <a href="#contatti" class="nav-trigger btn-fluid-primary !py-2 !px-4 text-xs font-semibold" data-target="contatti">Prenota a Peccioli</a>
                    </div>
                </div>

                <!-- PISA & FORNACETTE -->
                <div class="card-soft-gradient p-8 md:p-10 rounded-3xl space-y-6">
                    <div class="flex justify-between items-start">
                        <span class="bg-caldo-gold text-white text-[11px] font-semibold uppercase tracking-wider px-3.5 py-1.5 rounded-full">Medicina dello Sport</span>
                        <span class="text-xs text-caldo-muted">Pisa & Fornacette</span>
                    </div>
                    <div>
                        <h3 class="text-2xl font-serif text-caldo-text font-semibold">Athletica Pisa & Centro Fisiomed</h3>
                        <p class="text-xs text-caldo-muted mt-1">Valutazione sportiva, return-to-play e percorsi fisioterapici</p>
                    </div>
                    <div class="space-y-2 text-xs text-caldo-muted border-t border-caldo-borderSoft pt-4 font-light">
                        <p><strong>Sedi:</strong> Pisa centro e Fornacette (Calcinaia)</p>
                        <p><strong>Focus clinico:</strong> Traumi sportivi (spalla, gomito, polso), atleti professionisti e amatoriali, riabilitazione guidata.</p>
                    </div>
                    <div class="pt-4 border-t border-caldo-borderSoft flex justify-between items-center">
                        <span class="text-xs text-caldo-muted">Sport & Movimento</span>
                        <a href="#contatti" class="nav-trigger btn-fluid-primary !py-2 !px-4 text-xs font-semibold" data-target="contatti">Prenota a Pisa</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- ========================================================
             VISTA 5: NOTE CLINICHE / IL QUADERNO (ARTICOLI ESTESI)
             ======================================================== -->
        <section id="view-articoli" class="page-view max-w-5xl mx-auto px-6 py-16">
            <a href="#home" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal hover:text-caldo-coral mb-8 transition-colors" data-target="home">
                <span>← Torna alla Home</span>
            </a>
            <div class="max-w-3xl mb-16 space-y-4">
                <span class="text-xs font-semibold text-caldo-teal bg-caldo-tealLight px-3.5 py-1.5 rounded-full inline-block">Divulgazione Rigorosa</span>
                <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text leading-tight">Note cliniche.</h1>
                <p class="text-base text-caldo-muted font-light leading-relaxed">
                    Nessun contenuto acchiappa-click o generico: solo considerazioni cliniche tratte direttamente dai paper scientifici e dalla casistica operatoria del CESAT.
                </p>
            </div>

            <div class="space-y-8">
                <!-- Articolo 1 (Remplissage) -->
                <a href="#articoli-remplissage" class="nav-trigger block card-soft-gradient p-8 md:p-12 rounded-3xl group" data-target="articoli-remplissage">
                    <div class="flex items-center gap-3 mb-4">
                        <span class="bg-caldo-coralLight text-caldo-coral text-xs font-semibold px-3 py-1 rounded-full">Paper Osteology 2022</span>
                        <span class="text-xs text-caldo-muted">CESAT Fucecchio · DOI: 10.3390/osteology2040021</span>
                    </div>
                    <h2 class="text-2xl sm:text-3xl font-serif text-caldo-text group-hover:text-caldo-teal transition-colors mb-4 leading-snug">
                        Il dubbio nel remplissage: conciliare stabilità e rotazione nella spalla dello sportivo.
                    </h2>
                    <p class="text-sm text-caldo-muted leading-relaxed mb-6 font-light">
                        Nelle lussazioni recidivanti con difetto osseo della testa omerale (Hill-Sachs), colmare la cavità suturando il tendine infraspinato impedisce nuove fuoriuscite. I risultati a due anni confermano una rotazione preservata e zero recidive.
                    </p>
                    <div class="flex items-center justify-between border-t border-caldo-borderSoft pt-4 text-xs">
                        <span class="font-medium text-caldo-text">Dott. Michele Novi, Dott. M. Nicoletti et al.</span>
                        <span class="font-semibold text-caldo-teal group-hover:translate-x-1 transition-transform inline-flex items-center gap-1">Leggi la nota completa →</span>
                    </div>
                </a>

                <!-- Articolo 2 (Cuffia dei rotatori over 60) -->
                <div class="card-soft-gradient p-8 md:p-10 rounded-3xl opacity-85 space-y-3">
                    <div class="flex items-center gap-3 text-xs text-caldo-muted mb-1">
                        <span class="bg-caldo-tealLight text-caldo-teal font-semibold px-3 py-1 rounded-full">Nota Clinica CESAT</span>
                        <span>Approfondimento Terapeutico</span>
                    </div>
                    <h3 class="text-2xl font-serif text-caldo-text">
                        La cuffia dei rotatori nell'over 60: riparazione biologica o protesi inversa?
                    </h3>
                    <p class="text-sm text-caldo-muted font-light leading-relaxed">
                        Come orientarsi nella scelta tra sutura tendinea e impianto protesico: l'importanza di valutare l'infiltrazione adiposa secondo Goutallier e la retrazione tendinea di Patte, ponendo al centro la richiesta funzionale reale del paziente.
                    </p>
                </div>
            </div>
        </section>

        <!-- ARTICOLO COMPLETO REMPLISSAGE -->
        <section id="view-articoli-remplissage" class="page-view max-w-3xl mx-auto px-6 py-16">
            <a href="#articoli" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal hover:text-caldo-coral mb-8" data-target="articoli">← Torna alle Note cliniche</a>
            <div class="flex items-center gap-3 text-xs text-caldo-muted mb-4">
                <span class="bg-caldo-tealLight text-caldo-teal font-semibold px-3 py-1 rounded-full">Studio Clinico 2022</span>
                <span>Rivista Internazionale Osteology · Autori: M. Novi et al.</span>
            </div>
            <h1 class="text-3xl sm:text-5xl font-serif text-caldo-text leading-tight mb-8">
                Il dubbio nel remplissage: quando la stabilità rischia di sacrificare il movimento.
            </h1>
            <div class="space-y-6 text-base text-caldo-muted leading-relaxed font-light">
                <p class="text-lg text-caldo-text font-normal italic border-l-4 border-caldo-teal pl-4 bg-caldo-tealLight/40 py-3 rounded-r-2xl">
                    «Il timore del chirurgo che affronta la lussazione di spalla è duplice: riparare troppo poco e rischiare una recidiva, o bloccare troppo rigidamente e ridurre la rotazione esterna del braccio nell'atleta.»
                </p>
                <p>
                    Nelle lussazioni recidivanti anteriori, l'impatto ripetuto della testa omerale contro il ciglio anteriore della glenoide produce una tipica lesione ossea da compressione, nota storicamente come <strong>lesione di Hill-Sachs</strong>. Quando il paziente porta il braccio in abduzione ed extrarotazione — il classico gesto del lancio o del contatto nello sport — questa nicchia rischia di incastrarsi sul bordo osseo opposto, agendo come una leva rigida che scardina l'articolazione.
                </p>
                <h3 class="text-2xl font-serif text-caldo-text font-semibold pt-4">La procedura: colmare per pacificare</h3>
                <p>
                    Il <em>Remplissage</em> (dal termine francese "riempimento") risolve il problema alla radice: attraverso l'artroscopia, suturiamo la porzione posteriore della capsula articolare e il tendine dell'infraspinato direttamente all'interno della cavità di Hill-Sachs. Il difetto osseo viene così "spostato" all'esterno dell'articolazione: la testa dell'omero ritrova una superficie liscia e scivola senza più trovare alcuno scalino di inceppamento.
                </p>
                <h3 class="text-2xl font-serif text-caldo-text font-semibold pt-4">I risultati del nostro studio</h3>
                <p>
                    Nello studio condotto su una coorte di atleti seguiti presso l'Ospedale CESAT di Fucecchio con follow-up a due anni, abbiamo misurato con goniometro ottico il range di movimento post-operatorio. I risultati evidenziano una perdita media di rotazione esterna inferiore a 4 gradi (totalmente impercettibile nella pratica sportiva), a fronte di un tasso di re-lussazione completamente azzerato. La congruenza delle superfici era stata ripristinata.
                </p>
            </div>
            <div class="mt-12 p-6 bg-white rounded-3xl border border-caldo-borderSoft flex justify-between items-center shadow-sm">
                <span class="text-xs text-caldo-muted font-medium">Vuoi una valutazione sulla stabilità della tua spalla?</span>
                <a href="#contatti" class="nav-trigger btn-fluid-coral px-6 py-2.5 text-xs font-semibold" data-target="contatti">Contatta la segreteria</a>
            </div>
        </section>

        <!-- ========================================================
             VISTA 6: CONTATTI E PRENOTAZIONI (COMPLETO)
             ======================================================== -->
        <!-- ========================================== -->
        <!-- 13. VISTA CONTATTI E PRENOTAZIONI RICCA ED ESAUSTIVA -->
        <!-- ========================================== -->
        <section id="view-contatti" class="page-view max-w-6xl mx-auto px-6 py-16">
            <a href="#home" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal hover:text-caldo-coral mb-8 transition-colors" data-target="home">
                <span>← Torna alla Home</span>
            </a>
            
            <!-- HEADER PRINCIPALE -->
            <div class="max-w-3xl mb-14 space-y-4">
                <div class="inline-flex items-center gap-2 text-xs font-semibold text-caldo-coral bg-caldo-coralLight px-3.5 py-1.5 rounded-full">
                    <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                    <span>Canale Ufficiale & Segreteria Clinica</span>
                </div>
                <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text leading-tight">Prenotazioni, Sedi e Contatti.</h1>
                <p class="text-base text-caldo-muted font-light leading-relaxed">
                    Tutti i riferimenti ufficiali per concordare la tua prima visita specialistica, programmare un controllo post-operatorio o ricevere chiarimenti sul percorso diagnostico e chirurgico.
                </p>
            </div>

            <!-- BLOCCO 1: SEGRETERIA DIRETTA E FORM PRENOTAZIONE -->
            <div class="grid lg:grid-cols-12 gap-10 items-start mb-20">
                
                <!-- COLONNA SINISTRA: RECAPITI E LINEE GUIDA -->
                <div class="lg:col-span-5 space-y-6">
                    
                    <!-- BOX SEGRETERIA DEDICATA -->
                    <div class="card-soft-gradient p-8 rounded-3xl space-y-6 relative overflow-hidden">
                        <div class="flex items-center justify-between">
                            <span class="text-xs text-caldo-muted font-medium uppercase tracking-wider">Recapito Telefonico Unico</span>
                            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-semibold bg-emerald-50 text-emerald-700 border border-emerald-200/60">
                                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
                                Segreteria Attiva
                            </span>
                        </div>
                        
                        <div class="space-y-1">
                            <a href="tel:+393484331733" class="text-3xl sm:text-4xl font-serif text-caldo-teal font-normal hover:text-caldo-coral transition-colors block">
                                348 4331733
                            </a>
                            <span class="text-[11px] text-caldo-muted font-light block">Chiamata diretta con la segreteria del Dott. Novi</span>
                        </div>

                        <div class="space-y-2.5 text-xs text-caldo-muted border-t border-caldo-borderSoft pt-5 font-light">
                            <div class="flex items-start gap-2.5">
                                <svg class="w-4 h-4 text-caldo-teal shrink-0 mt-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                                <div>
                                    <strong class="text-caldo-text font-medium block">Orari Chiamate Telefoniche:</strong>
                                    Lunedì – Giovedì dalle 15:30 alle 17:30
                                </div>
                            </div>
                            <div class="flex items-start gap-2.5">
                                <svg class="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
                                <div>
                                    <strong class="text-caldo-text font-medium block">WhatsApp Assistenza:</strong>
                                    Attivo per messaggi di richiesta disponibilità
                                </div>
                            </div>
                            <div class="flex items-start gap-2.5">
                                <svg class="w-4 h-4 text-caldo-coral shrink-0 mt-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                                <div>
                                    <strong class="text-caldo-text font-medium block">Email Informazioni:</strong>
                                    segreteria@michelenovi.it
                                </div>
                            </div>
                        </div>

                        <div class="space-y-3 pt-2">
                            <a href="https://wa.me/393484331733?text=Buongiorno%2C%20vorrei%20richiedere%20informazioni%20per%20una%20visita%20con%20il%20Dott.%20Novi" 
                               target="_blank" 
                               class="w-full inline-flex items-center justify-center gap-2.5 py-3.5 px-4 rounded-2xl bg-[#25D366] text-white font-semibold text-xs shadow-sm hover:opacity-90 transition-all">
                                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
                                <span>Scrivi alla Segreteria su WhatsApp</span>
                            </a>

                            <div class="text-center">
                                <span class="text-[11px] text-caldo-muted font-light italic">Oppure prenota online in autonomia:</span>
                            </div>

                            <a href="https://www.doctolib.it" 
                               target="_blank" 
                               class="w-full inline-flex items-center justify-center gap-2 py-3 px-4 rounded-2xl bg-[#00264D] text-white font-semibold text-xs shadow-sm hover:bg-[#003870] transition-colors">
                                <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9v-2h2v2zm0-4H9V7h2v5zm4 4h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>
                                <span>Prenota su Doctolib (Studi San Pietro)</span>
                            </a>
                        </div>
                    </div>

                    <!-- REGOLE DI TRASPARENZA ED ETICA CLINICA -->
                    <div class="bg-white/90 p-6 rounded-3xl border border-caldo-borderSoft text-xs text-caldo-muted space-y-3 font-light">
                        <div class="flex items-center gap-2 text-caldo-teal font-semibold text-sm">
                            <svg class="w-4 h-4 text-caldo-teal" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
                            <span>Indicazioni per la prenotazione:</span>
                        </div>
                        <ul class="space-y-2 pl-1">
                            <li class="flex items-start gap-2">
                                <span class="text-caldo-coral font-bold">•</span>
                                <span><strong>Specifica la sede desiderata:</strong> Fucecchio, Peccioli, Fornacette o Pisa per trovare lo slot più vicino a te.</span>
                            </li>
                            <li class="flex items-start gap-2">
                                <span class="text-caldo-coral font-bold">•</span>
                                <span><strong>Sintetizza il motivo:</strong> ad esempio «dolore notturno alla spalla destra da due mesi» o «sospetta lesione meniscale / tendinea».</span>
                            </li>
                            <li class="flex items-start gap-2">
                                <span class="text-caldo-coral font-bold">•</span>
                                <span><strong>Segnala esami già eseguiti:</strong> se possiedi già RMN, RX o TAC recenti da visionare durante la visita.</span>
                            </li>
                        </ul>
                        <div class="pt-2 border-t border-caldo-borderSoft/60 text-[11px] text-caldo-coral font-medium flex items-center gap-1.5">
                            <svg class="w-3.5 h-3.5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
                            <span>Non allegare file radiologici pesanti via messaggio prima della visita in studio.</span>
                        </div>
                    </div>
                </div>

                <!-- COLONNA DESTRA: MODULO DI CONTATTO ONLINE -->
                <div class="lg:col-span-7 card-soft-gradient p-8 md:p-12 rounded-3xl">
                    <div class="mb-8">
                        <span class="text-[11px] font-semibold uppercase tracking-wider text-caldo-teal block mb-1">Richiesta Diretta</span>
                        <h3 class="text-2xl sm:text-3xl font-serif text-caldo-text font-semibold">Modulo di Richiesta Appuntamento</h3>
                        <p class="text-xs text-caldo-muted mt-2 font-light leading-relaxed">
                            Compila il modulo sottostante per essere ricontattato telefonicamente dalla segreteria entro 24 ore lavorative e concordare l'appuntamento nella sede a te più comoda.
                        </p>
                    </div>

                    <form onsubmit="event.preventDefault(); alert('Grazie! La richiesta è stata trasmessa alla segreteria del Dott. Novi. Verrai ricontattato telefonicamente entro 24 ore lavorative.');" class="space-y-6">
                        <div class="grid sm:grid-cols-2 gap-6">
                            <div>
                                <label class="block text-xs font-semibold text-caldo-text mb-2">Nome e Cognome *</label>
                                <input type="text" required class="w-full border border-caldo-border p-3.5 text-sm rounded-2xl bg-white focus:outline-none focus:border-caldo-teal transition-colors" placeholder="Es. Marco Bianchi">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-caldo-text mb-2">Recapito Telefonico *</label>
                                <input type="tel" required class="w-full border border-caldo-border p-3.5 text-sm rounded-2xl bg-white focus:outline-none focus:border-caldo-teal transition-colors" placeholder="Es. 340 1234567">
                            </div>
                        </div>

                        <div class="grid sm:grid-cols-2 gap-6">
                            <div>
                                <label class="block text-xs font-semibold text-caldo-text mb-2">Indirizzo Email (per conferma)</label>
                                <input type="email" class="w-full border border-caldo-border p-3.5 text-sm rounded-2xl bg-white focus:outline-none focus:border-caldo-teal transition-colors" placeholder="m.bianchi@email.it">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-caldo-text mb-2">Sede Desiderata *</label>
                                <select required class="w-full border border-caldo-border p-3.5 text-sm rounded-2xl bg-white focus:outline-none focus:border-caldo-teal transition-colors">
                                    <option value="fucecchio">Fucecchio — Studi Medici San Pietro (Piazza Lavagnini 6)</option>
                                    <option value="peccioli">Peccioli — Polo San Verano (Alta Valdera, piano terra)</option>
                                    <option value="fornacette">Fornacette — Centro Fisiomed (Tosco Romagnola)</option>
                                    <option value="pisa">Pisa — Athletica Pisa (Medicina dello Sport)</option>
                                </select>
                            </div>
                        </div>

                        <div class="grid sm:grid-cols-2 gap-6">
                            <div>
                                <label class="block text-xs font-semibold text-caldo-text mb-2">Articolazione / Motivo Visita</label>
                                <select class="w-full border border-caldo-border p-3.5 text-sm rounded-2xl bg-white focus:outline-none focus:border-caldo-teal transition-colors">
                                    <option>Spalla (dolore, cuffia, instabilità o lussazioni)</option>
                                    <option>Gomito (epicondilite, rigidità, tendinopatia)</option>
                                    <option>Mano e Polso (tunnel carpale, dito a scatto, rizoartrosi)</option>
                                    <option>Traumatologia dello Sport e Riatletizzazione</option>
                                    <option>Valutazione per Infiltrazione Eco-guidata</option>
                                    <option>Controllo Post-Operatorio o Revisione</option>
                                </select>
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-caldo-text mb-2">Preferenza di Giorno o Fascia</label>
                                <input type="text" class="w-full border border-caldo-border p-3.5 text-sm rounded-2xl bg-white focus:outline-none focus:border-caldo-teal transition-colors" placeholder="Es. Preferibilmente martedì o pomeriggio">
                            </div>
                        </div>

                        <div>
                            <label class="block text-xs font-semibold text-caldo-text mb-2">Brevi Note Aggiuntive per la Segreteria (Facoltativo)</label>
                            <textarea rows="3" class="w-full border border-caldo-border p-3.5 text-sm rounded-2xl bg-white focus:outline-none focus:border-caldo-teal transition-colors" placeholder="Indica ad esempio se hai già eseguito una RMN o RX, o se si tratta di una seconda opinione chirurgica..."></textarea>
                        </div>

                        <div class="flex items-start gap-3 bg-white/70 p-4 rounded-2xl border border-caldo-borderSoft">
                            <input type="checkbox" required id="privacy-box-contatti" class="mt-1 accent-caldo-teal shrink-0">
                            <label for="privacy-box-contatti" class="text-xs text-caldo-muted font-light leading-relaxed">
                                Dichiaro di aver preso visione dell'<strong class="text-caldo-teal font-medium">informativa sul trattamento dei dati personali</strong> ai sensi del Regolamento Europeo GDPR 679/2016 e acconsento a essere ricontattato telefonicamente o via email esclusivamente per finalità legate alla gestione della richiesta di appuntamento.
                            </label>
                        </div>

                        <button type="submit" class="btn-fluid-coral w-full justify-center !py-4 text-sm font-semibold shadow-md">
                            <span>Trasmetti Richiesta di Prenotazione</span>
                            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                        </button>
                    </form>
                </div>
            </div>

            <!-- BLOCCO 2: LE 4 SEDI AMBULATORIALI CON SCHEDE DETTAGLIATE -->
            <div class="mb-20">
                <div class="flex flex-col md:flex-row md:items-end justify-between mb-10 gap-4">
                    <div>
                        <span class="text-xs font-semibold text-caldo-coral uppercase tracking-wider block mb-1">Rete sul Territorio</span>
                        <h2 class="text-3xl sm:text-4xl font-serif text-caldo-text">Le 4 Sedi di Ricevimento Ambulatoriale</h2>
                    </div>
                    <a href="#sedi" class="nav-trigger inline-flex items-center gap-1.5 text-xs font-semibold text-caldo-teal hover:text-caldo-coral transition-colors" data-target="sedi">
                        <span>Visualizza guida completa e mappe dettagliate</span>
                        <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                    </a>
                </div>

                <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
                    <!-- SEDE 1: FUCECCHIO STUDI SAN PIETRO -->
                    <div class="card-soft-gradient p-6 rounded-3xl flex flex-col justify-between space-y-4 hover:border-caldo-teal/40 transition-all">
                        <div class="space-y-3">
                            <div class="flex items-center justify-between">
                                <span class="text-[10px] font-bold uppercase tracking-wider text-caldo-teal bg-caldo-tealLight px-2.5 py-1 rounded-full">Sede Principale</span>
                                <svg class="w-4 h-4 text-caldo-teal" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                            </div>
                            <h3 class="font-serif text-xl text-caldo-text font-semibold">Fucecchio</h3>
                            <p class="text-xs text-caldo-muted font-light">
                                <strong>Studi Medici San Pietro</strong><br>
                                Piazza Lavagnini 6, Fucecchio (FI)<br>
                                <span class="text-[11px] text-caldo-coral italic">A fianco dell'ospedale (civico 6 vs civico 5)</span>
                            </p>
                            <div class="text-[11px] text-caldo-muted space-y-1 pt-2 border-t border-caldo-borderSoft font-light">
                                <div class="flex items-center gap-1.5"><span>✓</span> <span>Visite e controlli specialistici</span></div>
                                <div class="flex items-center gap-1.5"><span>✓</span> <span>Ecografia muscoloscheletrica HD</span></div>
                                <div class="flex items-center gap-1.5"><span>✓</span> <span>Infiltrazioni eco-guidate con HA</span></div>
                            </div>
                        </div>
                        <a href="#sedi" class="nav-trigger inline-flex items-center gap-1.5 text-xs font-semibold text-caldo-teal hover:text-caldo-coral pt-3" data-target="sedi">
                            <span>Info e accesso Fucecchio →</span>
                        </a>
                    </div>

                    <!-- SEDE 2: PECCIOLI POLO SAN VERANO -->
                    <div class="card-soft-gradient p-6 rounded-3xl flex flex-col justify-between space-y-4 hover:border-caldo-teal/40 transition-all">
                        <div class="space-y-3">
                            <div class="flex items-center justify-between">
                                <span class="text-[10px] font-bold uppercase tracking-wider text-caldo-coral bg-caldo-coralLight px-2.5 py-1 rounded-full">Alta Valdera</span>
                                <svg class="w-4 h-4 text-caldo-coral" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                            </div>
                            <h3 class="font-serif text-xl text-caldo-text font-semibold">Peccioli</h3>
                            <p class="text-xs text-caldo-muted font-light">
                                <strong>Polo San Verano</strong><br>
                                Località San Verano, Peccioli (PI)<br>
                                <span class="text-[11px] text-emerald-700 font-medium">Piano terra · Parcheggio gratuito</span>
                            </p>
                            <div class="text-[11px] text-caldo-muted space-y-1 pt-2 border-t border-caldo-borderSoft font-light">
                                <div class="flex items-center gap-1.5"><span>✓</span> <span>Zero barriere architettoniche</span></div>
                                <div class="flex items-center gap-1.5"><span>✓</span> <span>Diagnostica ecografica dinamica</span></div>
                                <div class="flex items-center gap-1.5"><span>✓</span> <span>Ideale per mobilità ridotta</span></div>
                            </div>
                        </div>
                        <a href="#sedi" class="nav-trigger inline-flex items-center gap-1.5 text-xs font-semibold text-caldo-teal hover:text-caldo-coral pt-3" data-target="sedi">
                            <span>Info e accesso Peccioli →</span>
                        </a>
                    </div>

                    <!-- SEDE 3: FORNACETTE FISIOMED -->
                    <div class="card-soft-gradient p-6 rounded-3xl flex flex-col justify-between space-y-4 hover:border-caldo-teal/40 transition-all">
                        <div class="space-y-3">
                            <div class="flex items-center justify-between">
                                <span class="text-[10px] font-bold uppercase tracking-wider text-caldo-teal bg-caldo-tealLight px-2.5 py-1 rounded-full">Riabilitazione</span>
                                <svg class="w-4 h-4 text-caldo-teal" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                            </div>
                            <h3 class="font-serif text-xl text-caldo-text font-semibold">Fornacette</h3>
                            <p class="text-xs text-caldo-muted font-light">
                                <strong>Centro Fisiomed</strong><br>
                                Via Tosco Romagnola 201, Calcinaia (PI)<br>
                                <span class="text-[11px] text-caldo-muted">Presidio integrato con palestra medica</span>
                            </p>
                            <div class="text-[11px] text-caldo-muted space-y-1 pt-2 border-t border-caldo-borderSoft font-light">
                                <div class="flex items-center gap-1.5"><span>✓</span> <span>Sinergia chirurgo-fisioterapista</span></div>
                                <div class="flex items-center gap-1.5"><span>✓</span> <span>Protocolli post-operatori</span></div>
                                <div class="flex items-center gap-1.5"><span>✓</span> <span>Valutazioni kinesiterapiche</span></div>
                            </div>
                        </div>
                        <a href="#sedi" class="nav-trigger inline-flex items-center gap-1.5 text-xs font-semibold text-caldo-teal hover:text-caldo-coral pt-3" data-target="sedi">
                            <span>Info e accesso Fornacette →</span>
                        </a>
                    </div>

                    <!-- SEDE 4: PISA ATHLETICA -->
                    <div class="card-soft-gradient p-6 rounded-3xl flex flex-col justify-between space-y-4 hover:border-caldo-teal/40 transition-all">
                        <div class="space-y-3">
                            <div class="flex items-center justify-between">
                                <span class="text-[10px] font-bold uppercase tracking-wider text-caldo-coral bg-caldo-coralLight px-2.5 py-1 rounded-full">Sport & Atleti</span>
                                <svg class="w-4 h-4 text-caldo-coral" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                            </div>
                            <h3 class="font-serif text-xl text-caldo-text font-semibold">Pisa</h3>
                            <p class="text-xs text-caldo-muted font-light">
                                <strong>Athletica Pisa</strong><br>
                                Via G. Carducci 62, Ghezzano / Pisa<br>
                                <span class="text-[11px] text-caldo-muted">Medicina dello Sport e Performance</span>
                            </p>
                            <div class="text-[11px] text-caldo-muted space-y-1 pt-2 border-t border-caldo-borderSoft font-light">
                                <div class="flex items-center gap-1.5"><span>✓</span> <span>Traumi acuti overhead e contatto</span></div>
                                <div class="flex items-center gap-1.5"><span>✓</span> <span>Test di Return-to-Play</span></div>
                                <div class="flex items-center gap-1.5"><span>✓</span> <span>Inquadramento atleti agonisti</span></div>
                            </div>
                        </div>
                        <a href="#sedi" class="nav-trigger inline-flex items-center gap-1.5 text-xs font-semibold text-caldo-teal hover:text-caldo-coral pt-3" data-target="sedi">
                            <span>Info e accesso Pisa →</span>
                        </a>
                    </div>
                </div>
            </div>

            <!-- BLOCCO 3: TRASPARENZA TARIFFE E PRESTAZIONI CLINICHE (D10) -->
            <div class="mb-20 bg-white/80 backdrop-blur-sm border border-caldo-borderSoft p-8 md:p-12 rounded-3xl shadow-sm">
                <div class="max-w-3xl mb-10 space-y-2">
                    <span class="text-xs font-semibold text-caldo-teal uppercase tracking-wider block">Politica di Trasparenza Tariffaria (D10)</span>
                    <h2 class="text-3xl font-serif text-caldo-text">Tariffe Indicative delle Prestazioni Private</h2>
                    <p class="text-xs text-caldo-muted font-light leading-relaxed">
                        Massima chiarezza economica per le prestazioni specialistiche in regime libero-professionale. Gli interventi chirurgici e i ricoveri ospedalieri sono eseguiti in convenzione con il Servizio Sanitario Nazionale.
                    </p>
                </div>

                <div class="grid md:grid-cols-3 gap-6 mb-8">
                    <!-- TARIFFA 1: PRIMA VISITA -->
                    <div class="bg-white p-6 rounded-2xl border border-caldo-borderSoft shadow-sm space-y-4">
                        <div class="flex justify-between items-baseline">
                            <span class="text-xs font-semibold text-caldo-teal uppercase tracking-wider">Prima Visita</span>
                            <span class="text-2xl font-serif font-bold text-caldo-text">~ € 120</span>
                        </div>
                        <h4 class="font-serif text-lg text-caldo-text font-semibold">Visita Ortopedica Specialistica</h4>
                        <ul class="text-xs text-caldo-muted space-y-2 font-light">
                            <li class="flex items-start gap-2"><span class="text-caldo-coral font-bold">•</span><span>Anamnesi completa e colloquio clinico approfondito</span></li>
                            <li class="flex items-start gap-2"><span class="text-caldo-coral font-bold">•</span><span>Esame obiettivo con test articolari, forza e mobilità</span></li>
                            <li class="flex items-start gap-2"><span class="text-caldo-coral font-bold">•</span><span>Visione diretta e discussione degli esami radiografici (RX, RMN)</span></li>
                            <li class="flex items-start gap-2"><span class="text-caldo-coral font-bold">•</span><span>Definizione strategia (conservativa, fisioterapia o chirurgica)</span></li>
                        </ul>
                    </div>

                    <!-- TARIFFA 2: CONTROLLO -->
                    <div class="bg-white p-6 rounded-2xl border border-caldo-borderSoft shadow-sm space-y-4">
                        <div class="flex justify-between items-baseline">
                            <span class="text-xs font-semibold text-caldo-coral uppercase tracking-wider">Controllo</span>
                            <span class="text-2xl font-serif font-bold text-caldo-text">~ € 80 – 90</span>
                        </div>
                        <h4 class="font-serif text-lg text-caldo-text font-semibold">Visita di Controllo / Post-Op</h4>
                        <ul class="text-xs text-caldo-muted space-y-2 font-light">
                            <li class="flex items-start gap-2"><span class="text-caldo-teal font-bold">•</span><span>Verifica decorso clinico e monitoraggio del recupero</span></li>
                            <li class="flex items-start gap-2"><span class="text-caldo-teal font-bold">•</span><span>Ispezione cicatrici e mobilità nei post-operatori</span></li>
                            <li class="flex items-start gap-2"><span class="text-caldo-teal font-bold">•</span><span>Rimodulazione carichi ed esercizi con fisioterapisti</span></li>
                            <li class="flex items-start gap-2"><span class="text-caldo-teal font-bold">•</span><span>Rivalutazione esami di controllo o prescrizioni terapeutiche</span></li>
                        </ul>
                    </div>

                    <!-- TARIFFA 3: INFILTRAZIONE ECOGUIDATA -->
                    <div class="bg-white p-6 rounded-2xl border border-caldo-borderSoft shadow-sm space-y-4">
                        <div class="flex justify-between items-baseline">
                            <span class="text-xs font-semibold text-emerald-700 uppercase tracking-wider">Procedura</span>
                            <span class="text-2xl font-serif font-bold text-caldo-text">~ € 80 – 150</span>
                        </div>
                        <h4 class="font-serif text-lg text-caldo-text font-semibold">Infiltrazione con Guida Ecografica</h4>
                        <ul class="text-xs text-caldo-muted space-y-2 font-light">
                            <li class="flex items-start gap-2"><span class="text-emerald-600 font-bold">•</span><span>Inquadramento ecografico in tempo reale con sonda ad alta frequenza</span></li>
                            <li class="flex items-start gap-2"><span class="text-emerald-600 font-bold">•</span><span>Centratura millimetrica dell'ago nello spazio intra-articolare</span></li>
                            <li class="flex items-start gap-2"><span class="text-emerald-600 font-bold">•</span><span>Iniezione di acido ialuronico a differente peso molecolare</span></li>
                            <li class="flex items-start gap-2"><span class="text-emerald-600 font-bold">•</span><span>Tariffa variabile in base al tipo di farmaco o dispositivo impiegato</span></li>
                        </ul>
                    </div>
                </div>

                <div class="grid md:grid-cols-2 gap-6 pt-6 border-t border-caldo-borderSoft text-xs text-caldo-muted font-light">
                    <div class="space-y-1.5">
                        <strong class="text-caldo-teal font-semibold block text-sm">🏥 Interventi Chirurgici e Ricoveri Ospedalieri (CESAT Fucecchio):</strong>
                        <p>Tutti gli interventi maggiori (riparazioni artroscopiche di cuffia e cercine, protesi anatomiche e inverse, ricostruzioni tendinee) vengono svolti dal Dott. Novi in regime di convenzione con il <strong>Servizio Sanitario Nazionale (SSN)</strong> presso l'Ospedale San Pietro Igneo di Fucecchio, senza costi di degenza per il paziente.</p>
                    </div>
                    <div class="space-y-1.5">
                        <strong class="text-caldo-teal font-semibold block text-sm">💳 Modalità di Pagamento e Detraibilità Sanitaria:</strong>
                        <p>Le prestazioni ambulatoriali private possono essere saldate con POS (carte di debito, bancomat, carte di credito), bonifico bancario o contanti. Essendo spese mediche specialistiche, sono <strong>detraibili al 19%</strong> nella dichiarazione dei redditi tramite trasmissione automatica al Sistema Tessera Sanitaria.</p>
                    </div>
                </div>
            </div>

            <!-- BLOCCO 4: GUIDA PRATICA: COSA PORTARE E COME PREPARARSI ALLA VISITA -->
            <div class="mb-20">
                <div class="max-w-3xl mb-10 space-y-2">
                    <span class="text-xs font-semibold text-caldo-coral uppercase tracking-wider block">Guida al Paziente</span>
                    <h2 class="text-3xl sm:text-4xl font-serif text-caldo-text">Come Prepararsi alla Prima Visita</h2>
                    <p class="text-xs text-caldo-muted font-light leading-relaxed">
                        Tre passaggi fondamentali per ottimizzare il tempo della consultazione specialistica e consentire un inquadramento diagnostico immediato e preciso.
                    </p>
                </div>

                <div class="grid md:grid-cols-3 gap-6">
                    <div class="card-soft-gradient p-8 rounded-3xl space-y-4">
                        <div class="w-10 h-10 rounded-2xl bg-caldo-teal text-white flex items-center justify-center font-serif text-lg font-semibold">
                            01
                        </div>
                        <h4 class="font-serif text-xl text-caldo-text font-semibold">Supporti Radiografici (CD/DVD)</h4>
                        <p class="text-xs text-caldo-muted font-light leading-relaxed">
                            Porta con te non solo il referto cartaceo ma soprattutto il <strong>dischetto originale (CD/DVD o chiavetta USB)</strong> di RMN, RX o TAC recenti. Il chirurgo esamina personalmente le immagini native ad alta risoluzione per valutare il trofismo muscolare, le lesioni tendinee e lo stato osseo.
                        </p>
                    </div>

                    <div class="card-soft-gradient p-8 rounded-3xl space-y-4">
                        <div class="w-10 h-10 rounded-2xl bg-caldo-coral text-white flex items-center justify-center font-serif text-lg font-semibold">
                            02
                        </div>
                        <h4 class="font-serif text-xl text-caldo-text font-semibold">Documentazione & Terapie</h4>
                        <p class="text-xs text-caldo-muted font-light leading-relaxed">
                            Raccogli lettere di dimissione di interventi ortopedici precedenti, relazioni di visite fisiatriche o cartelle cliniche pregresse. È utile avere con sé l'elenco esatto dei <strong>farmaci assunti quotidianamente</strong> (anticoagulanti, antinfiammatori o terapie croniche).
                        </p>
                    </div>

                    <div class="card-soft-gradient p-8 rounded-3xl space-y-4">
                        <div class="w-10 h-10 rounded-2xl bg-caldo-tealLight text-caldo-teal flex items-center justify-center font-serif text-lg font-semibold border border-caldo-borderSoft">
                            03
                        </div>
                        <h4 class="font-serif text-xl text-caldo-text font-semibold">Abbigliamento Pratico</h4>
                        <p class="text-xs text-caldo-muted font-light leading-relaxed">
                            Indossa un abbigliamento comodo che consenta di scoprire agevolmente la spalla, il braccio o la mano (es. canottiera, maglietta a maniche corte o polo comoda). L'esame obiettivo prevede test di movimento a confronto con l'arto sano e l'eventuale ecografia dinamica in studio.
                        </p>
                    </div>
                </div>
            </div>

            <!-- BLOCCO 5: FAQ COMPLETE SU PRENOTAZIONI, VISITE E INTERVENTI -->
            <div class="mb-16">
                <div class="max-w-3xl mb-10 space-y-2">
                    <span class="text-xs font-semibold text-caldo-teal uppercase tracking-wider block">Domande Frequenti</span>
                    <h2 class="text-3xl sm:text-4xl font-serif text-caldo-text">Tutto Quello che C'è da Sapere</h2>
                    <p class="text-xs text-caldo-muted font-light leading-relaxed">
                        Risposte chiare e immediate ai quesiti più frequenti dei pazienti prima di concordare l'appuntamento.
                    </p>
                </div>

                <div class="space-y-4">
                    <!-- FAQ 1 -->
                    <details class="group bg-white rounded-2xl border border-caldo-borderSoft p-6 transition-all duration-300 open:shadow-sm open:border-caldo-teal/40">
                        <summary class="flex justify-between items-center cursor-pointer font-medium text-caldo-text list-none">
                            <span class="text-sm font-semibold text-caldo-text">È necessaria la ricetta medica (impegnativa del medico curante)?</span>
                            <span class="transition-transform duration-300 group-open:rotate-180 text-caldo-teal">
                                <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M6 9l6 6 6-6"/></svg>
                            </span>
                        </summary>
                        <div class="mt-4 text-xs text-caldo-muted font-light leading-relaxed border-t border-caldo-borderSoft/60 pt-4">
                            <strong>No.</strong> Per effettuare una prima visita specialistica ortopedica o un controllo in regime di libera professione presso gli Studi Medici San Pietro, Peccioli, Fornacette o Pisa non serve alcuna ricetta medica. L'impegnativa del medico di medicina generale sarà invece necessaria qualora si pianifichi un ricovero chirurgico programmato o un esame strumentale convenzionato SSN.
                        </div>
                    </details>

                    <!-- FAQ 2 -->
                    <details class="group bg-white rounded-2xl border border-caldo-borderSoft p-6 transition-all duration-300 open:shadow-sm open:border-caldo-teal/40">
                        <summary class="flex justify-between items-center cursor-pointer font-medium text-caldo-text list-none">
                            <span class="text-sm font-semibold text-caldo-text">Se dalla visita emerge indicazione a un intervento, come vengo inserito in lista?</span>
                            <span class="transition-transform duration-300 group-open:rotate-180 text-caldo-teal">
                                <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M6 9l6 6 6-6"/></svg>
                            </span>
                        </summary>
                        <div class="mt-4 text-xs text-caldo-muted font-light leading-relaxed border-t border-caldo-borderSoft/60 pt-4">
                            Se nel corso della visita viene concordata l'opportunità di procedere con un intervento (ad esempio sutura della cuffia dei rotatori, stabilizzazione di spalla o impianto protesico), il Dott. Novi compila direttamente la scheda di ricovero per il <strong>CESAT Ospedale San Pietro Igneo di Fucecchio</strong> in regime di convenzione con il Sistema Sanitario Nazionale (SSN). Il paziente viene inserito nel registro ufficiale e successivamente contattato dal servizio di pre-ospedalizzazione per eseguire esami ematochimici, ECG e visita anestesiologica.
                        </div>
                    </details>

                    <!-- FAQ 3 -->
                    <details class="group bg-white rounded-2xl border border-caldo-borderSoft p-6 transition-all duration-300 open:shadow-sm open:border-caldo-teal/40">
                        <summary class="flex justify-between items-center cursor-pointer font-medium text-caldo-text list-none">
                            <span class="text-sm font-semibold text-caldo-text">È possibile richiedere una Second Opinion su un intervento già proposto?</span>
                            <span class="transition-transform duration-300 group-open:rotate-180 text-caldo-teal">
                                <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M6 9l6 6 6-6"/></svg>
                            </span>
                        </summary>
                        <div class="mt-4 text-xs text-caldo-muted font-light leading-relaxed border-t border-caldo-borderSoft/60 pt-4">
                            <strong>Certamente.</strong> La richiesta di un secondo parere è una prassi frequente e assolutamente legittima, soprattutto quando si devono valutare opzioni complesse tra trattamento conservativo/riabilitativo e chirurgia aperta o artroscopica. È indispensabile portare tutta la documentazione pregressa e i dischetti radiologici per una revisione obiettiva e trasparente del caso.
                        </div>
                    </details>

                    <!-- FAQ 4 -->
                    <details class="group bg-white rounded-2xl border border-caldo-borderSoft p-6 transition-all duration-300 open:shadow-sm open:border-caldo-teal/40">
                        <summary class="flex justify-between items-center cursor-pointer font-medium text-caldo-text list-none">
                            <span class="text-sm font-semibold text-caldo-text">L'ecografia e le infiltrazioni possono essere eseguite contestualmente alla visita?</span>
                            <span class="transition-transform duration-300 group-open:rotate-180 text-caldo-teal">
                                <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M6 9l6 6 6-6"/></svg>
                            </span>
                        </summary>
                        <div class="mt-4 text-xs text-caldo-muted font-light leading-relaxed border-t border-caldo-borderSoft/60 pt-4">
                            <strong>Sì.</strong> Grazie al Diploma Nazionale SIUMB, il Dott. Novi dispone di ecografo in studio per integrare l'esame obiettivo in presa diretta. Qualora si riscontri un'indicazione appropriata (ad es. borsite subacromiale acuta, sinovite o artrosi che beneficiano di viscosuppletivazione con acido ialuronico), l'infiltrazione ecoguidata può essere effettuata durante la stessa seduta previa discussione con il paziente.
                        </div>
                    </details>

                    <!-- FAQ 5 -->
                    <details class="group bg-white rounded-2xl border border-caldo-borderSoft p-6 transition-all duration-300 open:shadow-sm open:border-caldo-teal/40">
                        <summary class="flex justify-between items-center cursor-pointer font-medium text-caldo-text list-none">
                            <span class="text-sm font-semibold text-caldo-text">Come posso disdire o modificare un appuntamento fissato?</span>
                            <span class="transition-transform duration-300 group-open:rotate-180 text-caldo-teal">
                                <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M6 9l6 6 6-6"/></svg>
                            </span>
                        </summary>
                        <div class="mt-4 text-xs text-caldo-muted font-light leading-relaxed border-t border-caldo-borderSoft/60 pt-4">
                            In caso di imprevisto o necessità di rinvio, chiediamo la cortesia di avvisare la segreteria con almeno <strong>24-48 ore di anticipo</strong> tramite messaggio WhatsApp o telefonata al <strong>348 4331733</strong>. Questo consente di riassegnare tempestivamente lo slot a un altro paziente con dolore articolare acuto o necessità urgente di controllo.
                        </div>
                    </details>
                </div>
            </div>

            <!-- BLOCCO 6: RACCORDO DI CHIUSURA ED ESPLORAZIONE CLINICA -->
            <div class="card-soft-gradient p-8 md:p-10 rounded-3xl border border-caldo-borderSoft flex flex-col md:flex-row items-center justify-between gap-6">
                <div class="space-y-2 text-center md:text-left">
                    <span class="text-xs font-semibold text-caldo-coral uppercase tracking-wider block">Approfondimenti Clinici</span>
                    <h3 class="text-2xl font-serif text-caldo-text font-semibold">Desideri approfondire la tua specifica patologia?</h3>
                    <p class="text-xs text-caldo-muted font-light max-w-xl">
                        Consulta le schede dedicate per comprendere l'anatomia, le tecniche artroscopiche mininvasive e i percorsi di recupero formulati dal Dott. Novi.
                    </p>
                </div>
                <div class="flex flex-wrap items-center gap-3 shrink-0">
                    <a href="#patologie-spalla" class="nav-trigger text-xs font-semibold px-4 py-2.5 rounded-full bg-white border border-caldo-borderSoft text-caldo-teal hover:border-caldo-teal transition-all" data-target="patologie-spalla">
                        Patologie Spalla
                    </a>
                    <a href="#patologie-gomito" class="nav-trigger text-xs font-semibold px-4 py-2.5 rounded-full bg-white border border-caldo-borderSoft text-caldo-teal hover:border-caldo-teal transition-all" data-target="patologie-gomito">
                        Patologie Gomito
                    </a>
                    <a href="#chi-sono" class="nav-trigger text-xs font-semibold px-4 py-2.5 rounded-full bg-caldo-teal text-white hover:bg-caldo-teal/90 transition-all" data-target="chi-sono">
                        Profilo Dott. Novi
                    </a>
                </div>
            </div>

        </section>

    </main>

    <!-- FOOTER COMPLETO DELLA BIBBIA -->
    <footer class="bg-white/80 backdrop-blur-md border-t border-caldo-borderSoft mt-32 py-16 px-6 relative z-10">
        <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-10 text-sm">
            <div class="space-y-3">
                <div class="font-serif text-2xl text-caldo-text font-normal">Dott. Michele Novi</div>
                <p class="text-xs text-caldo-muted font-light leading-relaxed">
                    Chirurgo Ortopedico Traumatologo.<br>
                    Dirigente Medico Ospedale CESAT Fucecchio.<br>
                    Iscritto all'Ordine dei Medici di Pisa n. 5988.<br>
                    P. IVA in attribuzione.
                </p>
            </div>

            <div class="space-y-2 text-xs font-light">
                <strong class="text-caldo-text uppercase font-semibold text-[11px] block mb-3">Navigazione Rapida</strong>
                <div><a href="#chi-sono" class="nav-trigger text-caldo-muted hover:text-caldo-teal" data-target="chi-sono">Chi sono</a></div>
                <div><a href="#patologie" class="nav-trigger text-caldo-muted hover:text-caldo-teal" data-target="patologie">Cosa curo (Patologie)</a></div>
                <div><a href="#sedi" class="nav-trigger text-caldo-muted hover:text-caldo-teal" data-target="sedi">Dove ricevo (Sedi)</a></div>
                <div><a href="#articoli" class="nav-trigger text-caldo-muted hover:text-caldo-teal" data-target="articoli">Note cliniche (Il Quaderno)</a></div>
                <div><a href="#contatti" class="nav-trigger text-caldo-muted hover:text-caldo-teal" data-target="contatti">Contatti e Prenotazioni</a></div>
            </div>

            <div class="space-y-2 text-xs font-light">
                <strong class="text-caldo-text uppercase font-semibold text-[11px] block mb-3">Polo Ospedaliero & Sedi</strong>
                <p class="text-caldo-muted leading-relaxed">
                    <strong>CESAT Fucecchio:</strong> Piazza Lavagnini 5 (Chirurgia)<br>
                    <strong>Studi San Pietro:</strong> Piazza Lavagnini 6 (Visite)<br>
                    <strong>Valdera:</strong> Polo San Verano, Peccioli<br>
                    <strong>Pisa & Fornacette:</strong> Athletica e Fisiomed
                </p>
            </div>

            <div class="space-y-3 text-xs">
                <strong class="text-caldo-text uppercase font-semibold text-[11px] block mb-3">Segreteria Unificata</strong>
                <a href="tel:+393484331733" class="text-2xl font-serif text-caldo-teal block">348 4331733</a>
                <p class="text-caldo-muted text-[11px] leading-relaxed font-light">
                    Chiamate: Lunedì – Giovedì 15:30 – 17:30.<br>
                    WhatsApp sempre disponibile per disponibilità appuntamenti.
                </p>
            </div>
        </div>

        <div class="max-w-7xl mx-auto mt-12 pt-6 border-t border-caldo-borderSoft flex flex-col sm:flex-row justify-between items-center text-xs text-caldo-muted gap-4 font-light">
            <div>© 2026 Dott. Michele Novi · Tutti i diritti riservati</div>
            <div class="flex gap-6">
                <span>Informativa Privacy</span>
                <span>Cookie Policy</span>
                <span class="text-caldo-teal font-medium">Conforme Linee Guida Sanitarie FNOMCeO</span>
            </div>
        </div>
    </footer>

    <!-- JS ROUTER & INCASTRI INTERATTIVI -->
    <script>
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
            
            const allBtns = btn.parentElement.querySelectorAll('button');
            allBtns.forEach(b => {
                b.className = "p-4 rounded-2xl border border-caldo-border bg-caldo-bg text-left hover:border-caldo-teal transition-all flex items-center justify-between group";
                b.querySelector('span:last-child').className = "w-6 h-6 rounded-full bg-white text-caldo-teal flex items-center justify-center font-bold text-xs shadow-sm";
                b.querySelector('span:last-child').innerText = "○";
            });

            btn.className = "p-4 rounded-2xl border-2 border-caldo-coral bg-caldo-coralLight text-left transition-all flex items-center justify-between group shadow-sm";
            btn.querySelector('span:last-child').className = "w-6 h-6 rounded-full bg-caldo-coral text-white flex items-center justify-center font-bold text-xs shadow-sm";
            btn.querySelector('span:last-child').innerText = "✓";

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

        document.addEventListener('DOMContentLoaded', () => {
            const curtain = document.getElementById('articular-curtain');
            const pageViews = document.querySelectorAll('.page-view');

            function switchViewWithJointTransition(targetId) {
                const targetEl = document.getElementById('view-' + targetId);
                if (!targetEl) return;

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
        });
    </script>
</body>
</html>
"""

target_path = "/Volumes/Programs/Temporary files/Progetti cursor/Michele_Novi_Website/handoff_sito.html"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_content)

proposte_path = "/Volumes/Programs/Temporary files/Progetti cursor/Michele_Novi_Website/Proposte HTML/index.html"
with open(proposte_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Prototipo CON TUTTO IL CONTENUTO REINTEGRATO generato con successo!")
