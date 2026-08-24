# Word-Length Vowel Economy & Convencos Explainer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a comprehensive explainer on word-length vowel economy, minimal pair disambiguation (`bm` vs `bum` / `bim`), the `convenco` / `convencao` / `convencos` triad, and eliminate redundant `Nūn` in `-ão` suffixes across all Aljamiado files.

**Architecture:** Update `pt/index.org` with formal theoretical explanations and corrected spellings, update `build.py` corpus cards with non-redundant `-ão` (`او`) spellings, and run `build.py` to generate consistent HTML/MD targets.

**Tech Stack:** Org-mode (`.org`), Python (`build.py`), Markdown (`.md`), HTML (`.html`).

## Global Constraints

- Do not insert explicit `Nūn` (`ن`) into `-ão` (`او`) unless `n` is a root consonant.
- Use `ـچاو` for `-ção`, `ـداو` for `-dão`, `ـچو` for `-ço`, and `ـچوها` for `-ções`.
- Plural nouns use nominal logogram `-hā` (`ـها`).
- Verbs ending in 1st person singular `-o` use Waw `و`.

---

### Task 1: Update Specification in `pt/index.org`

**Files:**
- Modify: `pt/index.org`

**Interfaces:**
- Produces: Updated Org-mode documentation with the new subsection and corrected `-ão` spellings.

- [ ] **Step 1: Inspect target sections in `pt/index.org`**

Check exact line locations in `pt/index.org` for Section 2 ("Sistema Vocálico") and Section 3.2 ("Ditongos Nasais").

- [ ] **Step 2: Add "Economia Escalar por Comprimento de Palavra e Desambiguação de Pares Mínimos" to `pt/index.org`**

Add the new subsection under Section 2 explaining:
1. Short words (`bm` `بم`, `bum` `بوم`, `bim` `بیم`).
2. Long words (*misericordioso* `مزریكردیوزو` / `مزركردیوزو`).
3. The `convenco` (`كنونچو`), `convencao` (`كنونچاو`), `convencos` (`كنونچوها`) triad and why `-hā` avoids the need for an extra internal vowel letter.

- [ ] **Step 3: Correct `-ão` spellings across `pt/index.org`**

Replace all instances of `چناو` with `چاو`, `دناو` with `داو`, `اتنچناو` with `اتنچاو`, `اچناو` with `اچاو`, `گرتیدناو` with `گرتیداو`, and `كرچناو` with `كرچاو`.

- [ ] **Step 4: Verify `pt/index.org` changes**

Run: `grep -E "چناو|دناو" pt/index.org || true`  
Expected: No matches found for `چناو` or `دناو`.

---

### Task 2: Update Corpus Cards in `build.py`

**Files:**
- Modify: `build.py`

**Interfaces:**
- Consumes: Clean `-ão` spelling rules (`ـچاو`, `ـداو`).
- Produces: Corrected Python sentence dictionary in `update_pt_cards()`.

- [ ] **Step 1: Update sentence dictionary in `build.py`**

Update sentences 3, 8, 22, 23 in `build.py` to replace `گرتیدناو` with `گرتیداو`, `كرچناو` with `كرچاو`, `اتنچناو` with `اتنچاو`, `اچناو` with `اچاو`.

- [ ] **Step 2: Verify `build.py` syntax**

Run: `python3 -m py_compile build.py`  
Expected: Clean compilation with 0 syntax errors.

---

### Task 3: Execute Build & Verify Generated Artifacts

**Files:**
- Modify: `pt/index.md`, `index.md`, `pt/index.html`, `index.html`

**Interfaces:**
- Consumes: `build.py` and `pt/index.org`.
- Produces: Fully synchronized production HTML and Markdown files.

- [ ] **Step 1: Execute `build.py`**

Run: `python3 build.py`  
Expected: Success messages for updating `pt/index.md`, `index.md`, `pt/index.html`, `index.html`.

- [ ] **Step 2: Verify site integrity and search for outdated spellings**

Run: `grep -E "چناو|دناو" pt/index.html pt/index.md || true`  
Expected: No matches for redundant `چناو` / `دناو`.

- [ ] **Step 3: Verify presence of new explainer section**

Run: `grep -i "Economia Escalar" pt/index.md pt/index.html`  
Expected: Heading and text found in both generated files.
