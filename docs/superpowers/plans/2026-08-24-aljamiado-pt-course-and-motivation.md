# Aljamiado Português Course (`curso.org`) & Motivation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a comprehensive, slow-paced course file `pt/curso.org` (and compiled `pt/curso.md`) for Portuguese speakers learning to write BR-Portuguese in the Persian alphabet, featuring early Gol He, form-based progression, full orthographic nuances, responsive vertical tables, and a beginner Nastaliq hide toggle; plus add the expanded motivation section to `pt/index.org`.

**Architecture:** Org-mode documentation (`.org`) exported to Markdown (`.md`) via `build.py`. Interactive UI features (Nastaliq toggle, script styling) supported via HTML export blocks and CSS/JS classes.

**Tech Stack:** Org-mode, Markdown, Python 3 (`build.py`), CSS Flexbox/Grid, Vanilla JS.

## Global Constraints

- Preserve all existing orthographic rules defined in `pt/index.org`.
- Both `pt/index.org` and `pt/curso.org` must include explicit Motivation sections with appropriate focus for each.
- `curso.org` must introduce Gol He in Lição 1 alongside non-connectors.
- Tables in `curso.org` must support both Naskh and Nastaliq display, defaulting to Naskh with a toggle to reveal/hide Nastaliq for beginners.
- On mobile (< 768px), tables must stack vertically in 1–2 columns.

---

### Task 1: Add Motivation Section to `pt/index.org`

**Files:**
- Modify: `pt/index.org:42-77`

**Interfaces:**
- Consumes: Existing header structure of `pt/index.org`.
- Produces: Complete Motivation section in `pt/index.org`.

- [ ] **Step 1: Edit `pt/index.org` to include Motivation section**

Add a dedicated `* Motivação e Objetivos` section right after `* Introdução e Visão Geral` covering:
1. Primary Goal: Tool for Brazilian Muslims and Lusophones to get closer to the Arabic alphabet and its mechanics through their native language.
2. Secondary Goal: Tool for other learners of Arabic and Persian.
3. Refugee Application: Helping Iranian and Afghani refugees learn Portuguese in a familiar script environment (adaptation of Persian alphabet).
4. Academic Context: Potential research on language learning, cross-script transfer, and second language acquisition at USP (Universidade de São Paulo).
5. Roadmap: Focus first on Portuguese speakers learning Aljamiado, with future tracking and planning for a Persophone Portuguese course.

- [ ] **Step 2: Verify `pt/index.org` syntax and structure**

Check that Org headings and export tags remain well-formed.

- [ ] **Step 3: Commit `pt/index.org` changes**

```bash
git add pt/index.org
git commit -m "docs: add motivation section to pt/index.org"
```

---

### Task 2: Create `pt/curso.org` Step-by-Step Pedagogical Course

**Files:**
- Create: `pt/curso.org`

**Interfaces:**
- Consumes: Orthographic rules from `pt/index.org`.
- Produces: `pt/curso.org` with 7 progressive form-based lessons and Naskh/Nastaliq parallel tables.

- [ ] **Step 1: Write `pt/curso.org` header & learner motivation section**

Include:
- `#+TITLE: Aljamiado Português: Curso Gradual de Escrita Perso-Árabe`
- `#+AUTHOR: Umar`
- Learner-focused motivation box.
- HTML export block for the Nastaliq Toggle button (*"👁️ Alternar Nastaliq (Estilo Persa)"*).

- [ ] **Step 2: Write Módulo 0 (Fundamentos do Alfabeto Perso-Árabe)**

Explain R&rarr;L direction, connective vs non-connective letters, 4 positional forms (Isolada, Inicial, Medial, Final), and diacritics vs. defective vowels.

- [ ] **Step 3: Write Lição 1 (Não-Conectores `ا`, `و`, `ر`, `ز` e Gol He `ہ` / `ـه`)**

Cover non-connecting forms AND Gol He final for unstressed final vowels (*-a*, *-e*, *-o*).
Table with side-by-side Naskh and Nastaliq: *a* (`ا`), *o* (`و`), *de* (`دہ`), *que* (`كہ`), *para* (`پرہ`), *ou* (`او`), *ao* (`او`), *ar* (`ار`), *ver* (`ور`), *por* (`پور`), *voz* (`وز`), *dor* (`دور`).

- [ ] **Step 4: Write Lição 2 (Traço Baixo: `ب`, `پ`, `ت` e Gancho Dāl: `د`)**

Cover lower stroke family and Dāl.
Table: *de* (`دہ`), *do* (`دو`), *da* (`دا`), *tudo* (`تودو`), *até* (`اتى`), *boa* (`بوہ`), *bom* (`بم`).

