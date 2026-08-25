# Human Review Warning & Work-in-Progress Disclaimer Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a clear warning banner near the top of index and course pages (`pt/index.html`, `pt/index.org`, `pt/index.md`, `index.html`, `index.org`, `index.md`, `pt/curso.html`, `pt/curso.org`, `pt/curso.md`) notifying readers that the examples and transcrições are actively under development and have yet to be individually human-reviewed.

**Architecture:** HTML warning callout block (`.review-warning-box`) styled in CSS with amber/warning highlight, present in `.org` export blocks and compiled to `.html` and `.md`.

**Tech Stack:** HTML5, CSS3, Org-mode, Markdown, Python 3 (`build.py`).

## Global Constraints

- Prominently display the warning banner near the top of `pt/index.html`, `pt/index.org`, `index.html`, `index.org`, `pt/curso.html`, and `pt/curso.org`.
- Recompile all markdown files cleanly via `python3 build.py`.
- Preserve existing font toggles, card layouts, and collapsible sections intact.

---

### Task 1: Add Warning Banner to Portuguese & English Pages

**Files:**
- Modify: `pt/index.html`, `pt/index.org`, `pt/curso.html`, `pt/curso.org`, `index.html`, `index.org`

- [ ] **Step 1: Design & add styled CSS warning banner to `pt/index.html`, `pt/curso.html`, and `index.html`**
  - Add CSS rule `.review-warning-box` (amber/gold border, dark amber-transparent background `#f59e0b15`, clear text icon ⚠️).
  - Text (Portuguese): `⚠️ <strong>Nota de Trabalho em Andamento:</strong> As transcrições e exemplos ortográficos contidos nesta especificação e curso são rascunhos de desenvolvimento e <em>ainda serão revisados individualmente por revisores humanos</em>. Este projeto está sob constante aperfeiçoamento.`
  - Text (English): `⚠️ <strong>Work-in-Progress Notice:</strong> The orthographic transcriptions and examples in this specification are active drafts and <em>have yet to be individually human-reviewed</em>. This project is undergoing continuous refinement.`

- [ ] **Step 2: Add warning banner to `.org` source files (`pt/index.org`, `pt/curso.org`, `index.org`)**
  - Insert `#+BEGIN_EXPORT html` warning block near the top of each `.org` file.

---

### Task 2: Build & Verification

**Files:**
- Modify: `pt/index.md`, `index.md`, `pt/curso.md`
- Script: `scratch/verify_warning_banner.py`

- [ ] **Step 1: Run `python3 build.py`**
  - Run: `python3 build.py`

- [ ] **Step 2: Run verification script confirming warning banner exists in all target files**
  - Run: `python3 scratch/verify_warning_banner.py`
  - Expected: PASS with zero errors.

- [ ] **Step 3: Commit to Git**
  - Run: `git add pt/index.html pt/index.org pt/index.md index.html index.org index.md pt/curso.html pt/curso.org pt/curso.md docs/superpowers/plans/2026-08-25-human-review-warning-plan.md`
  - Run: `git commit -m "docs: add work-in-progress human review warning banner to top of all index and course pages"`
