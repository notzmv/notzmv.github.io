# Increase Arabic Font Size Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Increase the font size for all Perso-Arabic text across index pages (`pt/index.html` and `index.html`) for enhanced legibility and visual prominence.

**Adjustments:**
- `.ar, .perso-arabic`: `1.8rem` $\rightarrow$ **`2.2rem`**
- `.aljamiado-naskh`: `2.0rem` $\rightarrow$ **`2.4rem`**
- `.aljamiado-nastaliq`: `2.2rem` $\rightarrow$ **`2.6rem`**
- `.card .naskh-card-row`: `1.85rem` $\rightarrow$ **`2.3rem !important`**
- `.card .nastaliq-card-row`: `2.2rem` $\rightarrow$ **`2.5rem !important`**

**Files:**
- Modify: `pt/index.html`, `index.html`

---

### Task 1: Update Font Sizes in `pt/index.html`

- [ ] **Step 1: Increase `.ar`, `.perso-arabic`, `.aljamiado-naskh`, `.aljamiado-nastaliq`, `.card .naskh-card-row`, and `.card .nastaliq-card-row` font sizes in `pt/index.html`**

---

### Task 2: Update Font Sizes in `index.html`

- [ ] **Step 1: Increase `.ar`, `.perso-arabic`, `.aljamiado-naskh`, `.aljamiado-nastaliq`, `.card .naskh-card-row`, and `.card .nastaliq-card-row` font sizes in `index.html`**

---

### Task 3: Build & Verification

- [ ] **Step 1: Run `python3 build.py`**
- [ ] **Step 2: Run Python verification script confirming larger font sizes are applied**
- [ ] **Step 3: Commit to Git**

```bash
git add pt/index.html index.html docs/superpowers/plans/2026-08-25-increase-arabic-font-size-plan.md
git commit -m "style(index): increase font size of Perso-Arabic text for enhanced readability"
```
