#exs1
def get_full_name(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    
    return full_name.title()

# Testing
print(get_full_name(first_name="john", middle_name="hooker", last_name="lee")) 
# Output: John Hooker Lee
print(get_full_name(first_name="bruce", last_name="lee")) 
# Output: Bruce Lee

#exs2
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': '/'
}

def to_morse(text):
    return " ".join([MORSE_CODE_DICT.get(char.upper(), "") for char in text])

def from_morse(code):
    # Reverse the dictionary
    rev_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    return "".join([rev_dict.get(symbol, " ") for symbol in code.split()])

# Testing
print(to_morse("Hello World")) 
# Output: .... . .-.. .-.. --- / .-- --- .-. .-.. -..

#exs3
def box_printer(*words):
    if not words:
        return

    length = max(len(word) for word in words)
    width = length + 4  # Adding padding and stars

    print("*" * width)
    for word in words:
        print(f"* {word.ljust(length)} *")
    print("*" * width)

# Testing
box_printer("Hello", "World", "in", "reallylongword", "a", "frame")