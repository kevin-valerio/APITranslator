# APITranslator
A library that help translating text in Python, with possibility of adding new translation module.

For now, only the DeepL traductor is developed.

## Installation

### Generate and install the package locally

```bash
pip install setuptools
python3 setup.py sdist
python3 -m pip install dist/ApiTranslatorLib-VERSION.tar.gz
```
### Test the package

```bash
pip install pytest
pip install pytest-runner
python3 setup.py pytest
```

## Usage

/!\ Coming soon /!\ , you can see for now the `test/` folder where there is an example.

```python
translator_module_to_english = DeepLTranslator(target_language_full="ENGLISH", source_language=None)
text_in_french : str = translator_module_to_english.translate("Je suis une phrase en français.")
```

## DeepL Configuration
### Get your DeepL API Key
You will need an api key to run the project, go to the https://www.deepl.com/en/pro-api website, and create your account for free

Then, store your API KEY to the .env file as the variable `KEY_DEEPL_API`
