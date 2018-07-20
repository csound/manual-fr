# -*- coding: utf8 -*-
# adapted from english cvs version=1.1

#categories and their order are defined here:
categories = ['Orchestra Syntax:Header',
              'Orchestra Syntax:Block Statements',
              'Orchestra Syntax:Macros',
              'Signal Generators:Additive Synthesis/Resynthesis',
              'Signal Generators:Basic Oscillators',
              'Signal Generators:Dynamic Spectrum Oscillators',
              'Signal Generators:FM Synthesis',
              'Signal Generators:Granular Synthesis',
              'Signal Generators:Hyper Vectorial Synthesis',
              'Signal Generators:Linear and Exponential Generators',
              'Signal Generators:Envelope Generators',
              'Signal Generators:Models and Emulations',
              'Signal Generators:Phasors',
              'Signal Generators:Random (Noise) Generators',
              'Signal Generators:Sample Playback',
              'Signal Generators:Scanned Synthesis',
              'Signal Generators:STK Opcodes',
              'Signal Generators:Table Access',
              'Signal Generators:Wave Terrain Synthesis',
              'Signal Generators:Waveguide Physical Modeling',
              'Signal I/O:File I/O',
              'Signal I/O:Signal Input',
              'Signal I/O:Signal Output',
              'Signal I/O:Software Bus',
              'Signal I/O:Printing and Display',
              'Signal I/O:Soundfile Queries',
              'Signal Modifiers:Amplitude Modifiers',
              'Signal Modifiers:Convolution and Morphing',
              'Signal Modifiers:Delay',
              'Signal Modifiers:Panning and Spatialization',
              'Signal Modifiers:Reverberation',
              'Signal Modifiers:Sample Level Operators',
              'Signal Modifiers:Signal Limiters',
              'Signal Modifiers:Special Effects',
              'Signal Modifiers:Standard Filters',
              'Signal Modifiers:Standard Filters:Resonant',
              'Signal Modifiers:Standard Filters:Control',
              'Signal Modifiers:Specialized Filters',
              'Signal Modifiers:Waveguides',
              'Signal Modifiers:Waveshaping',
              'Signal Modifiers:Comparators and Accumulators',
              'Instrument Control:Clock Control',
              'Instrument Control:Conditional Values',
              'Instrument Control:Compilation',
              'Instrument Control:Duration Control',
              'Instrument Control:Invocation',
              'Instrument Control:Program Flow Control',
              'Instrument Control:Realtime Performance Control',
              'Instrument Control:Initialization and Reinitialization',
              'Instrument Control:Sensing and Control',
              'Instrument Control:Stacks',
              'Instrument Control:Subinstrument Control',
              'Instrument Control:Time Reading',
              'Jacko Opcodes',
              'Lua Opcodes',
              'Serial I/O',
              'Table Control',
              'Table Control:Table Queries',
              'Table Control:Dynamic Selection',
              'Table Control:Read/Write Opreations',
              'FLTK:Containers',
              'FLTK:Valuators',
              'FLTK:Other',
              'FLTK:Appearance',
              'Mathematical Operations:Arithmetic and Logic Operations',
              'Mathematical Operations:Arrays',
              'Mathematical Operations:Comparators and Accumulators',
              'Mathematical Operations:Mathematical Functions',
              'Mathematical Operations:Trigonometric Functions',
              'Mathematical Operations:Amplitude Functions',
              'Mathematical Operations:Random Functions',
              'Mathematical Operations:Opcode Equivalents of Functions',
              'Mathematical Operations:Vectors',
              'Pitch Converters:Functions',
              'Pitch Converters:Tuning Opcodes',
              'Real-time MIDI:Input',
              'Real-time MIDI:Output',
              'Real-time MIDI:Converters',
              'Real-time MIDI:Generic I/O',
              'Real-time MIDI:Event Extenders',
              'Real-time MIDI:Note Output',
              'Real-time MIDI:MIDI/Score Interoperability',
              'Real-time MIDI:System Realtime',
              'Real-time MIDI:Slider Banks',
              'Signal Flow Graph Opcodes',
              'Spectral Processing:STFT',
              'Spectral Processing:LPC',
              'Spectral Processing:Non-Standard',
              'Spectral Processing:Streaming',
              'Spectral Processing:ATS',
              'Spectral Processing:Loris',
              'Spectral Processing:Other',
              'Strings:Definition',
              'Strings:Manipulation',
              'Strings:Conversion',
              'Vectorial:Tables',
              'Vectorial:Scalar operations',
              'Vectorial:Vectorial operations',
              'Vectorial:Envelopes',
              'Vectorial:Limiting and Wrapping',
              'Vectorial:Delay Paths',
              'Vectorial:Random',
              'Vectorial:Cellular Automata',
              'Zak Patch System',
              'Plugin Hosting:DSSI and LADSPA',
              'OSC',
              'Faust Opcodes',
              'Network',
              'Remote Opcodes',
              'Mixer Opcodes',
              'Ableton Link Opcodes',
              'Python Opcodes',
              'Image Processing Opcodes',
              'Arrays: Cepstrum',
              'Array Opcodes',
              'Array Operations: Fast Fourier Transform',
              'Array Operations: complex numbers',
              'Array Operations: Discrete Cosine Transform',
              'Array Operations: dot product',
              'Array Operations: Mel scale filterbank',
              'Array Operations: sorting',
              'Array Operations: Cepstrum',
              'Deprecated',
              'Miscellaneous',
              'Testing',
              'Utilities']

