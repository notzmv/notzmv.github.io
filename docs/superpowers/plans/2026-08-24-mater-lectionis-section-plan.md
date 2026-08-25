# Mater Lectionis & Vocalic Encounters Section Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a dedicated section in `pt/curso.org`, `pt/curso.md`, and `pt/curso.html` titled **"O Sistema de Mater Lectionis para Encontros Vocálicos"**, explaining how every vowel in Portuguese maps to its closest long vowel support (*Mater Lectionis*: Alif `ا`, Waw `و`, Ye `ی`, Gol He `ہ`).

**Architecture:**
- **Placement**: Placed right after *A Arte da Grafia Vocálica* and before `* Matriz Completa de Formas Posicionais`.
- **Key Concepts**:
  1. *O Princípio das Mães de Leitura (Mater Lectionis)*: Mapeamento de 5 vogais latinas para os 3 suportes semivocálicos/longos.
  2. *Atração por Proximidade Fonética*:
     - **Alif (`ا`)**: Família da vogal central **A**.
     - **Waw (`و`)**: Família labial/posterior (**O**, **U**, semivogal *w*).
     - **Ye (`ی`)**: Família palatal/anterior (**E**, **I**, semivogal *j*).
     - **Gol He (`ہ`)**: Vogais atónicas finais breves (*-a*, *-e*).
  3. *Tabela de Mapeamento de Ditongos e Hiatos em Aljamiado*.

**Tech Stack:** Org-mode (`pt/curso.org`), HTML5 (`pt/curso.html`), Markdown (`pt/curso.md`), Python 3 (`build.py`).

---

### Task 1: Update `pt/curso.org` with Mater Lectionis Section

**Files:**
- Modify: `pt/curso.org`

- [ ] **Step 1: Add the new section between Grafia Vocálica and Matriz Completa in `pt/curso.org`**
- [ ] **Step 2: Update Table of Contents in `pt/curso.org`**

---

### Task 2: Update `pt/curso.html` with Mater Lectionis Section

**Files:**
- Modify: `pt/curso.html`

- [ ] **Step 1: Add HTML formatted section between Grafia Vocálica and Matriz Completa in `pt/curso.html`**

---

### Task 3: Build & Verification

- [ ] **Step 1: Run `python3 build.py`**
- [ ] **Step 2: Run Python verification script checking section contents**
- [ ] **Step 3: Commit to Git**

```bash
git add pt/curso.org pt/curso.html pt/curso.md build.py docs/superpowers/plans/2026-08-24-mater-lectionis-section-plan.md
git commit -m "feat(pt): add section on mater lectionis and vocalic encounters mapping in course"
```
