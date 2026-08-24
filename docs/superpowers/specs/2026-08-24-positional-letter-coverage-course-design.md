# Design Specification: Positional Letter Coverage for Aljamiado Português Course

**Date**: 2026-08-24  
**Author**: Umar & AI Pair Assistant  
**Target Files**: `pt/curso.org`, `pt/curso.md`, `pt/curso.html`, `build.py`

---

## 1. Objective

Systematically expand the vocabulary and positional exemplification in the Aljamiado Português course (`pt/curso.org`, `pt/curso.md`, `pt/curso.html`) so that **every letter in the adapted Perso-Arabic alphabet** has at least one explicit Portuguese example word for **every valid positional form** (Isolada, Inicial, Medial, Final).

---

## 2. Structural Approach: Hybrid Model

1. **Lesson Vocabulary Expansion (Lições 1 a 7)**:
   - Ensure the tables in Lições 1 to 7 cover initial, medial, and final forms as each letter family is introduced.

2. **Master Positional Forms Matrix (Matriz Completa de Formas Posicionais)**:
   - Add a dedicated section at the end of the course (after Lição 7) containing a complete 21-letter reference matrix.
   - For each letter, list its name, shape family, and explicit Portuguese example words for:
     - **Isolada** (Isolated)
     - **Inicial** (Initial - for connecting letters)
     - **Medial** (Medial - for connecting letters)
     - **Final** (Final)

---

## 3. Letter & Positional Inventory Mapping

| Letra | Nome | Tipo | Formas Posicionais | Exemplo Isolada | Exemplo Inicial | Exemplo Medial | Exemplo Final |
|-------|------|------|--------------------+-----------------+-----------------+----------------+---------------|
| **ا** | Alif | Não-conector | Isolada / Final | *a* (`ا`) | &mdash; | &mdash; | *da* (`دا`), *já* (`ژا`) |
| **ب** | Bā | Conector | 4 Formas | *b* (`ب`) | *boa* (`بوہ`) | *sabedoria* (`سبدریہ`) | *sob* (`سب`) |
| **پ** | Pā | Conector | 4 Formas | *p* (`پ`) | *para* (`پرہ`) | *esperança* (`اسپرنچہ`) | *strip* (`ستریپ`) |
| **ت** | Tā | Conector | 4 Formas | *tu* (`تو`) | *tudo* (`تودو`) | *fruto* (`فروتو`) | *até* (`اتى`) |
| **ج** | Jīm | Conector | 4 Formas | *gênero* (`جinro`) | *gente* (`جنتہ`) | *generosidade* (`جنرزددہ`) | *gem* (`جم`) |
| **چ** | Chā | Conector | 4 Formas | *cê* (`چہ`) | *cidade* (`چددہ`) | *você* (`وچہ`) | *fixo* (`فيچو`) |
| **د** | Dāl | Não-conector | Isolada / Final | *de* (`دہ`) | *do* (`دو`) | &mdash; | *vida* (`ویدہ`) |
| **ر** | Rā | Não-conector | Isolada / Final | *rio* (`ریو`) | *rua* (`روه`) | &mdash; | *ver* (`ور`), *por* (`پور`) |
| **ز** | Zāy | Não-conector | Isolada / Final | *zé* (`زہ`) | *zero* (`زرو`) | &mdash; | *paz* (`پز`), *traz* (`ترز`) |
| **ژ** | Žā | Não-conector | Isolada / Final | *já* (`ژا`) | *jogo* (`ژگو`) | &mdash; | *hoje* (`وهژہ`) |
| **س** | Sīn | Conector | 4 Formas | *se* (`سہ`) | *sua* (`سوه`) | *processo* (`پرچسو`) | *mas* (`مس`) |
| **ش** | Shīn | Conector | 4 Formas | *chá* (`شا`) | *chave* (`شوه`) | *lixo* (`لیشو`) | *flash* (`فلاش`) |
| **ف** | Fā | Conector | 4 Formas | *fé* (`فی`) | *faz* (`فز`) | *professora* (`پرفسرہ`) | *off* (`اف`) |
| **ك** | Kāf | Conector | 4 Formas | *que* (`كہ`) | *cada* (`كدہ`) | *busca* (`بوسكہ`) | *check* (`چك`) |
| **گ** | Gāf | Conector | 4 Formas | *gostei* (`گوستى`) | *guia* (`گیہ`) | *água* (`آگوه`) | *blog* (`بلگ`) |
| **ل** | Lām | Conector | 4 Formas | *ele* (`إلى`) | *luz* (`لوز`) | *pelo* (`پلو`) | *sol* (`سل`) |
| **م** | Mīm | Conector | 4 Formas | *me* (`مہ`) | *muito* (`مویتو`) | *como* (`كمو`) | *bom* (`بم`) |
| **ن** | Nūn | Conector | 4 Formas | *na* (`نہ`) | *não* (`ناو`) | *análise* (`انالیزہ`) | *on* (`ان`) |
| **و** | Waw | Não-conector | Isolada / Final | *o* (`و`) | *ou* (`او`) | &mdash; | *como* (`كمو`), *livro* (`لیورو`) |
| **ه / ہ** | He | Conector/Gol He | 4 Formas | *honra* (`هنرہ`) | *homem* (`همم`) | *carro* (`كهو`) | *boa* (`بوہ`), *vida* (`ویدہ`) |
| **ی** | Ye | Conector | 4 Formas | *e* (`ی`) | *ilumina* (`یلومنہ`) | *minha* (`مینیہ`) | *até* (`اتى`), *gostei* (`گوستى`) |

---

## 4. Implementation Steps

1. Update `pt/curso.org` with the Master Positional Matrix section and expanded lesson tables.
2. Update `pt/curso.md` via `build.py`.
3. Update `pt/curso.html` with the formatted HTML matrix and updated lesson tables.
4. Verify all transcriptions, positional tags, and rendering in both Naskh and Nastaliq modes.
