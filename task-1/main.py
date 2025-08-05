

class Backpack:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
        print(f"Added '{item}' to backpack")
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Removed '{item}' from backpack")
        else:
            print(f"'{item}' not found in backpack")
    
    def show_items(self):
        if self.items:
            print("Backpack contains:")
            for item in self.items:
                print(f"  - {item}")
        else:
            print("Backpack is empty")

# Create a backpack
backpack = Backpack()

# Create 10 backpack items
items = [
    "Notebook", 
    "Pencil", 
    "Laptop", 
    "Pen", 
    "Headphones",
    "Handkerchief", 
    "Charger", 
    "lip gloss", 
    "Water Bottle", 
    "Snack"
]

# Add all 10 items to the backpack
print("Adding items to backpack:")
for item in items:
    backpack.add_item(item)

# show the items in the backpack
print("\n" + "="*40)
backpack.show_items()


# removing items from backpack
print("\n" + "="*40)
print("Removing some items from backpack:")
backpack.remove_item("Charger")
backpack.remove_item("Sunglasses")

# show the items in the backpack
print("\n" + "="*40)
backpack.show_items()