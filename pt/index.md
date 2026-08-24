# Aljamiado Português: Especificação Ortográfica e Fonológica

**Autor**: Umar  
**Data**: [2026-08-24 Mon]  
**Tags**: `#aljamiado` `#portuguese` `#orthography` `#linguistics` `#script`

---

## Índice
- [Introdução e Visão Geral](#introdução-e-visão-geral)
- [1. Inventário Consonantal e Mapeamento Perso-Árabe](#1-inventário-consonantal-e-mapeamento-perso-árabe)
  - [Tabela de Mapeamento Consonantal](#tabela-de-mapeamento-consonantal)
  - [Mapeamento Ortográfico de C Brando, G Brando e J](#mapeamento-ortográfico-de-c-brando-g-brando-e-j)
  - [Distinção R vs. RR (Rā vs. He)](#distinção-r-vs-rr-rā-vs-he)
  - [Contraste S vs. SS Intervocálico (Zāy vs. Sīn)](#contraste-s-vs-ss-intervocálico-zāy-vs-sīn)
  - [Dígrafos Palatais (lh, nh)](#dígrafos-palatais-lh-nh)
- [2. Sistema Vocálico, Diacríticos e Acentuação](#2-sistema-vocálico-diacríticos-e-acentuação)
  - [Vogais em Fim de Palavra (Urdu Gol He vs. Waw)](#vogais-em-fim-de-palavra-urdu-gol-he-vs-waw)
  - [Suportes de Vogal Inicial: Opções de Alif e Escolha do Escritor](#suportes-de-vogal-inicial-opções-de-alif-e-escolha-do-escritor)
  - [Alif Tónico (ا) e Inferência de Acentuação](#alif-tónico-ا-e-inferência-de-acentuação)
  - [Contrastes de Vogais Abertas vs. Fechadas (avô vs. avó)](#contrastes-de-vogais-abertas-vs-fechadas-avô-vs-avó)
  - [Regra das Vogais Tónicas Paroxítonas (a, e, o)](#regra-das-vogais-tónicas-paroxítonas-a-e-o)
  - [Princípio da Vogal Defectiva (Minimização de Vogais Longas Internas)](#princípio-da-vogal-defectiva-minimização-de-vogais-longas-internas)
  - [Encontros Vocálicos e Mater Lectionis](#encontros-vocálicos-e-mater-lectionis)
- [3. Motor de Nasalização](#3-motor-de-nasalização)
  - [Nasais Monossilábicas e em Fim de Sílaba](#nasais-monossilábicas-e-em-fim-de-sílaba)
  - [Ditongos Nasais (-ão, -ãe, -õe)](#ditongos-nasais--ão--ãe--õe)
- [4. Regras Morfofonêmicas e Mapeamento de Domínio](#4-regras-morfofonêmicas-e-mapeamento-de-domínio)
  - [Regra I: Domínio de Número Nominal (-hā / ـها)](#regra-i-domínio-de-número-nominal--hā--ـها)
  - [Regra II: Substituição de Superfície Direta](#regra-ii-substituição-de-superfície-direta)
  - [Regra III: Domínio Sibilante Verbal e Lexical (س / ز)](#regra-iii-domínio-sibilante-verbal-e-lexical-س--ز)
  - [Grafia Alternativa Histórica e Natural: -z Lexical Final (ز)](#grafia-alternativa-histórica-e-natural--z-lexical-final-ز)
- [5. Casos Especiais e Construções Particulares](#5-casos-especiais-e-construções-particulares)
  - [Representação das Preposições de e da](#representação-das-preposições-de-e-da)
  - [Singulares Lexicais em -s / -z vs. Flexões de Plural](#singulares-lexicais-em--s---z-vs-flexões-de-plural)
  - [Hiato vs. Ditongos (país vs. pais)](#hiato-vs-ditongos-país-vs-pais)
- [6. Tabelas de Paradigmas Mestre](#6-tabelas-de-paradigmas-mestre)
  - [Determinantes, Artigos e Pronomes Demonstrativos](#determinantes-artigos-e-pronomes-demonstrativos)
  - [Glossário de Termos Lingüísticos e Gramaticais em Aljamiado](#glossário-de-termos-lingüísticos-e-gramaticais-em-aljamiado)
  - [Alternâncias Ortográficas de Plural Nominal (Regra II)](#alternâncias-ortográficas-de-plural-nominal-regra-ii)
  - [Verbos vs. Concordância e Sibilantes](#verbos-vs-concordância-e-sibilantes)
- [7. Corpus e Amostras de Transcrição](#7-corpus-e-amostras-de-transcrição)

---

## Introdução e Visão Geral
*Bismillah al-Rahman al-Rahim* (Em nome de Deus, o Clemente, o Misericordioso).

**Aljamiado Português** é uma adaptação ortográfica e fonética pessoal e altamente sistemática do alfabeto perso-árabe desenvolvida para escrever a língua portuguesa. Historicamente, *Aljamiado* (do árabe *'ajamiyya*, "língua não-árabe / estrangeira escrita em carateres árabes") referia-se às línguas românicas (moçárabe, espanhol, ladino) transcritas com letras árabes.

Esta especificação formaliza o motor ortográfico para o português. O sistema prioriza:
1. **Clareza Morfofonêmica**: Distinguir a flexão nominal de plural da concordância verbal e das sibilantes lexicais da raiz.
2. **Ritmo Visual e Equilíbrio**: Utilizar um sufixo gráfico de plural (*-hā* / `ـها`) para evitar que longas caudas repetitivas de *sīn* (`س`) poluam o fluxo horizontal do texto.
3. **Precisão Fonética e Gráfica**: Diferenciar *c* brando (`چ`) de *g/j* brando (`ژ`), *r* simples (`ر`) de *rr* duplo (`ه`), *s* intervocálico (`ز`) de *ss* duplo (`س`), estabelecer regras explícitas de Madd para vogais iniciais e aproveitar o **Alif Tónico** (`ا`) para acentuação de intensidade.

---

## 1. Inventário Consonantal e Mapeamento Perso-Árabe

### Tabela de Mapeamento Consonantal

| Grafema Latino | Som IPA | Letra Perso-Árabe | Nome da Letra | Exemplo de Palavra | Transliteração Aljamiada |
|---|---|---|---|---|---|
| **b** | [b] | **ب** | Bā | *bom* | `بم` |
| **p** | [p] | **پ** | Pā | *prática* | `پراكتیكہ` |
| **t** | [t] | **ت** | Tā | *tu* | `تو` |
| **d** | [d] | **د** | Dāl | *do* | `دو` |
| **f** | [f] | **ف** | Fā | *fazes* | `فزس` |
| **v** | [v] | **و** | Waw | *você* | `وچہ` |
| **k / c / q** (duro) | [k] | **ك** | Kāf | *coisa* | `كویزہ` |
| **g** (duro) | [g] | **گ** | Gāf | *gostei* | `گوستى` |
| **c** (brando antes de e, i) | [s] / [tʃ] | **چ** | Chā | *cenoura* | `چنورہ` |
| **g** (brando antes de e, i) | [ʒ] | **ج** | Jīm | *gente* | `جنتہ` |
| **j** | [ʒ] | **ژ** | Žā | *projeto* | `پرژتو` |
| **ch** | [ʃ] / [tʃ] | **چ** | Chā | *chave* | `چاوہ` |
| **r** (simples / brando) | [ɾ] | **ر** | Rā | *caro* | `كرو` |
| **rr / r-** (inicial / forte) | [ʁ] / [r] | **ه** | Hā Árabe / Gol He Urdu | *carro* / *rio* | `كاهو` / `هیو` |
| **s** (intervocálico /z/) | [z] | **ز** | Zāy | *coisa* | `كویزہ` |
| **ss** (intervocálico /s/) | [s] | **س** | Sīn | *processo* | `پرچسو` |
| **m** (início de sílaba) | [m] | **م** | Mīm | *minha* | `مینیہ` |
| **n** (início de sílaba) | [n] | **ن** | Nūn | *não* | `ناو` |
| **s / z** (lexical/verbal) | [s] / [z] | **س** / **ز** | Sīn / Zāy | *sim* / *paz* | `سیم` / `پز` |
| **-s** (plural nominal) | [s] / [z] / [ʃ] | **ـها** | Hā | *livros* | `لیوروها` |

### Mapeamento Ortográfico de C Brando, G Brando e J
- **C brando** (antes de *e*, *i*, representando /s/ ou /tʃ/) mapeia para **Chā** (`چ`): *cenoura* $\rightarrow$ `چنورہ`, *você* $\rightarrow$ `وچہ`, *cidade* $\rightarrow$ `چدادہ`, *fácil* $\rightarrow$ `فاچل`.
- **G brando** (antes de *e*, *i*, representando /ʒ/) mapeia para **Jīm** (`ج`): *gente* $\rightarrow$ `جنتہ`, *gênero* $\rightarrow$ `جنرو`, *Gemini* $\rightarrow$ `جمینى`.
- **J** (grafema independente *j*, representando /ʒ/ lexical da raiz) mapeia para **Žā** (`ژ`): *projeto* $\rightarrow$ `پرژتو`, *jogo* $\rightarrow$ `ژگو`, *jeito* $\rightarrow$ `ژیتو`.
- **G duro** (antes de *a*, *o*, *u*, oclusivo velar /ɡ/) mapeia para **Gāf** (`گ`): *gostei* $\rightarrow$ `گوستى`, *gramática* $\rightarrow$ `گرامتیكہ`.

### Distinção R vs. RR (Rā vs. He)
- **R simples intervocálico ou brando (tepe alveolar [ɾ])** mapeia para **Rā** (`ر`): *caro* $\rightarrow$ `كرو`, *para* $\rightarrow$ `پرہ`, *escrever* $\rightarrow$ `اسكرور` / `سكرور`.
- **RR duplo ou R inicial forte (vibrante/fricativa velar [ʁ] / [r])** mapeia para **He** (`ه` / `ـہ`): *carro* $\rightarrow$ `كاهو`, *rio* $\rightarrow$ `هیو`, *rua* $\rightarrow$ `هوه`, *raiz* $\rightarrow$ `هایز`.

### Contraste S vs. SS Intervocálico (Zāy vs. Sīn)
- **S simples intervocálico (sonoro /z/)** mapeia para **Zāy** (`ز`): *coisa* $\rightarrow$ `كویزہ` (ou `كوزہ`), *casa* $\rightarrow$ `كزہ`.
- **SS duplo intervocálico (surdo /s/)** mapeia para **Sīn** (`س`): *processo* $\rightarrow$ `پرچسو`, *passo* $\rightarrow$ `پسو`.

### Dígrafos Palatais (lh, nh)
Representados como ligaduras usando **Lām-Ye** (`لی`) e **Nūn-Ye** (`نی`):
- **lh** [ʎ] $\rightarrow$ **لی**: *filho* $\rightarrow$ `فیلیو`, *espelho* $\rightarrow$ `اسپلیو`.
- **nh** [ɲ] $\rightarrow$ **نی**: *minha* $\rightarrow$ `مینیہ`, *tenho* $\rightarrow$ `تینیو`, *linhas* $\rightarrow$ `لینیاها`.

---

## 2. Sistema Vocálico, Diacríticos e Acentuação

### Vogais em Fim de Palavra (Urdu Gol He vs. Waw)
- **-a e -e finais** mapeiam para **Gol He ao estilo Urdu** (`ه` / `ـہ` - U+06C1): *boa* $\rightarrow$ `بوہ`, *gente* $\rightarrow$ `جنتہ`.
- **-o final** mapeia para **Waw** (`و` / `ـو`): *livro* $\rightarrow$ `لیورو`, *como* $\rightarrow$ `كمو`.

### Suportes de Vogal Inicial: Opções de Alif e Escolha do Escritor
1. **Suporte de Alif (Opção Clássica)**: Vogais iniciais utilizam suporte `ا` ou `آ`.
2. **Suporte de Ye Direto (Opção Simplificada)**: Vogais iniciais *e-* e *é-* também podem ser escritas com `ی` ou `یی`.

| Som Inicial | Representação Gráfica | Detalhe Diacrítico / Estrutural | Exemplo | Transliteração |
|---|---|---|---|---|
| **é aberto inicial** [ɛ] | **ای** / **یی** | Alif-Ye (`ای`) / Ye Duplo (`یی`) | *é* | `ای` / `یی` |
| **à aberto inicial** [a] | **آ** | Alif com Madd sobrescrito | *à* | `آ` |
| **e inicial / isolado** [i]/[e] | **ی** | Ye Simples | *e* / *estudar* | `ی` / `یستدر` |
| **a inicial** [a] | **ا** | Alif Simples | *alfabeto* | `الفبتو` |
| **o inicial** [o]/[u] | **او** | Alif-Waw | *os* | `وها` |

### Alif Tónico (ا) e Inferência de Acentuação
- **Inferência Padrão antes de *-r*, *-l*, *-z* Finais**: Paroxítonas e infinitivos (*-ar*, *-er*, *-ir*) **não** recebem Alif `ا` antes da consoante final, pois o acento é inferido pela consoante: *estudar* $\rightarrow$ `استدر` / `یستدر`, *analisar* $\rightarrow$ `انلیزر`, *escrever* $\rightarrow$ `اسكرور`.
- **Marcação Proparoxítona**: O Alif Tónico é reservado para proparoxítonas: *prática* $\rightarrow$ `پراكتیكہ`, *gênero* $\rightarrow$ `جانرو`.

### Contrastes de Vogais Abertas vs. Fechadas (avô vs. avó)
- **avô** [ɐ'vu] (*-ô* fechado) $\rightarrow$ `اوو` (Alif Waw Waw)
- **avó** [ɐ'vɔ] (*-ó* aberto) $\rightarrow$ `اووا` (Alif Waw Alif)

### Princípio da Vogal Defectiva (Minimização de Vogais Longas Internas)
Para otimizar o ritmo visual semítico (*Rasm*), as vogais breves/médias (**a**, **e**, **o**) dentro de sílabas internas simples **não** requerem letras explícitas de *mater lectionis*:
- *ortografia* $\rightarrow$ `ارتگرفیہ`
- *morfologia* $\rightarrow$ `مرفلجیه`
- *fonética* $\rightarrow$ `فنيتكہ`
- *sintaxe* $\rightarrow$ `سينتسہ`
- *semântica* $\rightarrow$ `سمنتیكہ`
- *filologia* $\rightarrow$ `فللجیہ`
- *isoglossa* $\rightarrow$ `ایزگلسہ`
- *paradigma* $\rightarrow$ `پردگمہ`

### Encontros Vocálicos e Mater Lectionis

| Tipo Vocálico | Som IPA | Mapeamento Perso-Árabe | Exemplo | Escrita Aljamiada |
|---|---|---|---|---|
| **Ditongo -ai / -ai-** | [aj] | **Alif + Ye** (`ای`) | *pai* / *mais* | `پای` / `مایها` |
| **Ditongo -ei / -ei-** | [ej] | **Ye + Ye** (`یی`) | *fiquei* / *leite* | `فیكیی` / `لییتہ` |
| **Ditongo -eu / -eu-** | [ew] | **Ye + Waw** (`یو`) | *meu* / *seu* | `میو` / `سیو` |
| **Ditongo -oi / -oi-** | [oj] | **Waw + Ye** (`وی`) | *foi* / *coisa* | `فوی` / `كویزہ` |
| **Ditongo -ou / -ou-** | [ow] | **Waw + Waw** (`وو`) | *sou* / *falou* | `سوو` / `فالوو` |
| **Ditongo -ui / -ui-** | [uj] | **Waw + Ye** (`وی`) | *fui* / *muito* | `فوی` / `مویتو` |
| **Hiato (com Hamzah)** | [i] / [u] | **Hamzah sobre Ye/Waw** (`ئ`/`ؤ`) | *país* / *saúde* | `پائیس` / `ساؤدہ` |

---

## 3. Motor de Nasalização

### Nasais Monossilábicas e em Fim de Sílaba
Vogais nasais em fim de sílaba (*-m*, *-n*) neutralizam em **Mīm** (`م`): *bom* $\rightarrow$ `بم`, *bem* $\rightarrow$ `بم`, *sim* $\rightarrow$ `سیم` / `سم`.

### Ditongos Nasais (-ão, -ãe, -õe)
- **-ão** $\rightarrow$ **ناو** (*Nūn-Alif-Waw*): *não* $\rightarrow$ `ناو`, *cão* $\rightarrow$ `كناو`.
- **-ãe / -ães** $\rightarrow$ **نای** / **نایها**: *mãe* $\rightarrow$ `مای`, *pães* $\rightarrow$ `پایها`.
- **-õe / -ões** $\rightarrow$ **نژو** / **نژوها** ou **conjonções**: *convenção* $\rightarrow$ `كونونجو`, *convenções* $\rightarrow$ `كونونجوها`.

---

## 4. Regras Morfofonêmicas e Mapeamento de Domínio

### Regra I: Domínio de Número Nominal (-hā / ـها)
O sufixo **-hā** (`ـها`) é o logograma para a flexão nominal de plural:
- *livros* $\rightarrow$ `لیوروها`
- *boas* $\rightarrow$ `بوها`
- *as* $\rightarrow$ `اها`
- *os* $\rightarrow$ `وها`

### Regra II: Substituição de Superfície Direta
- *canal* $\rightarrow$ *canais* $\rightarrow$ `كنایها`
- *papel* $\rightarrow$ *papéis* $\rightarrow$ `پپیسها`
- *homem* $\rightarrow$ *homens* $\rightarrow$ `همنها`

### Regra III: Domínio Sibilante Verbal e Lexical (س / ز)
- Concordância verbal mantém **Sīn** (`س`): *tu dizes* $\rightarrow$ `دزس`, *tu fazes* $\rightarrow$ `فزس`.
- Pronomes e clíticos mantêm **Sīn** (`س`): *se* $\rightarrow$ `سہ`, *nos* $\rightarrow$ `نوس`.

### Grafia Alternativa Histórica: -z Lexical Final (ز)
Palavras lexicais não-nominais em *-s* podem usar **Zāy** (`ز`): *mas* $\rightarrow$ `مز`, *três* $\rightarrow$ `ترز`, *inglês* $\rightarrow$ `انگلز`, *português* $\rightarrow$ `پرتگز`.

---

## 5. Casos Especiais e Construções Particulares

### Representação das Preposições de e da
- **Padrão**: `دہ` (Dāl + Gol He).
- **Desambiguação**: Kasrah (`دِہ`) para *de* vs Fathah (`دَہ`) para *da*, ou substituição vocálica `دی` / `دا`.
- **Contrações**: *do* $\rightarrow$ `دو`, *dos* $\rightarrow$ `دوها`, *da* $\rightarrow$ `دا`/`دہ`, *das* $\rightarrow$ `دها`, *no* $\rightarrow$ `نو`, *nos* (prep+art) $\rightarrow$ `نوها`.

---

## 6. Tabelas de Paradigmas Mestre

### Determinantes, Artigos e Pronomes Demonstrativos

| Item | Grafia Latina | Escrita Aljamiada | Notas Morfofonêmicas |
|---|---|---|---|
| **Art. Def. Masc. Sing.** | *o* | `و` | Waw isolado |
| **Art. Def. Masc. Plur.** | *os* | `وها` | *o* (`و`) + *-hā* (`ـها`) nominal |
| **Art. Def. Fem. Sing.** | *a* | `ا` / `اہ` | Alif / He Urdu |
| **Art. Def. Fem. Plur.** | *as* | `اها` | *a* (`ا`) + *-hā* (`ـها`) nominal |
| **Art. Indef. Masc. Sing.** | *um* | `ام` / `اوم` | Mīm nasalizador final |
| **Art. Indef. Masc. Plur.** | *uns* | `انها` / `اونها` | Nasal `n` + *-hā* nominal |
| **Art. Indef. Fem. Sing.** | *uma* | `اومہ` | He Mudo final |
| **Art. Indef. Fem. Plur.** | *umas* | `اومہا` | *uma* + *-hā* nominal |
| **Dem. Masc. Sing.** | *este* | `استہ` / `ستہ` | Suporte Alif ou zero Alif |
| **Dem. Masc. Plur.** | *estes* | `استها` / `ستها` | Radical *este* + *-hā* nominal |
| **Dem. Fem. Sing.** | *esta* | `استہ` / `ستہ` | Gol He final |
| **Dem. Fem. Plur.** | *estas* | `استها` / `ستها` | Radical *esta* + *-hā* nominal |
| **Dem. Neutro** | *isto* | `ایستو` / `ستو` | Vogal alta *i* (`ی`) + Waw final |

### Glossário de Termos Lingüísticos e Gramaticais em Aljamiado

| Termo Latino/Português | Escrita Aljamiada | Análise Ortográfica e Defectividade |
|---|---|---|
| **linguística** | `لنگویستیكہ` | *Lām-Ye* (`لی`), Nūn nasal, Waw-Ye (`وی`), *i* alto mantido |
| **fonologia** | `فنلجیه` | *o* e *o* internos defectivos, Jīm (`ج`) para G brando, Gol He final |
| **fonética** | `فنيتكہ` | *fn* + Ye (`ی`) para *e* tónico não-paroxítono + *tika* (`تيكہ`) |
| **morfologia** | `مرفلجیہ` | Esqueleto *m-r-f-l* + Jīm (`ج`) para G brando, Gol He final |
| **sintaxe** | `سينتسہ` | *Sīn-Ye-Nūn* (`سين`), *t* (`ت`), *x* como Sīn (`س`), Gol He final |
| **semântica** | `سمنتیكہ` | Nūn nasalizador interno, *i* alto mantido |
| **pragmática** | `پراگمتيكہ` | Alif tónico em proparoxítona, *a* interno defectivo |
| **etimologia** | `اتملجیہ` / `یتملجیہ` | Alif ou Ye inicial, *e*, *i*, *o* internos defectivos |
| **filologia** | `فللجیہ` | Esqueleto *f-l-l* + Jīm (`ج`) para G brando |
| **dialeto** / **dialecto** | `ديلتو` / `دالتم` | Ye para ditongo/hiato *ia*, Waw final |
| **isoglossa** | `ایزگلسہ` | Zāy (`ز`) para *s* intervocálico /z/ |
| **paradigma** | `پردگمہ` | *a* e *i* internos breves defectivos |
| **grafema** | `گرفمہ` | Gāf (`گ`) duro, Gol He final |
| **fonema** / **fonemas** | `فنمہ` / `فنمها` | Logograma `-hā` (`ـها`) para plural nominal |
| **morfema** / **morfemas** | `مرفمہ` / `مرفمها` | Plural nominal com `-hā` (`ـها`) |
| **palavra** / **palavras** | `پلورہ` / `پلورها` | *a* e *a* internos defectivos, plural com `-hā` |
| **manuscrito** | `منسكرتو` / `منسكرتوها` | *e-* protético omitido em *scrito*, plural `-hā` |

---

## 7. Corpus e Amostras de Transcrição

1. **Frase 1**: *Que a paz e as bênçãos estejam com você e sua família.*
   - **Aljamiado**: `كہ ا پز ی اها بنجوها استیوا كم وچہ ی سوہ فمیلیہ.`

2. **Frase 2**: *A busca pelo conhecimento é um dever de todos.*
   - **Aljamiado**: `ا بسكہ پلو كنیچمنتو ای ام دور دہ تدوها.`

3. **Frase 3**: *A paciência e a gratidão trazem paz e sabedoria no coração.*
   - **Aljamiado**: `ا پچنچیہ ی ا گرتیداو ترزم پز ی سبدوریہ نو كرجاو.`

4. **Frase 4**: *Seja muito bem-vindo à nossa comunidade.*
   - **Aljamiado**: `سژہ مویتو بم-وندو آ نسہ كمونیددہ.`

5. **Frase 5**: *As boas ações e as palavras sinceras transformam o mundo.*
   - **Aljamiado**: `اها بوها اجوها ی اها پلورها سنچرهها ترنسفرموا و مندو.`

6. **Frase 6**: *Que Deus abençoe o seu trabalho e os seus estudos.*
   - **Aljamiado**: `كہ دایوس ابنجوى و سیو تربلیو ی وها سیوها استودوها.`

7. **Frase 7**: *A verdade e a justiça iluminam o caminho dos homens.*
   - **Aljamiado**: `ا ورددہ ی ا ژستچیہ الومنوا و كمینیو دوها همنها.`

8. **Frase 8**: *A verdadeira riqueza está na generosidade do coração.*
   - **Aljamiado**: `ا ورددیره هكزہ استا نہ ژنرزددہ دو كرجاو.`

9. **Frase 9**: *Cada novo dia é uma oportunidade para fazer o bem.*
   - **Aljamiado**: `كدہ نوو دیہ ای اومہ اپرتنیددہ پرہ فزر دو بم.`

10. **Frase 10**: *A união de corações sinceros constrói uma vida cheia de paz.*
    - **Aljamiado**: `ا انیاو دہ كرجوها سنچروها كنستروى اومہ ویدہ چیه دہ پز.`
