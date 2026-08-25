# Default Naskh Script Mode Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Set Naskh (`font-naskh`) as the default script mode when opening index pages (`pt/index.html` and `index.html`), updating body classes and button labels accordingly.

**Files:**
- Modify: `pt/index.html`, `index.html`

---

### Task 1: Update Body Class and Initial Button Labels in `pt/index.html`

- [ ] **Step 1: Change `<body class="font-nastaliq">` to `<body class="font-naskh">`**
- [ ] **Step 2: Update inline font toggle button initial label to Naskh**
- [ ] **Step 3: Update floating font toggle button initial label to Naskh**

---

### Task 2: Update Body Class and Initial Button Labels in `index.html`

- [ ] **Step 1: Change `<body class="font-nastaliq">` to `<body class="font-naskh">`**
- [ ] **Step 2: Update floating font toggle button initial label to Naskh**

---

### Task 3: Build & Verification

- [ ] **Step 1: Run `python3 build.py`**
- [ ] **Step 2: Run Python verification script confirming `<body class="font-naskh">` is set by default**
- [ ] **Step 3: Commit to Git**

```bash
git add pt/index.html index.html docs/superpowers/plans/2026-08-25-default-naskh-mode-plan.md
git commit -m "feat(index): set Naskh as default script mode on index pages"
```
