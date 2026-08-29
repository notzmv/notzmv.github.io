# Anki Exporter Tool Plan for Aljamiado Português

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a CLI and Python tool `anki_exporter.py` to extract the **Curso progression**, **Corpus sentences**, and **Master paradigms**, generate **full Tashkīl (vowel marks & diacritics)** following all orthographic rules, and automatically push/sync structured decks to Anki via `AnkiConnect` API (port 8765) as well as generate TSV/JSON backups.

**Files:**
- Create: `anki_exporter.py`
- Create: `tests/test_anki_exporter.py`
- Output Decks in Anki via AnkiConnect:
  - `Aljamiado Português::01 - Curso Gradual::Lição 1` ... `Lição 7`
  - `Aljamiado Português::02 - Corpus de Frases`
  - `Aljamiado Português::03 - Vocabulário Mestre`

---

### Task 1: Design the Full Tashkīl Engine & Data Extractor

- [ ] **Step 1: Build the Tashkīl engine mapping Aljamiado words/sentences to full Harakāt (`vowelled_aljamiado`)**
- [ ] **Step 2: Build the Data Extractor parsing `pt/curso.org`, `pt/index.org`, and `build.py` datasets**
- [ ] **Step 3: Test Tashkīl generation and extraction logic with Python unit tests**

---

### Task 2: Build AnkiConnect REST Client & Card Renderer

- [ ] **Step 1: Implement `AnkiConnectClient` handling `createDeck`, `modelNames`, `addNote`, `sync`**
- [ ] **Step 2: Design HTML Card templates (Dark mode, Pink `#f472b6` Arabic text, Naskh & Nastaliq fonts, IPA, and orthographic notes)**
- [ ] **Step 3: Build TSV and JSON backup exporters**

---

### Task 3: Build CLI & Execute Sync to Anki

- [ ] **Step 1: Add CLI interface (`python3 anki_exporter.py --sync --deck-prefix "Aljamiado Português"`)**
- [ ] **Step 2: Run full export and sync to AnkiConnect API**
- [ ] **Step 3: Run verification tests checking AnkiConnect deck creation and card count**
- [ ] **Step 4: Commit to Git**

```bash
git add anki_exporter.py tests/test_anki_exporter.py docs/superpowers/plans/2026-08-29-anki-exporter-plan.md
git commit -m "feat(anki): add Anki exporter tool with full Tashkīl engine and AnkiConnect integration"
```
