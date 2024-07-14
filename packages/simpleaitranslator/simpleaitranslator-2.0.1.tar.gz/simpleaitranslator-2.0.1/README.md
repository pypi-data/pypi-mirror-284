# SimpleAITranslator

## Overview

SimpleAITranslator is a Python library designed to identify the language of a given text and translate text between multiple languages using OpenAI's GPT-4. The library is especially useful for translating text containing multiple languages into a single target language.

## Features

- **Language Detection:** Identify the language of a given text in ISO 639-3 format.
- **Translation:** Translate text containing multiple languages into another language in ISO 639-3 format.

## Requirements

To use this library, you must have an OpenAI API key. This key allows the library to utilize OpenAI's GPT-4 for translation and language detection.

## Installation

You can install the SimpleAITranslator library from PyPI:

```bash
pip install simpleaitranslator
```

## Usage

### Setting Up

Before using the library, set your OpenAI API key:

```python
import os
import simpleaitranslator.translator

# Set your OpenAI API key
simpleaitranslator.translator.OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
# or directly
simpleaitranslator.translator.OPENAI_API_KEY = "<YOUR_OPENAI_API_KEY>"
```

### Language Detection

To detect the language of a given text:

```python
import os
import simpleaitranslator.translator
from simpleaitranslator.translator import get_text_language
simpleaitranslator.translator.OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

print(get_text_language("Hello world"))  # Output: 'eng'
```

### Translation

To translate text containing multiple languages into another language:

```python
import os
import simpleaitranslator.translator
from simpleaitranslator.translator import translate
simpleaitranslator.translator.OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

print(translate("Cześć jak się masz? Meu nome é Adam", "eng"))  # Output: "Hello how are you? My name is Adam"
```


### Full Example

Here is a complete example demonstrating how to use the library:

```python
import os
import simpleaitranslator.translator
from simpleaitranslator.translator import get_text_language, translate

# Set your OpenAI API key
simpleaitranslator.translator.OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Detect language
print(get_text_language("jak ty się nazywasz"))  # Output: 'pol'

# Translate text
print(translate("Cześć jak się masz? Meu nome é Adam", "eng"))  # Output: "Hello how are you? My name is Adam"
```

## Supported Languages

SimpleAITranslator supports all languages supported by GPT-4. For a complete list of language codes, you can visit the [ISO 639-3 website](https://iso639-3.sil.org/code_tables/639/data).

Here are some of the most popular languages and their ISO 639-3 codes:

- English (eng)
- Spanish (spa)
- French (fra)
- German (deu)
- Chinese (zho)
- Japanese (jpn)
- Korean (kor)
- Portuguese (por)
- Russian (rus)
- Italian (ita)
- Dutch (nld)
- Arabic (ara)
- Hindi (hin)
- Bengali (ben)
- Turkish (tur)
- Polish (pol)
- Swedish (swe)
- Norwegian (nor)
- Danish (dan)
- Finnish (fin)
- Greek (ell)
- Hebrew (heb)

## Additional Resources

- [PyPI page](https://pypi.org/project/simpleaitranslator/)
- [ISO 639-3 Codes](https://iso639-3.sil.org/code_tables/639/data)
- [Github project repository](https://github.com/adam-pawelek/SimpleAITranslator)

## License

SimpleAITranslator is licensed under the MIT License. See the LICENSE file for more details.


