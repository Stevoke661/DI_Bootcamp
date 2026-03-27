#exs1
import random

def get_words_from_file(file_path):
    """Reads a file and returns a list of words."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # .split() handles spaces and newlines automatically
            words = content.split()
            return words
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []

def get_random_sentence(length):
    """Generates a random sentence from the word list."""
    words_list = get_words_from_file("words.txt")
    
    if not words_list:
        return "No words available to generate a sentence."

    # Select random words and join them
    selected_words = [random.choice(words_list) for _ in range(length)]
    sentence = " ".join(selected_words)
    
    return sentence.lower()

def main():
    print("--- Welcome to the Random Sentence Generator ---")
    print("This program creates a random sentence based on a word list file.\n")

    user_input = input("How long should the sentence be? (Enter a number between 2 and 20): ")

    # Validation
    try:
        length = int(user_input)
        if 2 <= length <= 20:
            result = get_random_sentence(length)
            print(f"\nGenerated Sentence:\n{result}")
        else:
            print("Error: Please enter a number between 2 and 20.")
    except ValueError:
        print("Error: Invalid input. Please enter a whole integer.")

if __name__ == "__main__":
    main()
    
#exs2
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Step 1: Load the JSON string
data = json.loads(sampleJson)

# Step 2: Access the nested “salary” key
salary_value = data["company"]["employee"]["payable"]["salary"]
print(f"The employee's salary is: {salary_value}")

# Step 3: Add the “birth_date” key
# We drill down to the 'employee' level to add the new pair
data["company"]["employee"]["birth_date"] = "1995-05-12"

# Step 4: Save the JSON to a file
file_name = "modified_employee.json"
with open(file_name, "w") as file:
    # indent=4 makes the file human-readable
    json.dump(data, file, indent=4)

print(f"\nSuccess! Modified data saved to {file_name}")