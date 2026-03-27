#challenge 1
# 1. User Input
word = input("Enter a word: ")

# 2. Creating the Dictionary
letter_indices = {}

for index, char in enumerate(word):
    # Check if the character is already a key
    if char in letter_indices:
        letter_indices[char].append(index)
    else:
        # If not, create a new key with the index inside a list
        letter_indices[char] = [index]

# 3. Output
print(letter_indices)

#challenge 2
def buy_items(items_purchase, wallet):
    # 1. Clean the wallet string
    wallet_amount = int(wallet.replace("$", "").replace(",", ""))
    
    basket = []

    # 2. Iterate through items
    for item, price_str in items_purchase.items():
        # Clean the item price
        price = int(price_str.replace("$", "").replace(",", ""))
        
        # 3. Check affordability
        if wallet_amount >= price:
            basket.append(item)
            wallet_amount -= price # Update the wallet

    # 4. Final Output Logic
    if not basket:
        return "Nothing"
    else:
        return sorted(basket)

# --- Test Case ---
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

print(buy_items(items_purchase, wallet))