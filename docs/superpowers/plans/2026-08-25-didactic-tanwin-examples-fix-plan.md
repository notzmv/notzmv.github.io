# Didactic Tanwīn Examples Correction Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update the Didactic Tanwīn examples across all files to use the exact user-specified examples for unmarked vowels:
1. **Fathatan (`ً` - Tanwīn A)**: **`prática`** $\rightarrow$ **`پرًكتیكہ`** (marks the unmarked tonic *a* in *prá-* when Alif is omitted).
2. **Kasratan (`ٍ` - Tanwīn I)**: **`ultimamente`** $\rightarrow$ **`التٍمنتہ`** (marks the unmarked *i* in *-tima-* when Ye is omitted).
3. **Dammatan (`ٌ` - Tanwīn U)**: **`estúpido`** $\rightarrow$ **`استٌپدو`** (marks the unmarked tonic *u* in *-tú-* when Waw is omitted).

**Files:**
- Modify: `pt/curso.org`, `pt/curso.html`, `pt/index.org`, `pt/index.html`

---

### Task 1: Update Course Files (`pt/curso.org`, `pt/curso.html`)

- [ ] **Step 1: Update Didactic Tanwīn table in `pt/curso.org`**
- [ ] **Step 2: Update Didactic Tanwīn table in `pt/curso.html`**

---

### Task 2: Update Index Files (`pt/index.org`, `pt/index.html`)

- [ ] **Step 1: Update Didactic Tanwīn section in `pt/index.org`**
- [ ] **Step 2: Update Didactic Tanwīn section in `pt/index.html`**

---

### Task 3: Build & Verification

- [ ] **Step 1: Run `python3 build.py`**
- [ ] **Step 2: Run Python verification script verifying new examples (`prática` `پرًكتیكہ`, `ultimamente` `التٍمنتہ`, `estúpido` `استٌپدو`)**
- [ ] **Step 3: Commit to Git**

```bash
git add pt/curso.org pt/curso.html pt/curso.md pt/index.org pt/index.html pt/index.md
git commit -m "fix(pt): update Didactic Tanwīn examples to prática, ultimamente, and estúpido for unmarked vowels"
```
