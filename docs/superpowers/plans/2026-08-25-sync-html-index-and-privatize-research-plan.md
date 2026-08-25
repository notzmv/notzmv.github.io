# Synchronize pt/index.html & Privatize Research Details Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Remove private academic research/USP references from all public documentation (`pt/index.org`, `pt/index.md`), update `pt/index.html` to fully render all enriched sections (Genesis, Balance of Constraints, 4-Tier Hierarchy, Organic Navigation, and Public Pitch), and recompile via `build.py`.

**Architecture:** HTML5 (`pt/index.html`), Org-mode (`pt/index.org`), Markdown (`pt/index.md`), Python (`build.py`).

**Tech Stack:** HTML5, CSS3, Org-mode, Markdown, Python 3.

## Global Constraints

- Keep research/USP details strictly private — remove USP/academic research references from public index files.
- Fully mirror all enriched sections in `pt/index.html` so that users viewing `pt/index.html` see the complete balance of constraints and public pitch.
- Recompile `pt/index.md` from `pt/index.org` using `build.py`.

---

### Task 1: Privatize Research Details & Update `pt/index.org`

**Files:**
- Modify: `pt/index.org`

- [ ] **Step 1: Remove USP/Research item from `Motivação e Visão Estratégica` in `pt/index.org`**
  - Replace the USP/Academic Research item with a clean, public-facing focus on Linguistic Systematization & Orthographic Standards for Lusophony.
  - Retain the 4 public pillars:
    1. Aproximação Nativa ao Alfabeto Perso-Árabe para Lusófonos e Revertidos.
    2. Ferramenta de Transição Pedagógica para Estudantes de Árabe, Persa e Urdu.
    3. Acolhimento e Integração Social de Refugiados Persófonos (Iranianos, Afegãos e Tadjiques).
    4. Ecossistema Completo e Roteiro de Expansão Institucional.

---

### Task 2: Update `pt/index.html` to Match `pt/index.org` Content

**Files:**
- Modify: `pt/index.html`

- [ ] **Step 1: Add Table of Contents links & HTML sections to `pt/index.html`**
  - Update `#introducao-e-visao-geral` in `pt/index.html` to include:
    - `** A Gênese do Sistema e o Balanço de Restrições Ortográficas` (Persian genesis, vowel frequency mismatch, Mater Lectionis solution, 3 trade-offs, 4-tier hierarchy, organic proficiency navigation & aesthetic taste).
    - `** Motivação e Visão Estratégica` (4 public pillars, omitting private research details).
  - Ensure all styles (collapsible/card boxes, headings, lists, code spans) match `pt/index.html` design system.

---

### Task 3: Build & Verification

**Files:**
- Modify: `pt/index.md`, `pt/index.html`
- Script: `scratch/verify_sync_index.py`

- [ ] **Step 1: Run `python3 build.py`**
  - Run: `python3 build.py`
  - Verify: `pt/index.md` updated cleanly from `pt/index.org`.

- [ ] **Step 2: Run verification script confirming zero USP references and full HTML sync**
  - Run: `python3 scratch/verify_sync_index.py`
  - Expected: PASS with zero errors.

- [ ] **Step 3: Commit to Git**
  - Run: `git add pt/index.org pt/index.html pt/index.md docs/superpowers/plans/2026-08-25-sync-html-index-and-privatize-research-plan.md`
  - Run: `git commit -m "feat(pt): sync pt/index.html with pt/index.org and keep research details private"`
