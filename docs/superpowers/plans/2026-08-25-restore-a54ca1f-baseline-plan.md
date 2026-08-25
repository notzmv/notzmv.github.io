# Restore Original Baseline (a54ca1f) & Isolate Dual Card Rows Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restore the exact, clean font-toggle CSS system from commit `a54ca1f` (10 commits ago) for all document text, Basmala hero, and tables, and isolate the dual card row display (`.card .naskh-card-row` with pink text and pink side friso) with `display: block !important` strictly inside `.card`.

---

### Task 1: Restore CSS in `pt/index.html`

- [ ] **Step 1: Revert CSS typography and font toggle rules in `pt/index.html` to baseline `a54ca1f`**
- [ ] **Step 2: Add isolated `.card .nastaliq-card-row` and `.card .naskh-card-row` rules with `display: block !important`**

---

### Task 2: Restore CSS in `index.html`

- [ ] **Step 1: Revert CSS typography and font toggle rules in `index.html` to baseline `a54ca1f`**
- [ ] **Step 2: Add isolated `.card .nastaliq-card-row` and `.card .naskh-card-row` rules with `display: block !important`**

---

### Task 3: Build & Verification

- [ ] **Step 1: Run `python3 build.py`**
- [ ] **Step 2: Run Python verification script confirming font toggle hides/shows dual script elements outside cards, tables switch font family, and cards render both rows**
- [ ] **Step 3: Commit to Git**

```bash
git add pt/index.html index.html docs/superpowers/plans/2026-08-25-restore-a54ca1f-baseline-plan.md
git commit -m "fix(css): restore exact a54ca1f font toggle baseline and isolate dual card rows"
```
