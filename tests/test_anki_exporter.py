#!/usr/bin/env python3
"""
Unit tests for anki_exporter.py
"""

import unittest
from anki_exporter import apply_tashkil_to_aljamiado, extract_curso_lessons, extract_corpus_sentences, TASHKIL_LEXICON

class TestAnkiExporter(unittest.TestCase):
    def test_tashkil_omitted_vowels_only(self):
        # Verify that long vowels like Waw, Alif, Ye are not overlaid with redundant diacritics
        # while omitted short internal vowels receive Tashkīl
        cidade_tashkil = apply_tashkil_to_aljamiado("چددہ", "cidade")
        self.assertIn("چِ", cidade_tashkil)  # Kasrah on omitted short i
        self.assertIn("دَ", cidade_tashkil)  # Fathah on omitted short a

        verdade_tashkil = apply_tashkil_to_aljamiado("ورددہ", "verdade")
        self.assertIn("وَرْ", verdade_tashkil) # Sukūn on r, Fathah on v

    def test_corpus_extraction(self):
        sentences = extract_corpus_sentences()
        self.assertGreaterEqual(len(sentences), 25)
        self.assertEqual(sentences[0]["id"], 1)
        self.assertIn("que", sentences[0]["pt"].lower())

    def test_curso_extraction(self):
        lessons = extract_curso_lessons()
        self.assertGreaterEqual(len(lessons), 7)
        first_lesson = lessons[0]
        self.assertTrue("Lição 1" in first_lesson["title"])
        self.assertGreater(len(first_lesson["cards"]), 0)

if __name__ == "__main__":
    unittest.main()
