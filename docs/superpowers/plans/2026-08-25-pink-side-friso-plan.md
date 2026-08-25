# Pink Side Friso Border for Naskh Card Row Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ensure the side border (friso lateral `border-right`) of `.naskh-card-row` is explicitly pink (`3px solid #f472b6 !important`), matching the pink text color, and `.nastaliq-card-row` is gold (`3px solid #fbbf24 !important`) across `pt/index.html` and `index.html`.

**Files:**
- Modify: `pt/index.html`, `index.html`

---

### Task 1: Update CSS in `pt/index.html` and `index.html`

- [ ] **Step 1: Update `border-right` on `.naskh-card-row` and `.nastaliq-card-row` with `!important` in `pt/index.html`**
- [ ] **Step 2: Update `border-right` on `.naskh-card-row` and `.nastaliq-card-row` with `!important` in `index.html`**

---

### Task 2: Build & Verification

- [ ] **Step 1: Run `python3 build.py`**
- [ ] **Step 2: Run Python verification script confirming `border-right: 3px solid #f472b6 !important` on `.naskh-card-row`**
- [ ] **Step 3: Commit to Git**

```bash
git add pt/index.html index.html docs/superpowers/plans/2026-08-25-pink-side-friso-plan.md
git commit -m "fix(cards): make side border friso pink for naskh card rows"
```
