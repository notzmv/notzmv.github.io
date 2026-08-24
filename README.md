# Aljamiado English & Aljamiado Português Specifications

**Author**: Umar  
**Date**: 2026-08-24  
**Tags**: `#aljamiado` `#english` `#portuguese` `#orthography` `#linguistics` `#script` `#persian`

---

## Interactive Typography & Corpus Studios

- 🇬🇧 **Aljamiado English Studio**: [index.html](index.html) (`/`)
- 🇵🇹 **Aljamiado Português Studio**: [pt/index.html](pt/index.html) (`/pt/`)

Both studios feature interactive Perso-Arabic font switching between **Gulzar Nastaliq**, **Vazirmatn**, **Noto Naskh**, and **Aref Ruqaa**.

---

## Available Specifications in Repository

### 1. English Aljamiado (Aljamiado English)
- **Web Studio**: [index.html](index.html)
- **Org-Mode Specification**: [index.org](index.org)
- **Markdown Specification**: [index.md](index.md)

Key Principles:
1. **Morphophonemic Plural Domain (`-hā` / `ـها`)**: Nominal plurals attach `-hā` (`books` &rarr; `بوكها`), distinguishing them from 3rd-person singular present verbs (`he speaks` &rarr; `هى اسپيكس`).
2. **Dental Fricatives**: Voiceless *th* [θ] uses **Sā** (`ث`), while voiced *th* [ð] uses **Zāl** (`ذ`).
3. **Velar Nasal**: Uses **Nūn-Gāf** (`نگ`) in digital contexts for clean web rendering (`sing` &rarr; `سنگ`), while **Sağır Kāf** (`ڭ`) is preferred when writing by hand for natural penmanship.

---

### 2. Portuguese Aljamiado (Aljamiado Português)
- **Web Studio**: [pt/index.html](pt/index.html)
- **Org-Mode Specification**: [pt/index.org](pt/index.org)
- **Markdown Specification**: [pt/index.md](pt/index.md)

Key Principles:
1. **Soft C vs. Soft G/J**: Soft *c* before *e/i* uses **Chā** (`چ`) (`cenoura` &rarr; `چنوره`), while soft *g/j* uses **Žā** (`ژ`) (`projeto` &rarr; `پرژتو`).
2. **Rhotic Distinction**: Single tap *r* uses **Rā** (`ر`) (`caro` &rarr; `كارو`), whereas double *rr* or initial *r-* uses **He** (`ه`) (`carro` &rarr; `كاهو`, `rio` &rarr; `هيو`).
3. **Palatal Digraphs**: *lh* [ʎ] maps to **Lām-Yā** (`لي`) (`filho` &rarr; `فيليو`) and *nh* [ɲ] maps to **Nūn-Yā** (`ني`) (`minha` &rarr; `مينيه`).
4. **Stress Accentuation**: Uses **Tonic Alif** (`ا`) to mark primary stress on non-initial syllables.
5. **Nasal Diphthongs**: Explicit *-ão* (`ناو`), *-ãe* (`ناي`), *-õe* (`نژو`).

---

## Repository Structure

```
.
├── README.md             # Multi-lingual overview and guide
├── index.html            # English interactive web studio
├── index.org             # English Org-mode specification
├── index.md              # English Markdown specification
└── pt/
    ├── index.html        # Portuguese interactive web studio
    ├── index.org         # Portuguese Org-mode specification
    └── index.md          # Portuguese Markdown specification
```
