#file 1
class AnagramChecker:
    def __init__(self, file_path):
        """Loads the word list from a file into a set for fast lookup."""
        try:
            with open(file_path, 'r') as file:
                # We use a set for O(1) average lookup time
                self.word_list = {line.strip().lower() for line in file if line.strip()}
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            self.word_list = set()

    def is_valid_word(self, word):
        """Checks if the word exists in our dictionary."""
        return word.lower() in self.word_list

    def is_anagram(self, word1, word2):
        """Core logic: checks if two strings have the same sorted characters."""
        w1 = word1.lower().replace(" ", "")
        w2 = word2.lower().replace(" ", "")
        return sorted(w1) == sorted(w2)

    def get_anagrams(self, word):
        """Finds all anagrams of the given word within the loaded dictionary."""
        word = word.lower()
        anagrams = []
        
        for candidate in self.word_list:
            # A word is not an anagram of itself
            if candidate != word and self.is_anagram(word, candidate):
                anagrams.append(candidate)
        
        return anagrams
    
#file 2
from anagram_checker import AnagramChecker

def main():
    # Initialize the checker with your text file
    checker = AnagramChecker('words.txt')
    
    print("--- Welcome to the Anagram Finder ---")
    
    while True:
        user_input = input("\nEnter a word (or type 'exit' to quit): ").strip()
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
            
        # Validation: Only letters allowed
        if not user_input.isalpha():
            print("⚠️ Please enter a single word containing only letters.")
            continue
            
        # Check validity and find anagrams
        if checker.is_valid_word(user_input):
            print(f"✅ '{user_input}' is a valid English word.")
            
            found_anagrams = checker.get_anagrams(user_input)
            
            if found_anagrams:
                print(f"Anagrams found: {', '.join(found_anagrams)}")
            else:
                print("No anagrams found for this word.")
        else:
            print(f"❌ '{user_input}' is not in the dictionary.")

if __name__ == "__main__":
    main()
