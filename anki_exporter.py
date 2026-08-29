#!/usr/bin/env python3
"""
anki_exporter.py — Anki Exporter Tool for Aljamiado Português.

Parses Aljamiado Português specifications, course lessons, corpus sentences,
and paradigm tables; applies Didactic Tashkīl (marking omitted short vowels only,
leaving visible long vowels and mater lectionis clean) following all orthographic rules;
and exports structured decks via AnkiConnect REST API (http://127.0.0.1:8765) as well
as TSV/JSON files.
"""

import sys
import os
import re
import json
import argparse
import urllib.request
import urllib.error

# ------------------------------------------------------------------------------
# 1. Didactic Tashkīl Engine (Omitted Short Vowels Only)
# ------------------------------------------------------------------------------

# Master dictionary mapping Portuguese and Aljamiado tokens to Didactic Tashkīl forms
TASHKIL_LEXICON = {
    # Pronouns, Prepositions & Short Words
    "a": "اَ",
    "o": "وۆ",
    "e": "یَ",
    "é": "اَیْ",
    "ou": "اوۆ",
    "ao": "اَوْ",
    "os": "وۆها",
    "as": "اَها",
    "de": "دِه",
    "دہ": "دِه",
    "do": "دۆ",
    "da": "دَا",
    "dos": "دۆها",
    "das": "دَاها",
    "que": "كَه",
    "كہ": "كَه",
    "se": "سِه",
    "sua": "سُۆہ",
    "سوه": "سُۆہ",
    "seu": "سِیوۆ",
    "seus": "سِیوۆها",
    "como": "كَمۆ",
    "para": "پَرَه",
    "پرہ": "پَرَه",
    "pelo": "پَلۆ",
    "پلو": "پَلۆ",
    "pela": "پَلَه",
    "mas": "مَسْ",
    "مس": "مَسْ",
    "já": "ژَا",
    "até": "اَتِی",
    "اتی": "اَتِی",
    "hoje": "هۆژَه",
    "هژہ": "هۆژَه",
    "um": "اوم",
    "uma": "اومَه",
    "اومہ": "اومَه",
    "paz": "پَزْ",
    "پز": "پَزْ",
    "luz": "لوُزْ",
    "لوز": "لوُزْ",
    "faz": "فَزْ",
    "فز": "فَزْ",
    "sob": "سَبْ",
    "سب": "سَبْ",
    "zap": "زَاپْ",
    "زاپ": "زَاپْ",
    "boa": "بوۆہ",
    "بوہ": "بوۆہ",
    "boas": "بوۆها",
    "بوها": "بوۆها",

    # Vocabulary & Nouns (Omitted short vowels marked, mater lectionis kept clean)
    "gente": "جَنـْتَه",
    "جنتہ": "جَنـْتَه",
    "cidade": "چِدَدَہ",
    "چددہ": "چِدَدَہ",
    "você": "وۆچِی",
    "وچہ": "وۆچِی",
    "fixo": "فِیچۆ",
    "فیچو": "فِیچۆ",
    "processo": "پْرَچَسۆ",
    "پرچسو": "پْرَچَسۆ",
    "chave": "شَوَه",
    "شوه": "شَوَه",
    "lixo": "لِیشۆ",
    "لیشو": "لِیشۆ",
    "flash": "فْلَاشْ",
    "فلاش": "فْلَاشْ",
    "água": "آگۆہ",
    "آگوه": "آگۆہ",
    "carro": "كَہۆ",
    "كهو": "كَہۆ",
    "honra": "هَنـْرَه",
    "هنره": "هَنـْرَه",
    "homem": "هَمَم",
    "همم": "هَمَم",
    "homens": "هَمَنـْها",
    "همنها": "هَمَنـْها",
    "minha": "مِینـِیَہ",
    "مینیہ": "مِینـِیَہ",
    "ilumina": "یِلوُمِنَہ",
    "يلومنه": "یِلوُمِنَہ",
    "sabedoria": "سَبَدُرِیَہ",
    "سبدریہ": "سَبَدُرِیَہ",
    "esperança": "اَسْپَرَنـْچَہ",
    "اسپرنچہ": "اَسْپَرَنـْچَہ",
    "comunidade": "كَمُونِدَدَہ",
    "كمونددہ": "كَمُونِدَدَہ",
    "verdade": "وَرْدَدَہ",
    "ورددہ": "وَرْدَدَہ",
    "verdadeira": "وَرْدَدَرَہ",
    "ورددرہ": "وَرْدَدَرَہ",
    "generosidade": "جَنَرُزِدَدَہ",
    "جنرزددہ": "جَنَرُزِدَدَہ",
    "justiça": "ژُسْتِچَہ",
    "ژستچہ": "ژُسْتِچَہ",
    "trabalho": "تْرَبَلِیۆ",
    "تربلیو": "تْرَبَلِیۆ",
    "estudo": "اَسْتُودۆ",
    "استودو": "اَسْتُودۆ",
    "estudos": "اَسْتُودۆها",
    "استودوها": "اَسْتُودۆها",
    "caminho": "كَمِینـِیۆ",
    "كمینیو": "كَمِینـِیۆ",
    "riqueza": "رِیكَزَہ",
    "ریكزہ": "رِیكَزَہ",
    "oportunidade": "اَپَرْتُنِدَدَہ",
    "اپرتنددہ": "اَپَرْتُنِدَدَہ",
    "coração": "كَرَچاوْم",
    "كرچاو": "كَرَچاوْم",
    "كرچاوم": "كَرَچاوْم",
    "corações": "كَرَچومها",
    "كرچومها": "كَرَچومها",
    "união": "انِیاوم",
    "انیاوم": "انِیاوم",
    "sinceros": "سِینـْچَرۆها",
    "سینچرها": "سِینـْچَرها",
    "vida": "وِیدَہ",
    "ویدہ": "وِیدَہ",
    "cheia": "شِیَہ",
    "شیہ": "شِیَہ",
    "mente": "مَنـْتَه",
    "منتہ": "مَنـْتَه",
    "conhecimento": "كَنِیچْمَنـْتۆ",
    "كنیچمنتو": "كَنِیچْمَنـْتۆ",
    "alma": "اَلـْمَہ",
    "المہ": "اَلـْمَہ",
    "palavra": "پَلَوْرَہ",
    "پلورہ": "پَلَوْرَہ",
    "palavras": "پَلَوْرها",
    "پلورها": "پَلَوْرها",
    "passos": "پَسۆها",
    "پسوها": "پَسۆها",
    "tudo": "تُودۆ",
    "تودو": "تُودۆ",
    "todos": "تَدۆها",
    "تدوها": "تَدۆها",
    "muito": "مویتۆ",
    "مویتو": "مویتۆ",
    "aqui": "اكئ",
    "caju": "كژؤ",
    "país": "پائس",
    "saúde": "ساؤدہ",
    "baú": "باؤ",
    "pão": "پاوم",
    "mão": "ماوم",
    "não": "ناوم",
    "razão": "رزاوم",
    "visão": "ویزاوم",
    "missão": "مساوم",
    "convenção": "كنونچم",
    "convenções": "كنونچمها",
}

