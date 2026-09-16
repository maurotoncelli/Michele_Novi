# -*- coding: utf-8 -*-
"""
Script per implementare:
1. Gradienti leggeri e luminosi (soft mesh gradients, sfumature calde e rassicuranti).
2. Logo tipografico pulito: SOLO IL NOME, niente box o quadrato attorno al logo.
3. Movimenti fluidi e apparizioni morbide (soft blur/fade transitions, micro-animazioni organiche).
4. Iconografia elegante e colorata integrata in badge morbidi.
5. Incastro e Strati declinati con estrema morbidezza ed eleganza.
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
    
    <!-- Google Fonts: Newsreader (classe ed empatia) + Plus Jakarta Sans (freschezza e leggibilità) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,300;1,6..72,400;1,6..72,500&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        caldo: {
                            bg: '#FAF8F5',          /* Caldo lino / pergamena chiara */
                            surface: '#FFFFFF',
                            border: '#EBE7DF',
                            borderSoft: 'rgba(235, 231, 223, 0.7)',
                            text: '#162122',        /* Petrolio caldissimo e profondo */
                            muted: '#5A6667',       /* Testo secondario sereno */
                            
                            /* Gradienti e accenti leggeri */
                            teal: '#0C535C',
                            tealLight: '#E8F3F4',
                            tealSoft: '#F0F7F8',
                            
                            coral: '#DC6D48',       /* Terracotta luminoso */
                            coralLight: '#FDF2ED',
                            coralSoft: '#FFF7F3',
                            
                            salvia: '#437A55',      /* Verde guarigione */
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
            --ease-gentle: cubic-bezier(0.25, 1, 0.5, 1);
        }

        body {
            background-color: #FAF8F5;
            color: #162122;
            font-family: 'Plus Jakarta Sans', sans-serif;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }

        /* 1. GRADIENTI LEGGERI D'AMBIENTE (Aura Morbida) */
        .ambient-mesh {
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            pointer-events: none;
            z-index: 0;
            background: 
                radial-gradient(ellipse 65% 55% at 15% 15%, rgba(232, 243, 244, 0.7) 0%, transparent 60%),
                radial-gradient(ellipse 60% 50% at 85% 25%, rgba(253, 242, 237, 0.5) 0%, transparent 60%),
                radial-gradient(ellipse 70% 60% at 50% 85%, rgba(237, 245, 240, 0.45) 0%, transparent 70%);
            filter: blur(40px);
            opacity: 0.85;
        }

        /* Gradienti su Testo */
        .text-gradient-teal {
            background: linear-gradient(135deg, #0C535C 0%, #1A7582 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .text-gradient-coral {
            background: linear-gradient(135deg, #DC6D48 0%, #E88361 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .text-gradient-blend {
            background: linear-gradient(120deg, #0C535C 0%, #DC6D48 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Card con gradienti leggeri e traslucenza soft */
        .card-soft-gradient {
            background: linear-gradient(180deg, rgba(255, 255, 255, 0.95) 0%, rgba(250, 248, 245, 0.85) 100%);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(235, 231, 223, 0.85);
            transition: all 0.45s var(--ease-silk);
        }
        .card-soft-gradient:hover {
            transform: translateY(-4px);
            border-color: rgba(12, 83, 92, 0.35);
            box-shadow: 0 20px 40px -15px rgba(12, 83, 92, 0.08), 0 8px 16px -6px rgba(220, 109, 72, 0.04);
        }

        /* 2. MOVIMENTI FLUIDI ED APPARIZIONI MORBIDE */
        .reveal-soft {
            opacity: 0;
            transform: translateY(22px);
            filter: blur(6px);
            transition: opacity 1.1s var(--ease-silk), transform 1.1s var(--ease-silk), filter 1.1s var(--ease-silk);
            will-change: opacity, transform, filter;
        }
        .reveal-soft.is-visible {
            opacity: 1;
            transform: translateY(0);
            filter: blur(0);
        }

        /* 3. L'INCASTRO MORBIDO (WIDGET CONGRUENZA) */
        .congruence-container {
            background: linear-gradient(145deg, #FFFFFF 0%, #F5F8F8 50%, #FAF8F5 100%);
            border: 1px solid rgba(235, 231, 223, 0.9);
            border-radius: 32px;
            transition: all 0.5s var(--ease-silk);
        }
        .congruence-container:hover {
            border-color: rgba(12, 83, 92, 0.4);
            box-shadow: 0 24px 50px -15px rgba(12, 83, 92, 0.1);
        }
        .congruence-head-orb {
            transform: translateX(-18px);
            transition: transform 0.65s var(--ease-gentle);
        }
        .congruence-container:hover .congruence-head-orb {
            transform: translateX(0); /* L'incastro si unisce con morbidezza vellutata */
        }

        /* 4. GLI STRATI STACKED MORBIDI */
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

        /* Bottoni Leggeri con Sfumature Armoniose */
        .btn-fluid-primary {
            background: linear-gradient(135deg, #0C535C 0%, #166A75 100%);
            color: #FFFFFF;
            border-radius: 9999px;
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
            transition: all 0.4s var(--ease-silk);
            box-shadow: 0 10px 24px -6px rgba(12, 83, 92, 0.28);
        }
        .btn-fluid-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 14px 30px -6px rgba(12, 83, 92, 0.38);
            background: linear-gradient(135deg, #094249 0%, #0C535C 100%);
        }

        .btn-fluid-coral {
            background: linear-gradient(135deg, #DC6D48 0%, #E87E5C 100%);
            color: #FFFFFF;
            border-radius: 9999px;
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
            transition: all 0.4s var(--ease-silk);
            box-shadow: 0 10px 24px -6px rgba(220, 109, 72, 0.28);
        }
        .btn-fluid-coral:hover {
            transform: translateY(-2px);
            box-shadow: 0 14px 30px -6px rgba(220, 109, 72, 0.4);
        }

        .btn-fluid-ghost {
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(8px);
            color: #0C535C;
            border: 1px solid #EBE7DF;
            border-radius: 9999px;
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
            transition: all 0.4s var(--ease-silk);
        }
        .btn-fluid-ghost:hover {
            background: #FFFFFF;
            border-color: #0C535C;
            transform: translateY(-2px);
            box-shadow: 0 8px 20px -6px rgba(12, 83, 92, 0.12);
        }

        /* Router SPA con transizioni dolci */
        .page-view {
            display: none;
            opacity: 0;
            filter: blur(8px);
            transform: translateY(18px);
            transition: opacity 0.55s var(--ease-silk), transform 0.55s var(--ease-silk), filter 0.55s var(--ease-silk);
        }
        .page-view.active-view {
            display: block;
            opacity: 1;
            filter: blur(0);
            transform: translateY(0);
        }
    </style>
</head>
<body class="selection:bg-caldo-tealLight selection:text-caldo-teal relative">

    <!-- Gradienti d'ambiente sfumati in background -->
    <div class="ambient-mesh" aria-hidden="true"></div>

    <!-- ============================================================
         HEADER: LOGO È SOLO IL NOME (NO LOGO QUADRATO), LINEE FLUIDE
         ============================================================ -->
    <header class="fixed top-0 left-0 w-full z-50 bg-[#FAF8F5]/85 backdrop-blur-md border-b border-caldo-borderSoft transition-all duration-300" id="main-header">
        <div class="max-w-7xl mx-auto px-6 h-20 flex justify-between items-center">
            
            <!-- LOGO: IL NOME PURO, TIPOGRAFICO, SENZA QUADRATI -->
            <a href="#home" class="nav-trigger group flex flex-col cursor-pointer" data-target="home">
                <span class="font-serif text-2xl sm:text-[26px] tracking-tight text-caldo-text font-normal leading-tight group-hover:text-caldo-teal transition-colors duration-400">
                    Dott. Michele Novi
                </span>
                <span class="text-[11px] font-medium text-caldo-muted group-hover:text-caldo-teal transition-colors flex items-center gap-1.5 mt-0.5">
                    <span class="w-1.5 h-1.5 rounded-full bg-caldo-coral"></span>
                    <span>Ortopedia & Chirurgia Arto Superiore · CESAT</span>
                </span>
            </a>

            <!-- Navigazione: Rotte Bibbia con hover morbido e fluido -->
            <nav class="hidden lg:flex items-center gap-1 text-sm font-medium text-caldo-text">
                <a href="#chi-sono" class="nav-trigger px-4 py-2 rounded-full hover:bg-white/80 hover:text-caldo-teal transition-all duration-300" data-target="chi-sono">
                    Chi sono
                </a>
                <a href="#patologie" class="nav-trigger px-4 py-2 rounded-full hover:bg-white/80 hover:text-caldo-teal transition-all duration-300" data-target="patologie">
                    Cosa curo
                </a>
                <a href="#sedi" class="nav-trigger px-4 py-2 rounded-full hover:bg-white/80 hover:text-caldo-teal transition-all duration-300" data-target="sedi">
                    Dove ricevo
                </a>
                <a href="#articoli" class="nav-trigger px-4 py-2 rounded-full hover:bg-white/80 hover:text-caldo-teal transition-all duration-300" data-target="articoli">
                    Note cliniche
                </a>
                <a href="#contatti" class="nav-trigger px-4 py-2 rounded-full hover:bg-white/80 hover:text-caldo-teal transition-all duration-300" data-target="contatti">
                    Contatti
                </a>
            </nav>

            <!-- Recapito e Prenotazione Calda -->
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
         CONTENUTI PRINCIPALI
         ============================================================ -->
    <main class="relative z-10 pt-20" id="app-root">

        <!-- ========================================================
             VISTA 1: HOME (GRADIENTI LEGGERI, FLUIDITÀ, INCASTRO & STRATI)
             ======================================================== -->
        <section id="view-home" class="page-view active-view">
            
            <!-- HERO: APPARIZIONE MORBIDA, GRADIENTI E ARMONIA -->
            <div class="max-w-7xl mx-auto px-6 pt-12 pb-24">
                
                <div class="reveal-soft inline-flex items-center gap-2 bg-gradient-to-r from-caldo-tealLight/80 to-caldo-coralLight/80 border border-white px-4 py-1.5 rounded-full shadow-sm mb-8">
                    <span class="w-2 h-2 rounded-full bg-caldo-coral"></span>
                    <span class="text-xs font-semibold text-caldo-teal">Ospedale CESAT Fucecchio</span>
                    <span class="text-caldo-muted text-xs">· Sedi tra Valdera, Empolese e Pisa</span>
                </div>

                <div class="grid lg:grid-cols-12 gap-12 items-center">
                    
                    <!-- Titoli con sfumature delicate e apparizioni morbide -->
                    <div class="lg:col-span-7 space-y-6">
                        
                        <h1 class="reveal-soft text-4xl sm:text-6xl xl:text-7xl font-serif text-caldo-text font-normal leading-[1.07] tracking-tight">
                            Ritrovare il movimento,<br>
                            con la cura di <br>
                            <span class="italic text-gradient-teal font-medium">due superfici che combaciano.</span>
                        </h1>

                        <p class="reveal-soft text-lg sm:text-xl text-caldo-muted font-light leading-relaxed max-w-xl">
                            Specialista della spalla, del gomito e della mano. 
                            Dalla precisione artroscopica mini-invasiva alle protesi articolari, 
                            con l'ascolto e la serenità che ogni paziente merita.
                        </p>

                        <!-- 3 Punti di Eccellenza con gradienti soffusi e icone curate -->
                        <div class="reveal-soft grid sm:grid-cols-3 gap-3.5 pt-2">
                            
                            <!-- Spalla -->
                            <div class="flex items-center gap-3 p-3.5 rounded-2xl bg-white/80 backdrop-blur-sm border border-caldo-borderSoft shadow-sm">
                                <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-caldo-tealLight to-white text-caldo-teal flex items-center justify-center flex-shrink-0 shadow-sm">
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

                            <!-- Artroscopia -->
                            <div class="flex items-center gap-3 p-3.5 rounded-2xl bg-white/80 backdrop-blur-sm border border-caldo-borderSoft shadow-sm">
                                <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-caldo-coralLight to-white text-caldo-coral flex items-center justify-center flex-shrink-0 shadow-sm">
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

                            <!-- CESAT -->
                            <div class="flex items-center gap-3 p-3.5 rounded-2xl bg-white/80 backdrop-blur-sm border border-caldo-borderSoft shadow-sm">
                                <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-caldo-salviaLight to-white text-caldo-salvia flex items-center justify-center flex-shrink-0 shadow-sm">
                                    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                                        <path d="M3 21h18M5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16"/>
                                        <path d="M9 10h6M12 7v6"/>
                                    </svg>
                                </div>
                                <div class="text-xs">
                                    <strong class="block text-caldo-text font-semibold">Polo CESAT</strong>
                                    <span class="text-caldo-muted text-[11px]">Chirurgia d'eccellenza</span>
                                </div>
                            </div>

                        </div>

                        <!-- Pulsanti d'Azione Fluidi -->
                        <div class="reveal-soft flex flex-wrap gap-4 pt-3">
                            <a href="#contatti" class="nav-trigger btn-fluid-primary px-8 py-4 text-sm font-semibold" data-target="contatti">
                                <span>Richiedi una Visita</span>
                                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                                    <path d="M5 12h14M12 5l7 7-7 7"/>
                                </svg>
                            </a>
                            <a href="#patologie" class="nav-trigger btn-fluid-ghost px-7 py-4 text-sm font-semibold" data-target="patologie">
                                <span>Esplora le Patologie</span>
                                <span>→</span>
                            </a>
                        </div>

                    </div>

                    <!-- Ritratto con sfumatura calda e riflessi soft -->
                    <div class="lg:col-span-5 relative reveal-soft">
                        <div class="relative z-10 p-3.5 rounded-[36px] bg-gradient-to-br from-white via-white/90 to-caldo-coralLight/40 border border-white shadow-xl shadow-caldo-teal/5">
                            
                            <div class="aspect-[4/5] rounded-[28px] overflow-hidden relative bg-gradient-to-tr from-caldo-tealLight/40 to-caldo-coralLight/40">
                                <img src="https://images.unsplash.com/photo-1622253692010-333f2da6031d?q=80&w=1000&auto=format&fit=crop" 
                                     alt="Dott. Michele Novi" 
                                     class="w-full h-full object-cover object-center filter contrast-[1.02]">
                                
                                <!-- Sfumatura leggera alla base del ritratto -->
                                <div class="absolute inset-0 bg-gradient-to-t from-caldo-teal/60 via-transparent to-transparent opacity-60"></div>

                                <!-- Badge Umano e Rassicurante -->
                                <div class="absolute bottom-5 left-5 right-5 bg-white/90 backdrop-blur-md p-4 rounded-2xl border border-white/80 shadow-md flex items-center justify-between">
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
                 SEZIONE 2: L'INCASTRO MORBIDO (CONGRUENZA ARTICOLARE)
                 Movimento fluido, gradienti sfumati e spiegazione del Remplissage
                 ======================================================== -->
            <div class="py-24 px-6 border-y border-caldo-borderSoft bg-gradient-to-b from-white via-[#FAF8F5] to-white">
                <div class="max-w-7xl mx-auto">
                    
                    <div class="max-w-2xl mb-16 space-y-3">
                        <span class="inline-flex items-center gap-2 text-xs font-semibold text-caldo-coral bg-caldo-coralLight px-3.5 py-1 rounded-full">
                            <span class="w-1.5 h-1.5 rounded-full bg-caldo-coral"></span>
                            Biologia & Meccanica Articolare
                        </span>
                        <h2 class="text-3xl sm:text-5xl font-serif text-caldo-text leading-tight">
                            L'Incastro perfetto: stabilità senza rinunciare al movimento.
                        </h2>
                        <p class="text-base text-caldo-muted leading-relaxed font-light">
                            Una spalla sana è il frutto di due superfici che scivolano e combaciano senza ostacoli. Nelle lussazioni recidivanti, il nostro lavoro è colmare i vuoti affinché il giunto torni a incastrarsi in modo sicuro.
                        </p>
                    </div>

                    <div class="grid lg:grid-cols-12 gap-10 items-center">
                        
                        <!-- Box Dimostrativo Interattivo Fluido -->
                        <div class="lg:col-span-6 congruence-container p-8 sm:p-12 relative overflow-hidden group cursor-pointer">
                            
                            <div class="flex justify-between items-center mb-8">
                                <span class="text-xs font-semibold text-caldo-teal flex items-center gap-2">
                                    <span class="w-2 h-2 rounded-full bg-caldo-teal animate-pulse"></span>
                                    Simulazione di Stabilità
                                </span>
                                <span class="text-xs bg-white/90 text-caldo-teal font-medium px-3.5 py-1.5 rounded-full border border-caldo-borderSoft shadow-sm">
                                    Passa sopra per unire le superfici
                                </span>
                            </div>

                            <!-- Animazione Incastro Glenoide + Testa Omerale -->
                            <div class="flex items-center justify-center my-10 relative">
                                
                                <!-- Glenoide (Superficie ricevente morbida con gradiente teal) -->
                                <div class="w-36 h-48 rounded-r-full bg-gradient-to-r from-caldo-tealLight to-white border-2 border-caldo-teal/70 flex items-center justify-start pl-4 shadow-sm">
                                    <div>
                                        <span class="text-xs font-bold text-caldo-teal block">Glenoide</span>
                                        <span class="text-[10px] text-caldo-muted">Superficie concava</span>
                                    </div>
                                </div>

                                <!-- Testa Omerale Mobile con gradiente corallo sfumato -->
                                <div class="congruence-head-orb w-40 h-40 rounded-full bg-gradient-to-tr from-caldo-coral to-caldo-coral/80 text-white flex items-center justify-center -ml-16 shadow-xl shadow-caldo-coral/20 border-4 border-white z-10">
                                    <div class="text-center p-2">
                                        <svg class="w-6 h-6 mx-auto mb-1 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                                            <circle cx="12" cy="12" r="9"/>
                                            <path d="M12 8v8M8 12h8"/>
                                        </svg>
                                        <strong class="text-xs font-semibold block">Testa Omerale</strong>
                                        <span class="text-[10px] opacity-90">Superficie convessa</span>
                                    </div>
                                </div>

                            </div>

                            <div class="bg-white/95 backdrop-blur-md p-4 rounded-2xl border border-caldo-borderSoft flex items-center justify-between text-xs">
                                <div class="flex items-center gap-2.5">
                                    <div class="w-6 h-6 rounded-full bg-caldo-salviaLight text-caldo-salvia flex items-center justify-center font-bold text-xs">✓</div>
                                    <span class="font-medium text-caldo-text">Congruenza ristabilita</span>
                                </div>
                                <span class="text-caldo-teal font-semibold">Procedura Remplissage</span>
                            </div>

                        </div>

                        <!-- Spiegazione Serena della Procedura -->
                        <div class="lg:col-span-6 space-y-6">
                            <div class="card-soft-gradient p-8 sm:p-10 rounded-3xl space-y-4">
                                <span class="text-xs font-bold uppercase tracking-wider text-caldo-coral block">Il Dubbio Clinico Risolto</span>
                                <h3 class="text-2xl font-serif text-caldo-text">
                                    Nelle lussazioni recidivanti, l'osso non deve ingranare nel vuoto.
                                </h3>
                                <p class="text-sm text-caldo-muted leading-relaxed font-light">
                                    Quando la spalla esce, si genera spesso un'intaccatura sulla testa dell'omero (lesione di Hill-Sachs). Nelle rotazioni del braccio, questa cavità rischia di incastrarsi contro il bordo glenoideo, provocando una nuova lussazione.
                                </p>
                                <p class="text-sm text-caldo-muted leading-relaxed font-light">
                                    Con il <strong>Remplissage</strong> ("riempimento" artroscopico), suturiamo il tendine dell'infraspinato all'interno della lesione: l'incastro sgradevole viene neutralizzato e l'articolazione ritrova una superficie liscia e stabile.
                                </p>
                                <div class="pt-2">
                                    <a href="#articoli-remplissage" class="nav-trigger text-sm font-bold text-caldo-teal hover:text-caldo-coral inline-flex items-center gap-1.5 transition-colors" data-target="articoli-remplissage">
                                        <span>Leggi l'approfondimento scientifico con il CESAT</span>
                                        <span>→</span>
                                    </a>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
            </div>

            <!-- ========================================================
                 SEZIONE 3: UNO STRATO SOTTO L'ALTRO (STACKED CARDS FLUIDE)
                 I 4 livelli anatomici con sfumature delicate
                 ======================================================== -->
            <div class="max-w-7xl mx-auto px-6 py-28">
                
                <div class="max-w-2xl mb-16 space-y-3">
                    <span class="inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal bg-caldo-tealLight px-3.5 py-1 rounded-full">
                        <span class="w-1.5 h-1.5 rounded-full bg-caldo-teal"></span>
                        Dissezione & Anatomia Funzionale
                    </span>
                    <h2 class="text-3xl sm:text-5xl font-serif text-caldo-text leading-tight">
                        Uno strato sotto l'altro: il percorso della cura.
                    </h2>
                    <p class="text-base text-caldo-muted font-light leading-relaxed">
                        In chirurgia non si aggredisce il corpo: si attraversano con delicatezza i diversi strati tessutali per raggiungere l'origine esatta del dolore.
                    </p>
                </div>

                <!-- Pila di Strati con gradienti leggeri -->
                <div class="space-y-8 relative">
                    
                    <!-- STRATO 1: CUTE E MINI-INVASIVITÀ -->
                    <div class="strata-card-soft p-8 md:p-12">
                        <div class="grid md:grid-cols-12 gap-6 items-center">
                            <div class="md:col-span-2 flex md:flex-col items-center gap-2">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-caldo-tealLight to-white text-caldo-teal flex items-center justify-center shadow-sm">
                                    <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                                        <path d="M12 2v20M2 12h20M7 7l10 10M7 17l10-10"/>
                                    </svg>
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
                                <span class="inline-block bg-caldo-tealLight text-caldo-teal text-xs font-semibold px-4 py-1.5 rounded-full">
                                    Artroscopia Avanzata
                                </span>
                            </div>
                        </div>
                    </div>

                    <!-- STRATO 2: CUFFIA DEI ROTATORI -->
                    <div class="strata-card-soft p-8 md:p-12">
                        <div class="grid md:grid-cols-12 gap-6 items-center">
                            <div class="md:col-span-2 flex md:flex-col items-center gap-2">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-caldo-coralLight to-white text-caldo-coral flex items-center justify-center shadow-sm">
                                    <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                                        <path d="M18 8h1a4 4 0 0 1 0 8h-1M6 8H5a4 4 0 0 0 0 8h1M2 12h20"/>
                                    </svg>
                                </div>
                                <span class="text-xs font-bold text-caldo-coral tracking-wider uppercase">Strato 02</span>
                            </div>
                            <div class="md:col-span-7 space-y-1.5">
                                <h3 class="text-2xl font-serif text-caldo-text">I Tendini della Cuffia dei Rotatori</h3>
                                <p class="text-sm text-caldo-muted leading-relaxed font-light">
                                    Il motore della spalla. Ripariamo le lesioni con suture anatomiche su micro-ancore biologiche, valutando sempre con attenzione quando è preferibile il percorso conservativo con fisioterapia mirata.
                                </p>
                            </div>
                            <div class="md:col-span-3 text-right">
                                <span class="inline-block bg-caldo-coralLight text-caldo-coral text-xs font-semibold px-4 py-1.5 rounded-full">
                                    Riparazione Tendinea
                                </span>
                            </div>
                        </div>
                    </div>

                    <!-- STRATO 3: CAPSULA E CERCINE GLENOIDEO -->
                    <div class="strata-card-soft p-8 md:p-12">
                        <div class="grid md:grid-cols-12 gap-6 items-center">
                            <div class="md:col-span-2 flex md:flex-col items-center gap-2">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-caldo-goldLight to-white text-caldo-gold flex items-center justify-center shadow-sm">
                                    <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                                        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                                    </svg>
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
                                <span class="inline-block bg-caldo-goldLight text-caldo-gold text-xs font-semibold px-4 py-1.5 rounded-full">
                                    Stabilità Articolare
                                </span>
                            </div>
                        </div>
                    </div>

                    <!-- STRATO 4: OSSO E CHIRURGIA PROTESICA -->
                    <div class="strata-card-soft p-8 md:p-12">
                        <div class="grid md:grid-cols-12 gap-6 items-center">
                            <div class="md:col-span-2 flex md:flex-col items-center gap-2">
                                <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-caldo-salviaLight to-white text-caldo-salvia flex items-center justify-center shadow-sm">
                                    <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                                        <circle cx="6" cy="6" r="3"/>
                                        <circle cx="6" cy="18" r="3"/>
                                        <line x1="6" y1="9" x2="6" y2="15"/>
                                        <circle cx="18" cy="6" r="3"/>
                                        <circle cx="18" cy="18" r="3"/>
                                        <line x1="18" y1="9" x2="18" y2="15"/>
                                        <line x1="9" y1="12" x2="15" y2="12"/>
                                    </svg>
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
                                <span class="inline-block bg-caldo-salviaLight text-caldo-salvia text-xs font-semibold px-4 py-1.5 rounded-full">
                                    Protesica d'Eccellenza
                                </span>
                            </div>
                        </div>
                    </div>

                </div>
            </div>

            <!-- ========================================================
                 SEZIONE 4: ANTEPRIMA DELLE 6 AREE (ICONE COLORATE E MORBIDE)
                 ======================================================== -->
            <div class="py-24 px-6 bg-white/70 backdrop-blur-md border-t border-caldo-borderSoft">
                <div class="max-w-7xl mx-auto">
                    
                    <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-6">
                        <div>
                            <span class="text-xs font-semibold text-caldo-teal uppercase tracking-wider block mb-2">Percorsi Dedicati</span>
                            <h2 class="text-3xl sm:text-5xl font-serif text-caldo-text">Cosa curo: 6 aree di specializzazione.</h2>
                        </div>
                        <a href="#patologie" class="nav-trigger btn-fluid-ghost px-6 py-3 text-xs font-bold" data-target="patologie">
                            Vedi tutte le patologie →
                        </a>
                    </div>

                    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
                        
                        <!-- 1. Spalla -->
                        <a href="#patologie-spalla" class="nav-trigger card-soft-gradient p-8 rounded-3xl group" data-target="patologie-spalla">
                            <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-caldo-tealLight to-white text-caldo-teal flex items-center justify-center mb-6 group-hover:scale-105 transition-transform">
                                <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                                    <circle cx="12" cy="12" r="9"/>
                                    <path d="M12 7v5l3 3"/>
                                </svg>
                            </div>
                            <h3 class="text-xl font-serif font-semibold text-caldo-text group-hover:text-caldo-teal transition-colors mb-2">Chirurgia della Spalla</h3>
                            <p class="text-xs text-caldo-muted leading-relaxed font-light mb-6">Cuffia dei rotatori, instabilità, lussazioni, protesi anatomiche e inverse.</p>
                            <span class="text-xs font-semibold text-caldo-teal inline-flex items-center gap-1 group-hover:translate-x-1 transition-transform">
                                Approfondisci spalla →
                            </span>
                        </a>

                        <!-- 2. Gomito -->
                        <a href="#patologie-gomito" class="nav-trigger card-soft-gradient p-8 rounded-3xl group" data-target="patologie-gomito">
                            <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-caldo-coralLight to-white text-caldo-coral flex items-center justify-center mb-6 group-hover:scale-105 transition-transform">
                                <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                                    <path d="M18 10h-4a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h4a2 2 0 0 0 2-2v-8a2 2 0 0 0-2-2Z"/>
                                    <path d="M6 4h4a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2Z"/>
                                </svg>
                            </div>
                            <h3 class="text-xl font-serif font-semibold text-caldo-text group-hover:text-caldo-teal transition-colors mb-2">Gomito e Traumi</h3>
                            <p class="text-xs text-caldo-muted leading-relaxed font-light mb-6">Epicondilite resistente, fratture del capitello radiale, lesioni del bicipite.</p>
                            <span class="text-xs font-semibold text-caldo-coral inline-flex items-center gap-1 group-hover:translate-x-1 transition-transform">
                                Approfondisci gomito →
                            </span>
                        </a>

                        <!-- 3. Mano e Polso -->
                        <a href="#patologie-mano" class="nav-trigger card-soft-gradient p-8 rounded-3xl group" data-target="patologie-mano">
                            <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-caldo-salviaLight to-white text-caldo-salvia flex items-center justify-center mb-6 group-hover:scale-105 transition-transform">
                                <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                                    <path d="M18 11V6a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v0"/>
                                    <path d="M14 10V4a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v2"/>
                                    <path d="M10 10.5V6a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v8"/>
                                </svg>
                            </div>
                            <h3 class="text-xl font-serif font-semibold text-caldo-text group-hover:text-caldo-teal transition-colors mb-2">Mano e Polso</h3>
                            <p class="text-xs text-caldo-muted leading-relaxed font-light mb-6">Tunnel carpale, dito a scatto, morbo di De Quervain, rizoartrosi del pollice.</p>
                            <span class="text-xs font-semibold text-caldo-salvia inline-flex items-center gap-1 group-hover:translate-x-1 transition-transform">
                                Approfondisci mano →
                            </span>
                        </a>

                        <!-- 4. Sport -->
                        <a href="#patologie-traumatologia-sportiva" class="nav-trigger card-soft-gradient p-8 rounded-3xl group" data-target="patologie-traumatologia-sportiva">
                            <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-caldo-goldLight to-white text-caldo-gold flex items-center justify-center mb-6 group-hover:scale-105 transition-transform">
                                <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                                    <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/>
                                    <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/>
                                    <path d="M4 22h16"/>
                                </svg>
                            </div>
                            <h3 class="text-xl font-serif font-semibold text-caldo-text group-hover:text-caldo-teal transition-colors mb-2">Traumatologia Sportiva</h3>
                            <p class="text-xs text-caldo-muted leading-relaxed font-light mb-6">Supporto ad atleti amatoriali e professionisti: ritorno all'attività senza rischi.</p>
                            <span class="text-xs font-semibold text-caldo-gold inline-flex items-center gap-1 group-hover:translate-x-1 transition-transform">
                                Percorso atleti →
                            </span>
                        </a>

                        <!-- 5. Artroscopia -->
                        <a href="#patologie-artroscopia" class="nav-trigger card-soft-gradient p-8 rounded-3xl group" data-target="patologie-artroscopia">
                            <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-caldo-tealLight to-white text-caldo-teal flex items-center justify-center mb-6 group-hover:scale-105 transition-transform">
                                <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                                    <circle cx="12" cy="12" r="3"/>
                                    <path d="M3 7V5a2 2 0 0 1 2-2h2M17 3h2a2 2 0 0 1 2 2v2M21 17v2a2 2 0 0 1-2 2h-2M7 21H5a2 2 0 0 1-2-2v-2"/>
                                </svg>
                            </div>
                            <h3 class="text-xl font-serif font-semibold text-caldo-text group-hover:text-caldo-teal transition-colors mb-2">Chirurgia Artroscopica</h3>
                            <p class="text-xs text-caldo-muted leading-relaxed font-light mb-6">Diagnosi e riparazioni a visione ottica diretta con rispetto dei tessuti.</p>
                            <span class="text-xs font-semibold text-caldo-teal inline-flex items-center gap-1 group-hover:translate-x-1 transition-transform">
                                Il metodo ottico →
                            </span>
                        </a>

                        <!-- 6. Ecografia -->
                        <a href="#patologie-ecografia-muscoloscheletrica" class="nav-trigger card-soft-gradient p-8 rounded-3xl group" data-target="patologie-ecografia-muscoloscheletrica">
                            <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-caldo-coralLight to-white text-caldo-coral flex items-center justify-center mb-6 group-hover:scale-105 transition-transform">
                                <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                                    <path d="M2 12h5l3 8 4-16 3 8h5"/>
                                </svg>
                            </div>
                            <h3 class="text-xl font-serif font-semibold text-caldo-text group-hover:text-caldo-teal transition-colors mb-2">Ecografia Muscoloscheletrica</h3>
                            <p class="text-xs text-caldo-muted leading-relaxed font-light mb-6">Diploma SIUMB: valutazione immediata e infiltrazioni eco-guidate mirate.</p>
                            <span class="text-xs font-semibold text-caldo-coral inline-flex items-center gap-1 group-hover:translate-x-1 transition-transform">
                                Diagnostica SIUMB →
                            </span>
                        </a>

                    </div>
                </div>
            </div>

            <!-- ========================================================
                 SEZIONE 5: DOVE RICEVO (LE SEDI CON COLORI CALDI)
                 ======================================================== -->
            <div class="py-24 px-6 max-w-7xl mx-auto">
                <div class="bg-gradient-to-br from-caldo-teal via-[#0E5C66] to-[#0A4850] text-white p-10 sm:p-16 rounded-[36px] shadow-xl relative overflow-hidden">
                    
                    <!-- Cerchi decorativi sfumati all'interno della card -->
                    <div class="absolute -right-20 -top-20 w-80 h-80 bg-caldo-coral/20 rounded-full blur-3xl pointer-events-none"></div>
                    <div class="absolute -left-20 -bottom-20 w-80 h-80 bg-caldo-salvia/20 rounded-full blur-3xl pointer-events-none"></div>

                    <div class="grid lg:grid-cols-12 gap-10 items-center relative z-10">
                        <div class="lg:col-span-7 space-y-6">
                            <span class="inline-flex items-center gap-2 bg-white/10 text-white text-xs font-semibold px-4 py-1.5 rounded-full border border-white/20">
                                📍 Presenza in Toscana
                            </span>
                            
                            <h2 class="text-3xl sm:text-5xl font-serif text-white leading-tight">
                                Vicini al paziente tra Valdera, Empolese e Pisa.
                            </h2>
                            <p class="text-white/80 text-base leading-relaxed max-w-xl font-light">
                                Gli interventi chirurgici ospedalieri si tengono all'Ospedale CESAT di Fucecchio. Le visite ambulatoriali e i controlli si svolgono nelle 4 sedi territoriali.
                            </p>

                            <div class="flex flex-wrap gap-4 pt-2">
                                <a href="#sedi" class="nav-trigger btn-fluid-coral px-6 py-3.5 text-xs font-semibold" data-target="sedi">
                                    Vedi tutte le sedi e orari
                                </a>
                                <a href="tel:+393484331733" class="inline-flex items-center gap-2 px-6 py-3.5 rounded-full bg-white/10 hover:bg-white/20 text-white text-xs font-semibold border border-white/25 transition-all">
                                    <span>Chiama la Segreteria</span>
                                    <span>→</span>
                                </a>
                            </div>
                        </div>

                        <!-- Card Sedi Compatta -->
                        <div class="lg:col-span-5 bg-white/95 backdrop-blur-md text-caldo-text p-8 rounded-3xl shadow-lg space-y-3.5">
                            <h4 class="font-serif text-xl font-semibold text-caldo-teal">Ambulatorio di Riferimento</h4>
                            
                            <div class="flex items-start gap-3 p-3 rounded-2xl bg-caldo-bg border border-caldo-border">
                                <div class="w-8 h-8 rounded-xl bg-caldo-teal text-white flex items-center justify-center font-bold text-xs flex-shrink-0">1</div>
                                <div>
                                    <strong class="block text-caldo-text text-sm">Fucecchio · Studi San Pietro</strong>
                                    <span class="text-caldo-muted text-xs">Piazza Lavagnini 6 (Accanto all'Ospedale)</span>
                                </div>
                            </div>
                            
                            <div class="flex items-start gap-3 p-3 rounded-2xl bg-caldo-bg border border-caldo-border">
                                <div class="w-8 h-8 rounded-xl bg-caldo-coral text-white flex items-center justify-center font-bold text-xs flex-shrink-0">2</div>
                                <div>
                                    <strong class="block text-caldo-text text-sm">Peccioli · Polo San Verano</strong>
                                    <span class="text-caldo-muted text-xs">Alta Valdera (Ambulatorio territoriale)</span>
                                </div>
                            </div>

                            <div class="flex items-start gap-3 p-3 rounded-2xl bg-caldo-bg border border-caldo-border">
                                <div class="w-8 h-8 rounded-xl bg-caldo-salvia text-white flex items-center justify-center font-bold text-xs flex-shrink-0">3</div>
                                <div>
                                    <strong class="block text-caldo-text text-sm">Pisa & Fornacette</strong>
                                    <span class="text-caldo-muted text-xs">Athletica Pisa e Centro Fisiomed</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </section>

        <!-- ========================================================
             VISTA 2: CHI SONO (PROFILO UMANO, FORMAZIONE, SEATTLE, CESAT)
             ======================================================== -->
        <section id="view-chi-sono" class="page-view max-w-6xl mx-auto px-6 py-16">
            
            <a href="#home" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal hover:text-caldo-coral mb-8 transition-colors" data-target="home">
                <span>← Torna alla Home</span>
            </a>

            <div class="max-w-3xl mb-16 space-y-4">
                <span class="text-xs font-semibold text-caldo-teal bg-caldo-tealLight px-3.5 py-1.5 rounded-full inline-block">
                    Identità e Visione
                </span>
                <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text leading-tight">
                    Chirurgia di rigore,<br>
                    <span class="italic text-gradient-teal font-medium">vicinanza alla persona.</span>
                </h1>
                <p class="text-lg text-caldo-muted font-light leading-relaxed">
                    «Operare bene è un dovere tecnico; guidare il paziente con parole chiare e senza fretta è una scelta di rispetto umano.»
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
                            <p class="text-xs text-caldo-muted">Dirigente Medico Ortopedico · CESAT Fucecchio</p>
                            <p class="text-xs text-caldo-teal font-medium">Ordine dei Medici di Pisa n. 5988</p>
                        </div>
                    </div>

                    <div class="bg-gradient-to-br from-caldo-coralLight to-caldo-goldLight/40 p-6 rounded-3xl border border-caldo-coral/20 space-y-3">
                        <span class="text-xs font-bold text-caldo-coral uppercase tracking-wider block">Due Tempi, Un Medico Solo</span>
                        <p class="text-xs text-caldo-muted leading-relaxed font-light">
                            <strong>La Sala di Volume:</strong> Al CESAT di Fucecchio affronto quotidianamente la chirurgia protesica e artroscopica complessa.
                        </p>
                        <p class="text-xs text-caldo-muted leading-relaxed font-light">
                            <strong>Il Territorio:</strong> Negli ambulatori della Valdera e di Pisa ascolto le storie dei pazienti, imposto il percorso e seguo la guarigione passo dopo passo.
                        </p>
                    </div>
                </div>

                <div class="lg:col-span-7 space-y-10">
                    <div class="space-y-6 text-base text-caldo-muted font-light leading-relaxed">
                        <p>
                            Mi sono laureato e specializzato con lode presso l'<strong>Università di Pisa</strong>, allievo della scuola del Prof. Porcellini e collaboratore del Dott. Nicoletti.
                        </p>
                        <p>
                            Durante la mia fellowship presso l'<strong>Harborview Medical Center di Seattle (USA)</strong>, ho approfondito la gestione dei traumi complessi e della microchirurgia dei nervi periferici dell'arto superiore.
                        </p>
                    </div>

                    <div class="border-t border-caldo-border pt-8 space-y-4">
                        <h4 class="text-xl font-serif text-caldo-text font-semibold">Tappe del Percorso Formativo</h4>

                        <div class="flex items-start gap-4 p-4 rounded-2xl bg-white border border-caldo-border shadow-sm">
                            <div class="w-10 h-10 rounded-xl bg-caldo-tealLight text-caldo-teal flex items-center justify-center font-bold text-base flex-shrink-0">
                                🏥
                            </div>
                            <div>
                                <span class="text-xs font-bold text-caldo-teal block">2020 – Presente</span>
                                <strong class="text-sm text-caldo-text block">Dirigente Medico Ortopedico · Ospedale CESAT Fucecchio</strong>
                                <p class="text-xs text-caldo-muted mt-0.5">Centro regionale toscano per la chirurgia protesica e ricostruttiva.</p>
                            </div>
                        </div>

                        <div class="flex items-start gap-4 p-4 rounded-2xl bg-white border border-caldo-border shadow-sm">
                            <div class="w-10 h-10 rounded-xl bg-caldo-coralLight text-caldo-coral flex items-center justify-center font-bold text-base flex-shrink-0">
                                🇺🇸
                            </div>
                            <div>
                                <span class="text-xs font-bold text-caldo-coral block">Fellowship Internazionale</span>
                                <strong class="text-sm text-caldo-text block">Harborview Medical Center · Seattle (USA)</strong>
                                <p class="text-xs text-caldo-muted mt-0.5">Microchirurgia dei lembi e chirurgia dei nervi periferici.</p>
                            </div>
                        </div>

                        <div class="flex items-start gap-4 p-4 rounded-2xl bg-white border border-caldo-border shadow-sm">
                            <div class="w-10 h-10 rounded-xl bg-caldo-salviaLight text-caldo-salvia flex items-center justify-center font-bold text-base flex-shrink-0">
                                🔬
                            </div>
                            <div>
                                <span class="text-xs font-bold text-caldo-salvia block">SIUMB</span>
                                <strong class="text-sm text-caldo-text block">Diploma Nazionale in Ecografia Muscoloscheletrica</strong>
                                <p class="text-xs text-caldo-muted mt-0.5">Precisione diagnostica e infiltrazioni eco-guidate sul paziente.</p>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

        </section>

        <!-- ========================================================
             VISTA 3: PATOLOGIE (HUB COMPLETO DELLE 6 AREE)
             ======================================================== -->
        <section id="view-patologie" class="page-view max-w-7xl mx-auto px-6 py-16">
            
            <a href="#home" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal hover:text-caldo-coral mb-8 transition-colors" data-target="home">
                <span>← Torna alla Home</span>
            </a>

            <div class="max-w-3xl mb-16 space-y-4">
                <span class="text-xs font-semibold text-caldo-teal bg-caldo-tealLight px-3.5 py-1.5 rounded-full inline-block">
                    Aree Cliniche
                </span>
                <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text leading-tight">
                    Cosa curo: diagnosi accurata e opzioni terapeutiche.
                </h1>
                <p class="text-base text-caldo-muted font-light leading-relaxed">
                    Dalla spalla al polso: ogni distretto articolare richiede un approccio su misura che bilancia terapie conservative e chirurgia d'avanguardia.
                </p>
            </div>

            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                
                <!-- Spalla -->
                <div class="card-soft-gradient p-8 rounded-3xl flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-caldo-tealLight text-caldo-teal flex items-center justify-center mb-6">
                            <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                                <circle cx="12" cy="12" r="9"/>
                                <path d="M12 7v5l3 3"/>
                            </svg>
                        </div>
                        <h3 class="text-2xl font-serif text-caldo-text mb-3">Chirurgia della Spalla</h3>
                        <p class="text-xs text-caldo-muted leading-relaxed font-light mb-6">
                            Rotture della cuffia dei rotatori, instabilità articolare (Bankart, Remplissage) e protesi anatomica o inversa.
                        </p>
                    </div>
                    <a href="#patologie-spalla" class="nav-trigger btn-fluid-primary !py-2.5 !px-5 text-xs justify-center" data-target="patologie-spalla">
                        Dettaglio spalla →
                    </a>
                </div>

                <!-- Gomito -->
                <div class="card-soft-gradient p-8 rounded-3xl flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-caldo-coralLight text-caldo-coral flex items-center justify-center mb-6">
                            <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                                <path d="M18 10h-4a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h4a2 2 0 0 0 2-2v-8a2 2 0 0 0-2-2Z"/>
                                <path d="M6 4h4a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2Z"/>
                            </svg>
                        </div>
                        <h3 class="text-2xl font-serif text-caldo-text mb-3">Gomito e Traumi</h3>
                        <p class="text-xs text-caldo-muted leading-relaxed font-light mb-6">
                            Rigidità, epicondilite resistente e riparazione del tendine distale del bicipite brachiale.
                        </p>
                    </div>
                    <a href="#patologie-gomito" class="nav-trigger btn-fluid-ghost !py-2.5 !px-5 text-xs justify-center" data-target="patologie-gomito">
                        Dettaglio gomito →
                    </a>
                </div>

                <!-- Mano -->
                <div class="card-soft-gradient p-8 rounded-3xl flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-caldo-salviaLight text-caldo-salvia flex items-center justify-center mb-6">
                            <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                                <path d="M18 11V6a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v0"/>
                                <path d="M14 10V4a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v2"/>
                                <path d="M10 10.5V6a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v8"/>
                            </svg>
                        </div>
                        <h3 class="text-2xl font-serif text-caldo-text mb-3">Mano e Polso</h3>
                        <p class="text-xs text-caldo-muted leading-relaxed font-light mb-6">
                            Decompressione del tunnel carpale, dito a scatto, morbo di De Quervain e rizoartrosi.
                        </p>
                    </div>
                    <a href="#patologie-mano" class="nav-trigger btn-fluid-ghost !py-2.5 !px-5 text-xs justify-center" data-target="patologie-mano">
                        Dettaglio mano →
                    </a>
                </div>

                <!-- Sport -->
                <div class="card-soft-gradient p-8 rounded-3xl flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-caldo-goldLight text-caldo-gold flex items-center justify-center mb-6">
                            <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                                <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/>
                                <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/>
                                <path d="M4 22h16"/>
                            </svg>
                        </div>
                        <h3 class="text-2xl font-serif text-caldo-text mb-3">Traumatologia Sportiva</h3>
                        <p class="text-xs text-caldo-muted leading-relaxed font-light mb-6">
                            Lussazioni acromion-claveari, lesioni da sovraccarico funzionale e return-to-play sicuro.
                        </p>
                    </div>
                    <a href="#patologie-traumatologia-sportiva" class="nav-trigger btn-fluid-ghost !py-2.5 !px-5 text-xs justify-center" data-target="patologie-traumatologia-sportiva">
                        Dettaglio sport →
                    </a>
                </div>

                <!-- Artroscopia -->
                <div class="card-soft-gradient p-8 rounded-3xl flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-caldo-tealLight text-caldo-teal flex items-center justify-center mb-6">
                            <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                                <circle cx="12" cy="12" r="3"/>
                                <path d="M3 7V5a2 2 0 0 1 2-2h2M17 3h2a2 2 0 0 1 2 2v2M21 17v2a2 2 0 0 1-2 2h-2M7 21H5a2 2 0 0 1-2-2v-2"/>
                            </svg>
                        </div>
                        <h3 class="text-2xl font-serif text-caldo-text mb-3">Chirurgia Artroscopica</h3>
                        <p class="text-xs text-caldo-muted leading-relaxed font-light mb-6">
                            La tecnica endoscopica ad alta definizione per riparazioni interne senza tagliare muscoli sani.
                        </p>
                    </div>
                    <a href="#patologie-artroscopia" class="nav-trigger btn-fluid-ghost !py-2.5 !px-5 text-xs justify-center" data-target="patologie-artroscopia">
                        Dettaglio artroscopia →
                    </a>
                </div>

                <!-- Ecografia -->
                <div class="card-soft-gradient p-8 rounded-3xl flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-caldo-coralLight text-caldo-coral flex items-center justify-center mb-6">
                            <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                                <path d="M2 12h5l3 8 4-16 3 8h5"/>
                            </svg>
                        </div>
                        <h3 class="text-2xl font-serif text-caldo-text mb-3">Ecografia Muscoloscheletrica</h3>
                        <p class="text-xs text-caldo-muted leading-relaxed font-light mb-6">
                            L'ecografo in studio: diagnostica dinamica immediata e infiltrazioni eco-guidate al millimetro.
                        </p>
                    </div>
                    <a href="#patologie-ecografia-muscoloscheletrica" class="nav-trigger btn-fluid-ghost !py-2.5 !px-5 text-xs justify-center" data-target="patologie-ecografia-muscoloscheletrica">
                        Dettaglio ecografia →
                    </a>
                </div>

            </div>

        </section>

        <!-- SOTTO-VISTE SPECIFICHE -->
        <section id="view-patologie-spalla" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal hover:text-caldo-coral mb-8 transition-colors" data-target="patologie">
                <span>← Torna a tutte le patologie</span>
            </a>
            <span class="text-xs font-semibold text-caldo-teal bg-caldo-tealLight px-3.5 py-1.5 rounded-full inline-block mb-3">
                Focus Specialistico
            </span>
            <h1 class="text-4xl sm:text-5xl font-serif text-caldo-text mb-6">Chirurgia della spalla.</h1>
            <p class="text-base text-caldo-muted leading-relaxed font-light mb-8">
                Trattiamo la patologia degenerativa e traumatica della spalla: lesioni della cuffia dei rotatori, instabilità articolare e protesi inversa con riabilitazione rapida.
            </p>
            <div class="pt-8 border-t border-caldo-borderSoft flex justify-between items-center">
                <span class="text-xs text-caldo-muted">Consulenza per la spalla</span>
                <a href="#contatti" class="nav-trigger btn-fluid-coral px-6 py-3 text-xs font-semibold" data-target="contatti">
                    Prenota un controllo per la spalla
                </a>
            </div>
        </section>

        <section id="view-patologie-gomito" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal mb-8" data-target="patologie">← Indietro</a>
            <h1 class="text-4xl font-serif text-caldo-text mb-4">Gomito: traumatologia e artroscopia</h1>
            <p class="text-caldo-muted">Rigidità, epicondilite resistente e rotture del tendine bicipite distale.</p>
        </section>
        <section id="view-patologie-mano" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal mb-8" data-target="patologie">← Indietro</a>
            <h1 class="text-4xl font-serif text-caldo-text mb-4">Mano e Polso</h1>
            <p class="text-caldo-muted">Tunnel carpale, dito a scatto, rizoartrosi del pollice.</p>
        </section>
        <section id="view-patologie-traumatologia-sportiva" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal mb-8" data-target="patologie">← Indietro</a>
            <h1 class="text-4xl font-serif text-caldo-text mb-4">Traumatologia Sportiva</h1>
            <p class="text-caldo-muted">Valutazione return-to-play per atleti amatoriali e professionisti.</p>
        </section>
        <section id="view-patologie-artroscopia" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal mb-8" data-target="patologie">← Indietro</a>
            <h1 class="text-4xl font-serif text-caldo-text mb-4">Chirurgia Artroscopica</h1>
            <p class="text-caldo-muted">Il metodo mini-invasivo a visione ottica diretta.</p>
        </section>
        <section id="view-patologie-ecografia-muscoloscheletrica" class="page-view max-w-4xl mx-auto px-6 py-16">
            <a href="#patologie" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal mb-8" data-target="patologie">← Indietro</a>
            <h1 class="text-4xl font-serif text-caldo-text mb-4">Ecografia Muscoloscheletrica</h1>
            <p class="text-caldo-muted">Diagnosi dinamica immediata con certificazione SIUMB.</p>
        </section>

        <!-- ========================================================
             VISTA 4: DOVE RICEVO (LE SEDI CON COLORI CALDI)
             ======================================================== -->
        <section id="view-sedi" class="page-view max-w-7xl mx-auto px-6 py-16">
            
            <a href="#home" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal hover:text-caldo-coral mb-8 transition-colors" data-target="home">
                <span>← Torna alla Home</span>
            </a>

            <div class="max-w-3xl mb-16 space-y-4">
                <span class="text-xs font-semibold text-caldo-teal bg-caldo-tealLight px-3.5 py-1.5 rounded-full inline-block">
                    Poli Ospedalieri e Ambulatori
                </span>
                <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text leading-tight">
                    Dove ricevo: le strutture in Toscana.
                </h1>
                <p class="text-base text-caldo-muted font-light leading-relaxed">
                    Un'unica segreteria centrale per prenotare visite e infiltrazioni vicino a te, con gli interventi ospedalieri concentrati al CESAT.
                </p>
            </div>

            <div class="grid md:grid-cols-2 gap-8">
                
                <!-- CESAT -->
                <div class="card-soft-gradient p-8 md:p-10 rounded-3xl space-y-6">
                    <div class="flex justify-between items-start">
                        <span class="bg-caldo-teal text-white text-[11px] font-semibold uppercase tracking-wider px-3.5 py-1.5 rounded-full">
                            Polo Ospedaliero di Eccellenza
                        </span>
                        <span class="text-xs text-caldo-muted">Fucecchio (FI)</span>
                    </div>
                    <div>
                        <h3 class="text-2xl font-serif text-caldo-text font-semibold">CESAT · Ospedale San Pietro Igneo</h3>
                        <p class="text-xs text-caldo-teal font-medium mt-1">Centro di Eccellenza Sostituzioni Articolari Toscana</p>
                    </div>
                    <div class="space-y-2 text-xs text-caldo-muted border-t border-caldo-borderSoft pt-4 font-light">
                        <p><strong>Indirizzo:</strong> Piazza Lavagnini, 5 · Fucecchio (FI)</p>
                        <p><strong>Attività:</strong> Interventi chirurgici in ricovero e day-surgery, protesica e artroscopia.</p>
                    </div>
                    <div class="pt-4 border-t border-caldo-borderSoft flex justify-between items-center">
                        <span class="text-xs text-caldo-muted">Ricoveri Ospedalieri</span>
                        <a href="tel:+393484331733" class="btn-fluid-ghost !py-2 !px-4 text-xs font-semibold">Info Ricoveri</a>
                    </div>
                </div>

                <!-- San Pietro -->
                <div class="card-soft-gradient p-8 md:p-10 rounded-3xl space-y-6">
                    <div class="flex justify-between items-start">
                        <span class="bg-caldo-coral text-white text-[11px] font-semibold uppercase tracking-wider px-3.5 py-1.5 rounded-full">
                            Ambulatorio Principale
                        </span>
                        <span class="text-xs text-caldo-muted">Fucecchio (FI)</span>
                    </div>
                    <div>
                        <h3 class="text-2xl font-serif text-caldo-text font-semibold">Studi Medici San Pietro</h3>
                        <p class="text-xs text-caldo-muted mt-1">Prime visite ortopediche, ecografie dinamiche e infiltrazioni</p>
                    </div>
                    <div class="space-y-2 text-xs text-caldo-muted border-t border-caldo-borderSoft pt-4 font-light">
                        <p><strong>Indirizzo:</strong> Piazza Lavagnini, 6 · Fucecchio (accanto all'ospedale)</p>
                        <p><strong>Orari:</strong> Su appuntamento (Lunedì – Giovedì)</p>
                    </div>
                    <div class="pt-4 border-t border-caldo-borderSoft flex justify-between items-center">
                        <span class="text-xs text-caldo-muted">Visite in studio</span>
                        <a href="#contatti" class="nav-trigger btn-fluid-coral !py-2 !px-4 text-xs font-semibold" data-target="contatti">Prenota a Fucecchio</a>
                    </div>
                </div>

                <!-- Peccioli -->
                <div class="card-soft-gradient p-8 md:p-10 rounded-3xl space-y-6">
                    <div class="flex justify-between items-start">
                        <span class="bg-caldo-salvia text-white text-[11px] font-semibold uppercase tracking-wider px-3.5 py-1.5 rounded-full">
                            Alta Valdera
                        </span>
                        <span class="text-xs text-caldo-muted">Peccioli (PI)</span>
                    </div>
                    <div>
                        <h3 class="text-2xl font-serif text-caldo-text font-semibold">Polo San Verano</h3>
                        <p class="text-xs text-caldo-muted mt-1">Visite specialistiche e screening per l'Alta Valdera</p>
                    </div>
                    <div class="space-y-2 text-xs text-caldo-muted border-t border-caldo-borderSoft pt-4 font-light">
                        <p><strong>Indirizzo:</strong> Località San Verano · Peccioli (PI)</p>
                        <p><strong>Caratteristiche:</strong> Comodo parcheggio e accessibilità al piano terra.</p>
                    </div>
                    <div class="pt-4 border-t border-caldo-borderSoft flex justify-between items-center">
                        <span class="text-xs text-caldo-muted">Ambulatorio Valdera</span>
                        <a href="#contatti" class="nav-trigger btn-fluid-ghost !py-2 !px-4 text-xs font-semibold" data-target="contatti">Prenota a Peccioli</a>
                    </div>
                </div>

                <!-- Pisa -->
                <div class="card-soft-gradient p-8 md:p-10 rounded-3xl space-y-6">
                    <div class="flex justify-between items-start">
                        <span class="bg-caldo-gold text-white text-[11px] font-semibold uppercase tracking-wider px-3.5 py-1.5 rounded-full">
                            Sport & Movimento
                        </span>
                        <span class="text-xs text-caldo-muted">Pisa & Fornacette</span>
                    </div>
                    <div>
                        <h3 class="text-2xl font-serif text-caldo-text font-semibold">Athletica Pisa & Fisiomed</h3>
                        <p class="text-xs text-caldo-muted mt-1">Medicina dello sport, riabilitazione e atleti agonistici</p>
                    </div>
                    <div class="space-y-2 text-xs text-caldo-muted border-t border-caldo-borderSoft pt-4 font-light">
                        <p><strong>Sedi:</strong> Pisa centro e Fornacette (Calcinaia)</p>
                        <p><strong>Focus:</strong> Traumi sportivi e test per il return-to-play.</p>
                    </div>
                    <div class="pt-4 border-t border-caldo-borderSoft flex justify-between items-center">
                        <span class="text-xs text-caldo-muted">Valutazione Atleti</span>
                        <a href="#contatti" class="nav-trigger btn-fluid-ghost !py-2 !px-4 text-xs font-semibold" data-target="contatti">Prenota a Pisa</a>
                    </div>
                </div>

            </div>

        </section>

        <!-- ========================================================
             VISTA 5: NOTE CLINICHE (IL QUADERNO RIVISITATO: EDITORIALE CALDO)
             ======================================================== -->
        <section id="view-articoli" class="page-view max-w-5xl mx-auto px-6 py-16">
            
            <a href="#home" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal hover:text-caldo-coral mb-8 transition-colors" data-target="home">
                <span>← Torna alla Home</span>
            </a>

            <div class="max-w-3xl mb-16 space-y-4">
                <span class="text-xs font-semibold text-caldo-teal bg-caldo-tealLight px-3.5 py-1.5 rounded-full inline-block">
                    Divulgazione Scientifica
                </span>
                <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text leading-tight">
                    Note cliniche: la medicina spiegata con chiarezza.
                </h1>
                <p class="text-base text-caldo-muted font-light leading-relaxed">
                    Nessun contenuto pubblicitario: solo riflessioni tratte dagli studi clinici pubblicati con l'équipe dell'Ospedale CESAT.
                </p>
            </div>

            <!-- Articolo in Evidenza Remplissage -->
            <a href="#articoli-remplissage" class="nav-trigger block card-soft-gradient p-8 md:p-12 rounded-3xl group" data-target="articoli-remplissage">
                <div class="flex items-center gap-3 mb-4">
                    <span class="bg-caldo-coralLight text-caldo-coral text-xs font-semibold px-3 py-1 rounded-full">
                        Pubblicazione CESAT
                    </span>
                    <span class="text-xs text-caldo-muted">Osteology 2022</span>
                </div>

                <h2 class="text-2xl sm:text-3xl font-serif text-caldo-text group-hover:text-caldo-teal transition-colors mb-4 leading-snug">
                    Il dubbio nel remplissage: conciliare stabilità e rotazione nella spalla dello sportivo.
                </h2>

                <p class="text-sm text-caldo-muted leading-relaxed mb-6 font-light">
                    Nelle lussazioni recidivanti con perdita ossea dell'omero (Hill-Sachs), colmare il difetto con il tendine infraspinato impedisce nuove fuoriuscite. I risultati a due anni su mobilità e ritorno allo sport.
                </p>

                <div class="flex items-center justify-between border-t border-caldo-borderSoft pt-4 text-xs">
                    <span class="font-medium text-caldo-text">Dott. Michele Novi et al.</span>
                    <span class="font-semibold text-caldo-teal group-hover:translate-x-1 transition-transform inline-flex items-center gap-1">
                        Leggi la nota completa →
                    </span>
                </div>
            </a>

        </section>

        <!-- SOTTO-VISTA DETTAGLIO ARTICOLO REMPLISSAGE -->
        <section id="view-articoli-remplissage" class="page-view max-w-3xl mx-auto px-6 py-16">
            <a href="#articoli" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal hover:text-caldo-coral mb-8" data-target="articoli">
                ← Torna alle Note cliniche
            </a>

            <div class="flex items-center gap-3 text-xs text-caldo-muted mb-4">
                <span class="bg-caldo-tealLight text-caldo-teal font-semibold px-3 py-1 rounded-full">Paper 2022</span>
                <span>DOI: 10.3390/osteology2040021</span>
            </div>

            <h1 class="text-3xl sm:text-5xl font-serif text-caldo-text leading-tight mb-8">
                Il dubbio nel remplissage: quando la stabilità rischia di sacrificare il movimento.
            </h1>

            <div class="space-y-6 text-base text-caldo-muted leading-relaxed font-light">
                <p class="text-lg text-caldo-text font-normal italic border-l-4 border-caldo-teal pl-4 bg-caldo-tealLight/40 py-3 rounded-r-2xl">
                    «Il timore del chirurgo che affronta la lussazione di spalla è duplice: riparare troppo poco e rischiare una recidiva, o bloccare troppo rigidamente e ridurre la rotazione esterna del braccio.»
                </p>
                <p>
                    Nelle lussazioni recidivanti, l'impatto tra testa dell'omero e ciglio glenoideo produce la lesione di Hill-Sachs. Nelle rotazioni del braccio, questa lesione funge da leva che scardina l'articolazione.
                </p>
                <h3 class="text-2xl font-serif text-caldo-text font-semibold pt-4">La procedura di Remplissage</h3>
                <p>
                    Suturando parte della capsula e dell'infraspinato nel difetto, la lesione viene esclusa dal giunto articolare: la spalla torna a scivolare in modo fluido senza punti di inceppamento. I nostri dati dimostrano una perdita media di rotazione inferiore a 4 gradi, garantendo al contempo zero recidive.
                </p>
            </div>

            <div class="mt-12 p-6 bg-white rounded-3xl border border-caldo-borderSoft flex justify-between items-center shadow-sm">
                <span class="text-xs text-caldo-muted font-medium">Vuoi una valutazione per la tua spalla?</span>
                <a href="#contatti" class="nav-trigger btn-fluid-coral px-6 py-2.5 text-xs font-semibold" data-target="contatti">
                    Contatta la segreteria
                </a>
            </div>
        </section>

        <!-- ========================================================
             VISTA 6: CONTATTI (SERENO, ACCOGLIENTE, ZERO STRESS)
             ======================================================== -->
        <section id="view-contatti" class="page-view max-w-6xl mx-auto px-6 py-16">
            
            <a href="#home" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal hover:text-caldo-coral mb-8 transition-colors" data-target="home">
                <span>← Torna alla Home</span>
            </a>

            <div class="max-w-3xl mb-16 space-y-4">
                <span class="text-xs font-semibold text-caldo-coral bg-caldo-coralLight px-3.5 py-1.5 rounded-full inline-block">
                    Contatto Diretto
                </span>
                <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text leading-tight">
                    Prenotazioni e Segreteria.
                </h1>
                <p class="text-base text-caldo-muted font-light leading-relaxed">
                    Siamo a disposizione per concordare la tua prima visita, un controllo post-operatorio o informazioni sui ricoveri ospedalieri.
                </p>
            </div>

            <div class="grid lg:grid-cols-12 gap-12 items-start">
                
                <!-- Box Telefono e WhatsApp -->
                <div class="lg:col-span-5 space-y-6">
                    
                    <div class="card-soft-gradient p-8 rounded-3xl space-y-6">
                        <div class="space-y-1">
                            <span class="text-xs text-caldo-muted block">Numero Unico della Segreteria</span>
                            <a href="tel:+393484331733" class="text-3xl sm:text-4xl font-serif text-caldo-teal font-normal hover:text-caldo-coral transition-colors">
                                348 4331733
                            </a>
                        </div>

                        <div class="space-y-2.5 text-xs text-caldo-muted border-t border-caldo-borderSoft pt-4 font-light">
                            <p><strong>Orari chiamate:</strong> Lunedì – Giovedì dalle 15:30 alle 17:30</p>
                            <p><strong>WhatsApp:</strong> Attivo per richieste disponibilità appuntamenti</p>
                        </div>

                        <!-- Bottone WhatsApp Diretto -->
                        <a href="https://wa.me/393484331733?text=Buongiorno%2C%20vorrei%20richiedere%20informazioni%20per%20una%20visita%20con%20il%20Dott.%20Novi" 
                           target="_blank" 
                           class="w-full inline-flex items-center justify-center gap-2 py-3 px-4 rounded-2xl bg-[#25D366] text-white font-semibold text-xs shadow-sm hover:opacity-90 transition-opacity">
                            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
                                <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.275.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.1.824z"/>
                            </svg>
                            <span>Invia messaggio WhatsApp</span>
                        </a>
                    </div>

                    <div class="bg-white/80 p-6 rounded-3xl border border-caldo-borderSoft text-xs text-caldo-muted space-y-1.5 font-light">
                        <strong class="text-caldo-teal block font-semibold">Consiglio per il messaggio:</strong>
                        <p>Indica nome, sede desiderata (Fucecchio, Peccioli, Fornacette, Pisa) e breve motivo della visita (es. "dolore spalla destra").</p>
                    </div>

                </div>

                <!-- Modulo di Richiesta Caldo -->
                <div class="lg:col-span-7 card-soft-gradient p-8 md:p-12 rounded-3xl">
                    
                    <div class="mb-8">
                        <h3 class="text-2xl font-serif text-caldo-text font-semibold">Richiesta di contatto online</h3>
                        <p class="text-xs text-caldo-muted mt-1 font-light">La segreteria ti ricontatterà telefonicamente entro 24 ore lavorative.</p>
                    </div>

                    <form onsubmit="event.preventDefault(); alert('Grazie! La segreteria del Dott. Novi ti ricontatterà al più presto.');" class="space-y-6">
                        
                        <div class="grid sm:grid-cols-2 gap-6">
                            <div>
                                <label class="block text-xs font-semibold text-caldo-text mb-2">Nome e Cognome *</label>
                                <input type="text" required class="w-full border border-caldo-border p-3.5 text-sm rounded-2xl bg-white focus:outline-none focus:border-caldo-teal transition-colors" placeholder="Mario Rossi">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-caldo-text mb-2">Numero di Telefono *</label>
                                <input type="tel" required class="w-full border border-caldo-border p-3.5 text-sm rounded-2xl bg-white focus:outline-none focus:border-caldo-teal transition-colors" placeholder="340 0000000">
                            </div>
                        </div>

                        <div class="grid sm:grid-cols-2 gap-6">
                            <div>
                                <label class="block text-xs font-semibold text-caldo-text mb-2">Sede Preferita</label>
                                <select class="w-full border border-caldo-border p-3.5 text-sm rounded-2xl bg-white focus:outline-none focus:border-caldo-teal transition-colors">
                                    <option>Fucecchio (Studi San Pietro)</option>
                                    <option>Peccioli (Polo San Verano)</option>
                                    <option>Fornacette (Fisiomed)</option>
                                    <option>Pisa (Athletica)</option>
                                </select>
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-caldo-text mb-2">Articolazione</label>
                                <select class="w-full border border-caldo-border p-3.5 text-sm rounded-2xl bg-white focus:outline-none focus:border-caldo-teal transition-colors">
                                    <option>Spalla</option>
                                    <option>Gomito</option>
                                    <option>Mano o Polso</option>
                                    <option>Traumatologia dello Sport</option>
                                </select>
                            </div>
                        </div>

                        <div>
                            <label class="block text-xs font-semibold text-caldo-text mb-2">Note (Facoltativo)</label>
                            <textarea rows="3" class="w-full border border-caldo-border p-3.5 text-sm rounded-2xl bg-white focus:outline-none focus:border-caldo-teal transition-colors" placeholder="Indica se preferisci una fascia oraria per la chiamata..."></textarea>
                        </div>

                        <div class="flex items-start gap-3">
                            <input type="checkbox" required id="privacy-box" class="mt-1 accent-caldo-teal">
                            <label for="privacy-box" class="text-xs text-caldo-muted font-light leading-relaxed">
                                Acconsento al trattamento dei dati personali ai sensi del GDPR 679/2016 per essere ricontattato in merito alla visita.
                            </label>
                        </div>

                        <button type="submit" class="btn-fluid-coral w-full justify-center !py-4 text-sm font-semibold">
                            <span>Invia Richiesta</span>
                            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                                <path d="M5 12h14M12 5l7 7-7 7"/>
                            </svg>
                        </button>

                    </form>

                </div>

            </div>

        </section>

    </main>

    <!-- ============================================================
         FOOTER ARMONIOSO E PULITO
         ============================================================ -->
    <footer class="bg-white/80 backdrop-blur-md border-t border-caldo-borderSoft mt-32 py-16 px-6 relative z-10">
        <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-10 text-sm">
            
            <div class="space-y-3">
                <div class="font-serif text-2xl text-caldo-text font-normal">Dott. Michele Novi</div>
                <p class="text-xs text-caldo-muted font-light leading-relaxed">
                    Chirurgo Ortopedico Traumatologo.<br>
                    Dirigente Medico Ospedale CESAT Fucecchio.<br>
                    Iscritto all'Ordine dei Medici di Pisa n. 5988.
                </p>
            </div>

            <div class="space-y-2 text-xs font-light">
                <strong class="text-caldo-text uppercase font-semibold text-[11px] block mb-3">Navigazione</strong>
                <div><a href="#chi-sono" class="nav-trigger text-caldo-muted hover:text-caldo-teal" data-target="chi-sono">Chi sono</a></div>
                <div><a href="#patologie" class="nav-trigger text-caldo-muted hover:text-caldo-teal" data-target="patologie">Cosa curo (Patologie)</a></div>
                <div><a href="#sedi" class="nav-trigger text-caldo-muted hover:text-caldo-teal" data-target="sedi">Dove ricevo (Sedi)</a></div>
                <div><a href="#articoli" class="nav-trigger text-caldo-muted hover:text-caldo-teal" data-target="articoli">Note cliniche</a></div>
                <div><a href="#contatti" class="nav-trigger text-caldo-muted hover:text-caldo-teal" data-target="contatti">Contatti</a></div>
            </div>

            <div class="space-y-2 text-xs font-light">
                <strong class="text-caldo-text uppercase font-semibold text-[11px] block mb-3">Sedi Principali</strong>
                <p class="text-caldo-muted leading-relaxed">
                    <strong>CESAT Fucecchio:</strong> Piazza Lavagnini 5 (Chirurgia)<br>
                    <strong>Studi San Pietro:</strong> Piazza Lavagnini 6 (Visite)<br>
                    <strong>Valdera & Pisa:</strong> Peccioli, Fornacette, Pisa
                </p>
            </div>

            <div class="space-y-3 text-xs">
                <strong class="text-caldo-text uppercase font-semibold text-[11px] block mb-3">Segreteria Diretta</strong>
                <a href="tel:+393484331733" class="text-2xl font-serif text-caldo-teal block">
                    348 4331733
                </a>
                <p class="text-caldo-muted text-[11px] leading-relaxed font-light">
                    Chiamate: Lunedì – Giovedì 15:30 – 17:30.<br>
                    WhatsApp sempre disponibile per richieste disponibilità.
                </p>
            </div>

        </div>

        <div class="max-w-7xl mx-auto mt-12 pt-6 border-t border-caldo-borderSoft flex flex-col sm:flex-row justify-between items-center text-xs text-caldo-muted gap-4 font-light">
            <div>© 2026 Dott. Michele Novi</div>
            <div class="flex gap-6">
                <span>Informativa Privacy</span>
                <span>Cookie Policy</span>
                <span class="text-caldo-teal">Conforme Linee Guida Sanitarie FNOMCeO</span>
            </div>
        </div>
    </footer>

    <!-- ============================================================
         SCRIPT JS: APPARIZIONI MORBIDE & ROUTER SPA FLUIDO
         ============================================================ -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // 1. Intersection Observer per apparizioni morbide (reveal-soft)
            const revealElements = document.querySelectorAll('.reveal-soft');
            const revealObserver = new IntersectionObserver((entries) => {
                entries.forEach((entry, index) => {
                    if (entry.isIntersecting) {
                        setTimeout(() => {
                            entry.target.classList.add('is-visible');
                        }, index * 80);
                    }
                });
            }, { threshold: 0.1 });

            revealElements.forEach(el => revealObserver.observe(el));

            // 2. Router SPA fluido con animazione soft
            const navTriggers = document.querySelectorAll('.nav-trigger');
            const pageViews = document.querySelectorAll('.page-view');

            function switchView(targetId) {
                const targetEl = document.getElementById('view-' + targetId);
                if (!targetEl) return;

                pageViews.forEach(view => {
                    view.classList.remove('active-view');
                });
                
                targetEl.classList.add('active-view');
                window.scrollTo({ top: 0, behavior: 'smooth' });
                history.pushState(null, '', '#' + targetId);

                // Re-innesca le apparizioni morbide se presenti nella nuova vista
                setTimeout(() => {
                    const newReveals = targetEl.querySelectorAll('.reveal-soft');
                    newReveals.forEach(el => el.classList.add('is-visible'));
                }, 100);
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

# Salva in handoff_sito.html
target_path = "/Volumes/Programs/Temporary files/Progetti cursor/Michele_Novi_Website/handoff_sito.html"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_content)

# Salva anche in Proposte HTML/index.html
proposte_path = "/Volumes/Programs/Temporary files/Progetti cursor/Michele_Novi_Website/Proposte HTML/index.html"
with open(proposte_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Prototipo 'Gradienti Leggeri, Logo Tipografico & Movimenti Fluidi' generato con successo!")
