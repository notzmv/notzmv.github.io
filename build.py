#!/usr/bin/env python3
import os
import re

def convert_org_to_md(org_path, md_path):
    if not os.path.exists(org_path):
        print(f"Error: {org_path} not found.")
        return

    with open(org_path, "r", encoding="utf-8") as f:
        org_content = f.read()

    md_content = org_content
    # Convert org headers (* Heading -> # Heading)
    md_content = re.sub(r'^\* (.*)$', r'# \1', md_content, flags=re.MULTILINE)
    md_content = re.sub(r'^\*\* (.*)$', r'## \1', md_content, flags=re.MULTILINE)
    md_content = re.sub(r'^\*\*\* (.*)$', r'### \1', md_content, flags=re.MULTILINE)
    # Internal links [[#anchor][label]] -> label
    md_content = re.sub(r'\[\[#.*?\]\[(.*?)\]\]', r'\1', md_content)

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Successfully updated {md_path} from {org_path}")

def update_pt_cards():
    html_path = "pt/index.html"
    sentences = [
        {
            "id": 1,
            "title": "Frase 1 — Saudação e Bênção",
            "pt": "Que a paz e as bênçãos estejam com você e sua família.",
            "ipa": "[ki ɐ 'pas i ɐs 'bẽsɐ̃wʃ es'tejɐ̃w kõ vo'se i 'suɐ fɐ'miljɐ]",
            "aljamiado": "كہ ا پز ی اها بنچوها استژم كم وچہ ی سوہ فمیلیہ.",
            "notes": "Gol He final (كہ, سوہ, فمیلیہ), sufixo nominal -hā (اها, بنچوها), Zāy em پز, verb ending -am (استژم)."
        },
        {
            "id": 2,
            "title": "Frase 2 — Busca pelo Conhecimento",
            "pt": "A busca pelo conhecimento é um dever de todos.",
            "ipa": "[ɐ 'buʃkɐ 'pelu kuɲesi'mẽtu 'ɛ ũ de'veɾ dʒi 'todus]",
            "aljamiado": "ا بوسكہ پلو كنیچیمنتو ای اوم دور دہ تدوها.",
            "notes": "Chā para C brando (كنیچیمنتو), um estritamente como اوم (Alif-Waw-Mīm), infinitivo verbal (دور), plural nominal -hā (تدوها)."
        },
        {
            "id": 3,
            "title": "Frase 3 — Paciência e Gratidão",
            "pt": "A paciência e a gratidão trazem paz e sabedoria no coração.",
            "ipa": "[ɐ pɐsi'ẽsiɐ i ɐ gɾɐtʃi'dɐ̃w 'tɾazĩw 'pas i sɐbedu'ɾiɐ nu koɾɐ'sɐ̃w]",
            "aljamiado": "ا پچنچیہ ی ا گرتیداو ترزم پز ی سبدوریہ نو كرچاو.",
            "notes": "Chā para C brando (پچنچیہ), Zāy em ترزم e پز, ditongo nasal (گرتیداو, كرچاو)."
        },
        {
            "id": 4,
            "title": "Frase 4 — Acolhimento e Comunidade",
            "pt": "Seja muito bem-vindo à nossa comunidade.",
            "ipa": "['seʒɐ 'mwĩtu bẽj 'vĩdu a 'nɔsɐ komuni'dadʒi]",
            "aljamiado": "سژہ مویتو بم-ویندو آ نسہ كمونیددہ.",
            "notes": "Žā para J/G brando (سژہ), ditongo ui (مویتو), Alif Madd inicial (آ)."
        },
        {
            "id": 5,
            "title": "Frase 5 — Boas Ações e Palavras Sinceras",
            "pt": "As boas ações e as palavras sinceras transformam o mundo.",
            "ipa": "[ɐs 'bowɐs ɐ'sɐ̃wʃ i ɐs pɐ'lavɾɐs sĩ'sɛɾɐs tɾɐ̃ʃ'fɔɾmɐ̃w u 'mũdu]",
            "aljamiado": "اها بوها اچوها ی اها پلورها سینچرها ترنسفرمم و مندو.",
            "notes": "Plurais nominais com -hā (اها, بوها, اچوها, پلورها, سینچرها), -am verbal defectivo (ترنسفرمم)."
        },
        {
            "id": 6,
            "title": "Frase 6 — Trabalho e Estudo",
            "pt": "Que Deus abençoe o seu trabalho e os seus estudos.",
            "ipa": "[ki 'dewʃ ɐbẽ'sɔj u 'sew tɾɐ'baʎu i uz 'sewʃ is'tudus]",
            "aljamiado": "كہ دیوس ابنچوى و سیو تربلیو ی وها سیوها استودوها.",
            "notes": "Lām-Ye em تربلیو, sufixo nominal -hā em plurais (وها, سیوها, استودوها)."
        },
        {
            "id": 7,
            "title": "Frase 7 — Sabedoria e Justiça",
            "pt": "A verdade e a justiça iluminam o caminho dos homens.",
            "ipa": "[ɐ veɾ'dadʒi i ɐ ʒuʃ'tisiɐ ilu'mi nɐ̃w u kɐ'miɲu dus 'omẽjʃ]",
            "aljamiado": "ا ورددہ ی ا ژستچیہ الومینم و كمینیو دوها همنها.",
            "notes": "Nūn-Ye em كمینیو, assimilação nasal m → n no plural (همنها), -am verbal defectivo (الومینم)."
        },
        {
            "id": 8,
            "title": "Frase 8 — Generosidade",
            "pt": "A verdadeira riqueza está na generosidade do coração.",
            "ipa": "[ɐ veɾdɐ'dejɾɐ ʁi'kezɐ es'ta na ʒeneɾozi'dadʒi du koɾɐ'sɐ̃w]",
            "aljamiado": "ا ورددیره ریكزہ استا نہ جنرزیددہ دو كرچاو.",
            "notes": "Rā para R inicial (ریكزہ, variante com He: هیكزہ), Jīm para G brando (جنرزیددہ), Zāy intervocálico."
        },
        {
            "id": 9,
            "title": "Frase 9 — Oportunidade e Recomeço",
            "pt": "Cada novo dia é uma oportunidade para fazer o bem.",
            "ipa": "['kadɐ 'novu 'dʒiɐ 'ɛ 'umɐ opoɾtuni'dadʒi 'paɾɐ fɐ'zeɾ u 'bẽj]",
            "aljamiado": "كدہ نوو دیہ ای اومہ اپرتونیددہ پرہ فزر و بم.",
            "notes": "uma estritamente como اومہ (Alif-Waw-Mīm-He), minimização defectiva (كدہ, اپرتونیددہ, پرہ), infinitivo verbal (فزر)."
        },
        {
            "id": 10,
            "title": "Frase 10 — União e Harmonia",
            "pt": "A união de corações sinceros constrói uma vida cheia de paz.",
            "ipa": "[ɐ uni'ɐ̃w dʒi koɾɐ'sɐ̃wʃ sĩ'sɛɾus kõʃ'tɾɔj 'umɐ 'vidɐ 'ʃejɐ dʒi 'pas]",
            "aljamiado": "ا انیناو دہ كرچوها سینچرها كنستروى اومہ ویدہ چیه دہ پز.",
            "notes": "uma estritamente como اومہ, plural nominal -hā (كرچوها, سینچرها), Chā para CH (چیہ), Zāy em پز."
        },
        {
            "id": 11,
            "title": "Frase 11 — Sabedoria e Razão",
            "pt": "A sabedoria ilumina a mente e o conhecimento fortalece a alma.",
            "ipa": "[ɐ sɐbedu'ɾiɐ ilu'minɐ ɐ 'mẽtʃi i u kuɲesi'mẽtu fɔɾtɐ'lɛsi ɐ 'awmɐ]",
            "aljamiado": "ا سبدوریہ الومینہ ا منتہ ی و كنیچیمنتو فرتلچہ ا المہ.",
            "notes": "Alif inicial em الومینہ e المہ, C brando em فرتلچہ (Chā), Gol He final."
        },
        {
            "id": 12,
            "title": "Frase 12 — Semeadores de Esperança",
            "pt": "Os homens de bem semeiam a esperança e colhem a justiça.",
            "ipa": "[uz 'omẽjʃ dʒi 'bẽj se'mejɐ̃w ɐ espe'ɾɐ̃sɐ i 'kɔʎẽj ɐ ʒuʃ'tisiɐ]",
            "aljamiado": "وها همنها دہ بم سمیم ا اسپرنچہ ی كولیم ا ژستچیہ.",
            "notes": "Assimilação nasal (همنها), ditongo ei (سمیم), Lām-Ye em كولیم, Žā em ژستچیہ."
        },
        {
            "id": 13,
            "title": "Frase 13 — Caminho da Verdade",
            "pt": "A luz da verdade guia os nossos passos pelo caminho da paz.",
            "ipa": "[ɐ 'luʃ dɐ veɾ'dadʒi 'giɐ uz 'nɔsus 'pasus 'pelu kɐ'miɲu dɐ 'pas]",
            "aljamiado": "ا لوز دا ورددہ گیہ وها نسوها پسوها پلو كمینیو دا پز.",
            "notes": "Zāy final em لوز e پز, Sīn duplo intervocálico em نسوها e پسوها com sufixo -hā."
        },
        {
            "id": 14,
            "title": "Frase 14 — Palavras de Fé",
            "pt": "As palavras de fé e amor renovam os corações dos homens.",
            "ipa": "[ɐs pɐ'lavɾɐs dʒi 'fɛ i ɐ'moɾ ʁe'nɔvɐ̃w uz koɾɐ'sɐ̃wʃ dus 'omẽjʃ]",
            "aljamiado": "اها پلورها دہ فی ی امور رنووم وها كرچوها دوها همنها.",
            "notes": "Rā para R inicial em رنووم (variante com He: هنووم), -am verbal defectivo (رنووم), plurais nominais -hā."
        },
        {
            "id": 15,
            "title": "Frase 15 — Busca pela Felicidade",
            "pt": "Quem busca a sabedoria encontra a verdadeira felicidade na vida.",
            "ipa": "[kẽj 'buʃkɐ ɐ sɐbedu'ɾiɐ ẽ'kõtɾɐ ɐ veɾdɐ'dejɾɐ felisi'dadʒi na 'vidɐ]",
            "aljamiado": "كم بوسكہ ا سبدوریہ انكنترہ ا ورددیره فلچیددہ نہ ویدہ.",
            "notes": "Kāf para Q (كم), C brando em فلچیددہ (Chā), Gol He final."
        },
        {
            "id": 16,
            "title": "Frase 16 — Reflexão e Honra",
            "pt": "Um bom amigo traz honra e alegria para a nossa casa.",
            "ipa": "[ũ 'bõj ɐ'migu 'tɾaʃ 'õɾɐ i ɐle'gɾiɐ 'paɾɐ ɐ 'nɔsɐ 'kazɐ]",
            "aljamiado": "اوم بم امیگو ترز هنرہ ی الگریہ پرہ ا نسہ كزہ.",
            "notes": "um estritamente como اوم (Alif-Waw-Mīm), He em هنرہ (honra), Zāy em كزہ (casa /z/), Sīn duplo em نسہ (nossa /s/)."
        },
        {
            "id": 17,
            "title": "Frase 17 — União da Família",
            "pt": "Os filhos e as filhas escutam os conselhos dos pais.",
            "ipa": "[uz 'fiʎus i ɐs 'fiʎɐs is'kutɐ̃w uz kõ'seʎus dus 'pajʃ]",
            "aljamiado": "وها فیلیوها ی اها فیلیه‌ها اسكوتم وها كنسیلیوها دوها پایها.",
            "notes": "Lām-Ye para LH (فیلیوها, كنسیلیوها), plurais nominais -hā, -am verbal (اسكوتم), ditongo pais → پایها."
        },
        {
            "id": 18,
            "title": "Frase 18 — Trabalho e Perseverança",
            "pt": "A paciência é uma virtude que transforma os maus momentos.",
            "ipa": "[ɐ pɐsi'ẽsiɐ 'ɛ 'umɐ vɪɾ'tudʒi ki tɾɐ̃ʃ'fɔɾmɐ uz 'mawʃ mo'mẽtus]",
            "aljamiado": "ا پچنچیہ ای اومہ ورتودہ كہ ترنسفرمہ وها ماوها مومنتوها.",
            "notes": "uma estritamente como اومہ, Chā em پچنچیہ, Waw para V (ورتودہ), plurais -hā (ماوها, مومنتوها)."
        },
        {
            "id": 19,
            "title": "Frase 19 — Esperança no Amanhã",
            "pt": "Quem planta a justiça colhe um futuro de paz e prosperidade.",
            "ipa": "[kẽj 'plɐ̃tɐ ɐ ʒuʃ'tisiɐ 'kɔʎi ũ fu'tuɾu dʒi 'pas i pɾospeɾi'dadʒi]",
            "aljamiado": "كم پلنتہ ا ژستچیہ كولہ اوم فوتورو دہ پز ی پرسپریددہ.",
            "notes": "um estritamente como اوم, Žā em ژستچیہ, Lām-Ye em كولہ, Zāy em پز."
        },
        {
            "id": 20,
            "title": "Frase 20 — Caminho e Destino",
            "pt": "As palavras voam com o vento, mas as boas obras permanecem.",
            "ipa": "[ɐs pɐ'lavɾɐs 'vwɐ̃w kõ u 'vẽtu mɐʃ ɐs 'bowɐs 'ɔbɾɐs peɾmɐ'nesẽj]",
            "aljamiado": "اها پلورها وووم كم و ونتو، مس اها بوها ابرها پرمنچم.",
            "notes": "Plurais nominais -hā (پلورها, بوها, ابرها), C brando em پرمنچم (Chā), -em verbal (پرمنچم)."
        },
        {
            "id": 21,
            "title": "Frase 21 — Conhecimento e Luz",
            "pt": "O estudo constante ilumina o espírito e abre a mente.",
            "ipa": "[u is'tudu kõʃ'tɐ̃tʃi ilu'minɐ u es'piɾitu i 'abɾi ɐ 'mẽtʃi]",
            "aljamiado": "و استودو كنستنتہ الومینہ و اسپیریتو ی ابرہ ا منتہ.",
            "notes": "Alif inicial de suporte (استودو, اسپیریتو), Gol He final em كنستنتہ, الومینہ, منتہ."
        },
        {
            "id": 22,
            "title": "Frase 22 — Respeito e Modéstia",
            "pt": "Um homem sábio fala com humildade e ouve com atenção.",
            "ipa": "[ũ 'omẽj 'sabju 'falɐ kõ umiw'dadʒi i 'owvi kõ ɐtẽ'sɐ̃w]",
            "aljamiado": "اوم همم سبیو فلہ كم اومیلددہ ی وو كم اتنچاو.",
            "notes": "um estritamente como اوم, assimilação nasal همم, Hā mudo em اومیلددہ, ditongo nasal -ção → تنچاو."
        },
        {
            "id": 23,
            "title": "Frase 23 — Semeando Bondade",
            "pt": "Uma boa ação traz uma grande recompensa no coração.",
            "ipa": "['umɐ 'bowɐ ɐ'sɐ̃w 'tɾaʃ 'umɐ 'gɾɐ̃dʒi ʁekõ'pẽsɐ nu koɾɐ'sɐ̃w]",
            "aljamiado": "اومہ بوہ اچاو ترز اومہ گرندہ ركمپنسہ نو كرچاو.",
            "notes": "uma estritamente como اومہ, Rā para R inicial em ركمپنسہ (variante com He: هكمپنسہ), Zāy em ترز."
        },
        {
            "id": 24,
            "title": "Frase 24 — Diálogo e Concórdia",
            "pt": "A verdade une as pessoas e constrói a verdadeira paz.",
            "ipa": "[ɐ veɾ'dadʒi 'uni ɐs pe'soɐs i kõʃ'tɾɔj ɐ veɾdɐ'dejɾɐ 'pas]",
            "aljamiado": "ا ورددہ اونی اها پسوها ی كنستروى ا ورددیره پز.",
            "notes": "Sīn duplo em پسوها com sufixo -hā, ditongo oi em كنستروى, Zāy em پز."
        },
        {
            "id": 25,
            "title": "Frase 25 — O Mar e o Horizonte",
            "pt": "Os rios correm para o mar e renovam as águas da terra.",
            "ipa": "[uz 'ʁiws 'kɔʁẽj 'paɾɐ u 'maɾ i ʁe'nɔvɐ̃w ɐs 'agwɐʃ dɐ 'tɛʁɐ]",
            "aljamiado": "وها ریوها كورم پرہ و مر ی رنووم اها اگوها دا تره.",
            "notes": "Rā para R inicial em ریوها e رنووم (variantes com He: هيوها, هنووم), He para RR intervocálico em تـره, plurais -hā."
        }
    ]

    cards_html = []
    for s in sentences:
        card = f'''    <div class="card">
      <div class="card-meta">{s["title"]}</div>
      <div class="portuguese">{s["pt"]}</div>
      <div class="ipa">{s["ipa"]}</div>
      <div class="perso-arabic ar">{s["aljamiado"]}</div>
      <div class="notes">{s["notes"]}</div>
    </div>'''
        cards_html.append(card)

    cards_block = "\n\n".join(cards_html)

    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        pattern = r'<div class="corpus-list">.*?(?=\s*<script>|\s*</body>)'
        replacement = '<div class="corpus-list">\n' + cards_block + '\n</div>\n\n'
        updated_html = re.sub(pattern, replacement, html_content, flags=re.DOTALL)

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(updated_html)
        print(f"Successfully updated {html_path} cards")