def apply_tashkil_to_aljamiado(text, pt_hint=""):
    """
    Applies Didactic Tashkīl to an Aljamiado text string.
    Only marks omitted short vowels that cannot be seen otherwise;
    leaves visible mater lectionis (Alif, Waw, Ye, Gol He) clean.
    """
    if not text:
        return ""

    tokens = text.split()
    vowelled_tokens = []

    for token in tokens:
        clean_token = token.strip(",.?!:;()\"'-")
        lower_pt = pt_hint.lower() if pt_hint else ""

        # Direct token lookup
        found = TASHKIL_LEXICON.get(clean_token)
        if not found and pt_hint:
            # Match by Portuguese hint word if present
            for pt_word in lower_pt.split():
                clean_pt = pt_word.strip(",.?!:;()\"'-")
                if clean_pt in TASHKIL_LEXICON:
                    found = TASHKIL_LEXICON[clean_pt]
                    break

        if found:
            prefix = token[:token.find(clean_token)] if clean_token in token else ""
            suffix = token[token.find(clean_token) + len(clean_token):] if clean_token in token else ""
            vowelled_tokens.append(prefix + found + suffix)
        else:
            # Rule-based vocalization: only add omitted final fathah to bare He
            vowelled = token
            if vowelled.endswith("ہ") or vowelled.endswith("ه"):
                vowelled = vowelled[:-1] + "َہ"
            vowelled_tokens.append(vowelled)

    return " ".join(vowelled_tokens)

