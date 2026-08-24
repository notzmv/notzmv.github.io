#+TITLE: Aljamiado Português: Especificação Ortográfica e Fonológica
#+AUTHOR: Umar
#+DATE: [2026-08-22 Sat]
#+FILETAGS: :aljamiado:portuguese:orthography:linguistics:script:

# Índice :toc:
- Introdução e Visão Geral
- 1. Inventário Consonantal e Mapeamento Perso-Árabe
  - Tabela de Mapeamento Consonantal
  - Mapeamento Ortográfico de C Brando, G Brando e J
  - Distinção R vs. RR (Rā vs. He)
  - Contraste S vs. SS Intervocálico (Zāy vs. Sīn)
  - Dígrafos Palatais (lh, nh)
- 2. Sistema Vocálico, Diacríticos e Acentuação
  - Vogais em Fim de Palavra (Urdu Gol He vs. Waw)
  - Suportes de Vogal Inicial: Opções de Alif e Escolha do Escritor (`آ` / `ا` vs. `ی` / `یی`)
  - Alif Tónico (ا) e Inferência de Acentuação em Consoante Final (*-r*, *-l*, *-z*)
  - Contrastes de Vogais Abertas vs. Fechadas (avô vs. avó)
  - Princípio da Vogal Defectiva (Minimização de Vogais Longas Internas para a, e, o)
  - Economia Escalar por Comprimento de Palavra e Desambiguação de Pares Mínimos
  - Encontros Vocálicos e Mater Lectionis
- 3. Motor de Nasalização
  - Nasais Monossilábicas e em Fim de Sílaba
  - Ditongos Nasais (-ão, -ãe, -õe)
- 4. Regras Morfofonêmicas e Mapeamento de Domínio
  - Regra I: Domínio de Número Nominal (-hā / ـها)
  - Regra II: Substituição de Superfície Direta
  - Regra III: Domínio Sibilante Verbal e Lexical (س / ز)
- 5. Casos Especiais e Construções Particulares
  - Representação das Preposições *de* e *da*
  - Singulares Lexicais em -s / -z vs. Flexões de Plural
  - Hiato vs. Ditongos (país vs. pais)
  - Anexação de Clíticos e Hifenização
  - Grupos Consonânticos
  - Economia Ortográfica e Variantes Etimológicas (Omissão de Alif e Redução Vocálica)
- 6. Tabelas de Paradigmas Mestre
  - Determinantes e Artigos
- 7. Corpus e Amostras de Transcrição

# Introdução e Visão Geral

#+BEGIN_EXPORT html
<div class="basmala-hero" style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border: 1px solid var(--primary-accent); border-radius: 16px; padding: 2rem 1.5rem; text-align: center; margin: 1.5rem 0 2rem 0; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
  <div class="ar-basmala-naskh ar" style="font-size: 2.6rem; color: var(--primary-accent); font-family: 'Noto Naskh Arabic', 'Amiri', serif !important; margin-bottom: 0.8rem; line-height: 1.5;">بِسْمِ ٱللَّهِ ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ</div>
  <div class="aljamiado-basmala-nastaliq ar" style="font-size: 1.7rem; color: #34d399; font-family: 'Noto Nastaliq Urdu', 'Gulzar', serif !important; margin-bottom: 0.5rem; line-height: 2.2;">ام نمہ دہ دیوس، و كلمنتہ، و مزركردیوزو. <span style="font-size: 0.85rem; color: #8b949e; font-family: 'Inter', sans-serif; vertical-align: middle;">(Nastaliq)</span></div>
  <div class="aljamiado-basmala-naskh ar" style="font-size: 1.5rem; color: #6ee7b7; font-family: 'Noto Naskh Arabic', 'Amiri', serif !important; margin-bottom: 0.6rem; line-height: 1.6;">ام نمہ دہ دیوس، و كلمنتہ، و مزركردیوزو. <span style="font-size: 0.85rem; color: #8b949e; font-family: 'Inter', sans-serif; vertical-align: middle;">(Naskh)</span></div>
  <div class="pt-basmala" style="font-size: 1.1rem; color: var(--text-muted); font-style: italic;">Em nome de Deus, o Clemente, o Misericordioso.</div>
</div>

<div class="script-explanation-box" style="background: var(--card-bg); border: 1px solid #3b82f6; border-left: 6px solid #3b82f6; border-radius: 12px; padding: 1.5rem; margin: 1.5rem 0 2rem 0;">
  <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; margin-bottom: 1rem;">
    <h3 style="margin: 0; color: #60a5fa; font-size: 1.2rem;">📖 Estilos Caligráficos: Nastaliq vs. Naskh</h3>
    <button id="font-toggle-btn-inline" class="btn-big-toggle" onclick="toggleScriptFont()" style="margin: 0;">
      ✨ Estilo Atual: <strong>Nastaliq (Persa/Urdu)</strong> &mdash; Clique para Naskh (Árabe)
    </button>
  </div>
  <p style="margin-bottom: 0.75rem; color: #f0f6fc; font-size: 0.95rem; line-height: 1.6;">
    O <strong>Aljamiado Português</strong> utiliza por padrão o estilo caligráfico <strong>Nastaliq</strong> (Persa/Urdu), caracterizado por seu fluxo elegante e inclinado, tradicionalmente empregado na escrita de línguas não-árabes.
  </p>
  <p style="margin-bottom: 0; color: #f0f6fc; font-size: 0.95rem; line-height: 1.6;">
    Como a maioria dos leitores e muçulmanos está habituada ao estilo <strong>Naskh</strong> (o estilo linear padronizado da caligrafia árabe e das edições do Alcorão), disponibilizamos o botão acima e o controle flutuante no canto da tela para alternar instantaneamente entre <strong>Nastaliq</strong> e <strong>Naskh</strong> em toda a documentação.
  </p>
</div>
#+END_EXPORT

