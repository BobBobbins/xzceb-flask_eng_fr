import unittest

from machinetranslation.translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase):
    def test_french_to_english_null(self):
        self.assertEqual(french_to_english(None), "")
        self.assertEqual(french_to_english(""), "")

    def test_french_to_english_bonjour(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")


class TestEnglishToFrench(unittest.TestCase):
    def test_english_to_french_null(self):
        self.assertEqual(english_to_french(None), "")
        self.assertEqual(english_to_french(""), "")

    def test_english_to_french_hello(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

