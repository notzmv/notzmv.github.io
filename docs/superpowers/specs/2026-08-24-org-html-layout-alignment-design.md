# Design Spec: Org → HTML Layout & Pipeline Alignment

## Goal
Restructure `index.html` (English) and `pt/index.html` (Portuguese) to mirror the exact layout, section sequence, sub-sections, Table of Contents, and detailed content of their respective Org-mode source files (`index.org` and `pt/index.org`). Replace the 5-button font bar with a prominent, large Naskh / Nasta'liq font toggle button at the top of both pages.

---

## 1. Top Control Bar & Font Toggle Design

Replace the multi-button font bar with a large, prominent single toggle button:
- **Button Label**: Displays current active font mode and click action (e.g. `✨ Script Style: Nasta'liq (Urdu Style) — Click to switch to Naskh`).
- **Modes**:
  1. **Nasta'liq Mode** (`font-nastaliq` / `font-gulzar`): Renders Perso-Arabic text in Urdu Nastaliq cursive font.
  2. **Naskh Mode** (`font-naskh`): Renders Perso-Arabic text in Noto Naskh Arabic font.
- **Language Switcher**: Retain `🇬🇧 English` / `🇵🇹 Português` links next to the big toggle button.

---

## 2. Page Hierarchy & Section Sequence

Both HTML pages follow the exact section order of their Org files:

### English (`index.html` matching `index.org`):
1. **Header & Sticky Control Bar**: Title, Subtitle, Large Naskh / Nasta'liq Toggle Button, Language Switcher.
2. **Table of Contents**:
   - Introduction & Overview
   - 1. Consonant Inventory & Perso-Arabic Mapping
   - 2. Vowel System & Orthographic Carrier Engine
   - 3. Morphophonemic Rules & Domain Mapping
   - 4. Master Paradigm Lookup Tables
   - 5. Expanded Corpus & Sample Transcriptions
3. **Introduction & Overview**
4. **1. Consonant Inventory & Perso-Arabic Mapping** (Table + Subsections for Dental fricatives, Velar nasal, Labials, Palatals)
5. **2. Vowel System & Orthographic Carrier Engine** (Rationale Table, Initial Carriers, Dual-Track Silent-e)
6. **3. Morphophonemic Rules & Domain Mapping** (Rule I Nominal Plural -hā, Rule II Verbal Agreement Sīn/Zāy, Rule III Past Tense -d/-t, Rule IV Silent He)
7. **4. Master Paradigm Lookup Tables** (Determiners & Pronouns, Nominal & Adjectival Inflection, Verbal Paradigms)
8. **5. Expanded Corpus & Sample Transcriptions** (Subsections with Pangrams, Literature, Speeches, Tech, Poetry + 12 Corpus Cards)

### Portuguese (`pt/index.html` matching `pt/index.org`):
1. **Header & Sticky Control Bar**: Title, Subtitle, Large Naskh / Nasta'liq Toggle Button, Language Switcher.
2. **Índice (Table of Contents)**:
   - Introdução e Visão Geral
   - 1. Inventário Consonantal e Mapeamento Perso-Árabe
   - 2. Sistema Vocálico, Diacríticos e Acentuação
   - 3. Motor de Nasalização
   - 4. Regras Morfofonêmicas e Mapeamento de Domínio
   - 5. Casos Especiais e Construções Particulares
   - 6. Tabelas de Paradigmas Mestre
   - 7. Corpus e Amostras de Transcrição
3. **Introdução e Visão Geral**
4. **1. Inventário Consonantal e Mapeamento Perso-Árabe** (Tabela + Subseções: C/G/J, R vs RR, S vs SS, Dígrafos)
5. **2. Sistema Vocálico, Diacríticos e Acentuação** (Gol He vs Waw, Suportes de Vogal Inicial, Alif Tónico, Avô vs Avó, Paroxítonas, Princípio Defectivo, Ditongos/Tritongos, Hiato/Hamzah)
6. **3. Motor de Nasalização** (Nasais Monossilábicas, -am/-em, Ditongos Nasais)
7. **4. Regras Morfofonêmicas e Mapeamento de Domínio** (Regra I -hā, Regra II Substituição de Superfície, Regra III Sīn/Zāy, -z Lexical Final)
8. **5. Casos Especiais e Construções Particulares** (Preposições de/da, Singulares em -s/-z vs Plural, Hiato vs Ditongos)
9. **6. Tabelas de Paradigmas Mestre** (Determinantes, Glossário Lingüístico, Flexão Nominal, Verbos vs Concordância)
10. **7. Corpus e Amostras de Transcrição** (15 Corpus Cards)

---

## 3. Pipeline (`build.py`) Automation

- `build.py` handles Org→MD conversion and card block injections.
- Run `python3 build.py` after updating HTML structures.