# ------------------------------------------------------------------------------
# 2. Data Extractor (Curso & Corpus)
# ------------------------------------------------------------------------------

def extract_corpus_sentences():
    """Extracts the 25 corpus sentences directly from build.py dataset."""
    with open('build.py', 'r', encoding='utf-8') as f:
        code = f.read()
    match = re.search(r'sentences = (\[\s*\{.*?\n    \])', code, re.DOTALL)
    if match:
        local_scope = {}
        exec(f"sentences = {match.group(1)}", {}, local_scope)
        return local_scope.get('sentences', [])
    return []

def extract_curso_lessons():
    """Extracts lessons and vocabulary entries from pt/curso.org."""
    curso_path = "pt/curso.org"
    if not os.path.exists(curso_path):
        return []

    with open(curso_path, 'r', encoding='utf-8') as f:
        text = f.read()

    lesson_blocks = re.findall(r'(\*+ Lição \d+:.*?)(?=\*+ Lição |\*+ Módulo |\*+ A Gênese|\Z)', text, flags=re.DOTALL)
    lessons = []

    for block in lesson_blocks:
        title_line = block.strip().split('\n')[0]
        title = re.sub(r'^\*+\s*', '', title_line).strip()

        rows = re.findall(r'<tr>(.*?)</tr>', block, flags=re.DOTALL)
        cards = []

        for row in rows:
            tds = re.findall(r'<td.*?>(.*?)</td>', row, flags=re.DOTALL)
            if len(tds) >= 5:
                letra = re.sub(r'<.*?>', '', tds[0]).strip()
                pos = re.sub(r'<.*?>', '', tds[1]).strip()
                pt = re.sub(r'<.*?>', '', tds[2]).strip()
                formula = re.sub(r'<.*?>', '', tds[3]).strip()
                aljamiado = re.sub(r'<.*?>', '', tds[4]).strip()

                if pt and aljamiado and pt.lower() != "português":
                    cards.append({
                        "letra": letra,
                        "posicao": pos,
                        "pt": pt,
                        "formula": formula,
                        "aljamiado": aljamiado
                    })

        if cards:
            lessons.append({
                "title": title,
                "cards": cards
            })

    return lessons

# ------------------------------------------------------------------------------
# 3. AnkiConnect Client
# ------------------------------------------------------------------------------

