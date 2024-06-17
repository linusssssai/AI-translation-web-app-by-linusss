import sys
import translation_agent as ta

# 确保脚本使用UTF-8编码
sys.stdout.reconfigure(encoding='utf-8')

source_lang = "English"
target_lang = "Spanish"
country = "Mexico"
source_text = "Hello, how are you?"

translation = ta.translate(source_lang, target_lang, source_text, country)
print(f"Translated text: {translation}")


import os

import translation_agent as ta


if __name__ == "__main__":
    source_lang, target_lang, country = "English", "Spanish", "Mexico"

    relative_path = "sample-texts/sample-short1.txt"
    script_dir = os.path.dirname(os.path.abspath(__file__))

    full_path = os.path.join(script_dir, relative_path)

    with open(full_path, encoding="utf-8") as file:
        source_text = file.read()

    print(f"Source text:\n\n{source_text}\n------------\n")

    translation = ta.translate(
        source_lang=source_lang,
        target_lang=target_lang,
        source_text=source_text,
        country=country,
    )

    print(f"Translation:\n\n{translation}")
