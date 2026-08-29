# Restore Hamzah for Tonic High Vowels (-í, -ú) and Hiatos Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the pre-positioned Alif idea with **Hamzah (`ئ` / `ؤ`)** as the official support for tonic final *-í*, *-ú*, and internal hiatos (*aqui* `اكئ`, *caju* `كژؤ`, *país* `پائس`, *saúde* `ساؤدہ`, *baú* `باؤ`) across `pt/index.org`, `pt/curso.org`, `SKILL.md`, and recompile via `build.py`.

**Files:**
- Modify: `pt/index.org`, `pt/curso.org`, `~/.gemini/config/plugins/superpowers/skills/aljamiado-portugues/SKILL.md`
- Recompile via `build.py`: `pt/index.html`, `pt/index.md`, `pt/curso.html`, `pt/curso.md`

---

### Task 1: Update `pt/index.org` with Hamzah for Tonic High Vowels & Hiatos

- [ ] **Step 1: Replace pre-positioned Alif section in `pt/index.org` with Hamzah (`ئ` / `ؤ`) for tonic final *-í* and *-ú***
- [ ] **Step 2: Update Hiato section in `pt/index.org` to use Hamzah (`پائس`, `ساؤدہ`, `باؤ`)**

---

### Task 2: Update `pt/curso.org` with Hamzah

- [ ] **Step 1: Update final vowels & oxítonas section in `pt/curso.org` to use Hamzah (`ئ` / `ؤ`)**
- [ ] **Step 2: Update hiato summary table and examples in `pt/curso.org`**

---

### Task 3: Update Skill & Build & Verify

- [ ] **Step 1: Update `aljamiado-portugues` SKILL.md with Hamzah rules for tonic high vowels & hiatos**
- [ ] **Step 2: Run `python3 build.py` to recompile HTML and Markdown files**
- [ ] **Step 3: Run Python verification script confirming Hamzah presence and clean build**
- [ ] **Step 4: Commit changes to Git**

```bash
git add pt/index.org pt/curso.org pt/index.html pt/curso.html pt/index.md pt/curso.md docs/superpowers/plans/2026-08-29-hamzah-tonic-high-vowels-plan.md
git commit -m "feat(pt): use Hamzah (ئ / ؤ) for tonic final -í/-ú and internal hiatos"
```
