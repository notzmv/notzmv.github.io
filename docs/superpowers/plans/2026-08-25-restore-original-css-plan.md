# Restore Original CSS & Fix Card Rows Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Completely restore the original, beautiful CSS styling for all sections (Basmala hero, tables, rules, hierarchy, Didactic Tanwīn) to how it was before card edits, and isolate the card row styles (`.naskh-card-row` in pink `#f472b6` with pink side friso, `.nastaliq-card-row` in gold `#fbbf24`) strictly inside `.card`.

---

### Task 1: Restore CSS in `pt/index.html`

- [ ] **Step 1: Restore `.ar`, `.perso-arabic`, `body.font-nastaliq`, `body.font-naskh` in `pt/index.html` to original baseline (`a54ca1f`)**
- [ ] **Step 2: Add isolated `.card .naskh-card-row` and `.card .nastaliq-card-row` rules**

---

### Task 2: Restore CSS in `index.html`

- [ ] **Step 1: Restore `.ar`, `.perso-arabic`, `body.font-nastaliq`, `body.font-naskh` in `index.html` to original baseline (`a54ca1f`)**
- [ ] **Step 2: Add isolated `.card .naskh-card-row` and `.card .nastaliq-card-row` rules**

---

### Task 3: Build & Verification

- [ ] **Step 1: Run `python3 build.py`**
- [ ] **Step 2: Run Python verification script confirming sections after cards have original gold styling, Basmala is complete, and card rows display properly**
- [ ] **Step 3: Commit to Git**

```bash
git add pt/index.html index.html docs/superpowers/plans/2026-08-25-restore-original-css-plan.md
git commit -m "fix(css): restore original CSS for sections outside cards while isolating dual card rows"
```