- [ ] **Step 5: Write Lição 3 (Cúpulas & Hastes: `ك`, `گ` e Suportes Vocálicos Iniciais)**

Cover Kāf/Gāf and initial vowel supports (`ا`, `آ`, `او`, `ای`).
Table: *que* (`كہ`), *com* (`كم`), *como* (`كمو`), *cada* (`كدہ`), *vida* (`ویدہ`), *faz* (`فز`), *água* (`آگوہ`).

- [ ] **Step 6: Write Lição 4 (Laços Circulares: `م`, `ن`, `ی` e Motor de Nasalização)**

Cover Mīm, Nūn, Ye, and nasal diphthongs (-ão, -ãe, -õe).
Table: *em* (`ام`), *um* (`اوم`), *uma* (`اومہ`), *não* (`ناو`), *na* (`نہ`), *no* (`نو`), *nem* (`نم`), *mais* (`میس`), *minha* (`مینیہ`).

- [ ] **Step 7: Write Lição 5 (Dentes `س`, `ش`, Barrigas `چ`, `ژ` e Hiato vs Ditongo)**

Cover Sīn, Shīn, Chā, Žā, and hiatus rules (*país* vs *pais*).
Table: *se* (`سہ`), *seu* (`سیo`), *sua* (`سوه`), *paz* (`پز`), *já* (`ژا`), *hoje* (`وهژہ`), *chega* (`چگہ`), *país* (`پایئس`), *pais* (`پایها`).

- [ ] **Step 8: Write Lição 6 (Hastes Altas `ل`, Dígrafos `ل-ی`, `ن-ی` e RR `ه`)**

Cover Lām, LH, NH, and RR (`ه`).
Table: *ele* (`إلى`), *ela* (`إلہ`), *filho* (`فیلیو`), *caminho* (`كمینیہ`), *terra* (`تہہ`), *carro* (`كهو`).

- [ ] **Step 9: Write Lição 7 (Sufixo Nominal de Plural `-hā` / `ـها`)**

Cover `-hā` suffix and summary tables.
Table: *os* (`وها`), *as* (`اها`), *dos* (`دوها`), *das* (`داها`), *todos* (`تدوها`), *palavras* (`پلورها`).

- [ ] **Step 10: Commit `pt/curso.org`**

```bash
git add pt/curso.org
git commit -m "feat: add pt/curso.org gradual course specification"
```

---

### Task 3: Update `build.py` to Compile `pt/curso.org`

**Files:**
- Modify: `build.py:377-385`

**Interfaces:**
- Consumes: `convert_org_to_md` function in `build.py`.
- Produces: Generated `pt/curso.md` file upon running `python3 build.py`.

- [ ] **Step 1: Modify `build.py` to add `pt/curso.org` compilation**

Add `convert_org_to_md("pt/curso.org", "pt/curso.md")` inside `def build()`.

- [ ] **Step 2: Run `python3 build.py` to verify compilation**

Run: `python3 build.py`
Expected: `Successfully updated pt/curso.md from pt/curso.org` and zero errors.

- [ ] **Step 3: Commit `build.py` and `pt/curso.md`**

```bash
git add build.py pt/curso.md pt/index.md
git commit -m "build: compile pt/curso.org to pt/curso.md"
```

---

### Task 4: Add Beginner Nastaliq Toggle & Mobile CSS Styles to `pt/index.html`

**Files:**
- Modify: `pt/index.html`

**Interfaces:**
- Consumes: CSS font utility classes (`.aljamiado-nastaliq`, `.aljamiado-naskh`).
- Produces: JS function `toggleNastaliqVisibility()` and CSS rules `.hide-nastaliq`.

- [ ] **Step 1: Add CSS rules for Nastaliq visibility toggle & mobile responsiveness**

In `pt/index.html` `<style>` section, add:
```css
.hide-nastaliq .aljamiado-nastaliq,
.hide-nastaliq .nastaliq-col {
  display: none !important;
}
@media (max-width: 768px) {
  .course-table-grid {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }
}
```

- [ ] **Step 2: Add JS toggle function for Nastaliq visibility**

Add `toggleNastaliqVisibility()` function to toggle `.hide-nastaliq` class on `.course-container` or `body`.

- [ ] **Step 3: Test and commit changes to `pt/index.html`**

```bash
git add pt/index.html
git commit -m "feat: add nastaliq beginner toggle and responsive CSS to pt/index.html"
```

---

### Task 5: Final Verification & Build Check

**Files:**
- Verify: `pt/index.org`, `pt/index.md`, `pt/curso.org`, `pt/curso.md`, `build.py`, `pt/index.html`

- [ ] **Step 1: Execute `python3 build.py`**
- [ ] **Step 2: Verify `git status` is clean**
- [ ] **Step 3: Verify markdown files contain accurate headings and table structures**
