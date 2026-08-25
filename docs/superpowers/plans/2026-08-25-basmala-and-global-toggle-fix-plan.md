# Complete Font Toggle & Basmala Hero Fix Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Completely restore the Basmala hero block (keeping both Nastaliq green and Naskh mint lines always visible) and ensure all text outside cards (in tables, prose, examples, headers) switches font family and color smoothly when toggling between Nastaliq (Yellow `#fbbf24`) and Naskh (Pink `#f472b6`) across `pt/index.html` and `index.html`.

---

### Task 1: Update CSS in `pt/index.html`

- [ ] **Step 1: Remove Basmala hiding rules (`.aljamiado-basmala-naskh { display: none }`) so Basmala hero always shows all 3 lines**
- [ ] **Step 2: Update `body.font-nastaliq` and `body.font-naskh` CSS rules to switch font family AND color (`#fbbf24` vs `#f472b6`) for all non-card Perso-Arabic text**
- [ ] **Step 3: Keep `.nastaliq-card-row` (yellow + gold friso) and `.naskh-card-row` (pink + pink friso) explicitly styled and isolated inside `.card`**

---

### Task 2: Update CSS in `index.html`

- [ ] **Step 1: Remove Basmala hiding rules in `index.html`**
- [ ] **Step 2: Update `body.font-nastaliq` and `body.font-naskh` CSS rules in `index.html`**

---

### Task 3: Build & Verification

- [ ] **Step 1: Run `python3 build.py`**
- [ ] **Step 2: Run Python verification script verifying Basmala elements are visible, font toggling works outside cards, and cards retain dual rows**
- [ ] **Step 3: Commit to Git**

```bash
git add pt/index.html index.html docs/superpowers/plans/2026-08-25-basmala-and-global-toggle-fix-plan.md
git commit -m "fix(css): restore full Basmala hero display and fix global font toggle system outside cards"
```
