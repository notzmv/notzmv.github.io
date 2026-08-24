# Design Specification: Aljamiado Português Course (`curso.org`), Motivation, & UI Enhancements

**Date**: 2026-08-24  
**Author**: Umar & AI Pair Assistant  
**Target Files**: `pt/index.org`, `pt/index.md`, `pt/curso.org`, `pt/curso.md`, `build.py`

---

## 1. Objectives & Overview

This project expands **Aljamiado Português** into a two-tiered learning ecosystem:

1. **`pt/index.org` (Main Specification & Reference)**:
   - Concise formal reference for experienced readers, linguists, and reference lookups.
   - Comprehensive **Motivation** section detailing project goals, USP academic research context, refugee language learning applications, and future course roadmaps.

2. **`pt/curso.org` (Gradual Step-by-Step Course for Beginners)**:
   - Ultra-gradual course teaching Portuguese speakers how to write BR-Portuguese using the Persian alphabet.
   - Progression organized by **letter shape families** combined with **maximum vocabulary yield in BR-Portuguese**.
   - Dual script support with a **beginner-friendly Nastaliq toggle** (defaulting to clear Naskh, with Nastaliq optional/collapsible).
   - Mobile-responsive vertical card/table design (max 2 columns × 3 rows per card on mobile, 3–4 columns on desktop).

---

## 2. Motivation Architecture

### 2.1 Motivation in `pt/index.org` (Broad / Structural Focus)
- **Primary Audience**: Brazilian Muslims and Lusophones getting acquainted with the mechanics of the Arabic alphabet (joining, letter forms, right-to-left orientation) using their native Portuguese.
- **Secondary Audience**: Learners of Arabic and Persian seeking familiar script transition tools.
- **Refugee & Pedagogical Application**: Helping Iranian and Afghani refugees learn Portuguese in a familiar script environment (since Aljamiado PT adapts the Persian alphabet).
- **Academic Research Context**: Opportunity for research at USP (Universidade de São Paulo) on cross-script transfer, orthographic adaptation, and second language acquisition.
- **Strategic Roadmap**: Focus initial development on Lusophone learners of Aljamiado, while tracking and planning for future courses (such as a Persophone Portuguese course).

### 2.2 Motivation in `pt/curso.org` (Learner-Centric Focus)
- Explains *why* writing Portuguese in Perso-Arabic script is an effective bridge for learning Arabic/Persian letter mechanics.
- Reduces cognitive load: learners master script rules (R&rarr;L flow, initial/medial/final shapes, diacritics) using vocabulary they already know fluently.

---

## 3. Pedagogical Progression in `pt/curso.org`

The course is structured into 7 form-based lessons, ordering letter shape families by their ability to immediately produce high-frequency BR-Portuguese words:

### Módulo 0: Como Funciona a Escrita Perso-Árabe
- Direção da direita para a esquerda (R&rarr;L).
- Letras conectoras vs. não-conectoras.
- As 4 posições (Isolada, Inicial, Medial, Final).
- Sistema de alternância Naskh/Nastaliq.

### Lição 1: Não-Conectores Fundamentais — Alif (`ا`), Waw (`و`) e Família Rā (`ر`, `ز`)
- **Formas**: Haste vertical (`ا`), gancho (`و`), curva descendente simples (`ر`, `ز`).
- **Rendimento de Vocabulário**: *a* (`ا`), *o* (`و`), *ou* (`او`), *ao* (`او`), *ar* (`ار`), *ver* (`ور`), *por* (`پور`), *voz* (`وز`), *dor* (`دور`).

### Lição 2: Traço Baixo — Bā' (`ب`, `پ`, `ت`) e Gancho Dāl (`د`)
- **Formas**: Traço horizontal inferior com pontos + curva angular de Dāl.
- **Novas Palavras**: *de* (`دہ`), *do* (`دو`), *da* (`دا`), *para* (`پرہ`), *tudo* (`تودو`), *até* (`اتى`), *boa* (`بوہ`).

### Lição 3: Cúpulas & Hastes — Kāf/Gāf (`ك`, `گ`) e Gol He (`ہ` / `ـه`)
- **Formas**: Haste com diagonal superior + laço fechado de He.
- **Novas Palavras**: *que* (`كہ`), *com* (`كم`), *como* (`كمو`), *cada* (`كدہ`), *vida* (`ویدہ`), *faz* (`فز`).

### Lição 4: Laços Circulares — Mīm (`م`), Nūn (`ن`) e Ye (`ی`)
- **Formas**: Círculo com cauda (`م`), tigela com ponto (`ن`), curva em S (`ی`).
- **Novas Palavras**: *em* (`ام`), *um* (`اوم`), *uma* (`اومہ`), *não* (`ناو`), *na* (`نہ`), *no* (`نو`), *nem* (`نم`), *mais* (`میس`), *minha* (`مینیہ`).

### Lição 5: Dentes & Barrigas Curvas — Sīn/Shīn (`س`, `ش`), Chā (`چ`), Žā (`ژ`)
- **Formas**: Três dentes curvos + barriga curva com 3 pontos.
- **Novas Palavras**: *se* (`سہ`), *seu* (`سیو`), *sua* (`سوه`), *paz* (`پز`), *já* (`ژا`), *hoje* (`وهژہ`), *chega* (`چگہ`).

### Lição 6: Hastes Altas & Dígrafos — Lām (`ل`), LH (`ل-ی`), NH (`ن-ی`), RR (`ه`)
- **Formas**: Haste vertical longa conectiva e combinações palatais.
- **Novas Palavras**: *ele* (`إلى`), *ela* (`إلہ`), *filho* (`فیلیو`), *caminho* (`كمینیہ`), *terra* (`تہہ`), *carro* (`كهو`).

### Lição 7: Sufixo Nominal de Plural (`-hā` / `ـها`)
- **Formas**: Conexão mediana de He com Alif.
- **Novas Palavras**: *os* (`وها`), *as* (`اها`), *dos* (`دوها`), *das* (`داها`), *todos* (`تدوها`), *palavras* (`پلورها`).

---

## 4. UI, Layout & Nastaliq Toggle

1. **Nastaliq Toggle for Beginners**:
   - `curso.html` defaults to showing **Naskh only** (hiding Nastaliq to reduce difficulty for absolute beginners).
   - An interactive toggle button allows switching between **Modo Iniciante (Apenas Naskh)** and **Modo Completo (Naskh + Nastaliq)**.
   - CSS rules handle hiding/showing `.nastaliq-col` or `.aljamiado-nastaliq` elements smoothly.

2. **Mobile-Responsive Card Tables**:
   - On screens `< 768px`: Card grids scale down to 1–2 columns with compact vertical stacking.
   - On screens `≥ 768px`: Full multi-column comparison table.

---

## 5. Build Integration (`build.py`)

- `build.py` is updated to compile `pt/curso.org` into `pt/curso.md`.
