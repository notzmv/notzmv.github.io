# Arabic Font Sizing Expansion Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Increase the Arabic font sizes everywhere across `pt/index.html` and `index.html` (to ~2.0rem-2.2rem), and increase it even more in `pt/curso.html` (to ~2.3rem-2.6rem) so that dots, teeth, and loops are ultra-legible for beginners.

**Architecture:**
- `pt/index.html` & `index.html`: Update `.ar`, `.perso-arabic`, `.aljamiado-naskh` (from 1.6rem to 2.0rem), `.aljamiado-nastaliq` (from 1.7rem to 2.2rem).
- `pt/curso.html`: Update `.aljamiado-naskh` to `2.3rem` (or `2.4rem`) and `.aljamiado-nastaliq` to `2.6rem` with `line-height: 2.6`.
- `build.py`: Ensure any inline HTML styling matches these expanded font dimensions.

**Tech Stack:** CSS3, HTML5, Python 3 (`build.py`).

---

### Task 1: Increase Arabic Font Sizes in `pt/index.html` and `index.html`

**Files:**
- Modify: `pt/index.html`, `index.html`

- [ ] **Step 1: Update CSS rules in `pt/index.html`**
  Set `.aljamiado-naskh`: `font-size: 2.0rem; line-height: 1.9;`
  Set `.aljamiado-nastaliq`: `font-size: 2.2rem; line-height: 2.4;`

- [ ] **Step 2: Update CSS rules in `index.html`**
  Set `.aljamiado-naskh`: `font-size: 2.0rem; line-height: 1.9;`
  Set `.aljamiado-nastaliq`: `font-size: 2.2rem; line-height: 2.4;`

---

### Task 2: Extra Font Size Expansion in `pt/curso.html`

**Files:**
- Modify: `pt/curso.html`

- [ ] **Step 1: Update CSS rules in `pt/curso.html`**
  Set `.aljamiado-naskh`: `font-size: 2.3rem; line-height: 2.0; font-weight: 600;`
  Set `.aljamiado-nastaliq`: `font-size: 2.6rem; line-height: 2.6;`

---

### Task 3: Build & Verification

- [ ] **Step 1: Run `python3 build.py`**

- [ ] **Step 2: Run Python verification script checking font sizes in HTML files**

- [ ] **Step 3: Commit to Git**

```bash
git add pt/index.html index.html pt/curso.html build.py docs/superpowers/plans/2026-08-24-arabic-font-size-expansion-plan.md
git commit -m "style: increase Arabic font sizes site-wide and add extra enlargement to curso for beginner legibility"
```