# catégories traduites en français :
translated_categories = ["Syntaxe de l'orchestre : en-tête",
              "Syntaxe de l'orchestre : bloc d'instructions",
              "Syntaxe de l'orchestre : macros",
              "Générateurs de signal : synthèse/resynthèse additive",
              "Générateurs de signal : oscillateurs élémentaires",
              "Générateurs de signal : oscillateurs à spectre dynamique",
              "Générateurs de signal : synthèse MF",
              "Générateurs de signal : synthèse granulaire",
              "Générateurs de signal : synthèse hyper vectorielle",
              "Générateurs de signal : générateurs linéaires et exponentiels",
              "Générateurs de signal : générateurs d'enveloppe",
              "Générateurs de signal : modèles et émulations",
              "Générateurs de signal : phaseurs",
              "Générateurs de signal : générateurs de nombres aléatoires (de bruit)",
              "Générateurs de signal : reproduction de sons échantillonnés",
              "Générateurs de signal : synthèse par balayage",
              "Générateurs de signal : opcodes STK",
              "Générateurs de signal : accès aux tables",
              "Générateurs de signal : synthèse par terrain d'ondes",
              "Générateurs de signal : modèles physiques par guide d'onde",
              "E/S de signal : E/S fichier",
              "E/S de signal : entrée de signal",
              "E/S de signal : sortie de signal",
              "E/S de signal : bus logiciel",
              "E/S de signal : impression et affichage",
              "E/S de signal : requêtes sur les fichiers sons",
              "Modificateurs de signal : modificateurs d'amplitude",
              "Modificateurs de signal : convolution et morphing",
              "Modificateurs de signal : retard",
              "Modificateurs de signal : panoramique et spatialisation",
              "Modificateurs de signal : réverbération",
              "Modificateurs de signal : opérateurs du niveau échantillon",
              "Modificateurs de signal : limiteurs de signal",
              "Modificateurs de signal : effets spéciaux",
              "Modificateurs de signal : filtres standard",
              "Modificateurs de signal : filtres standard : résonants",
              "Modificateurs de signal : filtres standard : contrôle",
              "Modificateurs de signal : filtres spécialisés",
              "Modificateurs de signal : guides d'onde",
              "Modificateurs de signal : distorsion non-linéaire",
              "Modificateurs de signal : comparateurs et accumulateurs",
              "Contrôle d'instrument : contrôle d'horloge",
              "Contrôle d'instrument : valeurs conditionnelles",
              "Contrôle d'instrument : compilation",
              "Contrôle d'instrument : contrôle de durée",
              "Contrôle d'instrument : appel d'instrument",
              "Contrôle d'instrument : contrôle séquentiel d'un programme",
              "Contrôle d'instrument : controle de l'exécution en temps réel",
              "Contrôle d'instrument : initialisation et réinitialisation",
              "Contrôle d'instrument : détection et contrôle",
              "Contrôle d'instrument : piles",
              "Contrôle d'instrument : contrôle de sous-instrument",
              "Contrôle d'instrument : lecture du temps",
              'Opcodes jacko',
              'Opcodes Lua',
              'E/S série',
              "Contrôle des tables de fonction",
              "Contrôle des tables de fonction : requêtes sur une table",
              "Contrôle des tables de fonction : sélection dynamique",
              "Contrôle des tables de fonction : opérations de lecture/écriture",
              "FLTK : conteneurs",
              "FLTK : valuateurs",
              "FLTK : autres",
              "FLTK : apparence",
              "Opérations mathématiques : opérations arithmétiques et logiques",
	          "Opérations mathématiques : tableaux",
	          "Opérations mathématiques : comparateurs et accumulateurs",
              "Opérations mathématiques : fonctions mathématiques",
              "Opérations mathématiques : fonctions trigonométriques",
              "Opérations mathématiques : fonctions d'amplitude",
              "Opérations mathématiques : fonctions aléatoires",
              "Opérations mathématiques : opcodes équivalents à des fonctions",
              "Opérations mathématiques : vecteurs",
              "Conversion des hauteurs : fonctions",
              "Conversion des hauteurs : opcodes de hauteurs",
              "MIDI en temps réel : entrée",
              "MIDI en temps réel : sortie",
	          "MIDI en temps réel : convertisseurs",
              "MIDI en temps réel : E/S génériques",
              "MIDI en temps réel : extension d'évènements",
              "MIDI en temps réel : sortie de note",
              "MIDI en temps réel : interopérabilité MIDI/partition",
              "MIDI en temps réel : système temsp réel",
              "MIDI en temps réel : banques de réglettes",
              "Graphe de fluence",
              "Traitement spectral : STFT",
              "Traitement spectral : LPC",
              "Traitement spectral : non-standard",
              "Traitement spectral : streaming",
              "Traitement spectral : ATS",
              "Traitement spectral : Loris",
              "Traitement spectral : autres",
              "Chaînes : définition",
              "Chaînes : manipulation",
              "Chaînes : conversion",
              "Vectoriel : tableaux",
              "Vectoriel : opérations scalaires",
              "Vectoriel : opérations vectorielles",
              "Vectoriel : enveloppes",
              "Vectoriel : limitation et enroulement",
              "Vectoriel : chemins de retard",
              "Vectoriel : aléatoire",
              "Vectoriel : automates cellulaires",
              "Système de patch zak",
              "Accueil de greffon : DSSI et LADSPA",
              "OSC",
              "Opcodes Faust",
              "Réseau",
              "Opcodes pour le traitement à distance",
              "Opcodes Mixer",
              "Opcodes Ableton Link",
              "Opcodes Python",
              "Opcodes pour le traitement d'image",
              "Tableaux : cepstre",
              "Opcodes de tableaux",
              "Opérations de tableau : transformée de Fourier rapide",
              "Opérations de tableau : nombres complexes",
              "Opérations de tableau : transformée cosinus discrète",
              "Opérations de tableau : produit scalaire",
              "Opérations de tableau : banc de filtres à échelle de Mel",
              "Opérations de tableau : tri",
              "Opérations de tableau : cepstre",
              "Opérations de tableau : obsolète",
              "Divers",
              "Essai",
              "Utilitaires"]

