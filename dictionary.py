import requests
import pandas as pd
from openpyxl.workbook import Workbook
# import

words = []
phonetics = []
partofspeeches = []
defenitions = []
synonyms = []

# def end():
        
    
def check():
    word_ask = input("Enter the word to be checked: ")
    endpoint = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word_ask}"

    data = requests.get(endpoint).json()
    global word_ddisplay
    # global word_phonetic
    global word_part
    global word_defenition
    # global words
    # global phonetics
    # global partofspeeches
    # global defenitions
    # global synonyms
    global word_synonym_1
    global word_synonym_2
    global word_synonym_3

    word_ddisplay = data[0]["word"]
    # word_phonetic = data[0]["phonetic"]
    word_part = data[0]["meanings"][0]["partOfSpeech"]
    word_defenition = data[0]["meanings"][0]["definitions"][0]["definition"]
    word_synonym_1 = data[0]["meanings"][0]["synonyms"][0]
    # word_synonym_2 = data[0]["meanings"][0]["synonyms"][1]
    # word_synonym_3 = data[0]["meanings"][0]["synonyms"][2]
    
    words.append(word_ddisplay)
    # phonetics.append(word_phonetic)
    partofspeeches.append(word_part)
    defenitions.append(word_defenition)
    synonyms.append(word_synonym_1)
    # synonyms.append(word_synonym_2)
    if word_ask == "stop":
        panda_data = {
            "Word": words,
            "Part Of Speech": partofspeeches,
    # "Phonetic": phonetics,
            "Defenition": defenitions,
            "Synonyms": synonyms
}

        real_data = pd.DataFrame(panda_data)
        file_path = "C:/Users/Basavaprabhu Ani/Desktop"
        name = input("What do you want to name the file? ")
        real_data.to_excel(f"{file_path}/{name}.xlsx", sheet_name=name, engine="openpyxl")

    else:
        check()

check()






