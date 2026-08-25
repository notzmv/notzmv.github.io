# Font, Color & Dual-Script Cards Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:**
1. Fix Naskh font in `pt/curso.html` to use clean `'Noto Naskh Arabic'` (instead of Amiri).
2. Apply the pink/rose (`#f472b6`) and yellow/gold (`#fbbf24`) color scheme to all Arabic script in `pt/curso.html`.
3. Add dual Naskh + Nastaliq rendering to all sentence cards in `pt/index.html`, `index.html`, and `build.py`.

**Architecture:**
- `pt/curso.html`: Import `Noto Naskh Arabic` & `Vazirmatn`. Set `.aljamiado-naskh` to `#f472b6` (pink/rose) and `.aljamiado-nastaliq` to `#fbbf24` (yellow/gold).
- `build.py`: Update `update_pt_cards()` and `update_en_cards()` card HTML generators to output both `.aljamiado-naskh` and `.aljamiado-nastaliq` blocks for each sentence.
- `pt/index.html` & `index.html`: Update CSS rules to support dual Naskh + Nastaliq card layouts.

---

### Task 1: Update Fonts and Colors in `pt/curso.html`

**Files:**
- Modify: `pt/curso.html`

- [ ] **Step 1: Update Google Fonts link in `pt/curso.html`**
  Import `Noto Naskh Arabic` and `Vazirmatn`.

- [ ] **Step 2: Update CSS font-family and colors for Naskh & Nastaliq in `pt/curso.html`**
  Set `.aljamiado-naskh`: `font-family: 'Noto Naskh Arabic', 'Vazirmatn', 'Amiri', serif; color: #f472b6;`
  Set `.aljamiado-nastaliq`: `font-family: 'Noto Nastaliq Urdu', serif; color: #fbbf24;`

---

### Task 2: Implement Dual Naskh + Nastaliq in `build.py` Cards Generator

**Files:**
- Modify: `build.py`

- [ ] **Step 1: Update `update_pt_cards()` in `build.py`**
  Generate both Naskh (`.aljamiado-naskh`) and Nastaliq (`.aljamiado-nastaliq`) divs inside each card.

- [ ] **Step 2: Update `update_en_cards()` in `build.py`**
  Generate both Naskh and Nastaliq divs for English cards.

---

### Task 3: Update CSS in `pt/index.html` and `index.html` for Dual Cards

**Files:**
- Modify: `pt/index.html`, `index.html`

- [ ] **Step 1: Update CSS rules for `.aljamiado-naskh` and `.aljamiado-nastaliq` in `pt/index.html` and `index.html`**
  Ensure `.aljamiado-naskh` is styled with `#f472b6` (pink/rose) and `.aljamiado-nastaliq` with `#fbbf24` (yellow/gold).

---

### Task 4: Execute Build & Verify

- [ ] **Step 1: Run `python3 build.py`**

- [ ] **Step 2: Verify `pt/curso.html`, `pt/index.html`, and `index.html`**

- [ ] **Step 3: Commit to Git**

```bash
git add pt/curso.html pt/index.html index.html build.py docs/superpowers/plans/2026-08-24-font-color-dual-cards-plan.md
git commit -m "feat: restore clean Noto Naskh font, pink/yellow colors in curso, and add dual Naskh+Nastaliq to index cards"
```
