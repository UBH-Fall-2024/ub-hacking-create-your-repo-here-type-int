from deep_translator import GoogleTranslator

def ChooseLanguage():
    language = input("")

def translatetext(text):
    translated = GoogleTranslator(source='auto', target='de').translate(text)  # output -> Weiter so, du bist großartig

    