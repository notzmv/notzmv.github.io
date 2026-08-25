# Full CSS & Font Toggle System Repair Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restore and fix the document-wide Perso-Arabic font toggle system (Nastaliq $\leftrightarrow$ Naskh) for all text (Basmala, tables, inline spans, headers) across `pt/index.html` and `index.html`, while keeping the dual-row card structure (Nastaliq yellow top + Naskh pink bottom with pink side friso) isolated inside `.card`.

**Fixes:**
1. **Fix broken CSS in `index.html`**: Restore missing `body.font-nastaliq .ar, body.font-nastaliq .perso-arabic` selector at line 239.
2. **Document-wide Font Toggle for non-card text**:
   - `body.font-nastaliq`: All general `.ar` / `.perso-arabic` text outside cards renders in Nastaliq font (`Noto Nastaliq Urdu`) and yellow `#fbbf24`.
   - `body.font-naskh`: All general `.ar` / `.perso-arabic` text outside cards renders in Naskh font (`Noto Naskh Arabic`) and pink `#f472b6`.
   - Hide dual Basmala rows conditionally (`.aljamiado-basmala-naskh` in Nastaliq mode, `.aljamiado-basmala-nastaliq` in Naskh mode).
3. **Card isolation**: Card rows (`.nastaliq-card-row` and `.naskh-card-row`) remain explicitly styled and always visible in `.card`, unaffected by document font toggles.

**Files:**
- Modify: `pt/index.html`, `index.html`

---

### Task 1: Clean and Repair CSS in `pt/index.html`

- [ ] **Step 1: Replace CSS block in `pt/index.html` with clean, non-conflicting font toggle and card row rules**
- [ ] **Step 2: Verify `pt/index.html` in browser/headless test**

---

### Task 2: Clean and Repair CSS in `index.html`

- [ ] **Step 1: Replace CSS block in `index.html` with clean, non-conflicting font toggle and card row rules**
- [ ] **Step 2: Verify `index.html` in browser/headless test**

---

### Task 3: Build & Verification

- [ ] **Step 1: Run `python3 build.py`**
- [ ] **Step 2: Run Python verification script verifying font toggle rules and card row isolation**
- [ ] **Step 3: Commit to Git**

```bash
git add pt/index.html index.html docs/superpowers/plans/2026-08-25-full-css-repair-plan.md
git commit -m "fix(css): repair global font toggle system and isolate dual card rows in index pages"
```
