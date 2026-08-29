# System Genesis, Design Evolution & Priority Hierarchy Section Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a new section detailing the historical genesis, Persian inspiration, evolution from diacritics to *Mater Lectionis*, and the 4-tier hierarchy of orthographic priorities in Aljamiado Português across `pt/curso.org`, `pt/curso.html`, `pt/curso.md`, `pt/index.org`, `pt/index.html`, and `pt/index.md`.

**Key Concepts to Document:**
1. **Gênese e Inspiração Persa**:
   - Início: Tentativa de transpor o sistema do Persa, onde as vogais breves (/a/, /e/, /o/) são omitidas ou marcadas com diacríticos (*fatha*, *kasra*, *damma*), e apenas /i/ e /u/ usam Ye/Waw.
   - Motivação inicial: Em português, as vogais **A, O, E** superam em larga escala as vogais **I, U**. Pelo princípio da economia pura, faria sentido deixar A, O, E não marcados.
2. **A Evolução: Da Omissão ao Sistema de Mater Lectionis**:
   - O problema: Escrever diacríticos (*harakat*) em todo o texto tornava a escrita manual lenta e poluída.
   - A solução: Criar um sistema fluido de **Mater Lectionis por Proximidade Fonética** (Alif, Waw, Ye, Gol He), eliminando diacríticos incômodos.
3. **A Hierarquia de Prioridades Ortográficas (A Busca pelo Equilíbrio)**:
   - **Prioridade 1: Encontros Vocálicos e Hiatos Críticos**:
     - Devem quase sempre ser grafados de forma explícita com ambas as vogais.
     - *Exceção Inteligente de Economia*: Omissão permitida quando não há risco de colisão homógrafa. Exemplo: *hiato* $\rightarrow$ **`هیتو`** (He + Ye + Tā + Waw), onde a omissão do Alif em *-ia-* não gera confusão com nenhuma outra palavra portuguesa.
   - **Prioridade 2: Oxítonas Tónicas e Vogais Acentuadas**:
     - Picos tónicos (*fé* `فی`, *até* `اتی`, *pó* `پو`, *riqueza* `ریكزہ`) exigem suporte vocálico explícito.
   - **Prioridade 3: Vogais Altas (I / U) e Redução de Polissílabos**:
     - Podem ser omitidas em palavras longas quando o esqueleto consonantal é inconfundível (*generosidade* `جنرزددہ`).
   - **Prioridade 4: Público, Contexto e Balanço Leitura vs. Escrita**:
     - O regime desliza conforme o objetivo (anotação pessoal rápida vs. texto formal legível para iniciantes).

**Tech Stack:** Org-mode (`pt/curso.org`, `pt/index.org`), HTML5 (`pt/curso.html`, `pt/index.html`), Markdown (`pt/curso.md`, `pt/index.md`), Python (`build.py`).

---

### Task 1: Update `pt/curso.org` and `pt/curso.html`

**Files:**
- Modify: `pt/curso.org`, `pt/curso.html`

- [ ] **Step 1: Insert section "A Gênese do Sistema: Da Inspiração Persa ao Equilíbrio das Mater Lectionis" in `pt/curso.org`**
- [ ] **Step 2: Insert HTML version in `pt/curso.html`**

---

### Task 2: Update `pt/index.org` and `pt/index.html`

**Files:**
- Modify: `pt/index.org`, `pt/index.html`

- [ ] **Step 1: Update design principles & history in `pt/index.org`**
- [ ] **Step 2: Update HTML version in `pt/index.html`**

---

### Task 3: Build & Verification

- [ ] **Step 1: Run `python3 build.py`**
- [ ] **Step 2: Run Python verification script confirming new section in all files**
- [ ] **Step 3: Commit to Git**

```bash
git add pt/curso.org pt/curso.html pt/curso.md pt/index.org pt/index.html pt/index.md docs/superpowers/plans/2026-08-25-genesis-and-priority-hierarchy-plan.md
git commit -m "docs(pt): document system genesis from Persian inspiration to Mater Lectionis priority hierarchy"
```
