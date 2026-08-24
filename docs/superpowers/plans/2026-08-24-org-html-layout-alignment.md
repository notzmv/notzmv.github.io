# Org → HTML Layout & Pipeline Alignment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restructure `index.html` (English) and `pt/index.html` (Portuguese) to mirror the exact section layout, TOC, and content hierarchy of `index.org` and `pt/index.org`, and expand `build.py` to compile Org to MD and update HTML cards for both languages.

**Architecture:** Update `build.py` to handle both English and Portuguese Org files, MD exports, and Corpus card generations. Re-organize HTML files to match Org section order, including sticky font controls, TOC links, full section content, and interactive corpus cards.

**Tech Stack:** HTML5, CSS3 (CSS Variables, Flexbox), JavaScript (Vanilla font switcher), Python 3 (Regex, File I/O).

## Global Constraints

- **Language Support**: English (`index.html`) and Portuguese (`pt/index.html`).
- **Font Styling**: Preserve `.ar` / `.perso-arabic` styling with font switching for Gulzar, Noto Nastaliq Urdu (for EN), Vazirmatn, Noto Naskh Arabic, and Aref Ruqaa.
- **Header Controls**: Retain sticky top controls bar with language switcher and font buttons.

---

### Task 1: Update `build.py` for Dual-Language Processing

**Files:**
- Modify: `build.py`

**Interfaces:**
- Consumes: `index.org`, `pt/index.org`, `index.html`, `pt/index.html`
- Produces: Updated `index.md`, `pt/index.md`, `index.html`, `pt/index.html`

- [ ] **Step 1: Write updated `build.py` code**

Edit `build.py` to include sentence data for English (12 cards) and Portuguese (15 cards), convert Org files to MD for both EN and PT, and inject generated cards into `index.html` and `pt/index.html`.

- [ ] **Step 2: Test `build.py` execution**

Run: `python3 build.py`
Expected output: Success messages for updating both `index.md`, `pt/index.md`, `index.html` cards, and `pt/index.html` cards.

- [ ] **Step 3: Commit changes**

```bash
git add build.py
git commit -m "feat(build): expand build.py to process both EN and PT Org and HTML files"
```

---

### Task 2: Restructure `pt/index.html` to Match `pt/index.org`

**Files:**
- Modify: `pt/index.html`

**Interfaces:**
- Consumes: Section layout, TOC, and content from `pt/index.org`
- Produces: Fully aligned `pt/index.html`

- [ ] **Step 1: Update `pt/index.html` layout and sections**

Re-order sections in `pt/index.html`:
1. Header & Sticky Control Panel (Font Selector + Language Toggle).
2. Índice / Table of Contents (Anchor jump links).
3. Introdução e Visão Geral.
4. 1. Inventário Consonantal e Mapeamento Perso-Árabe (Table + Subsections: C/G/J, R vs RR, S vs SS, Palatals).
5. 2. Sistema Vocálico, Diacríticos e Acentuação (Vowel Table, Initial Carriers, Tonic Alif, Defective Vowels).
6. 3. Motor de Nasalização & Regras Morfofonêmicas (Rule I -hā, Rule II Surface substitution, Rule III Sīn/Zāy, Nasalization).
7. 4. Casos Especiais & Construções Particulares (Prepositions, Singular -s/-z, Hiatus, Clitics).
8. 5. Tabelas de Paradigmas Mestre (Determiners, Noun/Adjective Inflection).
9. 6. Corpus & Amostras de Transcrição (15 Cards).

- [ ] **Step 2: Verify `pt/index.html` layout**

Run `python3 build.py` to ensure card injection works cleanly on restructured `pt/index.html`.

- [ ] **Step 3: Commit changes**

```bash
git add pt/index.html
git commit -m "style(pt): restructure pt/index.html to align with pt/index.org layout"
```

---

### Task 3: Restructure `index.html` to Match `index.org`

**Files:**
- Modify: `index.html`

**Interfaces:**
- Consumes: Section layout, TOC, and content from `index.org`
- Produces: Fully aligned `index.html`

- [ ] **Step 1: Update `index.html` layout and sections**

Re-order sections in `index.html`:
1. Header & Sticky Control Panel (Font Selector + Language Toggle).
2. Table of Contents (Anchor jump links).
3. Introduction & Overview.
4. 1. Consonant Inventory & Perso-Arabic Mapping (Table + Subsections: Dental Fricatives, Velar Nasal, Labials, Palatals).
5. 2. Vowel System & Orthographic Carrier Engine (Vowel Rationale Table, Initial Carriers, Dual-Track Silent-e).
6. 3. Morphophonemic Rules & Domain Mapping (Rule I Nominal Plural -hā, Rule II Verbal Agreement Sīn/Zāy, Rule III Past Tense -d/-t, Rule IV Silent He).
7. 4. Master Paradigm Lookup Tables (Determiners, Nominal Inflection, Verbal Paradigms).
8. 5. Expanded Corpus & Sample Transcriptions (12 Cards).

- [ ] **Step 2: Verify `index.html` layout**

Run `python3 build.py` to ensure card injection works cleanly on restructured `index.html`.

- [ ] **Step 3: Commit changes**

```bash
git add index.html
git commit -m "style(en): restructure index.html to align with index.org layout"
```

---

### Task 4: Final Pipeline Verification & Validation

**Files:**
- Modify: `index.html`, `pt/index.html`, `build.py`

- [ ] **Step 1: Execute `build.py`**

Run: `python3 build.py`
Verify output: Clean execution without warnings or regex failure.

- [ ] **Step 2: Validate HTML structure and navigation**

Check TOC anchor links (`#1-consonant-inventory-perso-arabic-mapping`, etc.) in both `index.html` and `pt/index.html`.

- [ ] **Step 3: Commit final updates**

```bash
git add index.html pt/index.html build.py index.md pt/index.md
git commit -m "chore: verify build pipeline and final Org to HTML layout alignment"
```
