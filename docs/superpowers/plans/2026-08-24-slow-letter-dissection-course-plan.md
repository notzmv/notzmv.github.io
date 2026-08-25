# Slow-Paced Letter-Family Dissection & He-Specialized Course Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redesign the course (`pt/curso.org`, `pt/curso.md`, `pt/curso.html`) to slow down the pace for beginners, systematically spread positional letter coverage across letter families in Lições 1-7, provide explicit "tearing apart and stitching together" (desconstrução e reconstrução) letter-by-letter breakdowns for every example word, and dedicate deep, focused attention to the complexities of **He (`ه` / `ہ`)**.

**Architecture:**
- **Lição 1**: Não-Conectores (`ا`, `د`, `ر`, `ز`, `ژ`, `و`) — Dissecção palavra por palavra nas formas Isolada e Final.
- **Lição 2**: Família do Bā (`ب`, `پ`, `ت`) — Análise posicional (Isolada, Inicial, Medial, Final) com desconstrução letra a letra.
- **Lição 3**: Família do Jīm (`ج`, `چ`) & Sīn (`س`, `ش`) — Desconstrução de caudas e conexões dentadas nas 4 posições.
- **Lição 4**: Conectores de Alça e Gancho (`ف`, `ك`, `گ`, `ل`) — Transição de hastes e ganchos nas 4 posições.
- **Lição 5**: Laços Circulares e Nasais (`م`, `ن`, `ی`) — Motor de nasalização e semivogais.
- **Lição 6**: **O Universo do He (`ه` / `ہ` Gol He) e Suas Complexidades**:
  - 1. *H mudo latino inicial*: `همم` (*homem*), `هنرہ` (*honra*), `وهژہ` (*hoje*).
  - 2. *RR intervocálico*: `كاهo` $\rightarrow$ `كاهو` (*carro*), `تہہ` (*terra*).
  - 3. *Gol He Urdu final (-a, -e)*: `بوہ` (*boa*), `كہ` (*que*).
  - 4. *Logograma de Plural -hā (`ـها`)*: `لیوروها` (*livros*).
  - 5. *Contraste R- inicial com Rā (`ر`)*: `ریو` (*rio*), `روه` (*rua*).
- **Lição 7**: Costura Final e Síntese de Leitura.
- **Matriz Completa de Formas Posicionais**: Tabela síntese mestre mantida ao final.

**Tech Stack:** Org-mode (`pt/curso.org`), HTML5/CSS3 (`pt/curso.html`), Markdown (`pt/curso.md`), Python (`build.py`).

---

### Task 1: Restructure `pt/curso.org` with Letter-by-Letter Breakdown & He Deep Dive

**Files:**
- Modify: `pt/curso.org`

- [ ] **Step 1: Expand Lições 1-5 with "Desconstrução e Reconstrução Gráfica" tables**
  Add explicit letter breakdown columns for every example word:
  - Exemplo: *esperança* $\rightarrow$ `ا` (Isolada) + `س` (Inicial) + `پ` (Medial) + `ر` (Final) + `ن` (Inicial) + `چ` (Medial) + `ہ` (Final) $\rightarrow$ `اسپرنچہ`.

- [ ] **Step 2: Rewrite Lição 6 into "O Universo do He (ه / ہ) e Suas Complexidades"**
  Detail the 5 core functions of **He** with step-by-step letter stitching and comparison tables.

- [ ] **Step 3: Update final Matriz Posicional Completa**

---

### Task 2: Update `pt/curso.html` with Dissection Tables & He Deep Dive

**Files:**
- Modify: `pt/curso.html`

- [ ] **Step 1: Add HTML step-by-step breakdown tables in Lições 1-7**
  Include Naskh and Nastaliq classes (`.aljamiado-naskh`, `.aljamiado-nastaliq`).

- [ ] **Step 2: Format Lição 6 (He Complexities) in `pt/curso.html`**

---

### Task 3: Build & Run Empirical Verification

**Files:**
- Execute: `python3 build.py`

- [ ] **Step 1: Run `python3 build.py`**

- [ ] **Step 2: Run verification script checking 21 letters & He breakdown**

- [ ] **Step 3: Commit to Git**

```bash
git add pt/curso.org pt/curso.md pt/curso.html build.py docs/superpowers/plans/2026-08-24-slow-letter-dissection-course-plan.md
git commit -m "feat(pt): expand course with slow letter dissection and deep He complexities dive"
```
