#-*- coding: utf-8 -*-
from iso639 import Lang
import requests
from langdetect import detect
# import sys
# import importlib
# importlib.reload(sys)
# sys.setdefaultencoding('utf-8')

# USE MY MEMORY API TO TRANSLATE
main_text = input("Enter the text you want to convert:")

identify_language = detect(main_text)


convert_language = input("Enter the language you want to convert text to: ")
convert_language_code = Lang(convert_language)
convert_language_real = convert_language_code.pt1

try:
    parameters = {
        "q": main_text,
        "langpair": f"{identify_language}|{convert_language_real}"
    }

    result = requests.get(url="https://api.mymemory.translated.net/get", params=parameters)
    text = result.json()["responseData"][u'translatedText']

    print(f"The translated text is:\n{text}")

except:
    print("Sorry, you did not enter the correct language... Try Again")
