from ApiTranslator.DeepLTranslator import DeepLTranslator


def test_first_translation_in_french():
    translator_module_to_english = DeepLTranslator(target_language_full="ENGLISH", source_language=None)
    assert (translator_module_to_english.translate("Je suis une phrase en français.") == translator_module_to_english.translate("I am a sentence in French."))