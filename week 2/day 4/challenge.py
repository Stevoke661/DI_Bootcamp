#text class
import string
import re

class Text:
    def __init__(self, text):
        self.text = text

    def _get_words(self):
        """Helper to normalize text and return a list of words."""
        # Lowercase and split to ensure 'The' and 'the' are treated the same
        return self.text.lower().split()

    def word_frequency(self, word):
        words = self._get_words()
        count = words.count(word.lower())
        return count if count > 0 else f"The word '{word}' was not found."

    def most_common_word(self):
        words = self._get_words()
        if not words:
            return None
        
        # Frequency dictionary
        freq_map = {}
        for word in words:
            freq_map[word] = freq_map.get(word, 0) + 1
        
        # Find the max value in the dictionary
        return max(freq_map, key=freq_map.get)

    def unique_words(self):
        words = self._get_words()
        # Using a set to automatically filter duplicates
        return list(set(words))

    @classmethod
    def from_file(cls, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return cls(content)
        except FileNotFoundError:
            return "File not found. Please check the path."
#text modification class
class TextModification(Text):
    def remove_punctuation(self):
        # string.punctuation contains: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        translator = str.maketrans('', '', string.punctuation)
        self.text = self.text.translate(translator)
        return self.text

    def remove_stop_words(self):
        stop_words = {
            "a", "an", "the", "and", "or", "but", "is", "if", "then", 
            "else", "when", "at", "from", "by", "for", "with", "about", 
            "against", "during", "before", "after", "above", "below", "to", "in"
        }
        words = self.text.split()
        filtered_words = [w for w in words if w.lower() not in stop_words]
        self.text = " ".join(filtered_words)
        return self.text

    def remove_special_characters(self):
        # Regex: Keep only alphanumeric characters and spaces
        self.text = re.sub(r'[^a-zA-Z0-9\s]', '', self.text)
        return self.text