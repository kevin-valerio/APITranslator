import src.ApiTranslator.Exceptions
from src.ApiTranslator._deepLTranslator import DeepLTranslator
import unittest
from src.ApiTranslator.Exceptions import DeepLAuthKeyNotSetException
from src.ApiTranslator.Exceptions import DeepLAuthKeyWrongException


class TestTranslationWithDeepL(unittest.TestCase):
    translator_module: DeepLTranslator = None

    def setup_class(cls):
        cls.set_translator_module(cls)

    def set_translator_module(self):
        self.translator_module = DeepLTranslator(target_language_full="ENGLISH", source_language=None)

    def test_translation_in_french_with_auth_env(self):
        self.translator_module.auth()
        self.assertEqual(self.translator_module.translate(
            "Je suis une phrase en français."), self.translator_module.translate("I am a sentence in French."))

    def test_translation_in_french_with_auth_failed(self):
        try:
            self.translator_module.auth("shouldfailed")
        except:
            pass
        try:
            self.translator_module.translate("Je suis une phrase en français.")
        except Exception as e:
            self.assertEqual(e.__class__.__name__, DeepLAuthKeyWrongException().__class__.__name__)

    def test_translation_in_french_without_auth(self):
        self.translator_module.translator_object = None
        try:
            self.translator_module.translate("Je suis une phrase en français.")
        except Exception as e:
            self.assertEqual(e.__class__.__name__, DeepLAuthKeyNotSetException().__class__.__name__)