# Mobile Responsiveness Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement mobile responsiveness rules across `index.html` and `pt/index.html` so controls, Perso-Arabic text, and tables scale seamlessly on smartphones.

**Architecture:** Add `@media (max-width: 680px)` styles for responsive containers, stacked controls, full-width touch toggle buttons, mobile table scrolling (`table { display: block; overflow-x: auto; }`), and word-wrapping for `.perso-arabic`.

**Tech Stack:** CSS3 Media Queries, HTML5.

## Global Constraints

- **Mobile Breakpoint**: `@media (max-width: 680px)`.
- **Target Devices**: Mobile phones (iPhone, Android, widths 320px–680px).
- **Touch Standard**: Minimum 44px height for interactive buttons and links.

---

### Task 1: Add Mobile Responsive Styles to `pt/index.html`

**Files:**
- Modify: `pt/index.html`

- [ ] **Step 1: Add mobile CSS rules to `pt/index.html`**

Add the following media query block to `pt/index.html`:
```css
    @media (max-width: 680px) {
      body {
        padding: 1rem 0.75rem;
      }

      h1 {
        font-size: 1.6rem;
      }

      h2 {
        font-size: 1.3rem;
        margin: 1.8rem 0 0.8rem 0;
      }

      .controls {
        flex-direction: column;
        align-items: stretch;
        gap: 0.8rem;
        padding: 0.8rem;
        top: 0.5rem;
      }

      .btn-big-toggle {
        width: 100%;
        justify-content: center;
        text-align: center;
        padding: 0.75rem 1rem;
        min-height: 44px;
      }

      .btn-group {
        width: 100%;
        justify-content: center;
      }

      .btn {
        min-height: 44px;
        display: inline-flex;
        align-items: center;
      }

      table {
        display: block;
        width: 100%;
        overflow-x: auto;
        white-space: nowrap;
        -webkit-overflow-scrolling: touch;
      }

      th, td {
        padding: 0.6rem 0.75rem;
        font-size: 0.88rem;
      }

      .ar, .perso-arabic {
        font-size: 1.5rem;
        line-height: 2.2;
        overflow-wrap: break-word;
        word-break: break-word;
      }

      .perso-arabic {
        padding: 0.8rem 1rem;
      }

      .card {
        padding: 1rem;
      }
    }
```

- [ ] **Step 2: Commit changes**

```bash
git add pt/index.html
git commit -m "style(pt): add mobile responsiveness CSS rules to pt/index.html"
```

---

### Task 2: Add Mobile Responsive Styles to `index.html`

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Add mobile CSS rules to `index.html`**

Add the same `@media (max-width: 680px)` block to `index.html`.

- [ ] **Step 2: Commit changes**

```bash
git add index.html
git commit -m "style(en): add mobile responsiveness CSS rules to index.html"
```

---

### Task 3: Build & Final Pipeline Verification

- [ ] **Step 1: Execute `build.py`**

Run: `python3 build.py`
Verify exit code is 0 and output confirms clean build.

- [ ] **Step 2: Commit final updates**

```bash
git add index.html pt/index.html build.py index.md pt/index.md
git commit -m "chore: verify mobile responsive build pipeline"
```
