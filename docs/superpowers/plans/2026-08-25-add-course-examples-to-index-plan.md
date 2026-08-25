# Add Course Examples & Vocabulary Range to Index Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Integrate the comprehensive range of step-by-step course vocabulary examples (from Lições 1 to 7 of `curso.org`) into `pt/index.org`, `pt/index.html`, and `pt/index.md` as an interactive reference section with Naskh and Nastaliq parallel views.

**Architecture:** Org-mode table / export block in `pt/index.org`, compiled via `build.py` to `pt/index.md` and rendered as HTML tables in `pt/index.html`.

**Tech Stack:** HTML5, CSS3, Org-mode, Markdown, Python 3 (`build.py`).

## Global Constraints

- Include the full range of vocabulary examples from Lições 1–7 of `curso.org`.
- Provide both Naskh and Nastaliq columns, with `<span class="ar">` styling and live font toggle reactivity.
- Include Português, Escrita Aljamiada (Naskh & Nastaliq), IPA, and Morphological Notes.
- Preserve all existing 25 corpus cards and master paradigm tables intact.
- Recompile `pt/index.md` via `python3 build.py`.

---

### Task 1: Create Course Vocabulary Table in `pt/index.org` & `pt/index.html`

**Files:**
- Modify: `pt/index.org`, `pt/index.html`

- [ ] **Step 1: Extract all vocabulary items from `pt/curso.org`**
  - Lição 1: Non-connectors (*a*, *da*, *do*, *vida*, *rio*, *ver*, *zero*, *paz*, *já*, *hoje*, *o*, *livro*).
  - Lição 2: Lower stroke & Dāl family (*bom*, *boa*, *para*, *pão*, *tu*, *tudo*, *até*, *de*, *cidade*).
  - Lição 3: Kāf/Gāf & Vowel Supports (*que*, *com*, *como*, *cada*, *gostei*, *água*, *fé*, *fazer*).
  - Lição 4: Nasals & Semi-vowels (*em*, *um*, *uma*, *não*, *nem*, *minha*, *dia*, *muito*).
  - Lição 5: Sibilantes, Affricates & Hiatos (*se*, *seu*, *sua*, *chave*, *chega*, *você*, *país*, *pais*).
  - Lição 6: Palatals, High Stems & RR (*ele*, *ela*, *filho*, *caminho*, *carro*, *terra*).
  - Lição 7: Plurals & Nominal Suffixes (*os*, *as*, *dos*, *das*, *todos*, *palavras*, *casas*).

- [ ] **Step 2: Add Section 8 ("Gama de Exemplos Didáticos e Vocabulário de Referência do Curso") to `pt/index.org` and `pt/index.html`**
  - Render as a clean, responsive HTML table with dual Naskh/Nastaliq font toggle reactivity and IPA notes.
  - Update Table of Contents in both `pt/index.org` and `pt/index.html`.

---

### Task 2: Build & Verification

**Files:**
- Modify: `pt/index.html`, `pt/index.org`, `pt/index.md`
- Script: `scratch/verify_course_examples_in_index.py`

- [ ] **Step 1: Run `python3 build.py`**
  - Run: `python3 build.py`

- [ ] **Step 2: Run verification script confirming Section 8 and course examples exist in org, html, and md**
  - Run: `python3 scratch/verify_course_examples_in_index.py`
  - Expected: PASS with zero errors.

- [ ] **Step 3: Commit to Git**
  - Run: `git add pt/index.html pt/index.org pt/index.md docs/superpowers/plans/2026-08-25-add-course-examples-to-index-plan.md`
  - Run: `git commit -m "feat(pt): introduce comprehensive course vocabulary examples range into pt/index"`
