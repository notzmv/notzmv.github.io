# Community-Focused Examples Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the 10 meta-academic example sentences across `pt/index.html`, `pt/index.md`, and `pt/index.org` with 10 warm, community-focused example sentences suitable for general and Muslim readers.

**Architecture:** Update corpus sections in HTML, Markdown, and Org formats to maintain identical text across all 3 files while strictly adhering to Aljamiado Português orthographic rules.

**Tech Stack:** HTML, Markdown, Org-mode, Python verification script.

## Global Constraints

- Preserve exact HTML structure (`.card`, `.card-meta`, `.portuguese`, `.ipa`, `.perso-arabic.ar`, `.notes`).
- Maintain exact orthographic rules (logogram `-hā` for nominal plurals, Urdu Gol He `ه` for final `-a`/`-e`, Waw `و` for final `-o`, Chā `چ` for soft C/CH, Žā `ژ` or Jīm `ج` for soft G/J).
- Ensure 0 stray ASCII characters in Perso-Arabic transcriptions.

---

### Task 1: Update Corpus Cards in `pt/index.html`

**Files:**
- Modify: `pt/index.html:324-404`

- [ ] **Step 1: Replace Frases 1 to 10 in `pt/index.html`**

Replace lines 324-404 in `pt/index.html` with the 10 community-focused cards:
Card 1: *Que a paz e as bênçãos estejam com você e sua família.*
Card 2: *A busca pelo conhecimento é um dever de todos.*
Card 3: *A paciência e a gratidão trazem paz e sabedoria no coração.*
Card 4: *Seja muito bem-vindo à nossa comunidade.*
Card 5: *As boas ações e as palavras sinceras transformam o mundo.*
Card 6: *Que Deus abençoe o seu trabalho e os seus estudos.*
Card 7: *A verdade e a justiça iluminam o caminho dos homens.*
Card 8: *A verdadeira riqueza está na generosidade do coração.*
Card 9: *Cada novo dia é uma oportunidade para fazer o bem.*
Card 10: *A união de corações sinceros constrói uma vida cheia de paz.*

- [ ] **Step 2: Verify HTML syntax**
Ensure all tags are closed properly.

- [ ] **Step 3: Commit**

```bash
git add pt/index.html
git commit -m "content(pt): update HTML corpus cards with community-focused examples"
```

---

### Task 2: Update Corpus Samples in `pt/index.md`

**Files:**
- Modify: `pt/index.md:246-281`

- [ ] **Step 1: Replace Corpus Section 7 in `pt/index.md`**

Replace Section 7 in `pt/index.md` with the 10 new community-focused examples matching the HTML content.

- [ ] **Step 2: Commit**

```bash
git add pt/index.md
git commit -m "content(pt): update Markdown corpus list with community-focused examples"
```

---

### Task 3: Update Corpus Samples in `pt/index.org`

**Files:**
- Modify: `pt/index.org:413-449`

- [ ] **Step 1: Replace Section 4 in `pt/index.org`**

Replace Section 4 in `pt/index.org` with the 10 new community-focused examples matching the HTML and Markdown content.

- [ ] **Step 2: Commit**

```bash
git add pt/index.org
git commit -m "content(pt): update Org-mode corpus list with community-focused examples"
```

---

### Task 4: Run Verification & Final Check

**Files:**
- Test: All files via python verification script

- [ ] **Step 1: Run Python ASCII verification script**

Run:
```bash
python3 -c "
import re, glob, os
files = glob.glob('/home/umar/projects/notzmv.github.io/**/*', recursive=True)
ascii_in_arabic_re = re.compile(r'[\u0600-\u06FF]+[a-zA-Z]+[\u0600-\u06FF]*|[\u0600-\u06FF]*[a-zA-Z]+[\u0600-\u06FF]+')
found = False
for f in sorted(files):
    if os.path.isfile(f) and not f.endswith('.git'):
        with open(f, 'r', encoding='utf-8') as fh:
            for line_num, line in enumerate(fh, 1):
                matches = ascii_in_arabic_re.findall(line)
                if matches:
                    print(f'{f}:{line_num}: {matches} ---> {line.strip()}')
                    found = True
if not found:
    print('VERIFICATION SUCCESSFUL')
"
```
Expected output: `VERIFICATION SUCCESSFUL`

- [ ] **Step 2: Commit final changes if any**
