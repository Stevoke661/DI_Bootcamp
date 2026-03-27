#exs1
#resturant menu
{
    "items": [
        {"name": "Vegetable soup", "price": 30},
        {"name": "Hamburger", "price": 44.9},
        {"name": "Milkshake", "price": 22.5},
        {"name": "Artichoke", "price": 18},
        {"name": "Beef stew", "price": 52.5}
    ]
}
#menu manager
import json

class MenuManager:
    def __init__(self):
        with open('restaurant_menu.json', 'r') as f:
            self.menu = json.load(f)

    def add_item(self, name, price):
        new_item = {"name": name, "price": price}
        self.menu["items"].append(new_item)

    def remove_item(self, name):
        for i, item in enumerate(self.menu["items"]):
            if item["name"].lower() == name.lower():
                del self.menu["items"][i]
                return True
        return False

    def save_to_file(self):
        with open('restaurant_menu.json', 'w') as f:
            json.dump(self.menu, f, indent=4)
#manu editor
from menu_manager import MenuManager

def load_manager():
    return MenuManager()

def show_restaurant_menu(manager):
    print("\n--- Current Restaurant Menu ---")
    for item in manager.menu["items"]:
        print(f"{item['name']}: ${item['price']}")

def add_item_to_menu(manager):
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    manager.add_item(name, price)
    print(f"'{name}' was added successfully.")

def remove_item_from_menu(manager):
    name = input("Enter item name to remove: ")
    if manager.remove_item(name):
        print(f"'{name}' was deleted successfully.")
    else:
        print("Error: Item not found.")

def show_user_menu():
    manager = load_manager()
    while True:
        print("\n--- Manager Program Menu ---")
        print("1. View Menu\n2. Add Item\n3. Remove Item\n4. Save & Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            show_restaurant_menu(manager)
        elif choice == '2':
            add_item_to_menu(manager)
        elif choice == '3':
            remove_item_from_menu(manager)
        elif choice == '4':
            manager.save_to_file()
            print("Menu saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    show_user_menu()
    
#exs2
import requests

api_key = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
query = "hilarious"
limit = 10
rating = "g"

# Building the URL with f-strings
url = f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={query}&limit={limit}&rating={rating}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()['data']
    
    # Filter: height > 100
    filtered_gifs = [gif for gif in data if int(gif['images']['original']['height']) > 100]
    
    print(f"Number of gifs received (filtered): {len(filtered_gifs)}")
    # The length should be 10 or less due to the 'limit' parameter
else:
    print("Failed to fetch data.")
    
#exs3
import requests

def get_gifs():
    api_key = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
    user_query = input("Enter a search term for GIFs: ").strip()
    
    search_url = f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={user_query}&limit=10"
    trending_url = f"https://api.giphy.com/v1/gifs/trending?api_key={api_key}&limit=10"
    
    response = requests.get(search_url)
    data = response.json().get('data', [])

    # If query is empty or no results found
    if not user_query or not data:
        print("Couldn't find the requested term. Showing trending GIFs instead.")
        response = requests.get(trending_url)
        data = response.json().get('data', [])

    for gif in data:
        print(f"Title: {gif['title']} | URL: {gif['url']}")

if __name__ == "__main__":
    get_gifs()