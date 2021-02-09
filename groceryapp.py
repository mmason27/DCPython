stores = []

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = []
class Item:
    def __init__(self, item, price, quantity):
        self.item = item
        self.price = price
        self.quantity = quantity 

print("\nEnter 1 to add a store. \nEnter 2 to add item to a store.\nEnter 3 to view your shopping list.\nEnter q to quit.")

while True:

    choice = input("Enter your choice:  ")
    if choice == "1":
        store_name = input("Enter store name: ")
        store_address = input("Enter store address: ")
        store = Store(store_name, store_address)
        stores.append(store)
    
    elif choice == "2":
        for index in range(0, len(stores)):
            store = stores[index]
            print(f"{index + 1} {store.name} - {store.address}")
        
        store_choice = int(input("Enter which store you would like to add your items to: "))
        store = stores[store_choice - 1]
        item = input("Enter the item:  ")
        price = input("Enter the price: ")
        quantity = input("Enter the quantity: ")
        new_item = Item(item, price, quantity)
        store.items.append(new_item)

    elif choice == "3": 
        for store in stores:
            print(f'{store.name} {store.address}')
            for item in store.items:
                print(f"{item.item} - ${item.price}")

    elif choice == "q":
        break 