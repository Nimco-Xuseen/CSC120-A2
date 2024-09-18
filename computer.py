class Computer:

    # What attributes will it need?

    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
        self.description= description
        self.processor_type= processor_type
        self.hard_drive_capacity= hard_drive_capacity
        self.memory= memory
        self.operating_system=operating_system
        self.year_made= year_made
        self.price= price


    # What methods will you need?
def buy(computer):
    computer_id = len(inventory) + 1  # Generate a simple ID
    inventory[computer_id] = computer
    return computer_id

def refurbish(computer_id, new_OS):         #refurbishing the computer
    if computer_id in inventory:
        inventory[computer_id].operating_system = new_OS

def print_inventory():          #checking if the inventory is empty
    if not inventory:
        print("Inventory is empty.")
    else:
        for computer_id, computer in inventory.items():
            print(f"ID: {computer_id}, Description: {computer.description}, "
                  f"OS: {computer.operating_system}, Price: ${computer.price}")

def sell(computer_id):              #selling the computer
    if computer_id in inventory:
        del inventory[computer_id]

def main():                     #adding a computer
    my_computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHz 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    

    