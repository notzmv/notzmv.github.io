# Nasalization Rules & -ão (اوم) Orthographic Specification Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the new orthographic standard across the entire codebase for nasalization and vocalic endings:
1. **Nasal *-ão***: Canonically spelled with **Alif + Waw + Mīm (`اوم`)** (*pão* `پاوم`, *mão* `ماوم`, *não* `ناوم`, *coração* `كرچاوم`, *razão* `رزاوم`). The Mīm is droppable in fast/economic writing (`او`), but `اوم` is the primary standard.
2. **Contrast *-ão* vs *-au***:
   - *pão* (`پاوم`) vs. *pau* (`پاو`)
   - *mão* (`ماوم`) vs. *mau* (`ماو`)
3. **Nasal Rules (Mīm `م` vs. Nūn `ن`)**:
   - **Mīm (`م`)**: Standard word-ending nasal (*bom* `بم`, *gem* `جم`, *homem* `همم`, *com* `كم`, *sim* `سم`, *-ão* `اوم`), plus nasal before **p** and **b** (*campo* `كمپو`, *também* `تمبم`).
   - **Nūn (`ن`)**: Nasal before all other consonants (*gente* `جنتہ`, *esperança* `اسپرنچہ`, *honra* `هنرہ`).
4. **Plural Nasal *-ções***: Document **`ـچومها`** / **`ـچویمها`** (Chā + Waw + [Ye] + Mīm + Gol He + Alif) alongside `ـچویها`.

**Tech Stack:** Org-mode (`pt/index.org`, `pt/curso.org`), HTML5 (`pt/index.html`, `pt/curso.html`), Markdown (`pt/index.md`, `pt/curso.md`), Python (`build.py`).

---

### Task 1: Update Specification in `pt/index.org` and `build.py`

**Files:**
- Modify: `pt/index.org`, `build.py`

- [ ] **Step 1: Update nasalization rules & diphthong table in `pt/index.org`**
  Add `اوم` for *-ão*, update *pão* (`پاوم`), *mão* (`ماوم`), *pau* (`پاو`), *mau* (`ماو`), *coração* (`كرچاوم`), *razão* (`رزاوم`).

- [ ] **Step 2: Update sentence corpus dictionary notes and transcriptions in `build.py`**

---

### Task 2: Update Course Files (`pt/curso.org`, `pt/curso.html`)

**Files:**
- Modify: `pt/curso.org`, `pt/curso.html`

- [ ] **Step 1: Update Lição 5 (Nasalization motor) in `pt/curso.org` and `pt/curso.html`**
  Detail Mīm (`م`) for word-final nasals and before p/b, Nūn (`ن`) before other consonants.

- [ ] **Step 2: Update Mater Lectionis & Vowel Economy sections**
  Update *pão* (`پاوم`) vs *pau* (`پاو`), *mão* (`ماوم`) vs *mau* (`ماو`), *coração* (`كرچاوم`), *-ções* (`ـچومها` / `ـچویها`).

- [ ] **Step 3: Update Lição 7 sentences**

---

### Task 3: Build & Verification

- [ ] **Step 1: Run `python3 build.py`**
- [ ] **Step 2: Run Python verification script confirming new standard across all compiled files**
- [ ] **Step 3: Commit to Git**

```bash
git add pt/index.org pt/index.md pt/index.html pt/curso.org pt/curso.md pt/curso.html build.py docs/superpowers/plans/2026-08-25-aom-nasal-standard-plan.md
git commit -m "feat(pt): establish AOM (اوم) as canonical standard for nasal -ão, Mīm for final/p/b nasals, and contrast with -au (او)"
```
