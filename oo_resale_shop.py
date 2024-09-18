from typing import Dict


class ResaleShop:

    # What attributes will it need?
    inventory: str
    sell:int
    refurbish: str
    buy:int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    class Store:
        def __init__(self, inventory: str, sell: int, refurbish: int, buy: int):
            self.inventory = inventory  
            self.sell = sell            
            self.refurbish = refurbish  
            self.buy = buy              

        
    # What methods will you need?
   
from typing import Dict, Optional

class ResaleShop:

    def __init__(self):
        self.inventory: Dict[int, Dict] = {}  # to store the computers
        self.itemID = 0  #  keeps track of the next ID for computers

    def buy(self, computer: Dict) -> int:
        self.itemID += 1  # gives the item ID for each new computer
        self.inventory[self.itemID] = computer  # Store the computer in the inventory
        return self.itemID

    def update_price(self, item_id: int, new_price: int):
        if item_id in self.inventory:
            self.inventory[item_id]["price"] = new_price
        else:
            print(f"Item {item_id} not found. Cannot update price.")

def print_inventory(self):
        if self.inventory:
            # For each item, print its details
            for item_id, computer in self.inventory.items():
                print(f'Item ID: {item_id} : {computer}')
        else:
            print("No inventory to display.")

def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id]  # Locate the computer
            year_made = int(computer["year_made"])
            
            # Update the price based on the year the computer was made
            if year_made < 2000:
                computer["price"] = 0  # Too old to sell, donation only
            elif year_made < 2012:
                computer["price"] = 250  # Discounted price for machines 10+ years old
            elif year_made < 2018:
                computer["price"] = 550  # Discounted price for 4-to-10 year old machines
            else:
                computer["price"] = 1000  # Recent machines

            # Update the operating system if a new one is provided
            if new_os is not None:
                computer["operating_system"] = new_os
        else:
            print(f"Item {item_id} not found. Please select another item to refurbish.")

# Example usage
shop = ResaleShop()

# Define a computer to add
computer_1 = {
    "brand": "Dell",
    "model": "XPS 13",
    "price": 1000,
    "specs": {
        "RAM": "16GB",
        "CPU": "Intel i7",
        "Storage": "512GB SSD"
    }
}

# Add the computer to the shop
computer_id = shop.buy(computer_1)
print(f"New computer added with ID: {computer_id}")

# Updating the price of the computer
shop.update_price(computer_id, 900)
print(f"Updated price for item {computer_id}: {shop.inventory[computer_id]['price']}")
