# Collapsible Gênese Section & Reading Reminder Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the "A Gênese do Sistema e o Balanço de Restrições Ortográficas" section collapsible (hidden by default under an interactive toggle title) in `pt/index.html` and `pt/index.org`, and add a friendly callout reminding readers to explore it later for deep architectural background.

**Architecture:** HTML5 `<details>` & `<summary>` / Org-mode export block in `pt/index.html`, `pt/index.org`, and `pt/index.md`.

**Tech Stack:** HTML5, CSS3, Org-mode, Markdown, Python 3 (`build.py`).

## Global Constraints

- Closed by default using `<details>` and `<summary>` styling or CSS interactive toggle.
- Include a clear reminder callout box pointing readers to the Gênese section.
- Preserve all existing content, Arabic text `<span class="ar">` markup, and font toggle reactivity.
- Recompile `pt/index.md` via `python3 build.py`.

---

### Task 1: Update `pt/index.html` & `pt/index.org`

**Files:**
- Modify: `pt/index.html`, `pt/index.org`

- [ ] **Step 1: Wrap Gênese section in `<details>` / `<summary>` block in `pt/index.html`**
  - Use custom styled `<details class="genese-details">` with `<summary class="genese-summary">💡 A Gênese do Sistema e o Balanço de Restrições Ortográficas (Clique para expandir / Leitura Opcional)</summary>`.
  - Add CSS styles for `.genese-details` and `.genese-summary` (rounded border, hover glow, smooth cursor, clean padding).

- [ ] **Step 2: Add callout reminder box in `pt/index.html` and `pt/index.org`**
  - Add a callout box: `💡 Dica: Para compreender as escolhas de engenharia ortográfica, a inspiração persa e a hierarquia de prioridades, expanda a seção "Gênese do Sistema" acima quando desejar aprofundar.`

---

### Task 2: Build & Verification

**Files:**
- Modify: `pt/index.html`, `pt/index.org`, `pt/index.md`
- Script: `scratch/verify_collapsible_genese.py`

- [ ] **Step 1: Run `python3 build.py`**
  - Run: `python3 build.py`

- [ ] **Step 2: Run verification script confirming Gênese is in `<details>` block and reminder callout exists**
  - Run: `python3 scratch/verify_collapsible_genese.py`
  - Expected: PASS with zero errors.

- [ ] **Step 3: Commit to Git**
  - Run: `git add pt/index.html pt/index.org pt/index.md docs/superpowers/plans/2026-08-25-collapsible-genese-section-plan.md`
  - Run: `git commit -m "feat(pt): make Genese section collapsible by default and add reader reminder callout"`
