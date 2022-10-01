import src.ApiTranslator.Exceptions
from src.ApiTranslator._deepLTranslator import DeepLTranslator


class TestTranslationWithDeepL:
    translator_module: DeepLTranslator = None


    def __init__(self):
        self.set_translator_module()

    def set_translator_module(self):
        self.translator_module = DeepLTranslator(target_language_full="ENGLISH", source_language=None)

    def test_translation_in_french_with_auth_env(self):
        self.translator_module.auth()
        assert (self.translator_module.translate(
            "Je suis une phrase en français.") == self.translator_module.translate("I am a sentence in French."))

    def test_translation_in_french_with_auth_failed(self):
        self.translator_module.auth("shouldfailed")
        assert (self.translator_module.translate(
            "Je suis une phrase en français.") == src.ApiTranslator.Exceptions.DeepLAuthKeyWrongException)

    def test_first_translation_in_french_without_auth(self):
        translator_module_to_english = DeepLTranslator(target_language_full="ENGLISH", source_language=None)
        assert (translator_module_to_english.translate(
            "Je suis une phrase en français.") == src.ApiTranslator.Exceptions.DeepLAuthKeyNotSetException)