**Aljamiado Português** é uma adaptação ortográfica e fonética pessoal e altamente sistemática do alfabeto perso-árabe desenvolvida para escrever a língua portuguesa. Historicamente, *Aljamiado* (do árabe *'ajamiyya*, "língua não-árabe / estrangeira escrita em carateres árabes") referia-se às línguas românicas (moçárabe, espanhol, ladino) transcritas com letras árabes.

Esta especificação formaliza o motor ortográfico para o português. O sistema prioriza:
1. **Clareza Morfofonêmica**: Distinguir a flexão nominal de plural da concordância verbal e das sibilantes lexicais da raiz.
2. **Ritmo Visual e Equilíbrio**: Utilizar um sufixo gráfico de plural (*-hā* / `ـها`) para evitar que longas caudas repetitivas de *sīn* (`س`) poluam o fluxo horizontal do texto.
3. **Precisão Fonética e Gráfica**: Diferenciar *c* brando (`چ`) de *g/j* brando (`ژ`), *r* simples (`ر`) de *rr* duplo (`ه`), *s* intervocálico (`ز`) de *ss* duplo (`س`), estabelecer regras explícitas de Madd para vogais iniciais e aproveitar o **Alif Tónico** (`ا`) para acentuação de intensidade.
4. **Recomendação de Teclado (GBoard Urdu)**: O melhor teclado para digitação é o **GBoard configurado para o idioma Urdu**, que possui o comportamento ortográfico desejado (exceto para a sequência de *He* final seguido do sufixo *-hā*, em que se pode pressionar e segurar o botão do *He* para digitar o segundo *He* correto).


# 1. Inventário Consonantal e Mapeamento Perso-Árabe

## Tabela de Mapeamento Consonantal

| Grafema Latino | Som IPA | Letra Perso-Árabe | Nome da Letra | Exemplo de Palavra | Transliteração Aljamiada |
|----------------+---------+-------------------+---------------+--------------------+--------------------------|
| **b** | [b] | **ب** | Bā | *bom* | `بم` |
| **p** | [p] | **پ** | Pā | *prática* | `پراكتیكہ` |
| **t** | [t] | **ت** | Tā | *tu* | `تو` |
| **d** | [d] | **د** | Dāl | *do* | `دو` |
| **f** | [f] | **ف** | Fā | *fazes* | `فزس` |
| **v** | [v] | **و** | Waw | *você* | `وچہ` |
| **k / c / q** (duro) | [k] | **ك** | Kāf | *coisa* | `كویزہ` |
| **g** (duro) | [g] | **گ** | Gāf | *gostei* | `گوستى` |
| **r** (simples / brando) | [ɾ] | **ر** | Rā | *caro* | `كرو` |
| **rr** (intervocálico forte) | [ʁ] / [h] | **ه** | He | *carro* / *terra* | `كاهو` / `تہہ` |
| **r-** (inicial forte) | [ʁ] / [r] | **ر** (frequente) / **ه** | Rā / He | *rio* / *rua* | `ریو` / `روه` (ou `هیو` / `هوه`) |
| **s** (intervocálico /z/) | [z] | **ز** | Zāy | *coisa* | `كویزہ` |
| **ss** (intervocálico /s/) | [s] | **س** | Sīn | *processo* | `پرچسو` |
| **m** (início de sílaba) | [m] | **م** | Mīm | *minha* | `مینیہ` |
| **n** (início de sílaba) | [n] | **ن** | Nūn | *não* | `ناو` |
| **s / z** (verbal/lexical) | [s] / [z] | **س** / **ز** | Sīn / Zāy | *sim* / *paz* | `سیم` / `پز` |
| **-s** (plural nominal) | [s] / [z] / [ʃ] | **ـها** | Hā | *livros* | `لیوروها` |

## Mapeamento Ortográfico de C Brando, G Brando e J
Para manter a fidelidade ortográfica e fonológica com as raízes latinas e a tradição Perso-Árabe:
- **C brando** (antes de *e*, *i*, representando /s/ ou /tʃ/) mapeia para **Chā** (`چ`):
  - *cenoura* $\rightarrow$ `چنورہ`
  - *você* $\rightarrow$ `وچہ`
  - *cidade* / *cidades* $\rightarrow$ `چدادہ` / `چدادها`
  - *ciência* $\rightarrow$ `چینچیہ`
  - *fácil* $\rightarrow$ `فاچل`
- **G brando** (antes de *e*, *i*, representando a fricativa palatal sonora /ʒ/) mapeia para **Jīm** (`ج`):
  - *gente* $\rightarrow$ `جنتہ`
  - *gênero* $\rightarrow$ `جنرو`
  - *gerúndio* $\rightarrow$ `جرندیو`
  - *giringonça* $\rightarrow$ `جرنگونسہ`
  - *Gemini* $\rightarrow$ `جمینى`
- **J** (grafema independente *j*, representando /ʒ/ lexical da raiz) mapeia para **Žā** (`ژ`):
  - *projeto* $\rightarrow$ `پرژتو`
  - *jogo* $\rightarrow$ `ژگو`
  - *jeito* $\rightarrow$ `ژیتو`
  - *sujeito* $\rightarrow$ `سژیتو`
- **G duro** (antes de *a*, *o*, *u*, o oclusivo velar /ɡ/) mapeia para **Gāf** (`گ`):
  - *gostei* $\rightarrow$ `گوستى`
  - *gramática* $\rightarrow$ `گرامتیكہ`
  - *isoglossa* $\rightarrow$ `ایزگلسہ`

## Distinção R vs. RR (Rā vs. He)
As vibrantes e tepes são divididas com base na posição silábica e no contraste fonológico:
- **R simples intervocálico ou brando (tepe alveolar [ɾ])**: Mapeia estritamente para **Rā** (`ر`):
  - *caro* $\rightarrow$ `كرو`
  - *para* $\rightarrow$ `پرہ`
  - *gramática* $\rightarrow$ `گرامتیكہ`
  - *morfema* $\rightarrow$ `مرفمہ`
  - *escrever* $\rightarrow$ `اسكرور` / `سكرور`
- **RR duplo intervocálico ([ʁ] / [h])**: Mapeia **prioritariamente para He** (`ه` / `ـہ` - Gol He Urdu) para estabelecer uma oposição gráfica imediata com o R simples intervocálico (*caro* `كرو` vs. *carro* `كاهو`). A escrita de RR com **Rā** (`ر`) é secundária, reservada especificamente para dialetos com vibrante alveolar (*trill* [r]):
  - *carro* $\rightarrow$ **`كاهو`** (variante dialetal com Rā: `كارو`)
  - *terra* $\rightarrow$ **`تہہ`** (um *He* `ه` para *rr* + um *He* final `ہ` para *-a*; variante dialetal com Rā: `تره`)
- **R inicial (word-initial R-)**: Ao contrário do RR intervocálico, o R inicial é grafado **com mais frequência e naturalidade por Rā (`ر`)** (ex.: *rio* `ریو`, *rua* `روه`, *raiz* `رایز`), enquanto o **He (`ه`)** é uma variante gráfica válida para quem deseja destacar a articulação glotal/velar ou evitar ambiguidade:
  - *rio* $\rightarrow$ **`ریو`** (padrão com Rā; variante com He: `هیو`)
  - *rua* $\rightarrow$ **`روه`** (padrão com Rā; variante com He: `هوه`)
  - *raiz* $\rightarrow$ **`رایز`** (padrão com Rā; variante com He: `هایز`)
  - *regra* $\rightarrow$ **`رگرہ`** (padrão com Rā; variante com He: `هگرہ`)
  - *riqueza* $\rightarrow$ **`ریكزہ`** (padrão com Rā; variante com He: `هیكزہ`)
  - *renovam* $\rightarrow$ **`رنووم`** (padrão com Rā; variante com He: `هنووم`)

## Contraste S vs. SS Intervocálico (Zāy vs. Sīn)
Nas posições intervocálicas onde o português opõe a fricativa alveolar sonora /z/ e a surda /s/:
- **S simples intervocálico (sonoro /z/)** mapeia para **Zāy** (`ز`):
  - *coisa* $\rightarrow$ `كویزہ` (ou `كوزہ`)
  - *casa* $\rightarrow$ `كزہ`
  - *análise* $\rightarrow$ `انلیزہ`
  - *isoglossa* $\rightarrow$ `ایزگلسہ`
- **SS duplo intervocálico (surdo /s/)** mapeia para **Sīn** (`س`):
  - *processo* $\rightarrow$ `پرچسو`
  - *passo* $\rightarrow$ `پسو`
  - *professora* $\rightarrow$ `پرفسرہ`
  - *morfossintaxe* $\rightarrow$ `مرفسينتسہ`

## Dígrafos Palatais (lh, nh)
As consoantes palatais são representadas como ligaduras de consoante-semivogal usando *Lām-Ye* (`لی`) e *Nūn-Ye* (`نی`):
- **lh** [ʎ] $\rightarrow$ **لی**: *filho* $\rightarrow$ `فیلیو`, *espelho* $\rightarrow$ `اسپلیو` / `سپلیو`, *folha* $\rightarrow$ `فولیہ`, *detalhe* $\rightarrow$ `دتلیہ`
- **nh** [ɲ] $\rightarrow$ **نی**: *minha* $\rightarrow$ `مینیہ`, *tenho* $\rightarrow$ `تینیو`, *linhas* $\rightarrow$ `لینیاها`, *desenho* $\rightarrow$ `دزنیو`

# 2. Sistema Vocálico, Diacríticos e Acentuação

## Vogais em Fim de Palavra (Urdu Gol He vs. Waw)
- **-a e -e finais** mapeiam ambas explicitamente para o **Gol He ao estilo Urdu** (`ه` / `ـہ` - U+06C1) para forçar uma renderização estilística adequada em todas as fontes:
  - *boa* $\rightarrow$ `بوہ`
  - *gente* $\rightarrow$ `جنتہ`
  - *prática* $\rightarrow$ `پراكتیكہ`
- **-o final** mapeia para **Waw** (`و` / `ـو`):
  - *livro* $\rightarrow$ `لیورو`
  - *como* $\rightarrow$ `كمو`

## Suportes de Vogal Inicial: Opções de Alif e Escolha do Escritor (`آ` / `ا` vs. `ی` / `یی`)
Quando uma palavra começa por vogal, a flexibilidade ortográfica é preservada, deixando a escolha da representação inicial ao escritor:
1. **Suporte de Alif (Opção Clássica/Tradicional)**: Vogais iniciais (*e-*, *é-*, *i-*, *a-*, *o-*) utilizam um **suporte de Alif simples ou com Madd** (`ا` / `آ`), sem Hamzah.
2. **Suporte de Ye Direto (Opção Simplificada)**: Vogais iniciais *e-* e *é-* também podem ser escritas diretamente com **Ye** (`ی`) ou **Ye Duplo** (`یی`).

Ambas as convenções são variantes ortográficas plenamente válidas no Aljamiado Português:

| Som Inicial | Representação Gráfica | Detalhe Diacrítico / Estrutural | Exemplo de Palavra | Transliteração Aljamiada |
|-------------+------------------------+---------------------------------+--------------------+--------------------------|
| **é aberto inicial** [ɛ] | **ای** / **یی** | Alif-Ye (`ای`, variante Alif) / Ye Duplo (`یی`, variante Ye) | *é* | `ای` / `یی` |
| **à aberto inicial** [a] | **آ** | Alif com Madd sobrescrito | *à* | `آ` |
| **e inicial / isolado** [i]/[e] | **ی** | Ye Simples | *e* / *estudar* / *estudo* | `ی` / `یستدر` / `یستدو` |
| **a inicial** [a] | **ا** | Alif Simples | *alfabeto* | `الفبتو` |
| **o inicial** [o]/[u] | **او** | Alif-Waw | *os* | `وها` |

- **Representação de *é* e *e***:
  - ***é* aberto** [ɛ] (ex.: verbo *ser*: *é*) mapeia principalmente para **Ye Duplo** (`یی`).
  - ***e* átono** [e]/[i] (ex.: conjunção *e*, *e-* inicial em *estudar*, *estudo*, *escrever*) mapeia para **Ye Simples** (`ی`):
    - *estudar* [iʃtuˈdaɾ] $\rightarrow$ **یستدر** / **استدر** / **ستدر** (com opção de dropar o suporte inicial inteiramente `ستدر`)
    - *estudo* [iʃˈtudu] $\rightarrow$ **یستدو** / **ستدو**
    - *escrever* [iʃkɾɨˈveɾ] $\rightarrow$ **یسكرور** / **اسكرور** / **سكرور** (escrever $\rightarrow$ *screver* `سكرور`)
  - **Omissão do Suporte Vocálico Inicial**: Em palavras com base latina iniciadas por *e-* protético (*escrever*, *estudar*, *estar*), existe a liberdade ortográfica de omitir completamente o Alif/Ye inicial, escrevendo diretamente o esqueleto consonantal (`سكرور`, `ستدر`, `ستر`).
  - **Regra de Ausência de Hamzah no Alif**: O Alif nunca carrega Hamzah (`إ` ou `أ`). Neste sistema, o Hamzah é reservado exclusivamente para assinalar hiato/ditongo sobre Ye (`ئ`) e Waw (`ؤ`). As vogais iniciais escritas com Alif usam Alif simples (`ا`) ou Alif com Madd (`آ`), podendo também ser representadas por Ye direto (`ی`) e Ye Duplo (`یی`).

## Alif Tónico (ا) e Inferência de Acentuação em Consoante Final (*-r*, *-l*, *-z*)
O **Alif Tónico** (`ا`) funciona como um **marcador especializado de proparoxítonas / acentuação irregular**:
- **Inferência Padrão de Acentuação e Ausência de Alif antes de *-r*, *-l*, *-z* Finais**:
  Paroxítonas padrão (acentuação na penúltima sílaba em palavras terminadas em vogal como *casa*, *livro*) e oxítonas padrão terminadas em consoante (*-r*, *-l*, *-z*) **nunca** levam Alif `ا` antes da consoante final. Nos verbos no infinitivo (*-ar*, *-er*, *-ir*) e palavras terminadas em *-r*, *-l*, *-z*, a acentuação na última sílaba é automaticamente inferida através da própria consoante:
  - *estudar* [iʃtuˈdaɾ] $\rightarrow$ **استدر** / **یستدر** (Sílaba *-dar* escrita `در`, sem Alif `ا` antes de `ر`, pois o acento tónico é completamente compreendido pelo `ر` final)
  - *analisar* [ɐnɐliˈzaɾ] $\rightarrow$ **انلیزر** (Sílaba *-zar* escrita `زر`, sem Alif `ا` antes de `ر`)
  - *conversar* [kõvɨɾˈsaɾ] $\rightarrow$ **كنورسر** (Sílaba *-sar* escrita `سر`, sem Alif `ا` antes de `ر`)
  - *escrever* [iʃkɾɨˈveɾ] $\rightarrow$ **اسكرور** / **یسكرور** (Sílaba *-ver* escrita `ور`, acentuação inferida pelo `ر` final)
  - *criar* [kɾiˈaɾ] $\rightarrow$ **كریر** (Escrito `ریر`, acentuação inferida pelo `ر` final)
- **Marcação Proparoxítona**: O Alif Tónico é estritamente reservado para **proparoxítonas** (*palavras esdrúxulas*) ou acentuação irregular que rompa com os padrões:
  - *prática* [ˈpɾatika] $\rightarrow$ `پراكتیكہ` (Alif Tónico inserido após *p-r-* para marcar a acentuação na primeira sílaba)
  - *gênero* [ˈʒenɨɾu] $\rightarrow$ `جانرو` / `جنِرو`

## Contrastes de Vogais Abertas vs. Fechadas (avô vs. avó)
Os contrastes de timbre nas vogais médias utilizam combinações de Alif e Waw:
- **avô** [ɐ'vu] (masculino avô, *-ô* fechado) $\rightarrow$ **اوو** (Alif Waw Waw) ou `اووہ`
- **avó** [ɐ'vɔ] (feminino avó, *-ó* aberto) $\rightarrow$ **اووا** (Alif Waw Alif) ou `اوواہ`

## Regra das Vogais Tónicas Paroxítonas (a, e, o)
Nas palavras **paroxítonas** (acentuação regular na penúltima sílaba), as vogais tónicas breves/médias (**a**, **e**, **o**) são por padrão **defectivas** (não recebem Alif `ا`, Ye `ی` ou Waw `و`), a menos que a sua escrita seja estritamente necessária (como para representar ditongos ou evitar ambiguidade):
- **casa** $\rightarrow$ `كزہ` (Kāf-Zāy-He: `ك-ز-ہ`, sem Alif `ا` tónico)
- **passo** $\rightarrow$ `پسو` (Pā-Sīn-Waw: sem Alif `ا` tónico)
- **processo** $\rightarrow$ `پرچسو` (sem Waw `و` pré-tónico nem Ye `ی` tónico)
- **professora** $\rightarrow$ `پرفسرہ` (sem Waw `و` tónico em *-so-*)

Em contraste, as **não-paroxítonas** (proparoxítonas e oxítonas) exigem letras de *mater lectionis* tónicas quando necessário (ex.: *gramática* `گرامتیكہ` com Alif tónico `ا`, *fonética* `فنيتكہ` com Ye tónico `ی`).

## Princípio da Vogal Defectiva (Minimização de Vogais Longas Internas para a, e, o)
Para preservar a compacidade visual e alinhar-se com a eficiência ortográfica semítica clássica (*Rasm*), as vogais médias/baixas breves (**a**, **e**, **o**) dentro de sílabas internas simples e não-ditongais **não** requerem letras explícitas de *mater lectionis* (Alif `ا`, Ye `ی`, Waw `و`).

1. **Regra Defectiva Interna**:
   - O *a*, *e*, *o* internos em sílabas simples CV/CVC são implícitos diretamente pelo esqueleto consonantal (ou indicados opcionalmente por diacríticos vocálicos: *fathah* `/ َ`, *kasrah* `/ ِ`, *dammah* `/ ُ`).
   - **Princípio de Minimização Estrita**: As vogais *a*, *e* e *o* são **apenas escritas se for estritamente necessário** e DEVEM ser evitadas a menos que a sua omissão causasse ambiguidade real.
   - Exemplos:
     - *ortografia* [ɔɾtuɡɾɐˈfiɐ] $\rightarrow$ **ارتگرفیہ** (*o-r-t-o-g-r-a-f-i-a*: apenas o suporte de Alif `ا` inicial, sem Waw `و`, *o* e *a* internos omitidos, vogal alta *i* (`ی`) e *-a* final (`ہ`) mantidos)
     - *gramática* [ɡɾɐˈmatikɐ] $\rightarrow$ **گرامتیكہ** (*grm* + Alif tónico `ا` + *tika* `تيكہ`)
     - *morfologia* [mɔɾfuluˈʒiɐ] $\rightarrow$ **مرفلجیہ** (*m-r-f-l* + Jīm `ج` para G brando + Ye `ی` + He `ہ`)
     - *fonética* [fuˈnɛtikɐ] $\rightarrow$ **فنيتكہ** (*fn* + Ye `ی` para *e* tónico não-paroxítono + *tika* `تيكہ`)
     - *sintaxe* [sĩˈtaksɨ] $\rightarrow$ **سينتسہ** (*sin* `سين` + *ta* `ت` + *sin* `س` + He `ہ`)
     - *semântica* [sɨˈmɐ̃tikɐ] $\rightarrow$ **سمنتیكہ** (*s-m-n-t-i-c-a*: Nūn nasalizador, *i* e *-a* final mantidos)
     - *filologia* [filuluˈʒiɐ] $\rightarrow$ **فللجیہ** (*fllg* com Jīm `ج` para G brando + Ye `ی` + He `ہ`)
     - *isoglossa* [izuˈɡlɔsɐ] $\rightarrow$ **ایزگلسہ** (*i-z-g-l-ss-a*: Ye inicial, *o* interno defectivo)
     - *paradigma* [pɐɾɐˈdiɡmɐ] $\rightarrow$ **پردگمہ** (*p-r-d-g-m-a*: *a* e *i* pré-consonântico defectivos)
     - *estudar* [iʃtuˈdaɾ] $\rightarrow$ **استدر** / **یستدر** / **ستدر** (*-dar* tónico escrito `در`, sem Alif `ا` antes de `ر`)
     - *analisar* [ɐnɐliˈzaɾ] $\rightarrow$ **انلیزر** (*-zar* tónico escrito `زر`, sem Alif `ا` antes de `ر`)
     - *caro* [ˈka.ɾu] $\rightarrow$ **كرو** (*k-r-o*, *a* interno omitido)
     - *processo* [pɾu'sɛ.su] $\rightarrow$ **پرچسو** (*p-r-c-ss-o*, *o* e *e* internos omitidos; *-o* final mantido)
     - *fazes* [ˈfa.zɨʃ] $\rightarrow$ **فزس** (*f-z-s*, *a* e *e* internos omitidos)
     - *gente* [ˈʒẽ.tɨ] $\rightarrow$ **جنتہ** (*g-* brando = Jīm `ج`, *e* interno omitido, *-e* final = gol he urdu `ہ`)

2. **Condições Estruturais Concretas para Mater Lectionis Obrigatório**:
   As letras de vogal longa (**Alif**, **Waw**, **Ye**) são **estritamente necessárias** para *a*, *e*, *o* APENAS nas seguintes condições concretas:
   - **Encontros Vocálicos (Ditongos, Tritongos e Hiatos)**: Requeridos para representar os encontros vocálicos sem ambiguidade (ex.: *dia* `دیہ`, *eu* `یو`, *boa* `بوہ`, *fiquei* `فیكیی`, *coisa* `كویزہ`, *leite* `لییتہ`, *muito* `مویتو`, *meu* `میو`).
   - **Vogais em Fim de Palavra**: *-o* final é explicitamente escrito com Waw (`و`), *-a* e *-e* finais com Gol He de estilo Urdu (`ہ` / `ـہ` - U+06C1).
   - **Suportes de Vogal Inicial**: Vogais iniciais usam suportes de Alif (`آ`, `او`) ou Ye (`ی`).
   - **Alif Tónico (Marcação de Acentuação)**: Reservado para proparoxítonas (*esdrúxulas*) ou acentuação irregular (*prática* `پراكتیكہ`).
   - **Vogais Altas (i e u)**: As vogais altas internas distintas *i* [i] e *u* [u] mantêm Ye (`ی`) e Waw (`و`) para preservar a identidade fonológica (ex.: *livro* `لیورو`, *minha* `مینیہ`).

## Economia Escalar por Comprimento de Palavra e Desambiguação de Pares Mínimos
A omissão e redução vocálica no Aljamiado Português seguem uma **escala inversa em relação ao comprimento da palavra**: quanto mais longa for a palavra, maior é a sua redundância fonológica e contextual, permitindo que a maioria das suas vogais pré-tónicas seja reduzida ou omitida sem qualquer perda de legibilidade. Em contrapartida, palavras curtas (monossilábicas ou dissilábicas) possuem baixa redundância e alta carga funcional, exigindo *mater lectionis* explícitas para desambiguar pares mínimos.

1. **Palavras Longas (Alta Redundância e Redução Pré-Tónica)**:
   Em polissílabos extensos, a estrutura consonantal e a posição da sílaba tónica identificam a palavra de forma unívoca. Portanto, vogais pré-tónicas internas podem ter as suas *mater lectionis* reduzidas:
   - *misericordioso* [mi.ze.ɾi.kɔɾ.ðjo.zu] $\rightarrow$ **`مزریكردیوزو`** / **`مزركردیوزو`** (as duas primeiras vogais pré-tónicas *i* e *e* são reduzidas defectivamente no esqueleto consonantal `م-ز-ر-ی-ك-ر-د-ی-و-ز-و`, preservando apenas a vogal tónica/alta essencial e o *-o* final).

2. **Palavras Curtas e Pares Mínimos (*bm* vs. *bum* / *bim*)**:
   Em monossílabos nasais ou curtos, o esqueleto consonantal defectivo básico (ex.: `بم` para *bm*) é intrinsecamente ambíguo entre *bem* e *bom*. Para garantir a precisão ortográfica quando o contexto exige desambiguação explícita, recorre-se a letras de *mater lectionis* tónicas:
   - **`بم`** (*bm*): Forma defectiva neutra/padrão para a sílaba nasal labial.
   - **`بوم`** (*bum*): Forma explicitamente desambiguada para **bom** (utilizando **Waw** `و` para marcar o timbre posterior /o/~/u/).
   - **`بیم`** (*bim*): Forma explicitamente desambiguada para **bem** (utilizando **Ye** `ی` para marcar o timbre anterior /e/~/i/).

3. **O Triad Morfológico de `convenco`, `convencao` e `convencos`**:
   A distinção entre formas verbais e nominais derivadas da mesma raiz (*convencer / convenção*) demonstra a eficiência deste sistema morfofonêmico e do sufixo de plural `-hā` (`ـها`):
   - **`convenco`** (*convenço*, "eu convenço" — 1ª pessoa do singular do presente do indicativo): Grafado como **`كنونچو`** / **`كونونچو`** (radical `كنونچ` + desinência verbal de 1ª pessoa em *-o* `ـچو`).
   - **`convencao`** (*convenção*, substantivo feminino singular): Grafado como **`كنونچاو`** / **`كونونچاو`** (radical `كنونچ` + ditongo nasal `-ção` `ـچاو` escrito com Alif-Waw `او`, sem Nūn redundante).
   - **`convencos`** (*convenções*, substantivo feminino plural): Grafado como **`كنونچوها`** / **`كونونچوها`** (radical com vocalização temático-nominal + sufixo gráfico de plural `-hā` `ـها`).
   - *Explicação Ortográfica Crucial*: A forma plural **`كنونچوها`** (*convenções*) **não necessita de uma letra vocálica extra no radical** para se diferenciar de *convenço* (`كنونچو`) ou *convenção* (`كنونچاو`), visto que o próprio logograma de plural nominal `-hā` (`ـها`) fornece uma desambiguação morfológica total e imediata.

## Encontros Vocálicos e Mater Lectionis
Para eliminar qualquer ambiguidade gráfica e representar os agrupamentos vocálicos (ditongos orais, tritongos e hiatos) com precisão matemática, o **Aljamiado Português** emprega um mapeamento explícito de *mater lectionis* (*ḥaraka / ḥarf 'illa*) para cada fone vocálico da sequência:

1. **Mapeamento de Vogal para Letra**:
   - **[a] / [ɐ]** $\rightarrow$ **Alif** (`ا` / `ـا`)
   - **[i] / [e] / [j]** $\rightarrow$ **Ye** (`ی` / `ـی` ou *Chhoti Yeh* Urdu `ی` / `ـی`)
   - **[u] / [o] / [w]** $\rightarrow$ **Waw** (`و` / `ـو`)
   - **Vogais Mudar em Fim de Palavra (-a / -e)** $\rightarrow$ **He Mudo de estilo Urdu** (*gol he / chhoti he*: `ه` / `ـہ`), servindo como uma libertação vocálica suave sem fricção consonantal.

2. **Tabela do Paradigma de Ditongos e Tritongos**:

| Tipo Vocálico | Agrupamento Latino | Som IPA | Mapeamento Perso-Árabe | Exemplo de Palavra | Escrita Aljamiada | Decomposição Estrutural |
|---------------+--------------------+---------+------------------------+--------------------+-------------------+-------------------------|
| **Ditongo Decrescente** | *-ai* / *-ai-* | [aj] | **Alif + Ye** (`ای`) | *pai* / *mais* | `پای` / `مایها` | Pā + Alif + Ye |
| **Ditongo Decrescente** | *-ei* / *-ei-* | [ej] / [ɛj] | **Ye + Ye** (`یی`) | *fiquei* / *leite* | `فیكیی` / `لییتہ` | Fā + Ye + Kāf + Ye + Ye |
| **Ditongo Decrescente** | *-eu* / *-eu-* | [ew] / [ɛw] | **Ye + Waw** (`یو`) | *eu* / *meu* / *seu* | `یو` / `میو` / `سیو` | Ye + Waw / Mīm + Ye + Waw |
| **Ditongo Decrescente** | *-iu* / *-iu-* | [iw] | **Ye + Waw** (`یو`) | *viu* / *partiu* | `ویو` / `پارتیو` | Waw + Ye + Waw |
| **Ditongo Decrescente** | *-oi* / *-oi-* | [oj] / [ɔj] | **Waw + Ye** (`وی`) ou **Waw** (`و`) | *foi* / *coisa* | `فوی` / `كویزہ` (ou `كوزہ`) | Fā + Waw + Ye / Kāf + Waw + Zāy + He |
| **Ditongo Decrescente** | *-ou* / *-ou-* | [ow] / [o] | **Waw + Waw** (`وو`) | *sou* / *falou* | `سوو` / `فالوو` | Sīn + Waw + Waw |
| **Ditongo Decrescente** | *-ui* / *-ui-* | [uj] | **Waw + Ye** (`وی`) | *fui* / *muito* | `فوی` / `مویتو` | Mīm + Waw + Ye + Tā + Waw |
| **Ditongo Decrescente** | *-au* / *-au-* | [aw] | **Alif + Waw** (`او`) | *pau* / *mau* | `پاو` / `ماو` | Pā + Alif + Waw |
| **Ditongo Crescente / Hiato** | *-ia* | [i.ɐ] / [jɐ] | **Ye + He Mudo** (`یہ` / `ـیہ`) | *dia* | `دیہ` / `دِیہ` | Dāl + Ye + Gol He Urdu |
| **Ditongo Crescente / Hiato** | *-ie* | [i.e] / [je] | **Ye + Ye + He Mudo** (`ییہ`) | *série* | `سیریہ` / `سیرییہ` | Sīn + Ye + Rā + Ye + He Mudo |
| **Ditongo Crescente / Hiato** | *-io* | [i.u] / [ju] | **Ye + Waw** (`یو`) | *rio* / *frio* | `هیو` / `فریو` | He + Ye + Waw |
| **Ditongo Crescente / Hiato** | *-ua* | [u.ɐ] / [wɐ] | **Waw + He Mudo** (`وه` / `ـوه`) | *rua* / *sua* | `هوه` / `سوه` | He + Waw + Gol He Urdu |
| **Ditongo Crescente / Hiato** | *-ue* | [u.e] / [we] | **Waw + Ye + He Mudo** (`ویہ`) | *estátua* / *statue* | `استاتوه` / `یستاتویہ` | Alif + Sīn + Tā + Alif + Tā + Waw + He Mudo |
| **Tritongo** | *-uai* | [waj] | **Waw + Alif + Ye** (`وای`) | *Paraguai* | `پرہگوای` | Pā + Rā + Gāf + Waw + Alif + Ye |
| **Tritongo** | *-uei* | [wej] | **Waw + Ye + Ye** (`ویی`) | *enxaguei* | `ینشاگویی` | Alif + Nūn + Shīn + Alif + Gāf + Waw + Ye + Ye |

3. **Acentuação de Hiatos e Assento de Hamzah**:
   Quando uma vogal alta tónica (*i* ou *u*) está em hiato explícito com uma vogal precedente (ex.: *país*, *saúde*, *baú*), uma **Hamzah** (`ئ` sobre Ye, `ؤ` sobre Waw) é colocada acima da letra vocálica para assinalar a separação silábica e o pico tónico:
   - **país** [pɐ'iʃ] (país, hiato) $\rightarrow$ **پائیس** (Pā + Alif + Hamzah_sobre_Ye + Sīn) $\neq$ **pais** [pajʃ] (pais, ditongo) $\rightarrow$ **پایها**
   - **saúde** [sɐ'u.dɨ] (saúde, hiato) $\rightarrow$ **ساؤدہ** (Sīn + Alif + Hamzah_sobre_Waw + Dāl + He Mudo)
   - **baú** [bɐ'u] (baú, hiato) $\rightarrow$ **باؤ** (Bā + Alif + Hamzah_sobre_Waw)

# 3. Motor de Nasalização

## Nasais Monossilábicas, Desinências Verbais (-am, -em) e Fim de Sílaba
Vogais nasais em fim de sílaba (*-m*, *-n*) neutralizam em **Mīm** (`م`):
- *bom* $\rightarrow$ `بم`
- *bem* $\rightarrow$ `بم`
- *sim* $\rightarrow$ `سیم` / `سم`

As desinências verbais átonas de 3ª pessoa do plural em **-am** e **-em** têm a sua vogal temática/átona defectiva, grafando-se simplesmente com **Mīm** final (`م`) sem Alif:
- *estejam* $\rightarrow$ `استژم`
- *transformam* $\rightarrow$ `ترنسفرمم`
- *iluminam* $\rightarrow$ `الومینم`
- *renovam* $\rightarrow$ `هنووم`
- *trazem* $\rightarrow$ `ترزم`
- *semeiam* $\rightarrow$ `سمیم`

## Ditongos Nasais (-ão, -ãe, -õe)
Os ditongos nasais combinam a base vocálica nasal com semivogais explícitas sem inserir Nūn (`ن`) redundante após consoantes de raiz:
- **-ão** $\rightarrow$ **او** (*Alif-Waw*):
  - *não* $\rightarrow$ `ناو` (consoante Nūn inicial da raiz + `-ão` `او`)
  - *cão* $\rightarrow$ `كاو`
  - *coração* $\rightarrow$ `كرچاو`
  - *gratidão* $\rightarrow$ `گرتیداو`
  - *atenção* $\rightarrow$ `اتنچاو`
  - *ação* $\rightarrow$ `اچاو`
  - *convenção* $\rightarrow$ `كنونچاو` / `كونونچاو`
  - Mantém uma distinção clara de *num* (`نم`) e *nem* (`نم`).
- **-ãe / -ães** $\rightarrow$ **ای** / **ایها**:
  - *mãe* $\rightarrow$ `مای`
  - *pães* $\rightarrow$ `پایها`
- **-ões** $\rightarrow$ **ـوها** (base com *-o* + logograma *-hā* `ـها`):
  - *convenção* $\rightarrow$ `كنونچاو`
  - *convenções* $\rightarrow$ `كنونچوها`

# 4. Regras Morfofonêmicas e Mapeamento de Domínio

## Regra I: Domínio de Número Nominal (-hā / ـها)
O sufixo **-hā** (`ـها`) é estritamente reservado como logograma gráfico para a **flexão nominal de número $[+\text{PL}]$**. Anexa-se a:
1. **Substantivos**: *âmbitos* $\rightarrow$ `آمبیتها`, *livros* $\rightarrow$ `لیوروها`
2. **Adjetivos**: *boas* $\rightarrow$ `بوها` / `اهابوها`, *bons* $\rightarrow$ `بنها`
3. **Determinantes e Artigos**: *as* $\rightarrow$ `اها` (*a* + *hā*), *os* $\rightarrow$ `وها` (*o* + *hā*)
4. **Clíticos Acusativos de 3ª Pessoa**: *fazê-los* $\rightarrow$ `فازیلوها` (*fazê-lo* + *hā*)

## Regra II: Substituição de Superfície Direta
As alternâncias morfofonológicas nos plurais do português são aplicadas **primeiro** para produzir a forma falada de superfície, após o que o `-s` latino é diretamente substituído por `ـها`:
- *plural* $\rightarrow$ *plurais* $\rightarrow$ **پلورایها**
- *real* $\rightarrow$ *reais* $\rightarrow$ **ریایها**
- *animal* $\rightarrow$ *animais* $\rightarrow$ **انیمایها**
- *bom* $\rightarrow$ *bons* $\rightarrow$ **بنها** (assimilação nasal $m \to n$ antes da sufixação)

## Regra III: Domínio Sibilante Verbal e Lexical (س / ز)
As letras **Sīn** (`س`) e **Zāy** (`ز`) são preservadas para sibilantes não-nominais:
1. **Concordância Verbal de 2ª Pessoa**: *tu fazes* $\rightarrow$ `فازس`, *tu tinhas* $\rightarrow$ `تینیاس`
2. **Pronomes Inerentes e Clíticos Reflexivos**: *se* $\rightarrow$ `سہ`, *nos* (clítico) $\rightarrow$ `نوس`
3. **Sibilantes Lexicais da Raiz**: *sim* $\rightarrow$ `سیم`, *mês* $\rightarrow$ `میس`, *paz* $\rightarrow$ `پاز`

## Grafia Alternativa Histórica e Natural: -z Lexical Final (ز)
Os escritores podem inspirar-se na ortografia histórica do português (onde os finais *-es*, *-ês*, *-as*, *-is* eram frequentemente grafados *-ez*, *-êz*, *-az*, *-iz*) e no som fonético natural:
- **Opção de Zāy Final (`ز`) para Palavras Lexicais**: Palavras lexicais não-nominais terminadas em *-s* (como *mas*, *três*, *inglês*, *português*) podem ser naturalmente escritas com **Zāy** (`ز`) em vez de **Sīn** (`س`).
  - *mas* $\rightarrow$ **مز** / **مس** (estritamente Mīm-Zāy ou Mīm-Sīn; NUNCA usar Alif `ا`, ex.: `ماز` ou `ماس` são inválidos)
  - *três* $\rightarrow$ **ترز** / **ترس** (ou **تریز**)
  - *inglês* $\rightarrow$ **انگلز** / **نگلز** (grafado de preferência sem Ye `ی` em *-glês*)
  - *português* $\rightarrow$ **پرتگز** (grafado de preferência sem Ye `ی` em *-guês*)
- Esta opção histórica/natural otimiza o ritmo visual, reduz o acúmulo de caudas de Sīn e aproveita uma tradição ortográfica românica/aljamiada arcaica bem atestada.

# 5. Casos Especiais e Construções Particulares

## Representação das Preposições *de* e *da*
- **Grafia Neutra Padrão**: Ambas as preposições **de** e **da** têm como padrão **Dāl + Gol He** (`دہ`):
  - *de* $\rightarrow$ `دہ`
  - *da* $\rightarrow$ `دہ`
- **Regras de Desambiguação / Contraste**:
  Quando o contexto exige estritamente uma distinção explícita entre *de* e *da*:
  1. **Marcação Diacrítica**: Kasrah (`/ ِ`) para *de* (`دِہ`) vs. Fathah (`/ َ`) para *da* (`دَہ`).
  2. **Substituição Vocálica Explícita**: Alternar para **Ye** (`دی` / `دِیہ`) para *de* vs. **Alif** (`دا`) para *da*.
- **Contrações de Preposição + Artigo**:
  - **do** $\rightarrow$ `دو` | **dos** $\rightarrow$ `دوها` (*do* + *hā*)
  - **da** (explícito) $\rightarrow$ `دا` / `دہ` | **das** $\rightarrow$ `دها` / `داها` (*da* + *hā*)
  - **no** $\rightarrow$ `نو` | **nos** (preposition + article) $\rightarrow$ **نوها** (*no* + *hā*)
    - *Distinção Crucial*: Preposicional *nos* (`نوها`) vs. clítico acusativo de 1ª pessoa *nos* (`نوس`).
  - **pelo** $\rightarrow$ `پلو` | **pelos** $\rightarrow$ `پلوها`

## Singulares Lexicais em -s / -z vs. Flexões de Plural
- As raízes lexicais no singular mantêm `س` ou `ز` explícitos:
  - *mês* $\rightarrow$ `میس`
  - *paz* $\rightarrow$ `پاز`
  - *luz* $\rightarrow$ `لوز`
- As suas flexões no plural levam o *-hā* nominal:
  - *meses* $\rightarrow$ `میزها` (radical *mês* + *hā*)
  - *luzes* $\rightarrow$ `لوزها` / `لوزیها`

## Hiato vs. Ditongos (país vs. pais)
- **Ditongos**: *pais* (plural de *pai*) $\rightarrow$ `پایها` (*pai* + *-hā*)

# 6. Tabelas de Paradigmas Mestre

## Determinantes, Artigos e Pronomes Demonstrativos

| Item do Paradigma | Grafia Latina | Escrita Aljamiada | Notas Morfofonêmicas / Regra Aplicada |
|-------------------+---------------+--------------------+---------------------------------------|
| **Art. Def. Masc. Sing.** | *o* | `و` | Waw isolado |
| **Art. Def. Masc. Plur.** | *os* | `وها` | *o* (`و`) + *-hā* (`ـها`) nominal |
| **Art. Def. Fem. Sing.** | *a* | `ا` / `اہ` | Alif / He Urdu |
| **Art. Def. Fem. Plur.** | *as* | `اها` | *a* (`ا`) + *-hā* (`ـها`) nominal |
| **Art. Indef. Masc. Sing.** | *um* | `اوم` / `وم` | Estritamente Alif-Waw-Mīm ou Waw-Mīm |
| **Art. Indef. Masc. Plur.** | *uns* | `اومها` / `ومها` | *um* (`اوم`) + *-hā* nominal |
| **Art. Indef. Fem. Sing.** | *uma* | `اومہ` / `ومہ` | Estritamente Alif-Waw-Mīm-He ou Waw-Mīm-He |
| **Art. Indef. Fem. Plur.** | *umas* | `اومہا` / `ومہا` | *uma* (`اومہ`) + *-hā* nominal |
| **Dem. Masc. Sing.** | *este* | `استہ` / `ستہ` | Suporte Alif ou zero Alif |
| **Dem. Masc. Plur.** | *estes* | `استها` / `ستها` | Radical *este* + *-hā* nominal |
| **Dem. Fem. Sing.** | *esta* | `استہ` / `ستہ` | Gol He final |
| **Dem. Fem. Plur.** | *estas* | `استها` / `ستها` | Radical *esta* + *-hā* nominal |
| **Dem. Neutro** | *isto* | `ایستو` / `ستو` | Vogal alta *i* (`ی`) + Waw final |
| **Dem. Masc. Distal** | *aquele* | `اكلہ` / `اكيلی` | Kāf + Gol He / Ye |
| **Dem. Masc. Distal Plur.** | *aqueles* | `اكلها` / `اكيليها` | Base + *-hā* nominal |

## Glossário de Termos Lingüísticos e Gramaticais em Aljamiado

| Termo Latino/Português | Escrita Aljamiada | Análise de Regras Ortográficas e Defectividade |
|------------------------|-------------------+------------------------------------------------|
| **linguística** | `لنگویستیكہ` | *Lām-Ye* (`لی`), Nūn nasal, Waw-Ye (`وی` ditongo), *i* alto mantido |
| **fonologia** | `فنلجیہ` | *o* e *o* internos defectivos omitidos, Jīm (`ج`) para G brando, Ye-Gol He final |
| **fonética** | `فنيتكہ` | *fn* + Ye (`ی`) para *e* tónico não-paroxítono + *tika* (`تيكہ`) |
| **morfologia** | `مرفلجیہ` | Esqueleto consonantal *m-r-f-l* + Jīm (`ج`) para G brando, Ye-Gol He final (`ی-ہ`) |
| **sintaxe** | `سينتسہ` | *Sīn-Ye-Nūn* (`سين`), *t* (`ت`), *x* como Sīn (`س`), Gol He final |
| **semântica** | `سمنتیكہ` | Nūn nasalizador interno, *i* alto mantido, Gol He final |
| **pragmática** | `پراگمتيكہ` | Alif tónico em proparoxítona, *a* interno defectivo omitido |
| **etimologia** | `اتملجیہ` / `یتملجیہ` | Alif ou Ye inicial, *e*, *i*, *o* internos defectivos |
| **filologia** | `فللجیہ` | Esqueleto *f-l-l* + Jīm (`ج`) para G brando + Ye-Gol He final (`ی-ہ`) |
| **dialeto** / **dialecto** | `ديلتو` / `دالتم` | Ye para ditongo/hiato *ia*, Waw final |
| **isoglossa** | `ایزgلسہ` -> `ایزگلسہ` | Zāy (`ز`) para *s* intervocálico /z/, Gol He final |

   - **IPA**: `[ki ɐ 'pas i ɐs 'bẽsɐ̃wʃ es'tejɐ̃w kõ vo'se i 'suɐ fɐ'miljɐ]`
   - **Aljamiado**: `كہ ا پز ی اها بنچوها استژم كم وچہ ی سوہ فمیلیہ.`
   - **Notas**: Gol He final (كہ, سوہ, فمیلیہ), sufixo nominal -hā (اها, بنچوها), Zāy em پز, desinência verbal -am defectiva sem Alif (استژم).

2. **Frase 2 — Busca pelo Conhecimento**
   - **Português**: *A busca pelo conhecimento é um dever de todos.*
   - **IPA**: `[ɐ 'buʃkɐ 'pelu kuɲesi'mẽtu 'ɛ ũ de'veɾ dʒi 'todus]`
   - **Aljamiado**: `ا بوسكہ پلو كنیچیمntو` -> `ا بوسكہ پلو كنیچیمنتو ای ام دور دہ تدوها.`
   - **Notas**: Chā para C brando (كنیچیمنتو), u mantido (بوسكہ), infinitivo verbal sem Alif (دور), plural nominal -hā (تدوها).

3. **Frase 3 — Paciência e Gratidão**
   - **Português**: *A paciência e a gratidão trazem paz e sabedoria no coração.*
   - **IPA**: `[ɐ pɐsi'ẽsiɐ i ɐ gɾɐtʃi'dɐ̃w 'tɾazĩw 'pas i sɐbedu'ɾiɐ nu koɾɐ'sɐ̃w]`
   - **Aljamiado**: `ا پچنچیہ ی ا گرتیدناو ترزم پز ی سبدوریہ نو كرچناو.`
   - **Notas**: Chā para C brando (پچنچیہ), Zāy em ترزم e پز, desinência verbal -em defectiva (ترزم), ditongo nasal -ão (گرتیدناو, كرچناو).

4. **Frase 4 — Acolhimento e Comunidade**
   - **Português**: *Seja muito bem-vindo à nossa comunidade.*
   - **IPA**: `['seʒɐ 'mwĩtu bẽj 'vĩdu a 'nɔsɐ komuni'dadʒi]`
   - **Aljamiado**: `سژہ مویتو بم-ویندو آ نسہ كمونیددہ.`
   - **Notas**: Žā para J/G brando (سژہ), ditongo ui (مویتو), Alif Madd inicial (آ), Gol He final.

5. **Frase 5 — Boas Ações e Palavras Sinceras**
   - **Português**: *As boas ações e as palavras sinceras transformam o mundo.*
   - **IPA**: `[ɐs 'bowɐs ɐ'sɐ̃wʃ i ɐs pɐ'lavɾɐs sĩ'sɛɾɐs tɾɐ̃ʃ'fɔɾmɐ̃w u 'mũdu]`
   - **Aljamiado**: `اها بوها اچوها ی اها پلورها سینچرها ترنسفرمم و مندو.`
   - **Notas**: Plurais nominais com -hā (اها, بوها, اچوها, پلورها, سینچرها), desinência verbal -am defectiva sem Alif (ترنسفرمم).

6. **Frase 6 — Trabalho e Estudo**
   - **Português**: *Que Deus abençoe o seu trabalho e os seus estudos.*
   - **IPA**: `[ki 'dewʃ ɐbẽ'sɔj u 'sew tɾɐ'baʎu i uz 'sewʃ is'tudus]`
   - **Aljamiado**: `كہ دیوس ابنچوى و سیو تربلیو ی وها سیوها استودوها.`
   - **Notas**: Lām-Ye em تربلیو, sufixo nominal -hā em plurais (وها, سیوها, استودوها).

7. **Frase 7 — Sabedoria e Justiça**
   - **Português**: *A verdade e a justiça iluminam o caminho dos homens.*
   - **IPA**: `[ɐ veɾ'dadʒi i ɐ ʒuʃ'tisiɐ ilu'minɐ̃w u kɐ'miɲu dus 'omẽjʃ]`
   - **Aljamiado**: `ا ورددہ ی ا ژستچیہ الومینم و كمینیو دوها همنها.`
   - **Notas**: Nūn-Ye em كمینیو, assimilação nasal m → n no plural (همنها), desinência verbal -am defectiva sem Alif (الومینم).

8. **Frase 8 — Generosidade**
   - **Português**: *A verdadeira riqueza está na generosidade do coração.*
   - **IPA**: `[ɐ veɾdɐ'dejɾɐ ʁi'kezɐ es'ta na ʒeneɾozi'dadʒi du koɾɐ'sɐ̃w]`
   - **Aljamiado**: `ا ورددیره هیكزہ استا نہ جنرزیددہ دو كرچناو.`
   - **Notas**: He inicial para R forte (هیكزہ), Jīm para G brando (جنرزیددہ), Zāy intervocálico, Alif tónico em استا.

9. **Frase 9 — Oportunidade e Recomeço**
   - **Português**: *Cada novo dia é uma oportunidade para fazer o bem.*
   - **IPA**: `['kadɐ 'novu 'dʒiɐ 'ɛ 'umɐ opoɾtuni'dadʒi 'paɾɐ fɐ'zeɾ u 'bẽj]`
   - **Aljamiado**: `كدہ نوو دیہ ای اومہ اپرتونیددہ پرہ فزر و بم.`
   - **Notas**: Minimização defectiva (كدہ, اپرتونیددہ, پرہ), infinitivo verbal sem Alif (فزر).

10. **Frase 10 — União e Harmonia**
    - **Português**: *A união de corações sinceros constrói uma vida cheia de paz.*
    - **IPA**: `[ɐ uni'ɐ̃w dʒi koɾɐ'sɐ̃wʃ sĩ'sɛɾus kõʃ'tɾɔj 'umɐ 'vidɐ 'ʃejɐ dʒi 'pas]`
    - **Aljamiado**: `ا انیناو دہ كرچوها سینچرها كنستروى اومہ ویدہ چیه دہ پز.`
    - **Notas**: Plural nominal -hā (كرچوها, سینچرها), Chā para CH (چیہ), Zāy em پز.

11. **Frase 11 — Sabedoria e Razão**
    - **Português**: *A sabedoria ilumina a mente e o conhecimento fortalece a alma.*
    - **IPA**: `[ɐ sɐbedu'ɾiɐ ilu'minɐ ɐ 'mẽtʃi i u kuɲesi'mẽtu fɔɾtɐ'lɛsi ɐ 'awmɐ]`
    - **Aljamiado**: `ا سبدوریہ الومینہ ا منتہ ی و كنیچیمنتو فرتلچہ ا المہ.`
    - **Notas**: Desinência verbal de 3ª pessoa do singular em -a com Gol He (الومینہ), C brando em فرتلچہ (Chā), Gol He final.

12. **Frase 12 — Semeadores de Esperança**
    - **Português**: *Os homens de bem semeiam a esperança e colhem a justiça.*
    - **IPA**: `[uz 'omẽjʃ dʒi 'bẽj se'mejɐ̃w ɐ espe'ɾɐ̃sɐ i 'kɔʎẽj ɐ ʒuʃ'tisiɐ]`
    - **Aljamiado**: `وها همنها دہ بم سمیم ا اسپرنچہ ی كولیم ا ژستچیہ.`
    - **Notas**: Desinências verbais de 3ª pessoa do plural -am (سمیم) e -em (كولیم) defectivas sem Alif, Lām-Ye em كولیم, Žā em ژستچیہ.

13. **Frase 13 — Caminho da Verdade**
    - **Português**: *A luz da verdade guia os nossos passos pelo caminho da paz.*
    - **IPA**: `[ɐ 'luʃ dɐ veɾ'dadʒi 'giɐ uz 'nɔsus 'pasus 'pelu kɐ'miɲu dɐ 'pas]`
    - **Aljamiado**: `ا لوز دا ورددہ گیہ وها نسوها پسوها پلو كمینیو دا پز.`
    - **Notas**: Zāy final em لوز e پز, Sīn duplo intervocálico em نسوها e پسوها com sufixo -hā.

14. **Frase 14 — Palavras de Fé**
    - **Português**: *As palavras de fé e amor renovam os corações dos homens.*
    - **IPA**: `[ɐs pɐ'lavɾɐs dʒi 'fɛ i ɐ'moɾ ʁe'nɔvɐ̃w uz koɾɐ'sɐ̃wʃ dus 'omẽjʃ]`
    - **Aljamiado**: `اها پلورها دہ فی ی امور هنووم وها كرچوها دوها همنها.`
    - **Notas**: He inicial em هنووم para R forte, desinência verbal -am defectiva sem Alif (هنووم), plurais nominais com -hā.

15. **Frase 15 — Busca pela Felicidade**
    - **Português**: *Quem busca a sabedoria encontra a verdadeira felicidade na vida.*
    - **IPA**: `[kẽj 'buʃkɐ ɐ sɐbedu'ɾiɐ ẽ'kõtɾɐ ɐ veɾdɐ'dejɾɐ felisi'dadʒi na 'vidɐ]`
    - **Aljamiado**: `كم بوسكہ ا سبدوریہ انكنترہ ا ورددیره فلچیددہ نہ ویدہ.`
    - **Notas**: Kāf para Q (كم), C brando em فلچیددہ (Chā), Gol He final.
| **razão** | *razões* | `هژو` | `هژوها` | Rā forte He (`ه`) + Zāy (`ژ` / `ز`) + `وها` |
| **cão** | *cães* | `كاو` | `كایها` | Ditongo nasal *-ães* $\rightarrow$ `ایها` |

## Verbos vs. Concordância e Sibilantes

| Categoria | Exemplo de Construção | Escrita Aljamiada | Tratamento da Sibilante |
|-----------+-----------------------+-------------------+-------------------------|
| **Verbo 2ª Pessoa Sing.** | *tu dizes* | `دزس` | Sīn verbal (`س`) |
| **Verbo 2ª Pessoa Sing.** | *tu fazes* | `فزس` | Sīn verbal (`س`) |
| **Verbo 2ª Pessoa Sing.** | *tu tinhas* | `تینیاس` | Sīn verbal (`س`) |
| **Substantivo Plural** | *as fases* | `فزها` | Logograma *-hā* nominal (`ـها`) |
| **Substantivo Plural** | *os dizes* | `دزها` | Logograma *-hā* nominal (`ـها`) |
| **Clítico 3ª Pessoa Plur.** | *fazê-los* | `فازیلوها` | Logograma *-hā* nominal (`ـها`) |
| **Clítico 1ª Pessoa Plur.** | *damo-nos* | `دامونوس` | Sīn clítico inerente (`س`) |
| **Clítico Reflexivo** | *disse-se* | `دیسیسہ` | Sīn clítico inerente (`س`) |

# 7. Corpus e Amostras de Transcrição

Abaixo apresentam-se as transcrições interlineares das 25 frases fundamentais para o Aljamiado Português, cobrindo o rigor morfofonêmico, as sibilantes e o mapeamento consonantal:

1. **Frase 1 — Saudação e Bênção**
   - **Português**: *Que a paz e as bênçãos estejam com você e sua família.*
   - **IPA**: `[ki ɐ 'pas i ɐs 'bẽsɐ̃wʃ es'tejɐ̃w kõ vo'se i 'suɐ fɐ'miljɐ]`
   - **Aljamiado**: `كہ ا پز ی اها بنچوها استژم كم وچہ ی سوہ فمیلیہ.`
   - **Notas**: Gol He final (`كہ`, `سوه`, `فمیلیہ`), sufixo nominal `-hā` (`اها`, `بنچوها`), Zāy em `پز`, desinência verbal `-am` defectiva (`استژم`).

2. **Frase 2 — Busca pelo Conhecimento**
   - **Português**: *A busca pelo conhecimento é um dever de todos.*
   - **IPA**: `[ɐ 'buʃkɐ 'pelu kuɲesi'mẽtu 'ɛ ũ de'veɾ dʒi 'todus]`
   - **Aljamiado**: `ا بوسكہ پلو كنیچیمنتو ای اوم دور دہ تدوها.`
   - **Notas**: Chā para C brando (`كنیچیمنتو`), *um* estritamente como `اوم` (Alif-Waw-Mīm), infinitivo verbal (`دور`), plural nominal `-hā` (`تدوها`).

3. **Frase 3 — Paciência e Gratidão**
   - **Português**: *A paciência e a gratidão trazem paz e sabedoria no coração.*
   - **IPA**: `[ɐ pɐsi'ẽsiɐ i ɐ gɾɐtʃi'dɐ̃w 'tɾazĩw 'pas i sɐbedu'ɾiɐ nu koɾɐ'sɐ̃w]`
   - **Aljamiado**: `ا پچنچیہ ی ا گرتیداو ترزم پز ی سبدوریہ نو كرچاو.`
   - **Notas**: Chā para C brando (`پچنچیہ`), Zāy em `ترزم` e `پز`, ditongo nasal (`گرتیداو`, `كرچاو`).

4. **Frase 4 — Acolhimento e Comunidade**
   - **Português**: *Seja muito bem-vindo à nossa comunidade.*
   - **IPA**: `['seʒɐ 'mwĩtu bẽj 'vĩdu a 'nɔsɐ komuni'dadʒi]`
   - **Aljamiado**: `سژہ مویتو بم-ویندو آ نسہ كمونیددہ.`
   - **Notas**: Žā para J/G brando (`سژہ`), ditongo `ui` (`مویتo` -> `مویتو`), Alif Madd inicial (`آ`).

5. **Frase 5 — Boas Ações e Palavras Sinceras**
   - **Português**: *As boas ações e as palavras sinceras transformam o mundo.*
   - **IPA**: `[ɐs 'bowɐs ɐ'sɐ̃wʃ i ɐs pɐ'lavɾɐs sĩ'sɛɾɐs tɾɐ̃ʃ'fɔɾmɐ̃w u 'mũdu]`
   - **Aljamiado**: `اها بوها اچوها ی اها پلورها سینچرها ترنسفرمم و مندو.`
   - **Notas**: Plurais nominais com `-hā` (`اها`, `بوها`, `اچوها`, `پلورها`, `سینچرها`), `-am` verbal defectivo (`ترنسفرمم`).

6. **Frase 6 — Trabalho e Estudo**
   - **Português**: *Que Deus abençoe o seu trabalho e os seus estudos.*
   - **IPA**: `[ki 'dewʃ ɐbẽ'sɔj u 'sew tɾɐ'baʎu i uz 'sewʃ is'tudus]`
   - **Aljamiado**: `كہ دیوس ابنچوى و سیو تربلیو ی وها سیوها استودوها.`
   - **Notas**: Lām-Ye em `تربلیو`, sufixo nominal `-hā` em plurais (`وها`, `سیوها`, `استودوها`).

7. **Frase 7 — Sabedoria e Justiça**
   - **Português**: *A verdade e a justiça iluminam o caminho dos homens.*
   - **IPA**: `[ɐ veɾ'dadʒi i ɐ ʒuʃ'tisiɐ ilu'mi nɐ̃w u kɐ'miɲu dus 'omẽjʃ]`
   - **Aljamiado**: `ا ورددہ ی ا ژستچیہ الومینم و كمینیو دوها همنها.`
   - **Notas**: Nūn-Ye em `كمینیو`, assimilação nasal `m → n` no plural (`همنها`), `-am` verbal defectivo (`الومینم`).

8. **Frase 8 — Generosidade**
   - **Português**: *A verdadeira riqueza está na generosidade do coração.*
   - **IPA**: `[ɐ veɾdɐ'dejɾɐ ʁi'kezɐ es'ta na ʒeneɾozi'dadʒi du koɾɐ'sɐ̃w]`
   - **Aljamiado**: `ا ورددیره هیكزہ استا نہ جنرزیددہ دو كرچاو.`
   - **Notas**: He inicial padrão para R forte (`هیكزہ`, variante com Rā: `ریكزہ`), Jīm para G brando (`جنرزیددہ`), Zāy intervocálico.

9. **Frase 9 — Oportunidade e Recomeço**
   - **Português**: *Cada novo dia é uma oportunidade para fazer o bem.*
   - **IPA**: `['kadɐ 'novu 'dʒiɐ 'ɛ 'umɐ opoɾtuni'dadʒi 'paɾɐ fɐ'zeɾ u 'bẽj]`
   - **Aljamiado**: `كدہ نوو دیہ ای اومہ اپرتونیددہ پرہ فزر و بم.`
   - **Notas**: *uma* estritamente como `اومہ` (Alif-Waw-Mīm-He), minimização defectiva (`كدہ`, `اپرتونیددہ`, `پرہ`), infinitivo verbal (`فزر`).

10. **Frase 10 — União e Harmonia**
    - **Português**: *A união de corações sinceros constrói uma vida cheia de paz.*
    - **IPA**: `[ɐ uni'ɐ̃w dʒi koɾɐ'sɐ̃wʃ sĩ'sɛɾus kõʃ'tɾɔj 'umɐ 'vidɐ 'ʃejɐ dʒi 'pas]`
    - **Aljamiado**: `ا انیناو دہ كرچوها سینچرها كنستروى اومہ ویدہ چیه دہ پز.`
    - **Notas**: *uma* estritamente como `اومہ`, plural nominal `-hā` (`كرچوها`, `سینچرها`), Chā para CH (`چیہ`), Zāy em `پز`.

11. **Frase 11 — Sabedoria e Razão**
    - **Português**: *A sabedoria ilumina a mente e o conhecimento fortalece a alma.*
    - **IPA**: `[ɐ sɐbedu'ɾiɐ ilu'minɐ ɐ 'mẽtʃi i u kuɲesi'mẽtu fɔɾtɐ'lɛsi ɐ 'awmɐ]`
    - **Aljamiado**: `ا سبدوریہ الومینہ ا منتہ ی و كنیچیمنتo فرتلچہ ا المہ.`
    - **Notas**: Alif inicial em `الومینہ` e `المہ`, C brando em `فرتلچہ` (Chā), Gol He final.

12. **Frase 12 — Semeadores de Esperança**
    - **Português**: *Os homens de bem semeiam a esperança e colhem a justiça.*
    - **IPA**: `[uz 'omẽjʃ dʒi 'bẽj se'mejɐ̃w ɐ espe'ɾɐ̃sɐ i 'kɔʎẽj ɐ ʒuʃ'tisiɐ]`
    - **Aljamiado**: `وها همنها دہ بم سمیم ا اسپرنچہ ی كولیم ا ژستچیہ.`
    - **Notas**: Assimilação nasal (`همنها`), ditongo `ei` (`سمیم`), Lām-Ye em `كولیم`, Žā em `ژستچیہ`.

13. **Frase 13 — Caminho da Verdade**
    - **Português**: *A luz da verdade guia os nossos passos pelo caminho da paz.*
    - **IPA**: `[ɐ 'luʃ dɐ veɾ'dadʒi 'giɐ uz 'nɔsus 'pasus 'pelu kɐ'miɲu dɐ 'pas]`
    - **Aljamiado**: `ا لوز دا ورددہ گیہ وها نسوها پسوها پلو كمینیو دا پز.`
    - **Notas**: Zāy final em `لوز` e `پز`, Sīn duplo intervocálico em `نسوها` e `پسوها` com sufixo `-hā`.

14. **Frase 14 — Palavras de Fé**
    - **Português**: *As palavras de fé e amor renovam os corações dos homens.*
    - **IPA**: `[ɐs pɐ'lavɾɐs dʒi 'fɛ i ɐ'moɾ ʁe'nɔvɐ̃w uz koɾɐ'sɐ̃wʃ dus 'omẽjʃ]`
    - **Aljamiado**: `اها پلورها دہ فی ی امور هنووم وها كرچوها دوها همنها.`
    - **Notas**: He inicial padrão em `هنووم` (variante com Rā: `رنووم`), `-am` verbal defectivo (`هنووم`), plurais nominais `-hā`.

15. **Frase 15 — Busca pela Felicidade**
    - **Português**: *Quem busca a sabedoria encontra a verdadeira felicidade na vida.*
    - **IPA**: `[kẽj 'buʃkɐ ɐ sɐbedu'ɾiɐ ẽ'kõtɾɐ ɐ veɾdɐ'dejɾɐ felisi'dadʒi na 'vidɐ]`
    - **Aljamiado**: `كم بوسكہ ا سبدوریہ انكنترہ ا ورددیره فلچیددہ نہ ویدہ.`
    - **Notas**: Kāf para Q (`كم`), C brando em `فلچیددہ` (Chā), Gol He final.

16. **Frase 16 — Reflexão e Honra**
    - **Português**: *Um bom amigo traz honra e alegria para a nossa casa.*
    - **IPA**: `[ũ 'bõj ɐ'migu 'tɾaʃ 'õɾɐ i ɐle'gɾiɐ 'paɾɐ ɐ 'nɔsɐ 'kazɐ]`
    - **Aljamiado**: `اوم بم امیگو ترز هنرہ ی الگریہ پرہ ا نسہ كزہ.`
    - **Notas**: *um* estritamente como `اوم` (Alif-Waw-Mīm), He em `هنرہ` (honra), Zāy em `كزہ` (casa /z/), Sīn duplo em `نسہ` (nossa /s/).

17. **Frase 17 — União da Família**
    - **Português**: *Os filhos e as filhas escutam os conselhos dos pais.*
    - **IPA**: `[uz 'fiʎus i ɐs 'fiʎɐs is'kutɐ̃w uz kõ'seʎus dus 'pajʃ]`
    - **Aljamiado**: `وها فیلیوها ی اها فیلیه‌ها اسكوتم وها كنسیلیوها دوها پایها.`
    - **Notas**: Lām-Ye para LH (`فیلیوها`, `کنسیلیوها`), plurais nominais `-hā`, `-am` verbal (`اسكوتم`), ditongo `pais` $\rightarrow$ `پایها`.

18. **Frase 18 — Trabalho e Perseverança**
    - **Português**: *A paciência é uma virtude que transforma os maus momentos.*
    - **IPA**: `[ɐ pɐsi'ẽsiɐ 'ɛ 'umɐ vɪɾ'tudʒi ki tɾɐ̃ʃ'fɔɾmɐ uz 'mawʃ mo'mẽtus]`
    - **Aljamiado**: `ا پچنچیہ ای اومہ ورتودہ كہ ترنسفرمہ وها ماوها مومنتوها.`
    - **Notas**: *uma* estritamente como `اومہ`, Chā em `پچنچیہ`, Waw para V (`ورتودہ`), plurais `-hā` (`ماوها`, `مومنتوها`).

19. **Frase 19 — Esperança no Amanhã**
    - **Português**: *Quem planta a justiça colhe um futuro de paz e prosperidade.*
    - **IPA**: `[kẽj 'plɐ̃tɐ ɐ ʒuʃ'tisiɐ 'kɔʎi ũ fu'tuɾu dʒi 'pas i pɾospeɾi'dadʒi]`
    - **Aljamiado**: `كم پلنتہ ا ژستچیہ كولہ اوم فوتورو دہ پز ی پرسپریددہ.`
    - **Notas**: *um* estritamente como `اوم`, Žā em `ژستچیہ`, Lām-Ye em `كولہ`, Zāy em `پز`.

20. **Frase 20 — Caminho e Destino**
    - **Português**: *As palavras voam com o vento, mas as boas obras permanecem.*
    - **IPA**: `[ɐs pɐ'lavɾɐs 'vwɐ̃w kõ u 'vẽtu mɐʃ ɐs 'bowɐs 'ɔbɾɐs peɾmɐ'nesẽj]`
    - **Aljamiado**: `اها پلورها وووم كم و ونتو، مس اها بوها ابرها پرمنچم.`
    - **Notas**: Plurais nominais `-hā` (`پلورها`, `بوها`, `ابرها`), C brando em `پرمنچم` (Chā), `-em` verbal (`پرمنچم`).

21. **Frase 21 — Conhecimento e Luz**
    - **Português**: *O estudo constante ilumina o espírito e abre a mente.*
    - **IPA**: `[u is'tudu kõʃ'tɐ̃tʃi ilu'minɐ u es'piɾitu i 'abɾi ɐ 'mẽtʃi]`
    - **Aljamiado**: `و استودو كنستنتہ الومینہ و اسپیریتو ی ابرہ ا منتہ.`
    - **Notas**: Alif inicial de suporte (`استودو`, `اسپیریتو`), Gol He final em `كنستنتہ`, `الومینہ`, `منتہ`.

22. **Frase 22 — Respeito e Modéstia**
    - **Português**: *Um homem sábio fala com humildade e ouve com atenção.*
    - **IPA**: `[ũ 'omẽj 'sabju 'falɐ kõ umiw'dadʒi i 'owvi kõ ɐtẽ'sɐ̃w]`
    - **Aljamiado**: `اوم همم سبیو فلہ كم اومیلددہ ی وو كم اتنچاو.`
    - **Notas**: *um* estritamente como `اوم`, assimilação nasal `همم`, Hā mudo em `اومیلددہ`, ditongo nasal `-ção` $\rightarrow$ `تنچاو`.

23. **Frase 23 — Semeando Bondade**
    - **Português**: *Uma boa ação traz uma grande recompensa no coração.*
    - **IPA**: `['umɐ 'bowɐ ɐ'sɐ̃w 'tɾaʃ 'umɐ 'gɾɐ̃dʒi ʁekõ'pẽsɐ nu koɾɐ'sɐ̃w]`
    - **Aljamiado**: `اومہ بوہ اچاو ترز اومہ گرندہ هكمپنسہ نو كرچاو.`
    - **Notas**: *uma* estritamente como `اومہ`, He inicial padrão em `هكمپنسہ` (variante: `ركمپنسہ`), Zāy em `ترز`.

24. **Frase 24 — Diálogo e Concórdia**
    - **Português**: *A verdade une as pessoas e constrói a verdadeira paz.*
    - **IPA**: `[ɐ veɾ'dadʒi 'uni ɐs pe'soɐs i kõʃ'tɾɔj ɐ veɾdɐ'dejɾɐ 'pas]`
    - **Aljamiado**: `ا ورددہ اونی اها پسوها ی كنستروى ا ورددیره پز.`
    - **Notas**: Sīn duplo em `پسوها` com sufixo `-hā`, ditongo `oi` em `كنستروى`, Zāy em `پز`.

25. **Frase 25 — O Mar e o Horizonte**
    - **Português**: *Os rios correm para o mar e renovam as águas da terra.*
    - **IPA**: `[uz 'ʁiws 'kɔʁẽj 'paɾɐ u 'maɾ i ʁe'nɔvɐ̃w ɐs 'agwɐʃ dɐ 'tɛʁɐ]`
    - **Aljamiado**: `وها ریوها كوهم پرہ و مر ی رنووم اها اگوها دا تہہ.`
    - **Notas**: Rā para R inicial em `ریوها` e `رنووم` (variantes com He: `هيوها`, `هنووم`), He para RR intervocálico em `كوهم` e `تہہ`, desinência verbal -em defectiva (`كوهم`), plurais `-hā` (`ریوها`, `اگوها`).