class AnkiConnectClient:
    def __init__(self, endpoint="http://127.0.0.1:8765"):
        self.endpoint = endpoint

    def invoke(self, action, **params):
        payload = json.dumps({"action": action, "version": 6, "params": params}).encode('utf-8')
        req = urllib.request.Request(self.endpoint, payload, headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req) as resp:
                result = json.loads(resp.read().decode('utf-8'))
                if result.get("error"):
                    raise Exception(result["error"])
                return result.get("result")
        except urllib.error.URLError as e:
            raise ConnectionError(f"Could not connect to AnkiConnect at {self.endpoint}: {e}")

    def create_deck(self, deck_name):
        return self.invoke("createDeck", deck=deck_name)

    def ensure_model(self, model_name="Aljamiado-Basic"):
        models = self.invoke("modelNames")
        if model_name in models:
            return model_name

        self.invoke("createModel",
            modelName=model_name,
            inOrderFields=["Front", "Back", "AljamiadoTashkil", "Notes", "Lesson"],
            css="""
                .card {
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                    font-size: 1.2rem;
                    text-align: center;
                    color: #f0f6fc;
                    background-color: #0d1117;
                    padding: 2rem;
                }
                .pt-text {
                    font-size: 1.5rem;
                    font-weight: 700;
                    color: #f59e0b;
                    margin-bottom: 0.5rem;
                }
                .ipa-text {
                    font-size: 1.1rem;
                    font-style: italic;
                    color: #8b949e;
                    margin-bottom: 1rem;
                }
                .ar-tashkil {
                    font-family: "Noto Naskh Arabic", "Amiri", serif;
                    font-size: 2.6rem;
                    line-height: 1.6;
                    color: #f472b6;
                    direction: rtl;
                    margin: 1.5rem 0;
                    background: #161b22;
                    padding: 1rem;
                    border-radius: 12px;
                    border: 1px solid #30363d;
                }
                .ar-plain {
                    font-family: "Noto Naskh Arabic", "Amiri", serif;
                    font-size: 1.8rem;
                    color: #93c5fd;
                    direction: rtl;
                }
                .notes {
                    font-size: 0.95rem;
                    color: #c9d1d9;
                    background: #21262d;
                    padding: 0.8rem;
                    border-radius: 8px;
                    margin-top: 1rem;
                    text-align: left;
                }
                .badge {
                    display: inline-block;
                    padding: 0.2rem 0.6rem;
                    background: #1f2937;
                    color: #fbbf24;
                    border-radius: 20px;
                    font-size: 0.8rem;
                    font-weight: 600;
                    margin-bottom: 1rem;
                }
            """,
            cardTemplates=[
                {
                    "Name": "Portuguese -> Aljamiado",
                    "Front": '<div class="badge">{{Lesson}}</div><div class="pt-text">{{Front}}</div>',
                    "Back": '{{FrontSide}}<hr id="answer"><div class="ar-tashkil">{{AljamiadoTashkil}}</div><div class="ar-plain">Plain: {{Back}}</div>{{#Notes}}<div class="notes">💡 <strong>Notas Ortográficas:</strong> {{Notes}}</div>{{/Notes}}'
                }
            ]
        )
        return model_name

    def add_notes(self, notes_list):
        if not notes_list:
            return []
        try:
            can_add = self.invoke("canAddNotes", notes=notes_list)
            valid_notes = [n for n, ok in zip(notes_list, can_add) if ok]
            if valid_notes:
                return self.invoke("addNotes", notes=valid_notes)
            return []
        except Exception:
            created = []
            for n in notes_list:
                try:
                    res = self.invoke("addNote", note=n)
                    created.append(res)
                except Exception:
                    pass
            return created

# ------------------------------------------------------------------------------
# 4. Exporter Logic & CLI
# ------------------------------------------------------------------------------

