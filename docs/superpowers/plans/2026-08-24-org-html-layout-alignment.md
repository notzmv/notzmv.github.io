# Org → HTML Layout & Pipeline Alignment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a prominent single toggle button for switching between Nasta'liq and Naskh scripts, and restructure `index.html` (EN) and `pt/index.html` (PT) to follow the exact section hierarchy and TOC of `index.org` and `pt/index.org`.

**Architecture:** Replace the 5-button font selector with a prominent `<button id="font-toggle-btn">` that toggles between Nasta'liq and Naskh modes. Align all section headings and sub-headings to match the Org files 1-to-1.

**Tech Stack:** HTML5, CSS3 (CSS Variables, Flexbox, Sticky controls), JavaScript (Font toggle script).

## Global Constraints

- **Language Support**: English (`index.html`) and Portuguese (`pt/index.html`).
- **Font Switching**: Primary toggle switches between Nasta'liq mode (`font-nastaliq`/`font-gulzar`) and Naskh mode (`font-naskh`).

---

### Task 1: Add Big Naskh / Nasta'liq Toggle Button & CSS Styling

**Files:**
- Modify: `index.html`, `pt/index.html`

- [ ] **Step 1: Add Big Toggle Button CSS & JS**

Add CSS for `.btn-big-toggle`:
```css
.btn-big-toggle {
  background: #21262d;
  border: 2px solid var(--primary-accent);
  color: var(--primary-accent);
  padding: 0.6rem 1.2rem;
  border-radius: 8px;
  font-size: 0.95rem;
  font-weight: 700;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  transition: all 0.2s ease;
  box-shadow: 0 4px 12px rgba(245, 158, 11, 0.15);
}
.btn-big-toggle:hover {
  background: var(--primary-accent);
  color: #000000;
  box-shadow: 0 6px 16px rgba(245, 158, 11, 0.3);
}
```

Add JavaScript for `toggleScriptFont()`:
```javascript
function toggleScriptFont() {
  var isNastaliq = document.body.classList.contains('font-nastaliq') || document.body.classList.contains('font-gulzar');
  var btn = document.getElementById('font-toggle-btn');
  if (isNastaliq) {
    document.body.className = 'font-naskh';
    if (btn) btn.innerHTML = '📖 Script Mode: <strong>Naskh (Arabic Style)</strong> &mdash; Click to switch to Nasta\'liq';
  } else {
    document.body.className = 'font-nastaliq';
    if (btn) btn.innerHTML = '✨ Script Mode: <strong>Nasta\'liq (Urdu Style)</strong> &mdash; Click to switch to Naskh';
  }
}
```

- [ ] **Step 2: Commit styling and toggle button script**

```bash
git add index.html pt/index.html
git commit -m "feat(ui): add big Naskh / Nasta'liq toggle button"
```

---

### Task 2: Align `pt/index.html` Sections with `pt/index.org`

**Files:**
- Modify: `pt/index.html`

- [ ] **Step 1: Update `pt/index.html` structure**

Align section order:
1. Header & Controls (Large Naskh / Nasta'liq Toggle Button + PT/EN Switcher).
2. Índice (Table of Contents with anchors).
3. Introdução e Visão Geral.
4. 1. Inventário Consonantal e Mapeamento Perso-Árabe.
5. 2. Sistema Vocálico, Diacríticos e Acentuação.
6. 3. Motor de Nasalização.
7. 4. Regras Morfofonêmicas e Mapeamento de Domínio.
8. 5. Casos Especiais e Construções Particulares.
9. 6. Tabelas de Paradigmas Mestre.
10. 7. Corpus e Amostras de Transcrição.

- [ ] **Step 2: Run `python3 build.py`**

Run: `python3 build.py`
Expected: Cards injected cleanly.

- [ ] **Step 3: Commit changes**

```bash
git add pt/index.html
git commit -m "style(pt): align pt/index.html exact section order with pt/index.org"
```

---

### Task 3: Align `index.html` Sections with `index.org`

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Update `index.html` structure**

Align section order:
1. Header & Controls (Large Naskh / Nasta'liq Toggle Button + EN/PT Switcher).
2. Table of Contents (with anchors).
3. Introduction & Overview.
4. 1. Consonant Inventory & Perso-Arabic Mapping.
5. 2. Vowel System & Orthographic Carrier Engine.
6. 3. Morphophonemic Rules & Domain Mapping.
7. 4. Master Paradigm Lookup Tables.
8. 5. Expanded Corpus & Sample Transcriptions.

- [ ] **Step 2: Run `python3 build.py`**

Run: `python3 build.py`
Expected: Cards injected cleanly.

- [ ] **Step 3: Commit changes**

```bash
git add index.html
git commit -m "style(en): align index.html exact section order with index.org"
```

---

### Task 4: Final Pipeline Verification

- [ ] **Step 1: Run build script**

Run: `python3 build.py`

- [ ] **Step 2: Verify git state and commit final updates**

```bash
git add index.html pt/index.html build.py index.md pt/index.md
git commit -m "chore: final verification of big font toggle and Org alignment"
```
