#challenge 2
from googletrans import Translator

# 1. Initialize the translator
translator = Translator()

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

# 2. Use a dictionary comprehension to translate and store results
# We specify src='fr' (French) and dest='en' (English)
translation_dict = {
    word: translator.translate(word, src='fr', dest='en').text 
    for word in french_words
}

print(translation_dict)