# Initial R- Spelling Uniformity (`Rā` ر) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ensure that all word-initial R- words in Portuguese (*rio*, *rua*, *raiz*, *regra*, *riqueza*, *recompensa*, *renovam*, *razão*, *razões*, etc.) ALWAYS and exclusively use **Rā (`ر`)**, and reserve **Hā / He (`ه` / `ہ`)** strictly for silent Latin H- (*homem*, *honra*, *hoje*, *herói*).

**Architecture:** Update orthographic mapping tables, rule definitions, example transcriptions, and sentence explanatory notes in `pt/index.org`, `pt/index.md`, `pt/index.html`, `pt/curso.org`, `pt/curso.md`, `pt/curso.html`, and `build.py`.

**Tech Stack:** Org-mode, Markdown, HTML5, Python 3 (`build.py`).

## Global Constraints

- **R- Inicial Rule**: Initial strong R- in Portuguese is **categorically and exclusively grafado com Rā (`ر`)**.
- **H- Inicial Rule**: Initial silent H- in Portuguese is **categorically and exclusively grafado com Hā / He (`ه` / `ہ`)**.
- Remove all mentions of `He (ه)` as an initial R- variant (`هیو`, `هوه`, `هایز`, `هگرہ`, `هیكزہ`, `هنووم`, `هزاو`, `هزویها`).
- Sentence notes explaining `Rā` in *riqueza*, *renovam*, *recompensa* must reflect that `Rā` is used by mandatory R- initial rule (reserving `Hā` for silent Latin H- in *honra*, *homem*).

---

### Task 1: Update Rules & Examples in `pt/index.org`

**Files:**
- Modify: `pt/index.org`

**Interfaces:**
- Consumes: Strict R- initial rule.
- Produces: Updated `pt/index.org` specification.

- [ ] **Step 1: Update Consonant Inventory Table in `pt/index.org:268`**

Change:
`| **r-** (inicial forte) | [ʁ] / [r] | **ر** (frequente) / **ه** | Rā / He | *rio* / *rua* | `ریو` / `روه` (ou `هیو` / `هوه`) |`
To:
`| **r-** (inicial forte) | [ʁ] / [r] | **ر** | Rā | *rio* / *rua* | `ریو` / `روه` |`

- [ ] **Step 2: Update Distinção R vs. RR section in `pt/index.org:343-349`**

Change the description for **R inicial** to state that R inicial is **estritamente e exclusivamente grafado por Rā (`ر`)**, reserving **He (`ه`)** for silent Latin H- (*homem*, *honra*, *hoje*). Remove all He variants (`هیو`, `هوه`, `هایز`, `هگرہ`, `هیكزہ`, `هنووم`).

- [ ] **Step 3: Update `renovam`, `razão`, and `razões` examples in `pt/index.org:590,608-610`**

Change `هنووم` to `رنوم` / `رنووم`, and `هزاو` / `هزویها` to `رزاو` / `رزویها`.

- [ ] **Step 4: Update sentence notes in `pt/index.org:147,183,237,249`**

Update notes to state that `Rā` is used by mandatory initial R- rule (reserving `Hā` for silent Latin H-).

---

### Task 2: Update `build.py` Sentence Notes & Dictionary

**Files:**
- Modify: `build.py:90,138,210`

**Interfaces:**
- Consumes: Updated initial R- notes.
- Produces: Updated `update_pt_cards()` in `build.py`.

- [ ] **Step 1: Update sentence notes in `build.py`**

Update sentences 8, 14, 23 notes in `build.py` to reflect mandatory R- initial rule for `Rā`.

- [ ] **Step 2: Verify `build.py` syntax**

Run: `python3 -m py_compile build.py`

---

### Task 3: Execute `build.py` & Verify Generated Files

**Files:**
- Modify: `pt/index.md`, `index.md`, `pt/curso.md`, `pt/index.html` (via `build.py`)

- [ ] **Step 1: Run `python3 build.py`**

Run: `python3 build.py`

- [ ] **Step 2: Run verification check for stray initial He variants**

Run:
```bash
grep -E "هیو|هوه|هایز|هگرہ|هیكزہ|هنووم|هزاو|هزویها" pt/index.org pt/index.md pt/index.html pt/curso.org pt/curso.md pt/curso.html build.py || true
```
Expected: 0 matches.

- [ ] **Step 3: Commit changes**

```bash
git add pt/index.org pt/index.md pt/index.html pt/curso.org pt/curso.md pt/curso.html build.py docs/superpowers/plans/2026-08-24-initial-r-spelling-uniformity.md
git commit -m "docs(pt): enforce strict initial R- spelling with Ra across all files"
```
