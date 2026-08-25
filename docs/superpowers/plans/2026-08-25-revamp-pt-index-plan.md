# Comprehensive Revamp of pt/index.org Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Thoroughly update `pt/index.org` to reflect all recent specification developments (AOM `اوم` standard for `-ão`, Didactic Tanwīn exact spellings, deprecation of Hamzah in hiatos, 4-tier priority hierarchy, organic proficiency navigation, `-ço/-ção/-ções` & `-são/-sões` morphological paradigms, `hoje` `هژہ`), deduplicate redundant sections, and build `pt/index.html` and `pt/index.md` via `build.py` (leaving the top 25 corpus sentences intact as requested).

**Files:**
- Modify: `pt/index.org`
- Generate via `build.py`: `pt/index.html`, `pt/index.md`

---

### Task 1: Update `pt/index.org` Content & Structure

- [ ] **Step 1: Update Consonantal Mapping & Letter X sections in `pt/index.org` (deduplicate Letter X block, set `hoje` `هژہ`, `visão` `ویزاوم`, `missão` `مساوم`, `razão` `رزاوم`)**
- [ ] **Step 2: Update System Vocálico & Didactic Tanwīn sections in `pt/index.org` (`prática` `پرًتكہ`, `mínimo` `مٍنمو`, `estúpido` `استٌپdo` / `استٌپدو`, 4-tier priority hierarchy, organic proficiency navigation, deduplicate scalar economy block)**
- [ ] **Step 3: Update Motor de Nasalização section in `pt/index.org` (AOM `اوم` standard for `-ão`, `-au` contrast, `-ções`/`-sões` plurals in `ـچومها` / `ـچویها` / `ـزومها` / `ـزویها` / `ـسومها`)**
- [ ] **Step 4: Update Regras Morfofonêmicas & Master Paradigm Tables in `pt/index.org` (deduplicate plural alternations table, synchronize spellings)**

---

### Task 2: Build & Verification

- [ ] **Step 1: Run `python3 build.py` to recompile `pt/index.html` and `pt/index.md`**
- [ ] **Step 2: Run Python verification script confirming AOM `اوم` standard, Didactic Tanwīn spellings, 4-tier priority hierarchy, and clean HTML compilation**
- [ ] **Step 3: Commit to Git**

```bash
git add pt/index.org pt/index.html pt/index.md docs/superpowers/plans/2026-08-25-revamp-pt-index-plan.md
git commit -m "feat(pt): comprehensively revamp pt/index.org specification with AOM standard, Didactic Tanwīn, and 4-tier priority hierarchy"
```
