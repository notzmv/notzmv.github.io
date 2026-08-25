# Enrich pt/index.org with Balance of Constraints & Strategic Pitch Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enrich `pt/index.org` with comprehensive documentation on the balance of orthographic constraints, system genesis, 4-tier priority hierarchy, organic proficiency navigation, and pitch the system as a landmark educational/academic initiative (USP research, refugee integration, Lusophone Muslim bridging), then recompile `pt/index.html` and `pt/index.md` via `build.py`.

**Architecture:** Org-mode documentation (`pt/index.org`), compiled via `build.py` to `pt/index.html` and `pt/index.md`.

**Tech Stack:** Org-mode, Markdown, Python 3 (`build.py`), HTML5/CSS3.

## Global Constraints

- Preserve all existing orthographic rules and top 25 corpus sentences in `pt/index.org`.
- Keep AOM `اوم` standard for `-ão`, Didactic Tanwīn exact spellings, and clean section headers.
- Recompile `pt/index.html` and `pt/index.md` cleanly via `python3 build.py`.

---

### Task 1: Enrich `pt/index.org` Content

**Files:**
- Modify: `pt/index.org`

**Interfaces:**
- Consumes: Existing structure of `pt/index.org`, concepts from genesis and organic proficiency plans.
- Produces: Updated `pt/index.org` with enriched early section on balance of constraints & expanded strategic pitch.

- [ ] **Step 1: Insert "Gênese do Sistema e O Balanço de Restrições Ortográficas" subsection under "Introdução e Visão Geral" in `pt/index.org`**
  - Cover Persian genesis, vowel frequency mismatch (A, O, E vs I, U), bottleneck of manual diacritics, transition to Mater Lectionis by Phonetic Proximity.
  - Detail the 3 core trade-offs: Economia vs. Legibilidade, Velocidade vs. Clareza (logograma `-hā`), Fidelidade Fonética vs. Identidade Radical.
  - Document the 4-tier hierarchy of orthographic priorities.
  - Detail organic proficiency navigation (slanted sliding scale) and personal aesthetic taste.

- [ ] **Step 2: Expand "Motivação e Visão Estratégica" section in `pt/index.org` into a comprehensive project pitch**
  - Pitch Aljamiado Português as a formal orthographic standard and educational initiative.
  - Highlight 5 core pillars:
    1. Aproximação Nativa ao Alfabeto Perso-Árabe para Lusófonos e Revertidos.
    2. Transição Pedagógica para Estudantes de Árabe, Persa e Urdu.
    3. Acolhimento e Integração Social de Refugiados Persófonos (Iranianos, Afegãos, Tadjiques).
    4. Pesquisa Acadêmica e Psicolinguística na Universidade de São Paulo (USP).
    5. Ecossistema Completo e Roteiro de Expansão (curso gradual `curso.org`, tipografia dupla Naskh/Nastaliq, pipeline `build.py`, futura trilha para persófonos).

---

### Task 2: Build & Verification

**Files:**
- Modify: `pt/index.html`, `pt/index.md`
- Script: `scratch/verify_enrich_index.py`

- [ ] **Step 1: Recompile files via `python3 build.py`**
  - Run: `python3 build.py`
  - Verify: `pt/index.html` and `pt/index.md` updated cleanly.

- [ ] **Step 2: Run python verification script confirming all new sections exist in org, html, and md**
  - Run: `python3 scratch/verify_enrich_index.py`
  - Expected: PASS with zero errors.

- [ ] **Step 3: Commit to Git**
  - Run: `git add pt/index.org pt/index.html pt/index.md docs/superpowers/plans/2026-08-25-enrich-index-balance-and-pitch-plan.md`
  - Run: `git commit -m "feat(pt): enrich pt/index with balance of constraints, priority hierarchy, and strategic project pitch"`
