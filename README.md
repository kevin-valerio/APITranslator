# APITranslator
A library that help translating text in Python, with possibility of adding new translation module.

For now, only the DeepL traductor is available.

## Installation

### Install the dependencies with poetry
```bash
poetry install
```
### Go in your virtualenv
```bash
poetry shell
```

### Generate and install the package locally

```bash
python3 -m build
python3 -m pip install dist/ApiTranslator-VERSION.tar.gz
```
### Test the package

```bash
python3 -m pytest
```

## Usage

For the DeepL translator module

### Construct your first object
```python
from ApiTranslator import DeepLTranslator
trans_module = DeepLTranslator(target_language_full="FRENCH",source_language=None)
```
To know all the language support by the library, check `Language support by the library` lower

### Authentification

#### Auth directly with your key

```python
trans_module.auth("yourkey")
```

#### Auth with a .env key store
```python
trans_module.auth()
```
> **_NOTE:_**  When you call auth() without argument, it will search in the .env file if there is a `KEY_DEEPL_API` key.

#### Get your DeepL API Key
You will need an api key to run the project, go to the https://www.deepl.com/en/pro-api website, and create your account for free

Then, store your API KEY to the .env file as the variable `KEY_DEEPL_API`

### Translate your first sentence

```python
text_in_french :str = trans_module.translate("I'm an English sentence.")
```
> **_NOTE:_** The DeepLModule will try to translate with formality if it supports for the language. To know the list of language support please see https://support.deepl.com/hc/en-us/articles/4406432463762-About-the-formal-informal-feature

## Language support by the library
### DeepL
 ` ['BULGARIAN', 'CZECH', 'DANISH', 'GERMAN', 'GREEK', 'ENGLISH', 'SPANISH', 'ESTONIAN', 'FINNISH', 'FRENCH', 'HUNGARIAN', 'INDONESIAN', 'ITALIAN', 'JAPANESE', 'LITHUANIAN', 'LATVIAN', 'DUTCH', 'POLISH', 'PORTUGUESE', 'ROMANIAN', 'RUSSIAN', 'SLOVAK', 'SLOVENIAN', 'TURKISH', 'SWEDISH', 'CHINESE']`.
