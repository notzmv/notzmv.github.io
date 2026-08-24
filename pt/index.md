# Aljamiado Português: Orthographic & Phonological Specification

**Author**: Umar  
**Date**: [2026-08-22 Sat]  
**Tags**: `#aljamiado` `#portuguese` `#orthography` `#linguistics` `#script`

---

## Table of Contents
- [Introduction & Overview](#introduction--overview)
- [1. Consonant Inventory & Perso-Arabic Mapping](#1-consonant-inventory--perso-arabic-mapping)
  - [Consonant Mapping Table](#consonant-mapping-table)
  - [Soft C vs. Soft G/J Distinction](#soft-c-vs-soft-gj-distinction)
  - [R vs. RR Distinction (Rā vs. He)](#r-vs-rr-distinction-rā-vs-he)
  - [Intervocalic S vs. SS Contrast (Zāy vs. Sīn)](#intervocalic-s-vs-ss-contrast-zāy-vs-sīn)
  - [Palatal Digraphs (lh, nh)](#palatal-digraphs-lh-nh)
- [2. Vowel System, Diacritics & Accentuation](#2-vowel-system-diacritics--accentuation)
  - [Word-Final Vowels (He vs. Waw)](#word-final-vowels-he-vs-waw)
  - [Initial Vowel Carriers & Madd Diacritics](#initial-vowel-carriers--madd-diacritics)
  - [Tonic Alif (ا) Stress Accentuation](#tonic-alif-ا-stress-accentuation)
  - [Open vs. Closed Vowel Contrasts (avô vs. avó)](#open-vs-closed-vowel-contrasts-avô-vs-avó)
- [3. Nasalization Engine](#3-nasalization-engine)
  - [Monosyllabic & Syllable-Final Nasals](#monosyllabic--syllable-final-nasals)
  - [Nasal Diphthongs (-ão, -ãe, -õe)](#nasal-diphthongs--ão--ãe--õe)
- [4. Morphophonemic Rules & Domain Mapping](#4-morphophonemic-rules--domain-mapping)
  - [Rule I: Nominal Number Domain (-hā / ـها)](#rule-i-nominal-number-domain--hā--ـها)
  - [Rule II: Direct Surface Substitution](#rule-ii-direct-surface-substitution)
  - [Rule III: Verbal & Lexical Sibilant Domain (س / ز)](#rule-iii-verbal--lexical-sibilant-domain-س--ز)
- [5. Edge Cases & Special Constructions](#5-edge-cases--special-constructions)
  - [Preposition + Article Contractions](#preposition--article-contractions)
  - [Lexical Singulars in -s / -z vs. Plural Inflections](#lexical-singulars-in--s--z-vs-plural-inflections)
  - [Hiatus vs. Diphthongs (país vs. pais)](#hiatus-vs-diphthongs-país-vs-pais)
  - [Clitic Attachment & Hyphenation](#clitic-attachment--hyphenation)
  - [Consonant Clusters](#consonant-clusters)
- [6. Master Paradigm Lookup Tables](#6-master-paradigm-lookup-tables)
  - [Determiners & Articles](#determiners--articles)
  - [Nominal & Adjectival Inflection](#nominal--adjectival-inflection)
  - [Verbal Agreement vs. Pronominal Clitics](#verbal-agreement-vs-pronominal-clitics)
- [7. Corpus & Sample Transcriptions](#7-corpus--sample-transcriptions)

---

## Introduction & Overview
*Bismillah al-Rahman al-Rahim* (In the name of God, the Most Gracious, the Most Merciful).

**Aljamiado Português** is a personal, highly systematic orthographic and phonetic adaptation of the Perso-Arabic script designed to write the Portuguese language. Historically, *Aljamiado* (from Arabic *'ajamiyya*, "non-Arabic / foreign language written in Arabic script") referred to Romance languages (Mozarabic, Spanish, Ladino) transcribed using Arabic letterforms.

This specification formalizes the orthographic engine for Portuguese. The system prioritizes:
1. **Morphophonemic Clarity**: Distinguishing nominal plural inflection from verbal agreement and lexical root sibilants.
2. **Visual Rhythm & Balance**: Utilizing a graphic plural suffix (`-hā` / `ـها`) to prevent long, repetitive *sīn* (`س`) tails from cluttering horizontal text flow.
3. **Phonetic & Graphic Precision**: Differentiating soft *c* (`چ`) from soft *g/j* (`ژ`), single *r* (`ر`) from double *rr* (`ه`), intervocalic *s* (`ز`) from double *ss* (`س`), establishing explicit Madd rules for initial vowels, and leveraging **Tonic Alif** (`ا`) for stress accentuation.

---

## 1. Consonant Inventory & Perso-Arabic Mapping

### Consonant Mapping Table

| Latin Grapheme | IPA Sound | Perso-Arabic Letter | Letter Name | Example Word | Aljamiado Transliteration |
|---|---|---|---|---|---|
| **b** | [b] | **ب** | Bā | *bom* | `بم` |
| **p** | [p] | **پ** | Pā | *prática* | `پراكتيكه` |
| **t** | [t] | **ت** | Tā | *tu* | `تو` |
| **d** | [d] | **د** | Dāl | *do* | `دو` |
| **f** | [f] | **ف** | Fā | *fazes* | `فازس` |
| **v** | [v] | **و** | Waw | *você* | `ووچه` |
| **k / c / q** (hard) | [k] | **ك** | Kāf | *coisa* | `كويزه` |
| **g** (hard) | [g] | **گ** | Gāf | *gostei* | `گوستى` |
| **c** (soft before e, i) | [s] / [tʃ] | **چ** | Chā | *cenoura* | `چنوره` |
| **g / j** (soft before e, i) | [ʒ] | **ژ** | Žā | *projeto* | `پرژتو` |
| **ch** | [ʃ] / [tʃ] | **چ** | Chā | *chave* | `چاوه` |
| **r** (single / tap) | [ɾ] | **ر** | Rā | *caro* | `كارو` |
| **rr / r-** (initial / trill) | [ʁ] / [r] | **ه** | He | *carro* / *rio* | `كاهو` / `هيو` |
| **s** (intervocalic /z/) | [z] | **ز** | Zāy | *coisa* | `كويزه` |
| **ss** (intervocalic /s/) | [s] | **س** | Sīn | *processo* | `پروچسو` |
| **m** (syllable onset) | [m] | **م** | Mīm | *minha* | `مينيه` |
| **n** (syllable onset) | [n] | **ن** | Nūn | *não* | `ناو` |
| **s / z** (lexical/verbal) | [s] / [z] | **س** / **ز** | Sīn / Zāy | *sim* / *paz* | `سيم` / `پاز` |
| **-s** (nominal plural) | [s] / [z] / [ʃ] | **ـها** | Hā | *livros* | `ليوروها` |

---

## 2. Vowel System, Diacritics & Accentuation

### Initial Vowel Carriers & Madd Diacritics

| Initial Sound | Graphic Representation | Diacritic Detail | Example Word | Aljamiado Transliteration |
|---|---|---|---|---|
| **Initial open é** [ɛ] | **إ̷** / **إي** | Alif with subscript Madd | *é* | `إ̷` / `إي` |
| **Initial open à** [a] | **آ** | Alif with superscript Madd | *à* | `آ` |
| **Initial unstressed e** [i]/[e] | **إ** | Alif with Kasrah | *estudo* | `إستودو` |
| **Initial a** [a] | **ا** | Plain Alif | *alfabeto* | `الفبتo` |
| **Initial o** [o]/[u] | **او** | Alif-Waw | *os* | `وها` |

---

## 3. Master Paradigm Lookup Tables

### Determiners & Articles

| Paradigm Item | Latin Spelling | Aljamiado Script | Morphophonemic Notes |
|---|---|---|---|
| **Masc. Sing. Def. Article** | *o* | `و` | Isolated Waw |
| **Masc. Plur. Def. Article** | *os* | `وها` | *o* (`و`) + *-hā* (`ـها`) |
| **Fem. Sing. Def. Article** | *a* | `ا` / `اه` | Alif / He |
| **Fem. Plur. Def. Article** | *as* | `اها` | *a* (`ا`) + *-hā* (`ـها`) |
| **Masc. Sing. Indef. Article** | *um* | `ام` / `اوم` | Mīm final |
| **Masc. Plur. Indef. Article** | *uns* | `انها` / `اونها` | Nasal assimilation + *-hā* |
| **Fem. Sing. Indef. Article** | *uma* | `اومه` | Final *-e/a* He |
| **Fem. Plur. Indef. Article** | *umas* | `اوماها` | *-uma* + *-hā* |

---

## 4. Corpus & Sample Transcriptions

1. *Equilíbrio é muito importante para a forma de escrever.* &rarr; `إكيليبكيو إ̷ مويتو إمپورتانته پارا ا فورمه دو إسكرور.`
2. *As coisas boas.* &rarr; `اها كويزها بوها`
3. *O livro bom e os livros bons.* &rarr; `و ليورو بم و وها ليوروها بنها`
4. *Consegui conversar com o Gemini sobre o projeto do português no alfabeto persa, ou melhor, uma adaptação.* &rarr; `كونسيگى كونورنار كم و جيمينى سوبره و پرژتو دو پرتوگيس نو الفبتو پرسه، او مليور، اومه ادپتاجو.`
5. *Boa sorte com os estudos! O processo de criar uma ortografia é fascinante, e muito bom ver como o sistema tá se desenvolvendo.* &rarr; `بوه سورته كم وها إستودوها! و پروچسو دو كزيار اومه اورتوگرافيه إ̷ فاسينانته، و مويتو بم وهر كومو و سيستمه تا سه ديزينوولويندو.`