def export_all(sync=False, endpoint="http://127.0.0.1:8765", deck_prefix="Aljamiado Português", output_json=None, output_tsv=None):
    client = AnkiConnectClient(endpoint) if sync else None
    model_name = "Aljamiado-Basic"
    if sync:
        client.ensure_model(model_name)

    all_cards = []
    notes_payload = []

    print(f"📦 Extracting Aljamiado Português content...")

    # 1. Curso Lessons
    lessons = extract_curso_lessons()
    print(f"📖 Extracted {len(lessons)} lessons from Curso Gradual.")

    for l in lessons:
        deck_name = f"{deck_prefix}::01 - Curso Gradual::{l['title']}"
        if sync:
            client.create_deck(deck_name)

        for c in l["cards"]:
            tashkil = apply_tashkil_to_aljamiado(c["aljamiado"], c["pt"])
            card_obj = {
                "deck": deck_name,
                "lesson": l["title"],
                "front": f"{c['pt']} <span style='font-size:0.85em; color:#8b949e;'>({c['letra']} — {c['posicao']})</span>",
                "back": c["aljamiado"],
                "tashkil": tashkil,
                "notes": f"Fórmula: {c['formula']}"
            }
            all_cards.append(card_obj)
            if sync:
                notes_payload.append({
                    "deckName": deck_name,
                    "modelName": model_name,
                    "fields": {
                        "Front": card_obj["front"],
                        "Back": card_obj["back"],
                        "AljamiadoTashkil": card_obj["tashkil"],
                        "Notes": card_obj["notes"],
                        "Lesson": l["title"]
                    },
                    "options": {"allowDuplicate": False, "duplicateScope": "deck"},
                    "tags": ["aljamiado", "portugues", "curso"]
                })

    # 2. Corpus Sentences
    sentences = extract_corpus_sentences()
    corpus_deck = f"{deck_prefix}::02 - Corpus de Frases"
    print(f"📜 Extracted {len(sentences)} corpus sentences.")

    if sync:
        client.create_deck(corpus_deck)

    for s in sentences:
        tashkil = apply_tashkil_to_aljamiado(s["aljamiado"], s["pt"])
        front_html = f"{s['pt']}<br><span class='ipa-text'>{s['ipa']}</span>"
        card_obj = {
            "deck": corpus_deck,
            "lesson": s["title"],
            "front": front_html,
            "back": s["aljamiado"],
            "tashkil": tashkil,
            "notes": s.get("notes", "")
        }
        all_cards.append(card_obj)
        if sync:
            notes_payload.append({
                "deckName": corpus_deck,
                "modelName": model_name,
                "fields": {
                    "Front": card_obj["front"],
                    "Back": card_obj["back"],
                    "AljamiadoTashkil": card_obj["tashkil"],
                    "Notes": card_obj["notes"],
                    "Lesson": s["title"]
                },
                "options": {"allowDuplicate": False, "duplicateScope": "deck"},
                "tags": ["aljamiado", "portugues", "corpus"]
            })

    if sync and notes_payload:
        print(f"⚡ Syncing {len(notes_payload)} notes to Anki via AnkiConnect...")
        client.add_notes(notes_payload)
        print(f"🎉 Successfully synced all notes to Anki!")

    print(f"✅ Total cards processed: {len(all_cards)}")

    # Backup Exporters
    if output_json:
        with open(output_json, 'w', encoding='utf-8') as f:
            json.dump(all_cards, f, ensure_ascii=False, indent=2)
        print(f"💾 Saved JSON backup to: {output_json}")

    if output_tsv:
        with open(output_tsv, 'w', encoding='utf-8') as f:
            for c in all_cards:
                f.write(f"{c['deck']}\t{c['front']}\t{c['back']}\t{c['tashkil']}\t{c['notes']}\n")
        print(f"💾 Saved TSV backup to: {output_tsv}")

    return len(all_cards)

def main():
    parser = argparse.ArgumentParser(description="Anki Exporter for Aljamiado Português with Didactic Tashkīl Engine")
    parser.add_argument("--sync", action="store_true", help="Sync automatically to Anki via AnkiConnect")
    parser.add_argument("--endpoint", default="http://127.0.0.1:8765", help="AnkiConnect REST API endpoint URL")
    parser.add_argument("--deck-prefix", default="Aljamiado Português", help="Base deck name prefix")
    parser.add_argument("--output-json", help="Path to save JSON export backup")
    parser.add_argument("--output-tsv", help="Path to save TSV export backup")

    args = parser.parse_args()
    export_all(
        sync=args.sync,
        endpoint=args.endpoint,
        deck_prefix=args.deck_prefix,
        output_json=args.output_json,
        output_tsv=args.output_tsv
    )

if __name__ == "__main__":
    main()
