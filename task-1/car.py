from main import Backpack

class Car:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        """Add any item to the car (including backpacks)"""
        self.items.append(item)
        
        # Check if it's a backpack object
        if isinstance(item, Backpack):
            print(f"Added backpack with {len(item.items)} items to car")
        else:
            print(f"Added '{item}' to car")
    
    def remove_item(self, item):
        """Remove an item from the car"""
        if item in self.items:
            self.items.remove(item)
            
            # Check if it's a backpack object
            if isinstance(item, Backpack):
                print(f"Removed backpack from car")
            else:
                print(f"Removed '{item}' from car")
        else:
            if isinstance(item, Backpack):
                print("Backpack not found in car")
            else:
                print(f"'{item}' not found in car")
    
    def show_items(self):
        """Display all items in the car"""
        if self.items:
            print("Car contains:")
            for i, item in enumerate(self.items, 1):
                if isinstance(item, Backpack):
                    print(f"  {i}. Backpack with {len(item.items)} items")
                    if item.items:
                        for backpack_item in item.items:
                            print(f"     - {backpack_item}")
                else:
                    print(f"  {i}. {item}")
        else:
            print("Car is empty")

# Create a car
car = Car()

# Create and populate a backpack
backpack = Backpack()
items = ["Water bottle", "Snacks", "Map", "Phone", "Keys"]

print("Creating backpack with items:")
for item in items:
    backpack.add_item(item)

print("\n" + "="*40)

# Add backpack to car
print("Adding backpack to car:")
car.add_item(backpack)

# Add other items to car
print("\nAdding other items to car:")
car.add_item("Spare tire")
car.add_item("Jumper cables")
car.add_item("Emergency kit")

print("\n" + "="*40)
car.show_items()

# Remove items from car
print("\n" + "="*40)
print("Removing items from car:")
car.remove_item("Spare tire")
car.remove_item(backpack)

print("\n" + "="*40) # this line is to help for a better understanding
car.show_items()

# Demonstrate removing items from backpack
print("\n" + "="*40)
print("Removing items from backpack:")
backpack.remove_item("Map")
backpack.remove_item("Phone")

print("\n" + "="*40)
backpack.show_items()