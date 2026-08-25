# Priority Hierarchy Example Tables & Dual Card Order Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:**
1. **Card Order in Index Pages (`pt/index.html` & `index.html`)**: Ensure **Nastaliq is rendered FIRST** and **Naskh SECOND (below Nastaliq)** on all index card items in `build.py`.
2. **Example Tables for New Sections**: Add exhausetive HTML/Org example tables illustrating the 4-tier Priority Hierarchy and Organic Navigation in `pt/curso.org`, `pt/curso.html`, `pt/curso.md`, `pt/index.org`, `pt/index.html`, and `pt/index.md`.

---

### Task 1: Re-order Card Script in `build.py` (Nastaliq top, Naskh below)

**Files:**
- Modify: `build.py`

- [ ] **Step 1: Swap line order in `update_pt_cards()` and `update_en_cards()` in `build.py` so Nastaliq is rendered above Naskh**
- [ ] **Step 2: Run `python3 build.py`**

---

### Task 2: Add Priority Hierarchy Example Tables to Course & Index Files

**Files:**
- Modify: `pt/curso.org`, `pt/curso.html`, `pt/index.org`, `pt/index.html`

- [ ] **Step 1: Add Priority Hierarchy Example Table in `pt/curso.org` and `pt/curso.html`**
  Table Columns:
  - *Nível de Prioridade*
  - *Foco Ortográfico*
  - *Exemplo em Português*
  - *Grafia no Aljamiado*
  - *Justificativa & Dinâmica de Navegação*
- [ ] **Step 2: Add Priority Hierarchy Example Table in `pt/index.org` and `pt/index.html`**

---

### Task 3: Build & Verification

- [ ] **Step 1: Run `python3 build.py`**
- [ ] **Step 2: Run Python verification script verifying card order and new tables**
- [ ] **Step 3: Commit to Git**

```bash
git add build.py pt/curso.org pt/curso.html pt/curso.md pt/index.org pt/index.html pt/index.md index.html docs/superpowers/plans/2026-08-25-priority-tables-and-card-order-plan.md
git commit -m "feat(pt): add example tables for priority hierarchy and enforce Nastaliq top / Naskh bottom card order"
```
