class ShoppingCart:

    def __init__(self):
        self.items={}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
            print("Item added successfully")
        else:
            self.items[item] = quantity
            print("Item added successfully")

    def remove_item(self,item):
        if item in self.items:
            del self.items[item]
            print("Item removed successfully")
        else:
            print("Item does not exist")

    def update_item(self, item, quantity):
        if item in self.items:
            self.items[item] = quantity
            print("Item updated successfully")
        else:
            print("Item does not exist")

    def check_items(self):
        print("Items in the cart")
        for item, quantity in self.items.items():
            print(f"{item} : {quantity}")
    
    def total_items(self):
        print("Total items in the cart")
        print(sum(self.items.values()))


shopcart= ShoppingCart()

while True:
    print("1. Add item")
    print("2. Remove item")
    print("3. Update item")
    print("4. Check items")
    print("5. Total items")
    print("6. Exit")
    choice= int(input("Enter your choice: "))

    if choice == 1:
        item= input("Enter item: ")
        quantity= int(input("Enter quantity: "))
        shopcart.add_item(item, quantity)

    elif choice == 2:
        item= input("Enter item: ")
        shopcart.remove_item(item)

    elif choice == 3:
        item= input("Enter item: ")
        quantity= int(input("Enter quantity: "))
        shopcart.update_item(item, quantity)

    elif choice == 4:
        shopcart.check_items()

    elif choice == 5:
        shopcart.total_items()

    elif choice == 6:
        break

    else:
        print("Invalid choice")
        continue