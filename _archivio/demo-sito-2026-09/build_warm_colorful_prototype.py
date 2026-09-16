# -*- coding: utf-8 -*-
"""
Script per la generazione del prototipo HTML "Calore, Colore, Icone & Design Moderno"
per il Dott. Michele Novi.

Richieste utente soddisfatte:
1. MENO DA SMANETTONE / TERMINALE: niente codici macchina, niente coordinate ASCII, niente croci grigie sterili.
2. MENO DA QUADERNINO DELLE NOTE: impaginazione moderna, calda, editoriale medica di alto livello.
3. PIÙ CALORE E PIÙ COLORE:
   - Palette calda ed empatica: Fondo "Crema Alabastro" (#FAF8F5), Deep Medical Teal (#0A444C), Accento Caldo Terracotta/Ambra (#D96B43), Verde Salvia e sfumature accoglienti.
   - Card luminose con morbidi bagliori e angoli raccordati.
4. PIÙ ICONE VETTORIALI DEDICATE (SVG custom rifiniti):
   - Icone anatomiche per Spalla, Gomito, Mano
   - Icone per Sport, Artroscopia, Ecografia SIUMB
   - Icone per Sedi, Ospedale, Orari, Telefono, WhatsApp, Badge di verifica
5. MANTENIMENTO DEI CONCETTI CHIAVE DELLA BIBBIA:
   - "Uno strato sotto l'altro": sezioni stacked card fluide, sfogliare i livelli anatomici
   - "L'incastro": congruenza articolare interattiva, giunti modulari a incastro geometrico
   - Nomi pagine e struttura 100% allineati a 04_Architettura_Informazione.md.
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
    
    <!-- Google Fonts: Plus Jakarta Sans (caldo, umano, moderno) + Newsreader (autorevolezza medica) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,300;1,6..72,400;1,6..72,500&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        caldo: {
                            bg: '#FBF9F5',          /* Caldo crema avorio / cashmere */
                            surface: '#FFFFFF',     /* Bianco puro caldo */
                            card: '#FFFFFF',
                            border: '#EFECE6',      /* Bordo caldo tenue */
                            borderDark: '#DDD8CE',
                            text: '#172021',        /* Nero petrolio caldo */
                            muted: '#5C6768',       /* Testo secondario morbido */
                            
                            /* Colori identità */
                            teal: '#094E57',        /* Teal chirurgico profondo e rassicurante */
                            tealLight: '#E8F3F4',   /* Bagliore teal morbido */
                            tealMedium: '#1D707B',
                            
                            coral: '#D96B43',       /* Accento caldo terracotta/ambra (energia, vita, sport) */
                            coralLight: '#FDF0EB',  /* Fondo corallo tenue */
                            
                            salvia: '#4A7C59',      /* Verde biologico per guarigione e recupero */
                            salviaLight: '#EDF5F0',
                            
                            gold: '#C88D42',        /* Tocco dorato prestigioso */
                            goldLight: '#FDF6ED'
                        }
                    },
                    fontFamily: {
                        serif: ['Newsreader', 'Georgia', 'serif'],
                        sans: ['Plus Jakarta Sans', 'system-ui', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace']
                    }
                }
            }
        }
    </script>
    
    <style>
        :root {
            --ease-fluid: cubic-bezier(0.16, 1, 0.3, 1);
            --ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
        }

        body {
            background-color: #FBF9F5;
            color: #172021;
            font-family: 'Plus Jakarta Sans', sans-serif;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }

        /* Ombre calde e morbide (niente grafica da terminale) */
        .shadow-warm-sm {
            box-shadow: 0 2px 8px -2px rgba(9, 78, 87, 0.05), 0 1px 4px -1px rgba(217, 107, 67, 0.03);
        }
        .shadow-warm-md {
            box-shadow: 0 12px 28px -6px rgba(9, 78, 87, 0.08), 0 4px 12px -2px rgba(217, 107, 67, 0.04);
        }
        .shadow-warm-lg {
            box-shadow: 0 20px 40px -12px rgba(9, 78, 87, 0.12), 0 8px 20px -4px rgba(217, 107, 67, 0.06);
        }

        /* 1. L'INCASTRO MODERNO (INTERLOCKING CARDS) */
        .joint-card {
            border: 1px solid #EFECE6;
            background: #FFFFFF;
            transition: all 0.35s var(--ease-fluid);
            position: relative;
        }
        .joint-card:hover {
            transform: translateY(-4px);
            border-color: #094E57;
            box-shadow: 0 16px 36px -8px rgba(9, 78, 87, 0.12);
        }

        /* Incastro angolare a linguetta arrotondata (Awwwards friendly) */
        .interlock-badge {
            border-radius: 0 0 14px 14px;
            box-shadow: 0 4px 12px rgba(9, 78, 87, 0.08);
        }

        /* Widget interattivo Congruenza: Testa e Glenoide calde */
        .congruence-box {
            background: linear-gradient(135deg, #FFFFFF 0%, #F8FAF9 100%);
            border: 1px solid #E2EBE6;
            border-radius: 24px;
            transition: all 0.4s var(--ease-fluid);
        }
        .congruence-box:hover {
            border-color: #094E57;
            box-shadow: 0 16px 40px -10px rgba(9, 78, 87, 0.15);
        }
        .congruence-head {
            transform: translateX(-14px);
            transition: transform 0.5s var(--ease-bounce);
        }
        .congruence-box:hover .congruence-head {
            transform: translateX(0px); /* L'incastro scatta con dolcezza */
        }
        .congruence-glow {
            opacity: 0;
            transition: opacity 0.5s var(--ease-fluid);
        }
        .congruence-box:hover .congruence-glow {
            opacity: 1;
        }

        /* 2. GLI STRATI SOVRAPPOSTI (WARM STACKED LAYERS) */
        .strata-panel {
            position: sticky;
            border-radius: 28px;
            background: #FFFFFF;
            border: 1px solid #EFECE6;
            box-shadow: 0 -10px 30px rgba(9, 78, 87, 0.05);
            transition: all 0.3s var(--ease-fluid);
        }
        .strata-panel:nth-child(1) { top: 6rem; z-index: 10; }
        .strata-panel:nth-child(2) { top: 8rem; z-index: 20; }
        .strata-panel:nth-child(3) { top: 10rem; z-index: 30; }
        .strata-panel:nth-child(4) { top: 12rem; z-index: 40; }

        /* Bottoni Caldi con Incastro e Micro-interazioni */
        .btn-warm-primary {
            background: linear-gradient(135deg, #094E57 0%, #0D616C 100%);
            color: #FFFFFF;
            border-radius: 9999px;
            transition: all 0.3s var(--ease-fluid);
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
            box-shadow: 0 8px 20px -4px rgba(9, 78, 87, 0.3);
        }
        .btn-warm-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 28px -4px rgba(9, 78, 87, 0.4);
            background: linear-gradient(135deg, #073B42 0%, #094E57 100%);
        }

        .btn-warm-coral {
            background: linear-gradient(135deg, #D96B43 0%, #E27953 100%);
            color: #FFFFFF;
            border-radius: 9999px;
            transition: all 0.3s var(--ease-fluid);
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
            box-shadow: 0 8px 20px -4px rgba(217, 107, 67, 0.3);
        }
        .btn-warm-coral:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 28px -4px rgba(217, 107, 67, 0.45);
        }

        .btn-warm-secondary {
            background: #FFFFFF;
            color: #094E57;
            border: 1px solid #DFE7E6;
            border-radius: 9999px;
            transition: all 0.3s var(--ease-fluid);
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
        }
        .btn-warm-secondary:hover {
            border-color: #094E57;
            background: #F4F9F9;
            transform: translateY(-2px);
        }

        /* SPA transitions */
        .page-view {
            display: none;
            opacity: 0;
        }
        .page-view.active-view {
            display: block;
            animation: viewFadeIn 0.5s var(--ease-fluid) forwards;
        }
        @keyframes viewFadeIn {
            0% { opacity: 0; transform: translateY(16px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        /* Cerchio decorativo con luce calda e accogliente in hero */
        .warm-aura {
            background: radial-gradient(circle, rgba(232, 243, 244, 0.8) 0%, rgba(253, 240, 235, 0.4) 50%, rgba(251, 249, 245, 0) 70%);
        }
    </style>
</head>
<body class="selection:bg-caldo-teal selection:text-white relative">

    <!-- Luce calda d'ambiente di sfondo -->
    <div class="fixed top-0 right-0 w-[600px] h-[600px] warm-aura pointer-events-none -z-10 rounded-full blur-3xl opacity-70"></div>
    <div class="fixed bottom-0 left-0 w-[500px] h-[500px] bg-caldo-coralLight pointer-events-none -z-10 rounded-full blur-3xl opacity-50"></div>

    <!-- ============================================================
         HEADER: ACCOGLIENTE, ELEGANTE E COLORATO
         ============================================================ -->
    <header class="fixed top-0 left-0 w-full z-50 bg-[#FBF9F5]/90 backdrop-blur-md border-b border-caldo-border transition-all duration-300" id="main-header">
        <div class="max-w-7xl mx-auto px-6 h-20 flex justify-between items-center">
            
            <!-- Logo Caldo: Dott. Michele Novi con badge specialistico -->
            <a href="#home" class="nav-trigger group flex items-center gap-3.5 cursor-pointer" data-target="home">
                <div class="w-11 h-11 rounded-2xl bg-gradient-to-br from-caldo-teal to-caldo-tealMedium flex items-center justify-center text-white font-bold text-sm shadow-warm-sm group-hover:scale-105 transition-transform duration-300">
                    <!-- Icona articolare stilizzata -->
                    <svg class="w-6 h-6 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/>
                        <circle cx="12" cy="12" r="3" fill="#D96B43" stroke="none"/>
                    </svg>
                </div>
                <div class="flex flex-col">
                    <span class="font-serif text-xl tracking-tight text-caldo-text font-medium leading-tight group-hover:text-caldo-teal transition-colors">
                        Dott. Michele Novi
                    </span>
                    <span class="text-xs font-medium text-caldo-teal flex items-center gap-1.5">
                        <span class="w-1.5 h-1.5 rounded-full bg-caldo-coral"></span>
                        Chirurgo Ortopedico · Spalla e Arto Superiore
                    </span>
                </div>
            </a>

            <!-- Navigazione Principale con Pillole di Hover -->
            <nav class="hidden lg:flex items-center gap-1 text-sm font-semibold text-caldo-text">
                <a href="#chi-sono" class="nav-trigger px-4 py-2 rounded-full hover:bg-white hover:text-caldo-teal hover:shadow-warm-sm transition-all" data-target="chi-sono">
                    Chi sono
                </a>
                <a href="#patologie" class="nav-trigger px-4 py-2 rounded-full hover:bg-white hover:text-caldo-teal hover:shadow-warm-sm transition-all flex items-center gap-1.5" data-target="patologie">
                    <span>Cosa curo</span>
                    <span class="w-2 h-2 rounded-full bg-caldo-teal/20 text-[10px] text-caldo-teal font-bold"></span>
                </a>
                <a href="#sedi" class="nav-trigger px-4 py-2 rounded-full hover:bg-white hover:text-caldo-teal hover:shadow-warm-sm transition-all" data-target="sedi">
                    Dove ricevo
                </a>
                <a href="#articoli" class="nav-trigger px-4 py-2 rounded-full hover:bg-white hover:text-caldo-teal hover:shadow-warm-sm transition-all" data-target="articoli">
                    Note cliniche
                </a>
                <a href="#contatti" class="nav-trigger px-4 py-2 rounded-full hover:bg-white hover:text-caldo-teal hover:shadow-warm-sm transition-all" data-target="contatti">
                    Contatti
                </a>
            </nav>

            <!-- CTA Segreteria e Telefono in evidenza con colori caldi -->
            <div class="flex items-center gap-3">
                <a href="tel:+393484331733" class="hidden sm:inline-flex items-center gap-2 px-3.5 py-2 rounded-full bg-caldo-tealLight text-caldo-teal font-medium text-xs hover:bg-caldo-teal hover:text-white transition-all shadow-warm-sm">
                    <svg class="w-4 h-4 text-caldo-coral animate-pulse" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                        <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
                    </svg>
                    <span>348 4331733</span>
                </a>
                
                <a href="#contatti" class="nav-trigger btn-warm-coral px-5 py-2.5 text-xs font-semibold" data-target="contatti">
                    <span>Prenota Visita</span>
                    <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                        <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                </a>
            </div>
        </div>
    </header>

    <!-- ============================================================
         CONTENUTI PRINCIPALI SPA
         ============================================================ -->
    <main class="pt-24 min-h-screen" id="app-root">

        <!-- ========================================================
             VISTA 1: HOME (CALORE, COLORE, INCASTRO & STRATI)
             ======================================================== -->
        <section id="view-home" class="page-view active-view">
            
            <!-- HERO: CALDO, UMANO E LUMINOSO -->
            <div class="max-w-7xl mx-auto px-6 pt-12 pb-20">
                
                <!-- Badge di fiducia e accoglienza -->
                <div class="inline-flex items-center gap-2.5 bg-white border border-caldo-border px-4 py-2 rounded-full shadow-warm-sm mb-8">
                    <span class="flex h-2.5 w-2.5 relative">
                        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-caldo-coral opacity-75"></span>
                        <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-caldo-coral"></span>
                    </span>
                    <span class="text-xs font-semibold text-caldo-teal">Ospedale CESAT Fucecchio</span>
                    <span class="text-caldo-borderDark">·</span>
                    <span class="text-xs text-caldo-muted">Ambulatori a Fucecchio, Peccioli, Fornacette, Pisa</span>
                </div>

                <!-- Griglia Hero a Incastro Caldo -->
                <div class="grid lg:grid-cols-12 gap-12 items-center">
                    
                    <!-- Testo Hero con Colore e Umanità -->
                    <div class="lg:col-span-7 space-y-6">
                        
                        <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text font-normal leading-[1.08] tracking-tight">
                            Ritrovare il movimento,<br>
                            con la precisione di <br>
                            <span class="italic text-caldo-teal bg-gradient-to-r from-caldo-teal to-caldo-tealMedium bg-clip-text text-transparent font-medium">due superfici che combaciano.</span>
                        </h1>

                        <p class="text-lg sm:text-xl text-caldo-muted font-light leading-relaxed max-w-xl">
                            Chirurgia ortopedica della spalla, del gomito e della mano. 
                            Dalle tecniche artroscopiche mini-invasive alle protesi articolari, 
                            con l'ascolto e la vicinanza di un medico del territorio.
                        </p>

                        <!-- Punti di forza con icone colorate -->
                        <div class="grid sm:grid-cols-3 gap-4 pt-2">
                            <div class="flex items-center gap-3 bg-white p-3 rounded-2xl border border-caldo-border shadow-warm-sm">
                                <div class="w-10 h-10 rounded-xl bg-caldo-tealLight text-caldo-teal flex items-center justify-center flex-shrink-0">
                                    <!-- Icona Spalla/Articolazione -->
                                    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                        <circle cx="12" cy="12" r="9"/>
                                        <path d="M12 7v5l3 3"/>
                                    </svg>
                                </div>
                                <div class="text-xs">
                                    <strong class="block text-caldo-text font-bold">Spalla & Arto</strong>
                                    <span class="text-caldo-muted">Core specialistico</span>
                                </div>
                            </div>

                            <div class="flex items-center gap-3 bg-white p-3 rounded-2xl border border-caldo-border shadow-warm-sm">
                                <div class="w-10 h-10 rounded-xl bg-caldo-coralLight text-caldo-coral flex items-center justify-center flex-shrink-0">
                                    <!-- Icona Mini-invasiva / Luce ottica -->
                                    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                        <path d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"/>
                                        <path d="M12 4v1M12 19v1M4 12h1M19 12h1"/>
                                    </svg>
                                </div>
                                <div class="text-xs">
                                    <strong class="block text-caldo-text font-bold">Artroscopia</strong>
                                    <span class="text-caldo-muted">Mini-invasività</span>
                                </div>
                            </div>

                            <div class="flex items-center gap-3 bg-white p-3 rounded-2xl border border-caldo-border shadow-warm-sm">
                                <div class="w-10 h-10 rounded-xl bg-caldo-salviaLight text-caldo-salvia flex items-center justify-center flex-shrink-0">
                                    <!-- Icona Ospedale d'eccellenza -->
                                    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                        <path d="M3 21h18M5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16"/>
                                        <path d="M9 10h6M12 7v6"/>
                                    </svg>
                                </div>
                                <div class="text-xs">
                                    <strong class="block text-caldo-text font-bold">CESAT Ospedale</strong>
                                    <span class="text-caldo-muted">Chirurgia & Protesi</span>
                                </div>
                            </div>
                        </div>

                        <!-- Bottoni di Azione Caldi -->
                        <div class="flex flex-wrap gap-4 pt-4">
                            <a href="#contatti" class="nav-trigger btn-warm-primary px-8 py-4 text-sm font-semibold" data-target="contatti">
                                <span>Richiedi una Visita</span>
                                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                                    <path d="M5 12h14M12 5l7 7-7 7"/>
                                </svg>
                            </a>
                            <a href="#patologie" class="nav-trigger btn-warm-secondary px-7 py-4 text-sm font-semibold" data-target="patologie">
                                <span>Scopri le Patologie</span>
                                <span class="text-caldo-teal font-bold">→</span>
                            </a>
                        </div>

                    </div>

                    <!-- Immagine Protagonista con cornice calda a incastro -->
                    <div class="lg:col-span-5 relative">
                        
                        <!-- Riquadro morbido con gradiente caldo -->
                        <div class="relative z-10 bg-white p-4 rounded-3xl border border-caldo-border shadow-warm-lg">
                            
                            <div class="aspect-[4/5] rounded-2xl overflow-hidden relative bg-caldo-tealLight">
                                <img src="https://images.unsplash.com/photo-1622253692010-333f2da6031d?q=80&w=1000&auto=format&fit=crop" 
                                     alt="Dott. Michele Novi Ortopedico" 
                                     class="w-full h-full object-cover object-center">
                                
                                <!-- Badge a incastro sulla foto -->
                                <div class="absolute bottom-4 left-4 right-4 bg-white/95 backdrop-blur-md p-4 rounded-2xl border border-caldo-border/80 shadow-warm-md flex items-center justify-between">
                                    <div>
                                        <span class="text-xs font-bold text-caldo-text block">Dott. Michele Novi</span>
                                        <span class="text-[11px] text-caldo-teal font-medium">Dirigente Medico Ortopedico</span>
                                    </div>
                                    <div class="w-9 h-9 rounded-full bg-caldo-coralLight text-caldo-coral flex items-center justify-center">
                                        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                                        </svg>
                                    </div>
                                </div>
                            </div>

                        </div>

                        <!-- Decorazione a incastro sotto la card -->
                        <div class="absolute -bottom-6 -right-6 w-48 h-48 bg-gradient-to-br from-caldo-coralLight to-caldo-goldLight rounded-3xl -z-0 opacity-70"></div>
                    </div>

                </div>
            </div>

            <!-- ========================================================
                 SEZIONE 2: L'INCASTRO E LA CONGRUENZA (INTERATTIVA & COLORATA)
                 Spiegazione visiva ma calda e accessibile per i pazienti
                 ======================================================== -->
            <div class="bg-white border-y border-caldo-border py-24 px-6">
                <div class="max-w-7xl mx-auto">
                    
                    <div class="max-w-2xl mb-16 space-y-3">
                        <div class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-caldo-coral bg-caldo-coralLight px-3 py-1 rounded-full">
                            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                                <circle cx="12" cy="12" r="10"/>
                                <path d="m9 12 2 2 4-4"/>
                            </svg>
                            <span>Il Principio della Stabilità</span>
                        </div>
                        <h2 class="text-3xl sm:text-5xl font-serif text-caldo-text">
                            L'Incastro perfetto: quando due superfici tornano a dialogare.
                        </h2>
                        <p class="text-base text-caldo-muted leading-relaxed">
                            Nell'articolazione della spalla, la testa dell'omero e la glenoide devono combaciare al millimetro. Quando un trauma o un'usura rompono questo equilibrio, il nostro obiettivo è ripristinare la congruenza naturale.
                        </p>
                    </div>

                    <!-- Modulo Incastro con Colori Empatici -->
                    <div class="grid lg:grid-cols-12 gap-8 items-center">
                        
                        <!-- Box Interattivo Congruenza -->
                        <div class="lg:col-span-6 congruence-box p-8 md:p-12 relative overflow-hidden cursor-pointer group">
                            
                            <div class="flex justify-between items-center mb-8">
                                <span class="text-xs font-bold uppercase text-caldo-teal tracking-wider flex items-center gap-2">
                                    <span class="w-2 h-2 rounded-full bg-caldo-teal animate-ping"></span>
                                    Esperienza Interattiva
                                </span>
                                <span class="text-xs font-semibold bg-caldo-teal text-white px-3.5 py-1.5 rounded-full shadow-warm-sm">
                                    Passa sopra per allineare l'incastro
                                </span>
                            </div>

                            <!-- Illustrazione interattiva dell'incastro -->
                            <div class="flex items-center justify-center my-10 relative">
                                
                                <!-- Glenoide (Superficie ricevente con curva calda) -->
                                <div class="w-36 h-48 rounded-r-full bg-caldo-tealLight border-2 border-caldo-teal flex items-center justify-start pl-4 relative shadow-warm-sm">
                                    <div class="text-left">
                                        <span class="text-xs font-bold text-caldo-teal block">Glenoide</span>
                                        <span class="text-[10px] text-caldo-muted">Superficie concava</span>
                                    </div>
                                </div>

                                <!-- Testa Omerale mobile che si incastra -->
                                <div class="congruence-head w-40 h-40 rounded-full bg-gradient-to-r from-caldo-coral to-caldo-coral/90 text-white flex items-center justify-center -ml-16 shadow-warm-md border-4 border-white z-10">
                                    <div class="text-center p-2">
                                        <svg class="w-6 h-6 mx-auto mb-1 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                            <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
                                        </svg>
                                        <strong class="text-xs font-bold block">Testa Omerale</strong>
                                        <span class="text-[10px] opacity-90">Superficie convessa</span>
                                    </div>
                                </div>

                                <!-- Bagliore di congruenza -->
                                <div class="congruence-glow absolute inset-0 bg-caldo-salviaLight/30 rounded-full blur-2xl pointer-events-none"></div>
                            </div>

                            <div class="bg-white p-4 rounded-2xl border border-caldo-border flex items-center justify-between text-xs">
                                <div class="flex items-center gap-2.5">
                                    <div class="w-7 h-7 rounded-full bg-caldo-salviaLight text-caldo-salvia flex items-center justify-center font-bold">✓</div>
                                    <span class="font-semibold text-caldo-text">Stabilità e movimento conservati</span>
                                </div>
                                <span class="text-caldo-teal font-medium">Procedura di Remplissage</span>
                            </div>

                        </div>

                        <!-- Spiegazione Calda per il Paziente -->
                        <div class="lg:col-span-6 space-y-6">
                            
                            <div class="bg-caldo-bg p-8 rounded-3xl border border-caldo-border space-y-4">
                                <div class="w-10 h-10 rounded-2xl bg-caldo-coralLight text-caldo-coral flex items-center justify-center">
                                    <!-- Icona Lucchetto Aperto / Chiuso -->
                                    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                        <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
                                        <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
                                    </svg>
                                </div>
                                <h3 class="text-2xl font-serif text-caldo-text">
                                    Nelle lussazioni recidivanti, l'osso non deve ingranare nel vuoto.
                                </h3>
                                <p class="text-sm text-caldo-muted leading-relaxed">
                                    Quando una spalla si lussa ripetutamente, si crea spesso una piccola usura ossea (lesione di Hill-Sachs). Nelle posizioni estreme, questa lesione rischia di incastrarsi sul ciglio dell'articolazione, provocando una nuova fuoriuscita.
                                </p>
                                <p class="text-sm text-caldo-muted leading-relaxed">
                                    Con il <strong>Remplissage</strong> ("riempimento" artroscopico), colmiamo questa nicchia con un tessuto tendineo, trasformando una leva pericolosa in una superficie liscia e protetta, senza sacrificare l'escursione di movimento.
                                </p>
                                <div class="pt-2">
                                    <a href="#articoli-remplissage" class="nav-trigger text-sm font-bold text-caldo-teal hover:text-caldo-coral inline-flex items-center gap-1.5 transition-colors" data-target="articoli-remplissage">
                                        <span>Approfondisci lo studio scientifico sul Remplissage</span>
                                        <span>→</span>
                                    </a>
                                </div>
                            </div>

                        </div>

                    </div>
                </div>
            </div>

            <!-- ========================================================
                 SEZIONE 3: UNO STRATO SOTTO L'ALTRO (STACKED CARDS CALDE)
                 Livelli anatomici che si sfogliano con morbidezza
                 ======================================================== -->
            <div class="max-w-7xl mx-auto px-6 py-28">
                
                <div class="max-w-2xl mb-16 space-y-3">
                    <div class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-caldo-teal bg-caldo-tealLight px-3.5 py-1 rounded-full">
                        <svg class="w-4 h-4 text-caldo-teal" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                            <line x1="12" y1="5" x2="12" y2="19"/>
                            <polyline points="19 12 12 19 5 12"/>
                        </svg>
                        <span>Approccio Graduale e Mini-Invasivo</span>
                    </div>
                    <h2 class="text-3xl sm:text-5xl font-serif text-caldo-text">
                        Uno strato sotto l'altro: la cura passo dopo passo.
                    </h2>
                    <p class="text-base text-caldo-muted leading-relaxed">
                        In chirurgia come in diagnosi non si interviene alla cieca: ogni strato del corpo ha una funzione biologica specifica e merita il trattamento più rispettoso.
                    </p>
                </div>

                <!-- Pila di Strati con Colori e Icone Calde -->
                <div class="space-y-8 relative">
                    
                    <!-- STRATO 1: CUTE & MINI-INVASIVITÀ -->
                    <div class="strata-panel p-8 md:p-12 border border-caldo-border bg-white shadow-warm-md">
                        <div class="grid md:grid-cols-12 gap-6 items-center">
                            <div class="md:col-span-2 flex md:flex-col items-center gap-3">
                                <div class="w-14 h-14 rounded-2xl bg-caldo-tealLight text-caldo-teal flex items-center justify-center font-bold text-xl">
                                    <!-- Icona Incisione precisa / Microscopio -->
                                    <svg class="w-7 h-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                        <path d="M12 2v20M2 12h20M7 7l10 10M7 17l10-10"/>
                                    </svg>
                                </div>
                                <span class="text-xs font-bold text-caldo-teal uppercase tracking-wider">Strato 01</span>
                            </div>
                            <div class="md:col-span-7 space-y-2">
                                <h3 class="text-2xl font-serif text-caldo-text">L'Accesso Mini-Invasivo</h3>
                                <p class="text-sm text-caldo-muted leading-relaxed">
                                    Nessuna grande incisione. Entriamo attraverso fori ottici di pochi millimetri, preservando la cute e la muscolatura per un risveglio con meno dolore e una cicatrice quasi invisibile.
                                </p>
                            </div>
                            <div class="md:col-span-3 text-right">
                                <span class="inline-block bg-caldo-tealLight text-caldo-teal text-xs font-bold px-4 py-2 rounded-full">
                                    Artroscopia Avanzata
                                </span>
                            </div>
                        </div>
                    </div>

                    <!-- STRATO 2: TENDINI E CUFFIA DEI ROTATORI -->
                    <div class="strata-panel p-8 md:p-12 border border-caldo-border bg-white shadow-warm-md">
                        <div class="grid md:grid-cols-12 gap-6 items-center">
                            <div class="md:col-span-2 flex md:flex-col items-center gap-3">
                                <div class="w-14 h-14 rounded-2xl bg-caldo-coralLight text-caldo-coral flex items-center justify-center font-bold text-xl">
                                    <!-- Icona Muscolo / Forza -->
                                    <svg class="w-7 h-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                        <path d="M18 8h1a4 4 0 0 1 0 8h-1M6 8H5a4 4 0 0 0 0 8h1M2 12h20"/>
                                    </svg>
                                </div>
                                <span class="text-xs font-bold text-caldo-coral uppercase tracking-wider">Strato 02</span>
                            </div>
                            <div class="md:col-span-7 space-y-2">
                                <h3 class="text-2xl font-serif text-caldo-text">La Cuffia dei Rotatori</h3>
                                <p class="text-sm text-caldo-muted leading-relaxed">
                                    I quattro tendini che garantiscono la rotazione della spalla. Ripariamo le lesioni con micro-ancore riassorbibili, valutando sempre quando ha senso aspettare e potenziare con la fisioterapia.
                                </p>
                            </div>
                            <div class="md:col-span-3 text-right">
                                <span class="inline-block bg-caldo-coralLight text-caldo-coral text-xs font-bold px-4 py-2 rounded-full">
                                    Riparazione Biologica
                                </span>
                            </div>
                        </div>
                    </div>

                    <!-- STRATO 3: LA CAPSULA E LA STABILITÀ -->
                    <div class="strata-panel p-8 md:p-12 border border-caldo-border bg-white shadow-warm-md">
                        <div class="grid md:grid-cols-12 gap-6 items-center">
                            <div class="md:col-span-2 flex md:flex-col items-center gap-3">
                                <div class="w-14 h-14 rounded-2xl bg-caldo-goldLight text-caldo-gold flex items-center justify-center font-bold text-xl">
                                    <!-- Icona Sigillo / Scudo -->
                                    <svg class="w-7 h-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                                    </svg>
                                </div>
                                <span class="text-xs font-bold text-caldo-gold uppercase tracking-wider">Strato 03</span>
                            </div>
                            <div class="md:col-span-7 space-y-2">
                                <h3 class="text-2xl font-serif text-caldo-text">Capsula e Cercine Glenoideo</h3>
                                <p class="text-sm text-caldo-muted leading-relaxed">
                                    La guarnizione anatomica che trattiene la spalla in sede. Fondamentale per i giovani atleti che praticano sport di contatto o di lancio dopo una lussazione traumatica.
                                </p>
                            </div>
                            <div class="md:col-span-3 text-right">
                                <span class="inline-block bg-caldo-goldLight text-caldo-gold text-xs font-bold px-4 py-2 rounded-full">
                                    Intervento di Bankart
                                </span>
                            </div>
                        </div>
                    </div>

                    <!-- STRATO 4: L'OSSO E LA CHIRURGIA PROTESICA -->
                    <div class="strata-panel p-8 md:p-12 border border-caldo-border bg-white shadow-warm-md">
                        <div class="grid md:grid-cols-12 gap-6 items-center">
                            <div class="md:col-span-2 flex md:flex-col items-center gap-3">
                                <div class="w-14 h-14 rounded-2xl bg-caldo-salviaLight text-caldo-salvia flex items-center justify-center font-bold text-xl">
                                    <!-- Icona Osso portante / Rigenerazione -->
                                    <svg class="w-7 h-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                        <circle cx="6" cy="6" r="3"/>
                                        <circle cx="6" cy="18" r="3"/>
                                        <line x1="6" y1="9" x2="6" y2="15"/>
                                        <circle cx="18" cy="6" r="3"/>
                                        <circle cx="18" cy="18" r="3"/>
                                        <line x1="18" y1="9" x2="18" y2="15"/>
                                        <line x1="9" y1="12" x2="15" y2="12"/>
                                    </svg>
                                </div>
                                <span class="text-xs font-bold text-caldo-salvia uppercase tracking-wider">Strato 04</span>
                            </div>
                            <div class="md:col-span-7 space-y-2">
                                <h3 class="text-2xl font-serif text-caldo-text">La Struttura Ossea e la Protesica</h3>
                                <p class="text-sm text-caldo-muted leading-relaxed">
                                    Quando l'usura della cartilagine o l'artrosi avanzata tolgono la possibilità di sollevare il braccio, le protesi anatomiche e inverse al CESAT ridonano autonomia completa e assenza di dolore.
                                </p>
                            </div>
                            <div class="md:col-span-3 text-right">
                                <span class="inline-block bg-caldo-salviaLight text-caldo-salvia text-xs font-bold px-4 py-2 rounded-full">
                                    Polo Ospedaliero CESAT
                                </span>
                            </div>
                        </div>
                    </div>

                </div>
            </div>

            <!-- ========================================================
                 SEZIONE 4: ANTEPRIMA AREE CLINICHE CON ICONE COLORATE
                 ======================================================== -->
            <div class="bg-caldo-surface border-t border-caldo-border py-24 px-6">
                <div class="max-w-7xl mx-auto">
                    
                    <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-6">
                        <div>
                            <span class="text-xs font-bold text-caldo-teal uppercase tracking-wider block mb-2">Percorsi di Cura</span>
                            <h2 class="text-3xl sm:text-5xl font-serif text-caldo-text">Cosa curo: 6 aree specialistiche.</h2>
                        </div>
                        <a href="#patologie" class="nav-trigger btn-warm-secondary px-6 py-3 text-xs font-bold" data-target="patologie">
                            Tutte le Patologie in dettaglio →
                        </a>
                    </div>

                    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
                        
                        <!-- Card 1: Spalla -->
                        <a href="#patologie-spalla" class="nav-trigger joint-card p-8 rounded-3xl group" data-target="patologie-spalla">
                            <div class="w-12 h-12 rounded-2xl bg-caldo-tealLight text-caldo-teal flex items-center justify-center mb-6 group-hover:bg-caldo-teal group-hover:text-white transition-colors">
                                <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <circle cx="12" cy="12" r="9"/>
                                    <path d="M12 7v5l3 3"/>
                                </svg>
                            </div>
                            <h3 class="text-xl font-serif font-semibold text-caldo-text group-hover:text-caldo-teal transition-colors mb-2">Chirurgia della Spalla</h3>
                            <p class="text-xs text-caldo-muted leading-relaxed mb-6">Cuffia dei rotatori, instabilità articolare, riparazione Bankart, protesi anatomiche e inverse.</p>
                            <span class="text-xs font-bold text-caldo-teal inline-flex items-center gap-1 group-hover:translate-x-1 transition-transform">
                                Scopri trattamenti spalla →
                            </span>
                        </a>

                        <!-- Card 2: Gomito -->
                        <a href="#patologie-gomito" class="nav-trigger joint-card p-8 rounded-3xl group" data-target="patologie-gomito">
                            <div class="w-12 h-12 rounded-2xl bg-caldo-coralLight text-caldo-coral flex items-center justify-center mb-6 group-hover:bg-caldo-coral group-hover:text-white transition-colors">
                                <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M18 10h-4a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h4a2 2 0 0 0 2-2v-8a2 2 0 0 0-2-2Z"/>
                                    <path d="M6 4h4a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2Z"/>
                                </svg>
                            </div>
                            <h3 class="text-xl font-serif font-semibold text-caldo-text group-hover:text-caldo-teal transition-colors mb-2">Gomito e Traumi</h3>
                            <p class="text-xs text-caldo-muted leading-relaxed mb-6">Epicondilite resistente (gomito del tennista), fratture capitello radiale, bicipite distale.</p>
                            <span class="text-xs font-bold text-caldo-coral inline-flex items-center gap-1 group-hover:translate-x-1 transition-transform">
                                Scopri trattamenti gomito →
                            </span>
                        </a>

                        <!-- Card 3: Mano e Polso -->
                        <a href="#patologie-mano" class="nav-trigger joint-card p-8 rounded-3xl group" data-target="patologie-mano">
                            <div class="w-12 h-12 rounded-2xl bg-caldo-salviaLight text-caldo-salvia flex items-center justify-center mb-6 group-hover:bg-caldo-salvia group-hover:text-white transition-colors">
                                <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M18 11V6a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v0"/>
                                    <path d="M14 10V4a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v2"/>
                                    <path d="M10 10.5V6a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v8"/>
                                    <path d="M18 8a2 2 0 1 1 4 0v6a8 8 0 0 1-8 8h-2c-2.8 0-4.5-.86-5.99-2.34l-3.6-3.6a2 2 0 0 1 2.83-2.82L7 15"/>
                                </svg>
                            </div>
                            <h3 class="text-xl font-serif font-semibold text-caldo-text group-hover:text-caldo-teal transition-colors mb-2">Mano e Polso</h3>
                            <p class="text-xs text-caldo-muted leading-relaxed mb-6">Tunnel carpale, dito a scatto, rizoartrosi pollice, microchirurgia e cisti tendinee.</p>
                            <span class="text-xs font-bold text-caldo-salvia inline-flex items-center gap-1 group-hover:translate-x-1 transition-transform">
                                Scopri mano e polso →
                            </span>
                        </a>

                        <!-- Card 4: Sport -->
                        <a href="#patologie-traumatologia-sportiva" class="nav-trigger joint-card p-8 rounded-3xl group" data-target="patologie-traumatologia-sportiva">
                            <div class="w-12 h-12 rounded-2xl bg-caldo-goldLight text-caldo-gold flex items-center justify-center mb-6 group-hover:bg-caldo-gold group-hover:text-white transition-colors">
                                <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/>
                                    <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/>
                                    <path d="M4 22h16"/>
                                    <path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"/>
                                    <path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"/>
                                    <path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"/>
                                </svg>
                            </div>
                            <h3 class="text-xl font-serif font-semibold text-caldo-text group-hover:text-caldo-teal transition-colors mb-2">Traumatologia Sportiva</h3>
                            <p class="text-xs text-caldo-muted leading-relaxed mb-6">Atleti professionisti e amatoriali: lussazioni da impatto, lesioni legamentose, return-to-play rapido.</p>
                            <span class="text-xs font-bold text-caldo-gold inline-flex items-center gap-1 group-hover:translate-x-1 transition-transform">
                                Percorso sportivo →
                            </span>
                        </a>

                        <!-- Card 5: Artroscopia -->
                        <a href="#patologie-artroscopia" class="nav-trigger joint-card p-8 rounded-3xl group" data-target="patologie-artroscopia">
                            <div class="w-12 h-12 rounded-2xl bg-caldo-tealLight text-caldo-teal flex items-center justify-center mb-6 group-hover:bg-caldo-teal group-hover:text-white transition-colors">
                                <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <circle cx="12" cy="12" r="3"/>
                                    <path d="M3 7V5a2 2 0 0 1 2-2h2M17 3h2a2 2 0 0 1 2 2v2M21 17v2a2 2 0 0 1-2 2h-2M7 21H5a2 2 0 0 1-2-2v-2"/>
                                </svg>
                            </div>
                            <h3 class="text-xl font-serif font-semibold text-caldo-text group-hover:text-caldo-teal transition-colors mb-2">Chirurgia Artroscopica</h3>
                            <p class="text-xs text-caldo-muted leading-relaxed mb-6">Metodologia video-guidata in alta definizione: precisione millimetrica all'interno dell'articolazione.</p>
                            <span class="text-xs font-bold text-caldo-teal inline-flex items-center gap-1 group-hover:translate-x-1 transition-transform">
                                Il metodo artroscopico →
                            </span>
                        </a>

                        <!-- Card 6: Ecografia -->
                        <a href="#patologie-ecografia-muscoloscheletrica" class="nav-trigger joint-card p-8 rounded-3xl group" data-target="patologie-ecografia-muscoloscheletrica">
                            <div class="w-12 h-12 rounded-2xl bg-caldo-coralLight text-caldo-coral flex items-center justify-center mb-6 group-hover:bg-caldo-coral group-hover:text-white transition-colors">
                                <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M2 12h5l3 8 4-16 3 8h5"/>
                                </svg>
                            </div>
                            <h3 class="text-xl font-serif font-semibold text-caldo-text group-hover:text-caldo-teal transition-colors mb-2">Ecografia Muscoloscheletrica</h3>
                            <p class="text-xs text-caldo-muted leading-relaxed mb-6">Valutazione dinamica in ambulatorio e infiltrazioni eco-guidate con acido ialuronico.</p>
                            <span class="text-xs font-bold text-caldo-coral inline-flex items-center gap-1 group-hover:translate-x-1 transition-transform">
                                Diagnostica SIUMB →
                            </span>
                        </a>

                    </div>
                </div>
            </div>

            <!-- ========================================================
                 SEZIONE 5: DOVE RICEVO (MAPPA CALDA DELLE SEDI)
                 ======================================================== -->
            <div class="py-24 px-6 max-w-7xl mx-auto">
                <div class="bg-gradient-to-br from-caldo-teal to-[#063339] text-white p-10 md:p-16 rounded-3xl shadow-warm-lg">
                    <div class="grid lg:grid-cols-12 gap-10 items-center">
                        <div class="lg:col-span-7 space-y-6">
                            <span class="inline-flex items-center gap-2 bg-white/10 text-white text-xs font-semibold px-4 py-1.5 rounded-full border border-white/20">
                                <svg class="w-4 h-4 text-caldo-coral" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/>
                                    <circle cx="12" cy="10" r="3"/>
                                </svg>
                                <span>Presenza Capillare in Toscana</span>
                            </span>
                            
                            <h2 class="text-3xl sm:text-5xl font-serif text-white leading-tight">
                                Vicini al paziente tra Valdera, Empolese e Pisa.
                            </h2>
                            <p class="text-white/80 text-base leading-relaxed max-w-xl">
                                Tutti gli interventi e i ricoveri ospedalieri si tengono all'Ospedale CESAT di Fucecchio. Le prime visite e i controlli avvengono nei 4 ambulatori territoriali comodamente accessibili.
                            </p>

                            <div class="flex flex-wrap gap-4 pt-2">
                                <a href="#sedi" class="nav-trigger btn-warm-coral px-6 py-3.5 text-xs font-bold" data-target="sedi">
                                    Vedi tutte le sedi e gli orari
                                </a>
                                <a href="tel:+393484331733" class="inline-flex items-center gap-2 px-6 py-3.5 rounded-full bg-white/10 hover:bg-white/20 text-white text-xs font-bold border border-white/20 transition-all">
                                    <span>Chiama la Segreteria</span>
                                    <span>→</span>
                                </a>
                            </div>
                        </div>

                        <!-- Card Riassuntiva Sedi -->
                        <div class="lg:col-span-5 bg-white text-caldo-text p-6 md:p-8 rounded-2xl shadow-warm-md space-y-4">
                            <h4 class="font-serif text-xl font-semibold text-caldo-teal">Ambulatorio di Riferimento</h4>
                            <div class="space-y-3 text-xs">
                                <div class="flex items-start gap-3 p-3 rounded-xl bg-caldo-bg border border-caldo-border">
                                    <div class="w-8 h-8 rounded-lg bg-caldo-teal text-white flex items-center justify-center flex-shrink-0 font-bold">1</div>
                                    <div>
                                        <strong class="block text-caldo-text text-sm">Fucecchio · Studi San Pietro</strong>
                                        <span class="text-caldo-muted">Piazza Lavagnini 6 (Accanto all'Ospedale CESAT)</span>
                                    </div>
                                </div>
                                <div class="flex items-start gap-3 p-3 rounded-xl bg-caldo-bg border border-caldo-border">
                                    <div class="w-8 h-8 rounded-lg bg-caldo-coral text-white flex items-center justify-center flex-shrink-0 font-bold">2</div>
                                    <div>
                                        <strong class="block text-caldo-text text-sm">Peccioli · Polo San Verano</strong>
                                        <span class="text-caldo-muted">Località San Verano (Alta Valdera)</span>
                                    </div>
                                </div>
                                <div class="flex items-start gap-3 p-3 rounded-xl bg-caldo-bg border border-caldo-border">
                                    <div class="w-8 h-8 rounded-lg bg-caldo-salvia text-white flex items-center justify-center flex-shrink-0 font-bold">3</div>
                                    <div>
                                        <strong class="block text-caldo-text text-sm">Pisa & Fornacette</strong>
                                        <span class="text-caldo-muted">Athletica Pisa e Centro Fisiomed</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </section>

        <!-- ========================================================
             VISTA 2: CHI SONO (PROFILO UMANO, FORMAZIONE, PASSIONE)
             ======================================================== -->
        <section id="view-chi-sono" class="page-view max-w-6xl mx-auto px-6 py-16">
            
            <a href="#home" class="nav-trigger inline-flex items-center gap-2 text-xs font-bold text-caldo-teal hover:text-caldo-coral mb-8 transition-colors" data-target="home">
                <span>← Torna alla Home</span>
            </a>

            <!-- Header Chi Sono -->
            <div class="max-w-3xl mb-16 space-y-4">
                <span class="text-xs font-bold uppercase tracking-wider text-caldo-teal bg-caldo-tealLight px-3.5 py-1.5 rounded-full inline-block">
                    Profilo Professionale & Umano
                </span>
                <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text leading-tight">
                    Chirurgia di precisione,<br>
                    <span class="italic text-caldo-teal font-normal">dedizione alla persona.</span>
                </h1>
                <p class="text-lg text-caldo-muted font-light leading-relaxed">
                    «Operare bene è fondamentale, ma spiegare con chiarezza al paziente perché si interviene — o perché è preferibile attendere — è la parte più importante del mio lavoro.»
                </p>
            </div>

            <div class="grid lg:grid-cols-12 gap-12 items-start">
                
                <!-- Colonna Foto e Badge -->
                <div class="lg:col-span-5 space-y-6">
                    <div class="bg-white p-4 rounded-3xl border border-caldo-border shadow-warm-md">
                        <div class="aspect-[3/4] rounded-2xl overflow-hidden bg-caldo-tealLight mb-4">
                            <img src="https://images.unsplash.com/photo-1622253692010-333f2da6031d?q=80&w=800&auto=format&fit=crop" 
                                 alt="Dott. Michele Novi" 
                                 class="w-full h-full object-cover">
                        </div>
                        <div class="p-2 space-y-1">
                            <h3 class="text-lg font-bold text-caldo-text">Dott. Michele Novi</h3>
                            <p class="text-xs text-caldo-muted">Dirigente Medico Ortopedico · CESAT Fucecchio</p>
                            <p class="text-xs text-caldo-teal font-semibold">Iscritto all'Ordine dei Medici di Pisa n. 5988</p>
                        </div>
                    </div>

                    <!-- Scheda "Due Tempi" con Colore -->
                    <div class="bg-caldo-coralLight/60 p-6 rounded-3xl border border-caldo-coral/20 space-y-3">
                        <span class="text-xs font-bold text-caldo-coral uppercase tracking-wider block">Due Anime, Una Sola Visione</span>
                        <p class="text-xs text-caldo-muted leading-relaxed">
                            <strong>La Sala di Volume:</strong> Al CESAT di Fucecchio affronto quotidianamente interventi complessi di protesi e ricostruzione con casistiche di alto livello.
                        </p>
                        <p class="text-xs text-caldo-muted leading-relaxed">
                            <strong>Il Territorio:</strong> Negli ambulatori di paese ritrovo il rapporto umano diretto, la visita accurata e il follow-up costante con le famiglie.
                        </p>
                    </div>
                </div>

                <!-- Bio e Tappe Formative -->
                <div class="lg:col-span-7 space-y-10">
                    
                    <div class="space-y-6 text-base text-caldo-muted font-light leading-relaxed">
                        <p>
                            Mi sono formato presso l'<strong>Università di Pisa</strong>, dove ho conseguito la Laurea in Medicina e Chirurgia e successivamente la Specializzazione in Ortopedia e Traumatologia con il massimo dei voti e lode, crescendo nella scuola del Prof. Porcellini e a stretto contatto con il Dott. Nicoletti.
                        </p>
                        <p>
                            Credo fermamente che un chirurgo debba confrontarsi con il panorama internazionale. Per questo ho trascorso periodi di formazione avanzata all'estero, in particolare presso il prestigioso <strong>Harborview Medical Center di Seattle (USA)</strong>, centro di riferimento mondiale per la traumatologia complessa e la microchirurgia dell'arto superiore.
                        </p>
                    </div>

                    <!-- Timeline Formativa Accogliente -->
                    <div class="border-t border-caldo-border pt-8 space-y-6">
                        <h4 class="text-xl font-serif text-caldo-text font-semibold">Tappe Principali del Percorso</h4>

                        <div class="space-y-4">
                            <div class="flex items-start gap-4 p-4 rounded-2xl bg-white border border-caldo-border shadow-warm-sm">
                                <div class="w-10 h-10 rounded-xl bg-caldo-tealLight text-caldo-teal flex items-center justify-center font-bold flex-shrink-0">
                                    🏥
                                </div>
                                <div>
                                    <span class="text-xs font-bold text-caldo-teal block">2020 – Oggi</span>
                                    <strong class="text-sm text-caldo-text block">Dirigente Medico · Ospedale CESAT di Fucecchio</strong>
                                    <p class="text-xs text-caldo-muted mt-0.5">Centro regionale di eccellenza per le sostituzioni articolari e chirurgia artroscopica.</p>
                                </div>
                            </div>

                            <div class="flex items-start gap-4 p-4 rounded-2xl bg-white border border-caldo-border shadow-warm-sm">
                                <div class="w-10 h-10 rounded-xl bg-caldo-coralLight text-caldo-coral flex items-center justify-center font-bold flex-shrink-0">
                                    🇺🇸
                                </div>
                                <div>
                                    <span class="text-xs font-bold text-caldo-coral block">Fellowship Internazionale</span>
                                    <strong class="text-sm text-caldo-text block">Harborview Medical Center · Seattle (USA)</strong>
                                    <p class="text-xs text-caldo-muted mt-0.5">Focus su traumatologia ad alta energia e ricostruzioni complesse dei nervi periferici.</p>
                                </div>
                            </div>

                            <div class="flex items-start gap-4 p-4 rounded-2xl bg-white border border-caldo-border shadow-warm-sm">
                                <div class="w-10 h-10 rounded-xl bg-caldo-salviaLight text-caldo-salvia flex items-center justify-center font-bold flex-shrink-0">
                                    🔬
                                </div>
                                <div>
                                    <span class="text-xs font-bold text-caldo-salvia block">Certificazione SIUMB</span>
                                    <strong class="text-sm text-caldo-text block">Diploma Nazionale in Ecografia Muscoloscheletrica</strong>
                                    <p class="text-xs text-caldo-muted mt-0.5">Diagnostica dinamica in studio e precisione per le infiltrazioni eco-guidate.</p>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>

            </div>

        </section>

        <!-- ========================================================
             VISTA 3: PATOLOGIE (TUTTE LE 6 AREE CON SCHEDE COMPLETE)
             ======================================================== -->
        <section id="view-patologie" class="page-view max-w-7xl mx-auto px-6 py-16">
            
            <a href="#home" class="nav-trigger inline-flex items-center gap-2 text-xs font-bold text-caldo-teal hover:text-caldo-coral mb-8 transition-colors" data-target="home">
                <span>← Torna alla Home</span>
            </a>

            <div class="max-w-3xl mb-16 space-y-4">
                <span class="text-xs font-bold uppercase tracking-wider text-caldo-teal bg-caldo-tealLight px-3.5 py-1.5 rounded-full inline-block">
                    Aree di Trattamento
                </span>
                <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text leading-tight">
                    Cosa curo: diagnosi chiara e percorsi dedicati.
                </h1>
                <p class="text-base text-caldo-muted font-light leading-relaxed">
                    Dall'indicazione conservativa alla chirurgia avanzata, ogni articolazione dell'arto superiore viene trattata con l'obiettivo del massimo recupero funzionale.
                </p>
            </div>

            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                
                <!-- 1. SPALLA -->
                <div class="bg-white p-8 rounded-3xl border border-caldo-border shadow-warm-md flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-caldo-tealLight text-caldo-teal flex items-center justify-center mb-6">
                            <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <circle cx="12" cy="12" r="9"/>
                                <path d="M12 7v5l3 3"/>
                            </svg>
                        </div>
                        <h3 class="text-2xl font-serif text-caldo-text mb-3">Chirurgia della Spalla</h3>
                        <p class="text-xs text-caldo-muted leading-relaxed mb-6">
                            È il nucleo principale della mia attività: rotture della cuffia dei rotatori, instabilità articolare da lussazione (Bankart, Remplissage) e protesi anatomica o inversa.
                        </p>
                    </div>
                    <a href="#patologie-spalla" class="nav-trigger btn-warm-primary !py-2.5 !px-5 text-xs justify-center" data-target="patologie-spalla">
                        Scheda approfondita spalla →
                    </a>
                </div>

                <!-- 2. GOMITO -->
                <div class="bg-white p-8 rounded-3xl border border-caldo-border shadow-warm-md flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-caldo-coralLight text-caldo-coral flex items-center justify-center mb-6">
                            <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M18 10h-4a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h4a2 2 0 0 0 2-2v-8a2 2 0 0 0-2-2Z"/>
                                <path d="M6 4h4a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2Z"/>
                            </svg>
                        </div>
                        <h3 class="text-2xl font-serif text-caldo-text mb-3">Gomito e Traumatologia</h3>
                        <p class="text-xs text-caldo-muted leading-relaxed mb-6">
                            Trattamento di rigidità, lesioni del tendine distale del bicipite, instabilità complesse ed epicondiliti resistenti alle terapie standard.
                        </p>
                    </div>
                    <a href="#patologie-gomito" class="nav-trigger btn-warm-secondary !py-2.5 !px-5 text-xs justify-center" data-target="patologie-gomito">
                        Scheda gomito →
                    </a>
                </div>

                <!-- 3. MANO E POLSO -->
                <div class="bg-white p-8 rounded-3xl border border-caldo-border shadow-warm-md flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-caldo-salviaLight text-caldo-salvia flex items-center justify-center mb-6">
                            <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M18 11V6a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v0"/>
                                <path d="M14 10V4a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v2"/>
                                <path d="M10 10.5V6a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v8"/>
                            </svg>
                        </div>
                        <h3 class="text-2xl font-serif text-caldo-text mb-3">Mano e Polso</h3>
                        <p class="text-xs text-caldo-muted leading-relaxed mb-6">
                            Sindrome del tunnel carpale con recupero rapido, dito a scatto, morbo di De Quervain e rizoartrosi con protesi o tecniche conservative.
                        </p>
                    </div>
                    <a href="#patologie-mano" class="nav-trigger btn-warm-secondary !py-2.5 !px-5 text-xs justify-center" data-target="patologie-mano">
                        Scheda mano e polso →
                    </a>
                </div>

                <!-- 4. SPORT -->
                <div class="bg-white p-8 rounded-3xl border border-caldo-border shadow-warm-md flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-caldo-goldLight text-caldo-gold flex items-center justify-center mb-6">
                            <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/>
                                <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/>
                                <path d="M4 22h16"/>
                            </svg>
                        </div>
                        <h3 class="text-2xl font-serif text-caldo-text mb-3">Traumatologia Sportiva</h3>
                        <p class="text-xs text-caldo-muted leading-relaxed mb-6">
                            Assistenza per sportivi agonistici e amatoriali: lussazioni acromion-claveari, sovraccarico funzionale del tennista, scalatore e motociclista.
                        </p>
                    </div>
                    <a href="#patologie-traumatologia-sportiva" class="nav-trigger btn-warm-secondary !py-2.5 !px-5 text-xs justify-center" data-target="patologie-traumatologia-sportiva">
                        Scheda sport →
                    </a>
                </div>

                <!-- 5. ARTROSCOPIA -->
                <div class="bg-white p-8 rounded-3xl border border-caldo-border shadow-warm-md flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-caldo-tealLight text-caldo-teal flex items-center justify-center mb-6">
                            <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <circle cx="12" cy="12" r="3"/>
                                <path d="M3 7V5a2 2 0 0 1 2-2h2M17 3h2a2 2 0 0 1 2 2v2M21 17v2a2 2 0 0 1-2 2h-2M7 21H5a2 2 0 0 1-2-2v-2"/>
                            </svg>
                        </div>
                        <h3 class="text-2xl font-serif text-caldo-text mb-3">Chirurgia Artroscopica</h3>
                        <p class="text-xs text-caldo-muted leading-relaxed mb-6">
                            La tecnica di riferimento: intervenire all'interno dell'articolazione sotto visione ottica diretta, senza dissezionare le strutture sane.
                        </p>
                    </div>
                    <a href="#patologie-artroscopia" class="nav-trigger btn-warm-secondary !py-2.5 !px-5 text-xs justify-center" data-target="patologie-artroscopia">
                        Scheda artroscopia →
                    </a>
                </div>

                <!-- 6. ECOGRAFIA -->
                <div class="bg-white p-8 rounded-3xl border border-caldo-border shadow-warm-md flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-caldo-coralLight text-caldo-coral flex items-center justify-center mb-6">
                            <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M2 12h5l3 8 4-16 3 8h5"/>
                            </svg>
                        </div>
                        <h3 class="text-2xl font-serif text-caldo-text mb-3">Ecografia Muscoloscheletrica</h3>
                        <p class="text-xs text-caldo-muted leading-relaxed mb-6">
                            L'ecografo in ambulatorio: diagnosi dinamica immediata dei tendini in movimento e precisione millimetrica per le infiltrazioni.
                        </p>
                    </div>
                    <a href="#patologie-ecografia-muscoloscheletrica" class="nav-trigger btn-warm-secondary !py-2.5 !px-5 text-xs justify-center" data-target="patologie-ecografia-muscoloscheletrica">
                        Scheda ecografia →
                    </a>
                </div>

            </div>

        </section>

        <!-- SOTTO-VISTA DETTAGLIO: SPALLA -->
        <section id="view-patologie-spalla" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-bold text-caldo-teal hover:text-caldo-coral mb-8 transition-colors" data-target="patologie">
                <span>← Torna a tutte le patologie</span>
            </a>
            
            <span class="text-xs font-bold uppercase tracking-wider text-caldo-teal bg-caldo-tealLight px-3 py-1 rounded-full inline-block mb-3">
                Focus Specialistico
            </span>
            <h1 class="text-4xl sm:text-5xl font-serif text-caldo-text mb-6">Chirurgia della spalla.</h1>
            
            <div class="space-y-6 text-base text-caldo-muted leading-relaxed font-light">
                <p>
                    La spalla è un miracolo di mobilità, ma la sua stabilità dipende interamente dalla perfetta armonia tra osso, tendini e legamenti. La diagnosi accurata è il primo passo: differenziare un'infiammazione reversibile da una lesione tendinea strutturata evita interventi non necessari o ritardi terapeutici.
                </p>

                <div class="my-8 p-6 bg-white rounded-2xl border border-caldo-border space-y-4">
                    <h3 class="text-xl font-serif font-bold text-caldo-text">Principali patologie trattate</h3>
                    <ul class="space-y-3 text-sm">
                        <li class="flex items-start gap-3">
                            <span class="w-5 h-5 rounded-full bg-caldo-tealLight text-caldo-teal flex items-center justify-center font-bold text-xs flex-shrink-0">✓</span>
                            <span><strong>Lesioni della Cuffia dei Rotatori:</strong> riparazione biologica artroscopica con ancore di sutura riassorbibili.</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <span class="w-5 h-5 rounded-full bg-caldo-coralLight text-caldo-coral flex items-center justify-center font-bold text-xs flex-shrink-0">✓</span>
                            <span><strong>Instabilità e Lussazioni Recidivanti:</strong> ricostruzione del cercine di Bankart e procedura di Remplissage.</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <span class="w-5 h-5 rounded-full bg-caldo-salviaLight text-caldo-salvia flex items-center justify-center font-bold text-xs flex-shrink-0">✓</span>
                            <span><strong>Artroplastica e Protesi Inversa:</strong> per artrosi avanzata o rotture irreparabili, restituendo l'elevazione del braccio.</span>
                        </li>
                    </ul>
                </div>
            </div>

            <div class="pt-8 border-t border-caldo-border flex justify-between items-center">
                <span class="text-xs text-caldo-muted font-medium">Hai dolore alla spalla?</span>
                <a href="#contatti" class="nav-trigger btn-warm-coral px-6 py-3 text-xs font-bold" data-target="contatti">
                    Prenota un controllo per la spalla
                </a>
            </div>
        </section>

        <!-- SOTTO-VISTE SINTETICHE: GOMITO, MANO, SPORT, ARTROSCOPIA, ECOGRAFIA -->
        <section id="view-patologie-gomito" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-bold text-caldo-teal hover:text-caldo-coral mb-8" data-target="patologie">← Indietro</a>
            <h1 class="text-4xl font-serif text-caldo-text mb-4">Gomito e Traumi</h1>
            <p class="text-caldo-muted leading-relaxed">Trattamento di rigidità, epicondilite resistente e fratture complesse.</p>
        </section>
        <section id="view-patologie-mano" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-bold text-caldo-teal hover:text-caldo-coral mb-8" data-target="patologie">← Indietro</a>
            <h1 class="text-4xl font-serif text-caldo-text mb-4">Mano e Polso</h1>
            <p class="text-caldo-muted leading-relaxed">Tunnel carpale, dito a scatto, de Quervain e rizoartrosi.</p>
        </section>
        <section id="view-patologie-traumatologia-sportiva" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-bold text-caldo-teal hover:text-caldo-coral mb-8" data-target="patologie">← Indietro</a>
            <h1 class="text-4xl font-serif text-caldo-text mb-4">Traumatologia Sportiva</h1>
            <p class="text-caldo-muted leading-relaxed">Recupero del gesto atletico e prevenzione recidive negli sportivi.</p>
        </section>
        <section id="view-patologie-artroscopia" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-bold text-caldo-teal hover:text-caldo-coral mb-8" data-target="patologie">← Indietro</a>
            <h1 class="text-4xl font-serif text-caldo-text mb-4">Chirurgia Artroscopica</h1>
            <p class="text-caldo-muted leading-relaxed">Il metodo mini-invasivo a visione ottica diretta.</p>
        </section>
        <section id="view-patologie-ecografia-muscoloscheletrica" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-bold text-caldo-teal hover:text-caldo-coral mb-8" data-target="patologie">← Indietro</a>
            <h1 class="text-4xl font-serif text-caldo-text mb-4">Ecografia Muscoloscheletrica</h1>
            <p class="text-caldo-muted leading-relaxed">Diagnosi dinamica immediata con certificazione SIUMB.</p>
        </section>

        <!-- ========================================================
             VISTA 4: DOVE RICEVO (LE SEDI CON COLORI, ICONE E DETTAGLI)
             ======================================================== -->
        <section id="view-sedi" class="page-view max-w-7xl mx-auto px-6 py-16">
            
            <a href="#home" class="nav-trigger inline-flex items-center gap-2 text-xs font-bold text-caldo-teal hover:text-caldo-coral mb-8 transition-colors" data-target="home">
                <span>← Torna alla Home</span>
            </a>

            <div class="max-w-3xl mb-16 space-y-4">
                <span class="text-xs font-bold uppercase tracking-wider text-caldo-teal bg-caldo-tealLight px-3.5 py-1.5 rounded-full inline-block">
                    Punti di Visita e Ospedale
                </span>
                <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text leading-tight">
                    Dove ricevo: le strutture in Toscana.
                </h1>
                <p class="text-base text-caldo-muted font-light leading-relaxed">
                    Un'unica segreteria per prenotare visite e infiltrazioni nella sede più comoda vicino a te, con gli interventi chirurgici concentrati al CESAT.
                </p>
            </div>

            <div class="grid md:grid-cols-2 gap-8">
                
                <!-- SEDE 1: OSPEDALE CESAT FUCECCHIO -->
                <div class="bg-white p-8 md:p-10 rounded-3xl border border-caldo-border shadow-warm-md space-y-6">
                    <div class="flex justify-between items-start">
                        <span class="bg-caldo-teal text-white text-[11px] font-bold uppercase tracking-wider px-3.5 py-1.5 rounded-full">
                            Polo Chirurgico Ospedaliero
                        </span>
                        <span class="text-xs font-semibold text-caldo-muted">Fucecchio (FI)</span>
                    </div>

                    <div>
                        <h3 class="text-2xl font-serif text-caldo-text font-semibold">Ospedale CESAT · San Pietro Igneo</h3>
                        <p class="text-xs text-caldo-teal font-medium mt-1">Centro di Eccellenza Sostituzioni Articolari Toscana</p>
                    </div>

                    <div class="space-y-3 text-xs text-caldo-muted border-t border-caldo-border pt-4">
                        <div class="flex items-center gap-2.5">
                            <span class="text-caldo-teal font-bold">📍 Indirizzo:</span>
                            <span>Piazza Lavagnini, 5 · 50054 Fucecchio (FI)</span>
                        </div>
                        <div class="flex items-center gap-2.5">
                            <span class="text-caldo-teal font-bold">🏥 Attività:</span>
                            <span>Ricoveri chirurgici, protesi spalla/arto, interventi artroscopici.</span>
                        </div>
                    </div>

                    <div class="pt-4 border-t border-caldo-border flex justify-between items-center">
                        <span class="text-xs text-caldo-muted">Chirurgia Ospedaliera</span>
                        <a href="tel:+393484331733" class="btn-warm-secondary !py-2 !px-4 text-xs font-bold">Informazioni Ricoveri</a>
                    </div>
                </div>

                <!-- SEDE 2: STUDI SAN PIETRO (AMBULATORIO LIBERA PROFESSIONE) -->
                <div class="bg-white p-8 md:p-10 rounded-3xl border border-caldo-border shadow-warm-md space-y-6">
                    <div class="flex justify-between items-start">
                        <span class="bg-caldo-coral text-white text-[11px] font-bold uppercase tracking-wider px-3.5 py-1.5 rounded-full">
                            Ambulatorio Principale
                        </span>
                        <span class="text-xs font-semibold text-caldo-muted">Fucecchio (FI)</span>
                    </div>

                    <div>
                        <h3 class="text-2xl font-serif text-caldo-text font-semibold">Studi Medici San Pietro</h3>
                        <p class="text-xs text-caldo-muted mt-1">Prime visite ortopediche, ecografie di controllo e infiltrazioni</p>
                    </div>

                    <div class="space-y-3 text-xs text-caldo-muted border-t border-caldo-border pt-4">
                        <div class="flex items-center gap-2.5">
                            <span class="text-caldo-coral font-bold">📍 Indirizzo:</span>
                            <span>Piazza Lavagnini, 6 · Fucecchio (accanto all'ospedale)</span>
                        </div>
                        <div class="flex items-center gap-2.5">
                            <span class="text-caldo-coral font-bold">🕒 Orari:</span>
                            <span>Su appuntamento (Lunedì – Giovedì)</span>
                        </div>
                    </div>

                    <div class="pt-4 border-t border-caldo-border flex justify-between items-center">
                        <span class="text-xs text-caldo-muted">Prenotazione diretta</span>
                        <a href="#contatti" class="nav-trigger btn-warm-coral !py-2 !px-4 text-xs font-bold" data-target="contatti">Prenota a Fucecchio</a>
                    </div>
                </div>

                <!-- SEDE 3: PECCIOLI (VALDERA) -->
                <div class="bg-white p-8 md:p-10 rounded-3xl border border-caldo-border shadow-warm-md space-y-6">
                    <div class="flex justify-between items-start">
                        <span class="bg-caldo-salvia text-white text-[11px] font-bold uppercase tracking-wider px-3.5 py-1.5 rounded-full">
                            Alta Valdera
                        </span>
                        <span class="text-xs font-semibold text-caldo-muted">Peccioli (PI)</span>
                    </div>

                    <div>
                        <h3 class="text-2xl font-serif text-caldo-text font-semibold">Polo San Verano</h3>
                        <p class="text-xs text-caldo-muted mt-1">Visite specialistiche e screening articolare per i residenti in Valdera</p>
                    </div>

                    <div class="space-y-3 text-xs text-caldo-muted border-t border-caldo-border pt-4">
                        <div class="flex items-center gap-2.5">
                            <span class="text-caldo-salvia font-bold">📍 Indirizzo:</span>
                            <span>Località San Verano · Peccioli (PI)</span>
                        </div>
                        <div class="flex items-center gap-2.5">
                            <span class="text-caldo-salvia font-bold">🅿️ Servizi:</span>
                            <span>Comodo parcheggio e accessibilità senza barriere</span>
                        </div>
                    </div>

                    <div class="pt-4 border-t border-caldo-border flex justify-between items-center">
                        <span class="text-xs text-caldo-muted">Territorio Valdera</span>
                        <a href="#contatti" class="nav-trigger btn-warm-secondary !py-2 !px-4 text-xs font-bold" data-target="contatti">Prenota a Peccioli</a>
                    </div>
                </div>

                <!-- SEDE 4: PISA & FORNACETTE -->
                <div class="bg-white p-8 md:p-10 rounded-3xl border border-caldo-border shadow-warm-md space-y-6">
                    <div class="flex justify-between items-start">
                        <span class="bg-caldo-gold text-white text-[11px] font-bold uppercase tracking-wider px-3.5 py-1.5 rounded-full">
                            Sport & Movimento
                        </span>
                        <span class="text-xs font-semibold text-caldo-muted">Pisa & Fornacette</span>
                    </div>

                    <div>
                        <h3 class="text-2xl font-serif text-caldo-text font-semibold">Athletica Pisa · Centro Fisiomed</h3>
                        <p class="text-xs text-caldo-muted mt-1">Valutazione atleti, traumi da sport e fisioterapia riabilitativa</p>
                    </div>

                    <div class="space-y-3 text-xs text-caldo-muted border-t border-caldo-border pt-4">
                        <div class="flex items-center gap-2.5">
                            <span class="text-caldo-gold font-bold">📍 Sedi:</span>
                            <span>Pisa centro e Fornacette (Calcinaia)</span>
                        </div>
                        <div class="flex items-center gap-2.5">
                            <span class="text-caldo-gold font-bold">🏃 Attività:</span>
                            <span>Test funzionali e ritorno allo sport agonistico</span>
                        </div>
                    </div>

                    <div class="pt-4 border-t border-caldo-border flex justify-between items-center">
                        <span class="text-xs text-caldo-muted">Ambulatorio Sportivo</span>
                        <a href="#contatti" class="nav-trigger btn-warm-secondary !py-2 !px-4 text-xs font-bold" data-target="contatti">Prenota a Pisa</a>
                    </div>
                </div>

            </div>

        </section>

        <!-- ========================================================
             VISTA 5: NOTE CLINICHE (IL QUADERNO RIVISITATO: CALDO, EDITORIALE)
             ======================================================== -->
        <section id="view-articoli" class="page-view max-w-5xl mx-auto px-6 py-16">
            
            <a href="#home" class="nav-trigger inline-flex items-center gap-2 text-xs font-bold text-caldo-teal hover:text-caldo-coral mb-8 transition-colors" data-target="home">
                <span>← Torna alla Home</span>
            </a>

            <div class="max-w-3xl mb-16 space-y-4">
                <span class="text-xs font-bold uppercase tracking-wider text-caldo-teal bg-caldo-tealLight px-3.5 py-1.5 rounded-full inline-block">
                    Divulgazione Scientifica
                </span>
                <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text leading-tight">
                    Note cliniche: la scienza spiegata semplice.
                </h1>
                <p class="text-base text-caldo-muted font-light leading-relaxed">
                    Nessun articolo acchiappa-click: solo approfondimenti derivati direttamente dagli studi e dai paper scientifici pubblicati con l'équipe del CESAT.
                </p>
            </div>

            <!-- Articolo in evidenza (Remplissage) -->
            <a href="#articoli-remplissage" class="nav-trigger block bg-white p-8 md:p-12 rounded-3xl border border-caldo-border shadow-warm-md hover:border-caldo-teal hover:shadow-warm-lg transition-all group" data-target="articoli-remplissage">
                <div class="flex items-center gap-3 mb-4">
                    <span class="bg-caldo-coralLight text-caldo-coral text-xs font-bold px-3 py-1 rounded-full">
                        Pubblicazione Scientifica
                    </span>
                    <span class="text-xs text-caldo-muted">Osteology 2022 · CESAT</span>
                </div>

                <h2 class="text-2xl sm:text-3xl font-serif text-caldo-text group-hover:text-caldo-teal transition-colors mb-4 leading-snug">
                    Il dubbio nel remplissage: conciliare stabilità e rotazione nella spalla dello sportivo.
                </h2>

                <p class="text-sm text-caldo-muted leading-relaxed mb-6 font-light">
                    Nelle lussazioni recidivanti con difetto osseo della testa omerale (Hill-Sachs), riempire la nicchia previene nuove uscite della spalla. I risultati a medio termine su atleti e mobilità residua.
                </p>

                <div class="flex items-center justify-between border-t border-caldo-border pt-4 text-xs">
                    <span class="font-medium text-caldo-text">Dott. Michele Novi et al.</span>
                    <span class="font-bold text-caldo-teal group-hover:translate-x-1 transition-transform inline-flex items-center gap-1">
                        Leggi la nota completa →
                    </span>
                </div>
            </a>

        </section>

        <!-- SOTTO-VISTA DETTAGLIO: ARTICOLO REMPLISSAGE -->
        <section id="view-articoli-remplissage" class="page-view max-w-3xl mx-auto px-6 py-16">
            <a href="#articoli" class="nav-trigger inline-flex items-center gap-2 text-xs font-bold text-caldo-teal hover:text-caldo-coral mb-8" data-target="articoli">
                ← Torna alle Note cliniche
            </a>

            <div class="flex items-center gap-3 text-xs text-caldo-muted mb-4">
                <span class="bg-caldo-tealLight text-caldo-teal font-bold px-3 py-1 rounded-full">Paper 2022</span>
                <span>DOI: 10.3390/osteology2040021</span>
            </div>

            <h1 class="text-3xl sm:text-5xl font-serif text-caldo-text leading-tight mb-8">
                Il dubbio nel remplissage: quando la stabilità rischia di sacrificare il movimento.
            </h1>

            <div class="space-y-6 text-base text-caldo-muted leading-relaxed font-light">
                <p class="text-lg text-caldo-text font-normal italic border-l-4 border-caldo-teal pl-4 bg-caldo-tealLight/30 py-3 rounded-r-xl">
                    «Il timore del chirurgo che affronta la lussazione di spalla è duplice: riparare troppo poco e rischiare una recidiva, o riparare troppo rigidamente e ridurre la rotazione esterna del braccio.»
                </p>

                <p>
                    Quando la testa omerale esce dalla propria sede naturale, l'impatto contro il margine anteriore della cavità glenoidea produce spesso una tipica intaccatura da compressione, nota come <strong>lesione di Hill-Sachs</strong>. Durante i movimenti di torsione del braccio, questa lesione può ingranare sul bordo osseo opposto, agendo come una vera e propria leva che scardina l'articolazione.
                </p>

                <h3 class="text-2xl font-serif text-caldo-text font-semibold pt-4">La tecnica: riempire per proteggere</h3>
                <p>
                    La procedura di <em>Remplissage</em> (dal verbo francese "riempire") consiste nell'ancorare parte della capsula posteriore e il tendine dell'infraspinato direttamente all'interno della lesione ossea. In questo modo il difetto viene escluso dalla camera articolare: la spalla non trova più lo scalino su cui incepparsi.
                </p>

                <p>
                    Nello studio condotto con i colleghi del CESAT su pazienti atleti, abbiamo verificato che la perdita di rotazione esterna è mediamente inferiore a 4 gradi: un valore impercettibile nella pratica sportiva, a fronte di un tasso di recidiva dell'instabilità completamente azzerato.
                </p>
            </div>

            <div class="mt-12 p-6 bg-white rounded-2xl border border-caldo-border flex justify-between items-center">
                <span class="text-xs text-caldo-muted font-medium">Vuoi una consulenza sulla stabilità della tua spalla?</span>
                <a href="#contatti" class="nav-trigger btn-warm-coral px-6 py-2.5 text-xs font-bold" data-target="contatti">
                    Contatta la segreteria
                </a>
            </div>
        </section>

        <!-- ========================================================
             VISTA 6: CONTATTI (CALDO, RASSICURANTE, ZERO STRESS)
             ======================================================== -->
        <section id="view-contatti" class="page-view max-w-6xl mx-auto px-6 py-16">
            
            <a href="#home" class="nav-trigger inline-flex items-center gap-2 text-xs font-bold text-caldo-teal hover:text-caldo-coral mb-8 transition-colors" data-target="home">
                <span>← Torna alla Home</span>
            </a>

            <div class="max-w-3xl mb-16 space-y-4">
                <span class="text-xs font-bold uppercase tracking-wider text-caldo-coral bg-caldo-coralLight px-3.5 py-1.5 rounded-full inline-block">
                    Contatto Diretto
                </span>
                <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text leading-tight">
                    Prenotazioni e Segreteria.
                </h1>
                <p class="text-base text-caldo-muted font-light leading-relaxed">
                    Siamo a disposizione per fissare la tua prima visita, un controllo post-operatorio o per fornirti informazioni sui ricoveri ospedalieri.
                </p>
            </div>

            <div class="grid lg:grid-cols-12 gap-12 items-start">
                
                <!-- Box Telefono e WhatsApp -->
                <div class="lg:col-span-5 space-y-6">
                    
                    <div class="bg-white p-8 rounded-3xl border border-caldo-border shadow-warm-md space-y-6">
                        <div class="flex items-center gap-3">
                            <div class="w-12 h-12 rounded-2xl bg-caldo-tealLight text-caldo-teal flex items-center justify-center">
                                <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
                                </svg>
                            </div>
                            <div>
                                <span class="text-xs text-caldo-muted block">Numero Segreteria Unificato</span>
                                <strong class="text-2xl sm:text-3xl text-caldo-teal font-bold tracking-tight">348 4331733</strong>
                            </div>
                        </div>

                        <div class="space-y-3 text-xs text-caldo-muted border-t border-caldo-border pt-4">
                            <div class="flex items-center gap-2">
                                <span class="font-bold text-caldo-text">🕒 Orari Chiamate:</span>
                                <span>Lunedì – Giovedì dalle 15:30 alle 17:30</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <span class="font-bold text-caldo-text">💬 Messaggi WhatsApp:</span>
                                <span>Attivo per richieste disponibilità appuntamento</span>
                            </div>
                        </div>

                        <!-- Bottone WhatsApp Diretto -->
                        <a href="https://wa.me/393484331733?text=Buongiorno%2C%20vorrei%20richiedere%20informazioni%20per%20una%20visita%20con%20il%20Dott.%20Novi" 
                           target="_blank" 
                           class="w-full inline-flex items-center justify-center gap-2 py-3 px-4 rounded-2xl bg-[#25D366] text-white font-bold text-xs shadow-warm-sm hover:opacity-90 transition-opacity">
                            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
                                <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.275.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.1.824z"/>
                            </svg>
                            <span>Scrivi su WhatsApp alla Segreteria</span>
                        </a>
                    </div>

                    <div class="bg-caldo-tealLight/50 p-6 rounded-3xl border border-caldo-teal/20 text-xs text-caldo-muted space-y-2">
                        <strong class="text-caldo-teal block font-semibold">Cosa indicare nel messaggio:</strong>
                        <p>Nome, cognome, la sede preferita (Fucecchio, Peccioli, Fornacette, Pisa) e una breve descrizione non clinica del motivo della visita (es. "dolore spalla destra").</p>
                    </div>

                </div>

                <!-- Modulo di Richiesta Caldo e Pulito -->
                <div class="lg:col-span-7 bg-white p-8 md:p-12 rounded-3xl border border-caldo-border shadow-warm-md">
                    
                    <div class="mb-8">
                        <h3 class="text-2xl font-serif text-caldo-text font-semibold">Invia una richiesta online</h3>
                        <p class="text-xs text-caldo-muted mt-1">Verrai ricontattato telefonicamente dalla segreteria entro 24 ore lavorative.</p>
                    </div>

                    <form onsubmit="event.preventDefault(); alert('Grazie! La segreteria del Dott. Novi ti ricontatterà a breve.');" class="space-y-6">
                        
                        <div class="grid sm:grid-cols-2 gap-6">
                            <div>
                                <label class="block text-xs font-bold text-caldo-text mb-2">Nome e Cognome *</label>
                                <input type="text" required class="w-full border border-caldo-border p-3.5 text-sm rounded-2xl bg-caldo-bg focus:outline-none focus:border-caldo-teal transition-colors" placeholder="Mario Rossi">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-caldo-text mb-2">Numero di Telefono *</label>
                                <input type="tel" required class="w-full border border-caldo-border p-3.5 text-sm rounded-2xl bg-caldo-bg focus:outline-none focus:border-caldo-teal transition-colors" placeholder="340 0000000">
                            </div>
                        </div>

                        <div class="grid sm:grid-cols-2 gap-6">
                            <div>
                                <label class="block text-xs font-bold text-caldo-text mb-2">Sede Desiderata</label>
                                <select class="w-full border border-caldo-border p-3.5 text-sm rounded-2xl bg-caldo-bg focus:outline-none focus:border-caldo-teal transition-colors">
                                    <option>Fucecchio (Studi San Pietro)</option>
                                    <option>Peccioli (Polo San Verano)</option>
                                    <option>Fornacette (Fisiomed)</option>
                                    <option>Pisa (Athletica)</option>
                                </select>
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-caldo-text mb-2">Articolazione Interessata</label>
                                <select class="w-full border border-caldo-border p-3.5 text-sm rounded-2xl bg-caldo-bg focus:outline-none focus:border-caldo-teal transition-colors">
                                    <option>Spalla</option>
                                    <option>Gomito</option>
                                    <option>Mano o Polso</option>
                                    <option>Traumatologia Sportiva</option>
                                </select>
                            </div>
                        </div>

                        <div>
                            <label class="block text-xs font-bold text-caldo-text mb-2">Note per la Segreteria (Facoltativo)</label>
                            <textarea rows="3" class="w-full border border-caldo-border p-3.5 text-sm rounded-2xl bg-caldo-bg focus:outline-none focus:border-caldo-teal transition-colors" placeholder="Indica eventuali preferenze di giorni o orari per essere ricontattato..."></textarea>
                        </div>

                        <div class="flex items-start gap-3">
                            <input type="checkbox" required id="privacy-check" class="mt-1 accent-caldo-teal">
                            <label for="privacy-check" class="text-xs text-caldo-muted leading-relaxed">
                                Acconsento al trattamento dei dati personali ai fini della prenotazione, ai sensi del Regolamento Europeo GDPR 679/2016.
                            </label>
                        </div>

                        <button type="submit" class="btn-warm-coral w-full justify-center !py-4 text-sm font-bold">
                            <span>Invia Richiesta di Appuntamento</span>
                            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                                <path d="M5 12h14M12 5l7 7-7 7"/>
                            </svg>
                        </button>

                    </form>

                </div>

            </div>

        </section>

    </main>

    <!-- ============================================================
         FOOTER ACCOGLIENTE E COMPLETO
         ============================================================ -->
    <footer class="bg-white border-t border-caldo-border mt-32 py-16 px-6 relative z-10">
        <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-10 text-sm">
            
            <div class="space-y-3">
                <div class="font-serif text-2xl text-caldo-text font-semibold">Dott. Michele Novi</div>
                <p class="text-xs text-caldo-muted leading-relaxed">
                    Chirurgo Ortopedico Traumatologo.<br>
                    Dirigente Medico Ospedale CESAT Fucecchio.<br>
                    Ordine dei Medici di Pisa n. 5988.
                </p>
            </div>

            <div class="space-y-2.5 text-xs">
                <strong class="text-caldo-text uppercase font-bold text-[11px] block mb-3">Navigazione</strong>
                <div><a href="#chi-sono" class="nav-trigger text-caldo-muted hover:text-caldo-teal" data-target="chi-sono">Chi sono</a></div>
                <div><a href="#patologie" class="nav-trigger text-caldo-muted hover:text-caldo-teal" data-target="patologie">Cosa curo (Patologie)</a></div>
                <div><a href="#sedi" class="nav-trigger text-caldo-muted hover:text-caldo-teal" data-target="sedi">Dove ricevo (Sedi)</a></div>
                <div><a href="#articoli" class="nav-trigger text-caldo-muted hover:text-caldo-teal" data-target="articoli">Note cliniche</a></div>
                <div><a href="#contatti" class="nav-trigger text-caldo-muted hover:text-caldo-teal" data-target="contatti">Contatti e Prenotazioni</a></div>
            </div>

            <div class="space-y-2.5 text-xs">
                <strong class="text-caldo-text uppercase font-bold text-[11px] block mb-3">Le Sedi Principali</strong>
                <p class="text-caldo-muted leading-relaxed">
                    <strong>CESAT Fucecchio:</strong> Ospedale San Pietro Igneo (Ricoveri)<br>
                    <strong>Studi San Pietro:</strong> Piazza Lavagnini 6, Fucecchio<br>
                    <strong>Valdera & Pisa:</strong> Peccioli, Fornacette, Pisa
                </p>
            </div>

            <div class="space-y-3 text-xs">
                <strong class="text-caldo-text uppercase font-bold text-[11px] block mb-3">Segreteria Unica</strong>
                <a href="tel:+393484331733" class="text-xl font-bold text-caldo-teal block">
                    348 4331733
                </a>
                <p class="text-caldo-muted text-[11px] leading-relaxed">
                    Chiamate: Lun – Gio 15:30 – 17:30.<br>
                    WhatsApp attivo tutti i giorni per disponibilità visite.
                </p>
            </div>

        </div>

        <div class="max-w-7xl mx-auto mt-12 pt-6 border-t border-caldo-border flex flex-col sm:flex-row justify-between items-center text-xs text-caldo-muted gap-4">
            <div>© 2026 Dott. Michele Novi · P. IVA in attribuzione</div>
            <div class="flex gap-6">
                <span class="hover:text-caldo-teal cursor-pointer">Privacy Policy</span>
                <span class="hover:text-caldo-teal cursor-pointer">Cookie Policy</span>
                <span class="text-caldo-teal">Conforme Linee Guida Sanitarie</span>
            </div>
        </div>
    </footer>

    <!-- ============================================================
         JS ROUTER SPA NATIVO E INTERAZIONI
         ============================================================ -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
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

            if (window.location.hash) {
                const hashId = window.location.hash.replace('#', '');
                switchView(hashId);
            }
        });
    </script>

</body>
</html>
"""

# Scriviamo direttamente su handoff_sito.html
target_path = "/Volumes/Programs/Temporary files/Progetti cursor/Michele_Novi_Website/handoff_sito.html"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_content)

# Copiamo in Proposte HTML
proposte_path = "/Volumes/Programs/Temporary files/Progetti cursor/Michele_Novi_Website/Proposte HTML/index.html"
with open(proposte_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Prototipo 'Calore, Colore e Icone' generato con successo!")
