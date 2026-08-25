# Dual Card Rows (Nastaliq Yellow + Naskh Pink) Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix index cards in `pt/index.html` and `index.html` to display two distinct styled rows:
1. Top row: **Nastaliq** (`nastaliq-card-row`) in yellow `#fbbf24` with gold right border (`3px solid #fbbf24`).
2. Bottom row: **Naskh** (`naskh-card-row`) in pink `#f472b6` with pink right border (`3px solid #f472b6`).
3. Ensure both card rows stay **always visible** inside `.card` regardless of global font toggles (`display: block !important`).

**Files:**
- Modify: `build.py`, `pt/index.html`, `index.html`

---

### Task 1: Update Card HTML Generator in `build.py`

- [ ] **Step 1: Add `naskh-card-row` class to the Naskh element in `update_pt_cards()` and `update_en_cards()` in `build.py`**

---

### Task 2: Add CSS for `.nastaliq-card-row`, `.naskh-card-row`, and card row visibility

- [ ] **Step 1: Add CSS rules to `pt/index.html`**
- [ ] **Step 2: Add CSS rules to `index.html`**

---

### Task 3: Build & Verification

- [ ] **Step 1: Run `python3 build.py`**
- [ ] **Step 2: Run Python verification script verifying card HTML structure and CSS in both `pt/index.html` and `index.html`**
- [ ] **Step 3: Commit to Git**

```bash
git add build.py pt/index.html index.html docs/superpowers/plans/2026-08-25-dual-card-rows-plan.md
git commit -m "fix(cards): add dedicated pink naskh row below nastaliq row in index cards"
```
