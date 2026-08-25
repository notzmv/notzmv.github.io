# Match Non-Card Arabic Text to Toggled Font and Color Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ensure all Arabic text after the cards (and everywhere outside `.card`) matches the exact visual appearance of the toggled script choice:
1. **Nastaliq Mode (`body.font-nastaliq` or default)**: All non-card Arabic text (`.ar`, `.perso-arabic`) renders in **Nastaliq** font (`Noto Nastaliq Urdu`) with **Yellow/Gold color (`#fbbf24`)**.
2. **Naskh Mode (`body.font-naskh`)**: All non-card Arabic text (`.ar`, `.perso-arabic`) renders in **Naskh** font (`Noto Naskh Arabic`) with **Pink color (`#f472b6`)**.
3. **Corpus Cards (`.card`)**: Always render both rows (Nastaliq yellow top + Naskh pink bottom with pink side friso).

**Files:**
- Modify: `pt/index.html`, `index.html`

---

### Task 1: Update CSS in `pt/index.html`

- [ ] **Step 1: Set `body.font-nastaliq` and `body.font-naskh` rules to target all non-card `.ar` and `.perso-arabic` elements with matching font-family and color (`#fbbf24` for Nastaliq, `#f472b6` for Naskh)**

---

### Task 2: Update CSS in `index.html`

- [ ] **Step 1: Set `body.font-nastaliq` and `body.font-naskh` rules in `index.html` to target all non-card `.ar` and `.perso-arabic` elements with matching font-family and color (`#fbbf24` for Nastaliq, `#f472b6` for Naskh)**

---

### Task 3: Build & Verification

- [ ] **Step 1: Run `python3 build.py`**
- [ ] **Step 2: Run Python verification script verifying font family AND color switching for non-card elements**
- [ ] **Step 3: Commit to Git**

```bash
git add pt/index.html index.html docs/superpowers/plans/2026-08-25-toggled-font-matching-plan.md
git commit -m "fix(css): make all Arabic text outside cards match toggled font and color (yellow nastaliq vs pink naskh)"
```
