from deep_translator import GoogleTranslator

def translatetext(text):
    translated = GoogleTranslator(source='auto', target='en' '''gui_language_dropdown()''').translate(text)  # source detects a language -> target is whatever user decides (temp english)