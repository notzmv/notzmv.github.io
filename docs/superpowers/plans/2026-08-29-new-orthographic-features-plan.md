# Implement New Orthographic Features & Adapt Documentation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Integrate the user's new orthographic innovations into `pt/index.org`, `pt/curso.org`, and the `aljamiado-portugues` skill, then recompile `pt/index.html`, `pt/index.md`, `pt/curso.html`, and `pt/curso.md` via `build.py`:
1. **Final *-e* mapped to Ye (`ی`)** and **pre-positioned Alif support (`ـای` / `ـاو`) for tonic final *-í* and *-ú*** (*aqui* `اكای`, *rubi* `ربای`, *caju* `كژاو`).
2. **Ultra-Compact Shorthand Logograma Mīm (`ـم`) for Nasal Diphthongs** (*convenção* `كنونچم`, *coração* `كرچم`, *convenções* `كنونچمها`, *razões* `رزمها`).

**Files:**
- Modify: `pt/index.org`, `pt/curso.org`, `~/.gemini/config/plugins/superpowers/skills/aljamiado-portugues/SKILL.md`
- Recompile via `build.py`: `pt/index.html`, `pt/index.md`, `pt/curso.html`, `pt/curso.md`

---

### Task 1: Update Specification in `pt/index.org`

- [ ] **Step 1: Add Final *-e* in Ye (`ی`) & Pre-positioned Alif support (`ـای` / `ـاو`) for tonic final *-í* / *-ú* to `pt/index.org`**
- [ ] **Step 2: Add Ultra-Compact Shorthand Logograma Mīm (`ـم`) for Nasal Diphthongs to `pt/index.org`**
- [ ] **Step 3: Update surrounding tables and descriptions in `pt/index.org`**

---

### Task 2: Update Gradual Course in `pt/curso.org`

- [ ] **Step 1: Document Final *-e* in Ye (`ی`) & Pre-positioned Alif support (`ـای` / `ـاو`) for tonic final *-í* / *-ú* in `pt/curso.org`**
- [ ] **Step 2: Document Ultra-Compact Shorthand Logograma Mīm (`ـم`) for Nasal Diphthongs in `pt/curso.org`**
- [ ] **Step 3: Update surrounding summary tables in `pt/curso.org`**

---

### Task 3: Update Skill & Build & Verification

- [ ] **Step 1: Update `aljamiado-portugues` SKILL.md with the new features**
- [ ] **Step 2: Run `python3 build.py` to recompile HTML and Markdown files**
- [ ] **Step 3: Run Python verification script confirming clean build and feature presence**
- [ ] **Step 4: Commit to Git**

```bash
git add pt/index.org pt/curso.org pt/index.html pt/curso.html pt/index.md pt/curso.md docs/superpowers/plans/2026-08-29-new-orthographic-features-plan.md
git commit -m "feat(pt): document final -e in Ye, tonic -í/-ú in -ai/-au, and Mīm shorthand for nasal diphthongs"
```
