# Hamzah Deprecation & Didactic Tanwīn Diacritics Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:**
1. **Deprecate Hamzah in Hiatos**: Replace Hamzah variants (`پائیس`, `ساؤدہ`, `باؤ`) with standard *Mater Lectionis* encounters without Hamzah (**`پایس`**, **`ساودہ`**, **`باو`**).
2. **Add Didactic Diacritics & Tanwīn Notation in Genesis Section & Specs**:
   - Document the early Persian/Urdu diacritic experiment (*Harakat*: *fatḥah*, *kasrah*, *ḍammah*).
   - Add the **Didactic Tanwīn Notation** for marking implicit/unmarked vowels in educational contexts ONLY:
     - **Fathatan (`ً`)** $\rightarrow$ Marks *unmarked tonic A* / *á*.
     - **Kasratan (`ٍ`)** $\rightarrow$ Marks *unmarked I*.
     - **Dammatan (`ٌ`)** $\rightarrow$ Marks *unmarked U*.
   - Emphasize: *Tanwīn diacritics are strictly for pedagogical/historical demonstration and never used in normal writing.*

**Tech Stack:** Org-mode (`pt/curso.org`, `pt/index.org`), HTML5 (`pt/curso.html`, `pt/index.html`), Markdown (`pt/curso.md`, `pt/index.md`), Python (`build.py`).

---

### Task 1: Deprecate Hamzah in Course & Index Files

**Files:**
- Modify: `pt/curso.org`, `pt/curso.html`, `pt/index.org`, `pt/index.html`

- [ ] **Step 1: Replace Hamzah hiatos (`پائیس`, `ساؤدہ`) with standard Mater Lectionis (`پایس`, `ساودہ`) in `pt/curso.org` and `pt/curso.html`**
- [ ] **Step 2: Replace Hamzah hiatos in `pt/index.org` and `pt/index.html`**

---

### Task 2: Add Didactic Diacritics & Tanwīn Table in Genesis Section & Specs

**Files:**
- Modify: `pt/curso.org`, `pt/curso.html`, `pt/index.org`, `pt/index.html`

- [ ] **Step 1: Add Didactic Diacritics & Tanwīn Table in `pt/curso.org` and `pt/curso.html` under "A Gênese do Sistema"**
- [ ] **Step 2: Add Didactic Diacritics & Tanwīn Table in `pt/index.org` and `pt/index.html` under "Sistema Vocálico e Diacríticos"**

---

### Task 3: Build & Verification

- [ ] **Step 1: Run `python3 build.py`**
- [ ] **Step 2: Run Python verification script confirming Hamzah removal and Tanwīn table presence**
- [ ] **Step 3: Commit to Git**

```bash
git add pt/curso.org pt/curso.html pt/curso.md pt/index.org pt/index.html pt/index.md build.py docs/superpowers/plans/2026-08-25-hamzah-deprecation-and-tanwin-plan.md
git commit -m "feat(pt): deprecate Hamzah in hiatos for pure Mater Lectionis and introduce Didactic Tanwīn diacritics for unmarked vowels"
```
