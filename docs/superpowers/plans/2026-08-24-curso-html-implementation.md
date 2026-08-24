# Curso Gradual HTML (`pt/curso.html`) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a standalone, fully styled, mobile-responsive HTML course page `pt/curso.html` generated from `pt/curso.org` / `pt/curso.md`, complete with an interactive beginner Nastaliq toggle, side-by-side Naskh/Nastaliq tables, and cross-navigation links between `pt/index.html` and `pt/curso.html`.

**Architecture:** Create `pt/curso.html` with dark theme styling matching `pt/index.html`, add CSS classes for Naskh (`.aljamiado-naskh`) and Nastaliq (`.aljamiado-nastaliq`), implement `toggleNastaliqVisibility()` JS, link `pt/index.html` and `pt/curso.html` via header navigation buttons, and update `build.py`.

**Tech Stack:** HTML5, CSS3 (CSS Variables, Flexbox, Sticky Controls), Vanilla JS, Python 3 (`build.py`).

## Global Constraints

- Preserve all orthographic spellings from `pt/curso.org` and `pt/index.org`.
- Default script visibility in `pt/curso.html` is **Naskh only** (with `.hide-nastaliq` active or Nastaliq hidden by default for absolute beginners).
- The toggle button allows switching between **Modo Iniciante (Apenas Naskh)** and **Modo Completo (Naskh + Nastaliq)**.
- Mobile screens (< 768px) must format tables cleanly with horizontal scrolling or responsive stacking.

---

### Task 1: Create `pt/curso.html` Standalone Interactive Course Page

**Files:**
- Create: `pt/curso.html`

**Interfaces:**
- Consumes: Content and structure from `pt/curso.org` / `pt/curso.md`.
- Produces: `pt/curso.html` with complete Módulo 0 and Lições 1–7.

- [ ] **Step 1: Write HTML `<head>`, CSS styles, and sticky controls panel in `pt/curso.html`**

Include:
- Google Fonts (`Inter`, `Noto Naskh Arabic`, `Noto Nastaliq Urdu`, `Vazirmatn`, `Gulzar`).
- CSS rules for `.hide-nastaliq .nastaliq-col`, `.hide-nastaliq .aljamiado-nastaliq`, `.course-table`, and `@media (max-width: 768px)` responsive styles.
- Navigation header with links back to `pt/index.html` (*"📖 Especificação Ortográfica"*) and `index.html` (*"🌐 English Studio"*).
- Sticky controls panel with the big toggle button (*"👁️ Modo Iniciante (Apenas Naskh) — Clique para mostrar Nastaliq"*).

- [ ] **Step 2: Add Módulo 0 (Fundamentos) & Hero Section**

Include hero box detailing goals for Brazilian Muslims, reverts, Lusophones, and Persophone refugees.

- [ ] **Step 3: Add Lições 1 a 7 with side-by-side Naskh and Nastaliq tables**

Lição 1: Non-connectors (`ا`, `و`, `ر`, `ز`) & Gol He (`ہ` / `ـه`)  
Lição 2: Lower stroke (`ب`, `پ`, `ت`) & Dāl (`د`)  
Lição 3: Kāf/Gāf (`ك`, `گ`) & Initial Vowel Supports  
Lição 4: Mīm (`م`), Nūn (`ن`), Ye (`ی`) & Nasalization Motor  
Lição 5: Sīn/Shīn (`س`, `ش`), Chā (`چ`), Žā (`ژ`) & Hiatus vs. Diphthong  
Lição 6: Lām (`ل`), LH (`ل-ی`), NH (`ن-ی`), RR (`ه`)  
Lição 7: Plural Logogram `-hā` (`ـها`) & Final Summary  

- [ ] **Step 4: Add `toggleNastaliqVisibility()` JavaScript function before `</body>`**

```javascript
function toggleNastaliqVisibility() {
  var container = document.getElementById('course-content');
  var btn = document.getElementById('toggle-nastaliq-btn');
  var isHidden = container.classList.contains('hide-nastaliq');
  
  if (isHidden) {
    container.classList.remove('hide-nastaliq');
    if (btn) btn.innerHTML = '👁️ Modo Completo (Naskh + Nastaliq) &mdash; Clique para ocultar Nastaliq';
  } else {
    container.classList.add('hide-nastaliq');
    if (btn) btn.innerHTML = '👁️ Modo Iniciante (Apenas Naskh) &mdash; Clique para mostrar Nastaliq';
  }
}
```

- [ ] **Step 5: Verify `pt/curso.html` in browser / terminal syntax check**

Verify HTML tag structure and ensure no broken tags.

---

### Task 2: Add Navigation Banner to `pt/index.html` and `index.html`

**Files:**
- Modify: `pt/index.html`
- Modify: `index.html`

- [ ] **Step 1: Add link to `pt/curso.html` in `pt/index.html` controls bar**

Add a prominent button:
```html
<a href="curso.html" class="btn btn-primary" style="background: #2563eb; color: #fff; text-decoration: none; padding: 0.6rem 1rem; border-radius: 6px; font-weight: 600;">
  🎓 Curso Gradual para Iniciantes (curso.html)
</a>
```

- [ ] **Step 2: Add link to `pt/curso.html` in `index.html` controls bar**

Add link to Portuguese course for English users seeking the step-by-step course.

---

### Task 3: Update `build.py` & Final Verification

**Files:**
- Modify: `build.py`
- Verify: `pt/curso.html`, `pt/index.html`, `index.html`

- [ ] **Step 1: Update `build.py` to confirm compilation pipeline**

Ensure `python3 build.py` executes cleanly and updates all targets.

- [ ] **Step 2: Run `python3 build.py` and verify clean build**

Run: `python3 build.py`

- [ ] **Step 3: Commit all changes**

```bash
git add pt/curso.html pt/index.html index.html build.py docs/superpowers/plans/2026-08-24-curso-html-implementation.md
git commit -m "feat(pt): create interactive pt/curso.html course page with nastaliq toggle"
```
