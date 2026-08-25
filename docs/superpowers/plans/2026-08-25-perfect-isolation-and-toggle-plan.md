# Perfect Isolation and Font Toggle System Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Completely fix and isolate the CSS typography system across `pt/index.html` and `index.html` so that:
1. **Basmala Hero (`.basmala-hero`)**: Explicitly styled with `!important` on its custom fonts and colors (Line 1 Gold Naskh, Line 2 Emerald Nastaliq `#34d399`, Line 3 Mint Naskh `#6ee7b7`), staying 100% visible and protected from font-toggle overrides.
2. **Corpus Cards (`.card`)**: Explicitly styled with `!important` on both rows (`.nastaliq-card-row` in Yellow `#fbbf24` + gold side friso, `.naskh-card-row` in Pink `#f472b6` + pink side friso), staying 100% visible and protected from font-toggle overrides.
3. **All Arabic Text Outside Cards & Basmala (`.ar`, `.perso-arabic`)**: Toggles smoothly between **Nastaliq Yellow (`#fbbf24`)** in Nastaliq mode and **Naskh Pink (`#f472b6`)** in Naskh mode.

**Files:**
- Modify: `pt/index.html`, `index.html`

---

### Task 1: Update CSS in `pt/index.html`

- [ ] **Step 1: Replace CSS typography rules in `pt/index.html` with explicit container-isolated rules for Basmala hero, Corpus cards, and global `.ar` toggle**

---

### Task 2: Update CSS in `index.html`

- [ ] **Step 1: Replace CSS typography rules in `index.html` with explicit container-isolated rules for Basmala hero, Corpus cards, and global `.ar` toggle**

---

### Task 3: Build & Verification

- [ ] **Step 1: Run `python3 build.py`**
- [ ] **Step 2: Run Python verification script confirming Basmala lines are intact, card rows are intact, and all non-card Arabic text switches font AND color when toggling**
- [ ] **Step 3: Commit to Git**

```bash
git add pt/index.html index.html docs/superpowers/plans/2026-08-25-perfect-isolation-and-toggle-plan.md
git commit -m "fix(css): isolate Basmala hero and corpus cards while enabling full font+color toggle for non-card Arabic text"
```
