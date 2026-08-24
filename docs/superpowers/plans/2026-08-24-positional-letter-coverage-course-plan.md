# Positional Letter Coverage for Course (`pt/curso.*`) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Expand `pt/curso.org`, `pt/curso.md`, and `pt/curso.html` so every letter in the Perso-Arabic alphabet has at least one Portuguese example word for all valid positional forms (Isolada, Inicial, Medial, Final), including a dedicated Master Positional Forms Matrix.

**Architecture:** Add a new section `* Matriz Completa de Formas Posicionais` in `pt/curso.org`, update `pt/curso.html` with responsive positional reference tables, and run `build.py`.

**Tech Stack:** Org-mode, Markdown, HTML5, CSS3, Python 3 (`build.py`).

## Global Constraints

- Complete coverage of all 21 letters across 4 positional forms (Isolada, Inicial, Medial, Final; non-connectors omit medial/initial as grammatically appropriate).
- Maintain 100% orthographic accuracy with rules from `pt/index.org` (e.g. logogram `-hā` `ـها`, Gol He `ہ` / `ـه`, `او` for `-ão`).
- Maintain Naskh & Nastaliq parallel font support in `pt/curso.html`.

---

### Task 1: Update `pt/curso.org` with Master Positional Matrix & Positional Vocabulary

**Files:**
- Modify: `pt/curso.org`

**Interfaces:**
- Consumes: Design spec from `docs/superpowers/specs/2026-08-24-positional-letter-coverage-course-design.md`.
- Produces: Updated Org-mode document containing the new section `* Matriz Completa de Formas Posicionais (21 Letras nas 4 Posições)`.

- [ ] **Step 1: Add `* Matriz Completa de Formas Posicionais` section to `pt/curso.org`**

Add the complete 21-letter positional matrix table at the end of `pt/curso.org` covering Isolada, Inicial, Medial, and Final Portuguese example words.

- [ ] **Step 2: Verify `pt/curso.org` Org structure**

Ensure headings, table borders, and anchors remain valid Org syntax.

---

### Task 2: Update `pt/curso.html` with Master Positional Matrix & Styles

**Files:**
- Modify: `pt/curso.html`

**Interfaces:**
- Consumes: Updated `pt/curso.org` positional data.
- Produces: Fully styled HTML matrix table in `pt/curso.html`.

- [ ] **Step 1: Add HTML `Matriz Completa de Formas Posicionais` section to `pt/curso.html`**

Add a styled, responsive 5-column table displaying: Letra, Forma Isolada, Forma Inicial, Forma Medial, Forma Final with Naskh and Nastaliq classes.

- [ ] **Step 2: Test `pt/curso.html` Nastaliq toggle compatibility**

Ensure `.hide-nastaliq` smoothly toggles Nastaliq columns in the new positional matrix table.

---

### Task 3: Execute `build.py` & Final Verification

**Files:**
- Modify: `pt/curso.md` (via `build.py`)
- Verify: `pt/curso.org`, `pt/curso.md`, `pt/curso.html`, `build.py`

- [ ] **Step 1: Run `python3 build.py`**

Run: `python3 build.py`  
Expected: `Successfully updated pt/curso.md from pt/curso.org` with zero errors.

- [ ] **Step 2: Verify positional completeness via Python check script**

Run:
```bash
python3 -c "
with open('pt/curso.html', 'r', encoding='utf-8') as f:
    html = f.read()

letters = ['ا', 'ب', 'پ', 'ت', 'ج', 'چ', 'د', 'ر', 'ز', 'ژ', 'س', 'ش', 'ف', 'ك', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی']
missing = [l for l in letters if l not in html]
print('Missing letters:', missing)
assert len(missing) == 0, 'Some letters are missing from curso.html!'
print('ALL 21 LETTERS PRESENT IN CURSO.HTML!')
"
```

- [ ] **Step 3: Commit all changes**

```bash
git add pt/curso.org pt/curso.md pt/curso.html docs/superpowers/plans/2026-08-24-positional-letter-coverage-course-plan.md
git commit -m "feat(pt): add complete positional letter coverage matrix to curso"
```
