# Fix Arabic Text Settings Uniformity Across pt/index.html & pt/index.org Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ensure ALL Perso-Arabic text examples throughout `pt/index.html` (both before and after the corpus cards) and `pt/index.org` share the exact same styling settings: wrapped in `<span class="ar">` (or Org equivalent) with proper font family (Naskh/Nastaliq), RTL direction, color, size, and live font toggle reactivity.

**Architecture:** HTML5 (`pt/index.html`), Org-mode (`pt/index.org`), Markdown (`pt/index.md`), Python (`build.py`).

**Tech Stack:** HTML5, CSS3, Org-mode, Python 3.

## Global Constraints

- Every single Perso-Arabic text snippet before AND after the corpus cards must be wrapped in `<span class="ar">...</span>` (or `<code class="ar">...</code>`).
- Ensure `body.font-naskh .ar` and `body.font-nastaliq .ar` apply uniformly to all Arabic snippets across the entire document.
- Preserve all existing orthographic rules, Didactic Tanwīn spellings, AOM standard (`-ão = اوم`), and top 25 corpus cards intact.
- Recompile `pt/index.md` via `python3 build.py`.

---

### Task 1: Audit & Replace All Arabic Code Snippets with `<span class="ar">` in `pt/index.html`

**Files:**
- Modify: `pt/index.html`

- [ ] **Step 1: Write a python script to scan and replace all Arabic text snippets in `pt/index.html` before and after cards with `<span class="ar">...</span>`**
  - Identify all Arabic characters/words (e.g. `ـها`, `س`, `چ`, `ژ`, `ر`, `ه`, `ز`, `ا`, `بم`, `بوم`, `جنرزددہ`, `كنایها`, `پایس`, `پایها`, `هیتو`, `فی`, `اتی`, `پو`, `پرچسو`, `جنتہ`, `سبدریہ`, `سبدوریا`, `ناوم`, `كاوم`, `پاوم`, `ماوم`, `كرچاوم`, `گرتیداوم`, `اتنچاوم`, `اچاوم`, `كنونچاوم`, `ویزاوم`, `مساوم`, `رزاوم`, `پاو`, `ماو`, `گراو`, `ـچو`, `ـچومها`, `ـچویها`, `ـزاوم`, `ـزومها`, `ـزویها`, `ـساوم`, `ـسومها`, `ـایها`, `پرًتكہ`, `مٍنمو`, `استٌپدو`, `ـً`, `ـٍ`, `ـٌ`, `م`, `ن`, etc.).
  - Wrap any Arabic snippet currently inside plain `<code>` or `<span>` with `<span class="ar">...</span>`.

- [ ] **Step 2: Update CSS in `pt/index.html` to refine `.ar` inline display**
  - Ensure `.ar` inline elements within paragraphs/lists have `display: inline-block; font-size: 1.5rem; line-height: 1.4; vertical-align: middle; margin: 0 0.15rem;` so they render cleanly in prose without disrupting line spacing while remaining prominent and toggle-reactive.

---

### Task 2: Build & Verification

**Files:**
- Modify: `pt/index.html`, `pt/index.org`, `pt/index.md`
- Script: `scratch/verify_arabic_settings.py`

- [ ] **Step 1: Run `python3 build.py`**
  - Run: `python3 build.py`

- [ ] **Step 2: Run verification script confirming ZERO plain `<code>` tags containing Arabic characters exist in `pt/index.html`**
  - Run: `python3 scratch/verify_arabic_settings.py`
  - Expected: PASS with zero plain Arabic code tags.

- [ ] **Step 3: Commit to Git**
  - Run: `git add pt/index.html pt/index.org pt/index.md docs/superpowers/plans/2026-08-25-fix-arabic-text-settings-uniformity-plan.md`
  - Run: `git commit -m "fix(css): unify Arabic text settings before and after cards in pt/index.html"`