def update_en_cards():
    html_path = "index.html"
    sentences = [
        {
            "title": "Pangram & Benchmark",
            "english": "The quick brown fox jumps over the lazy dog.",
            "ipa": "[ðə kwɪk braʊn fɒks dʒʌmps ˈoʊvər ðə ˈleɪzi dɒɡ]",
            "aljamiado": "ذا كویك براون فاكس جمپس اوڤر ذا لیزى داگ.",
            "notes": "Voiced th (ذ), v (ڤ), nominal agreement, silent-e dropped."
        },
        {
            "title": "Literature & Drama",
            "english": "To be, or not to be, that is the question.",
            "ipa": "[tuː biː ɔːr nɒt tuː biː ðæt ɪz ðə ˈkwɛstʃən]",
            "aljamiado": "تو بہ، اور نات تو بہ، ذات إز ذا كوإسچن.",
            "notes": "Selective monosyllabic He (بہ), th (ث / ذ), ch (چ)."
        },
        {
            "title": "Famous Speech",
            "english": "I have a dream that one day this nation will rise up.",
            "ipa": "[aɪ hæv ə driːm ðæt wʌn deɪ ðɪs ˈneɪʃən wɪl raɪz ʌp]",
            "aljamiado": "ای هڤ ا دریم ذات وان دی ذس نیشن وِل رایز اپ.",
            "notes": "Diphthong ay (ای), voiced th (ذ), w (و), sh (ش)."
        },
        {
            "title": "Historical Document",
            "english": "We hold these truths to be self-evident, that all men are created equal.",
            "ipa": "[wiː hoʊld ðiːz truːðz tuː biː sɛlf ˈɛvɪdənt ðæt ɔːl mɛn ɑːr kriːˈeɪtɪd ˈiːkwəl]",
            "aljamiado": "وى هولد ذیز ثروثها تو بہ سلف-إڤدنت، ذات آل من آر كرییتد ایكول.",
            "notes": "Nominal plural -hā (ثروثها), past tense -ed (كرییتد), broad aw (آل)."
        },
        {
            "title": "Velar Nasal (Sağır Kāf ڭ vs Nūn-Gāf نگ)",
            "english": "I am writing a new writing system for English using Perso-Arabic script.",
            "ipa": "[aɪ æm ˈraɪtɪŋ ə njuː ˈraɪtɪŋ ˈsɪstəm fɔːr ˈɪŋɡlɪʃ ˈjuːzɪŋ ˈpɜːrʒoʊ ˈærəbɪk skrɪpt]",
            "aljamiado": "ای ام رایتڭ ا نیو رایتڭ سیستم فور إنگلش یوزڭ پرسو-اربیك سكریپت.",
            "notes": "Option A (Sağır Kāf ڭ): رایتڭ, یوزڭ. Option B (Nūn-Gāf نگ): رایتنگ, یوزنگ."
        },
        {
            "title": "Daily Conversation & Plurals",
            "english": "She bought three books, two laptops, and five new pens.",
            "ipa": "[ʃiː bɔːt θriː bʊks tuː ˈlæptɒps ænd faɪv njuː pɛnz]",
            "aljamiado": "شہ بات ثرى بوكها، تو لپتاپها، اند فایل نیو پنها.",
            "notes": "Nominal plurals systematically take -hā (بوكها, لپتاپها, پنها)."
        },
        {
            "title": "Verbal vs Nominal Contrast",
            "english": "He speaks fast while reading many books.",
            "ipa": "[hiː spiːks fæst waɪl ˈriːdɪŋ ˈmɛni bʊks]",
            "aljamiado": "هى اسپیكس فاست وایل ریدڭ منى بوكها.",
            "notes": "Verbal agreement retains Sīn (اسپیكس) while nominal plural uses -hā (بوكها)."
        },
        {
            "title": "Past Tense Morphophonemics",
            "english": "She walked to the city and played music for her friends.",
            "ipa": "[ʃiː wɔːkt tuː ðə ˈsɪti ænd pleɪd ˈmjuːzɪk fɔːr hɜːr frɛndz]",
            "aljamiado": "شہ واكت تو ذا ستى اند پلاید میوزك فور هر فرندها.",
            "notes": "Surface past tense -t (واكت) vs -d (پلاید)."
        },
        {
            "title": "Song & Music",
            "english": "The king was singing a long song in the house.",
            "ipa": "[ðə kɪŋ wɒz ˈsɪŋɪŋ ə lɒŋ sɒŋ ɪn ðə haʊs]",
            "aljamiado": "ذا كڭ واز سڭڭ ا لاڭ ساڭ إن ذا هاوس.",
            "notes": "Sağır Kāf (كڭ, سڭڭ, لاڭ, ساڭ) compact velar nasals."
        },
        {
            "title": "Classic Proverb",
            "english": "Actions speak louder than words.",
            "ipa": "[ˈækʃənz spiːk ˈlaʊdər ðæn wɜːdz]",
            "aljamiado": "آكشنها اسپیك لاودر ذان وردها.",
            "notes": "Initial Alif Madd (آكشنها), plural -hā (آكشنها, وردها)."
        },
        {
            "title": "Classic Proverb",
            "english": "A journey of a thousand miles begins with a single step.",
            "ipa": "[ə ˈdʒɜːrni ɒv ə ˈθaʊzənd maɪlz bɪˈɡɪnz wɪð ə ˈsɪŋɡəl stɛp]",
            "aljamiado": "ا جرنى اوڤ ا ثاوزند مایلها بگینز وث ا سنگل ستپ.",
            "notes": "j (ج), v (ڤ), th (ث), plural -hā (مایلها), agreement (بگینز)."
        },
        {
            "title": "Poetry",
            "english": "Two roads diverged in a yellow wood, and I took the one less traveled by.",
            "ipa": "[tuː roʊdz daɪˈvɜːrdʒd ɪn ə ˈjɛloʊ wʊd ænd aɪ tʊk ðə wʌn lɛs ˈtrævəld baɪ]",
            "aljamiado": "تو رودها داىڤرجد إن ا یلو وود، اند ای توك ذا وان لس ترڤلد بای.",
            "notes": "Plural (رودها), past tense -d (داىڤرجد, ترڤلد), diphthong eye (ای, بای)."
        }
    ]

    cards_html = []
    for s in sentences:
        card = f'''    <div class="card">
      <div class="card-meta">{s["title"]}</div>
      <div class="english">{s["english"]}</div>
      <div class="ipa">{s["ipa"]}</div>
      <div class="perso-arabic ar">{s["aljamiado"]}</div>
      <div class="notes">{s["notes"]}</div>
    </div>'''
        cards_html.append(card)

    cards_block = "\n\n".join(cards_html)

    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        pattern = r'<div class="corpus-list">.*?(?=\s*<script>|\s*</body>)'
        replacement = '<div class="corpus-list">\n' + cards_block + '\n</div>\n\n'
        updated_html = re.sub(pattern, replacement, html_content, flags=re.DOTALL)

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(updated_html)
        print(f"Successfully updated {html_path} cards")

def build():
    convert_org_to_md("pt/index.org", "pt/index.md")
    convert_org_to_md("index.org", "index.md")
    update_pt_cards()
    update_en_cards()

if __name__ == "__main__":
    build()
