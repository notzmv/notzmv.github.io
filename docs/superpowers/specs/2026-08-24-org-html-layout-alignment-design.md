# Design Spec: Org → HTML Layout & Pipeline Alignment

## Goal
Restructure `index.html` (English) and `pt/index.html` (Portuguese) to mirror the layout, section sequence, Table of Contents, and detailed content of their respective Org-mode source files (`index.org` and `pt/index.org`), and update `build.py` to maintain both documents in sync.

---

## 1. Page Hierarchy & Structure

Both HTML pages will be structured as follows:

1. **Header & Sticky Control Panel**:
   - Page Title and Subtitle.
   - Sticky bar with:
     - **Font Selector**: Switches Persian/Arabic script font dynamically between `Gulzar Nastaliq`, `Noto Nastaliq Urdu` (or `Noto Nastaliq`), `Vazirmatn`, `Noto Naskh Arabic`, and `Aref Ruqaa`.
     - **Language Toggle**: Switches between 🇬🇧 English (`index.html`) and 🇵🇹 Português (`pt/index.html`).

2. **Table of Contents (TOC / Índice)**:
   - Navigational jump links corresponding to the Org `:toc:` header.

3. **Introduction & Overview / Introdução e Visão Geral**:
   - Full introductory text, architectural background (*Bismillah*, Aljamiado definition), core design principles.

4. **1. Consonant Inventory & Perso-Arabic Mapping / 1. Inventário Consonantal e Mapeamento Perso-Árabe**:
   - Consonant mapping table.
   - All subsections:
     - EN: Dental fricatives (th: Sā vs Zāl), Velar nasal (ng: Sağır Kāf vs Nūn-Gāf), Labials (v vs w), Palatals (ch, sh, j, zh).
     - PT: C/G/J mapping, R vs RR (Rā vs He), S vs SS (Zāy vs Sīn), Palatal Digraphs (lh, nh).

5. **2. Vowel System & Orthographic Carrier Engine / 2. Sistema Vocálico, Diacríticos e Acentuação**:
   - Master Vowel Rationale Table.
   - Initial Vowel Carriers / Alif Madd rules.
   - Matres Lectionis vs. Silent-e / Urdu Gol He (`ه`/`ـہ` vs `و`).
   - Tonic Alif (`ا`) & Accentuation Inference.
   - Defective Vowel Principle (Minimization of internal long vowels).

6. **3. Morphophonemic Rules & Domain Mapping / 3. Motor de Nasalização e Regras Morfofonêmicas**:
   - Styled Rule Boxes for:
     - Rule I: Nominal Plural Domain (`-hā` / `ـها`).
     - Rule II: Verbal Agreement & Lexical Sibilants (`س` / `ز`).
     - Rule III: Verbal Past Tense Domain (`-d`/`-t`: `ـد`/`ـت` for EN) / Surface Substitution (for PT).
     - Rule IV: Selective Silent He (for EN) / Nasalization Engine (for PT).

7. **4 / 5. Special Cases & Master Paradigm Lookup Tables / 4. Tabelas de Paradigmas Mestre & Casos Especiais**:
   - Tables for Determiners & Pronouns, Nominal & Adjectival Inflection, Verbal Paradigms, Prepositions, Singulares in -s/-z vs Plural.

8. **5 / 7. Corpus & Sample Transcriptions / 7. Corpus e Amostras de Transcrição**:
   - Interactive Corpus Cards with metadata, Latin original, IPA, Perso-Arabic rendering (styled `.ar`), and linguistic notes.
   - EN Corpus: 12 sentence benchmark cards.
   - PT Corpus: 15 sentence benchmark cards.

---

## 2. Pipeline (`build.py`) Automation

`build.py` will be expanded to:
- Convert `index.org` → `index.md` and `pt/index.org` → `pt/index.md`.
- Store sentence data arrays for both English and Portuguese corpora.
- Generate and update card blocks in both `index.html` and `pt/index.html`.
- Log success for both English and Portuguese targets.

---

## 3. Verification Plan

1. Run `python3 build.py` and ensure zero errors.
2. Verify section sequence in `index.html` matches `index.org`.
3. Verify section sequence in `pt/index.html` matches `pt/index.org`.
4. Test sticky font toggle and language switcher across browsers/resolutions.
