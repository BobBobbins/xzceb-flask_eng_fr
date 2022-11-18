import unittest

from machinetranslation.translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase):
    def test_french_to_english_null(self):
        self.assertEqual(french_to_english(None), "")
        self.assertEqual(french_to_english(""), "")
        self.assertEqual(french_to_english(0), "")

    def test_french_to_english_bonjour(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")


class TestEnglishToFrench(unittest.TestCase):
    def test_english_to_french_null(self):
        self.assertEqual(english_to_french(None), "")
        self.assertEqual(english_to_french(""), "")
        self.assertEqual(english_to_french(0), "")

    def test_english_to_french_hello(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Hello"), "Hello")

