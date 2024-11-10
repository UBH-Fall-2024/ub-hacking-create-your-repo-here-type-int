from deep_translator import GoogleTranslator

def translatetext(text):
    translated = GoogleTranslator(source='auto', target="en").translate(text)  # output -> Weiter so, du bist großartig
    print(translated)

def test1():
    translatetext("أنا أحب علوم الكمبيوتر")

if __name__ == '__main__':
    test1()