def translate(language):
    translations = {
  'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
  'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
  'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
    }
    def translate_word(word):
        if word.lower() in translations[language]:
            return translations[language][word.lower()]
        else:
            return "Translation not available"
    
    return translate_word

print(translate('spanish'))
