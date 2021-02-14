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

while True:
    print("*****************\nEnter 1 to add a store. \nEnter 2 to add an item.\nEnter 3 to view your shopping list.\nEnter 4 to delete a store.\nEnter 5 to delete an item.\nEnter q to quit.\n*****************")

    try:
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
            
            store_choice = int(input("Enter the store you would like to add your items to: "))
            store = stores[store_choice - 1]
            item = input("Enter the item:  ")
            price = input("Enter the price: ")
            quantity = input("Enter the quantity: ")
            new_item = Item(item, price, quantity)
            store.items.append(new_item)
    
        elif choice == "3": 
            print("Your Shopping List:")
            for store in stores:
                print(f'{store.name} - {store.address}')
                for item in store.items:
                    print(f"{item.item} - ${item.price}")

        elif choice == "4":
            for index in range(0, len(stores)):
                store = stores[index]
                print(f"{index + 1} {store.name} - {store.address}")
            store_index = int(input("Enter the store you would like to delete: "))
            del stores[store_index -1]
            
        elif choice == "5":
            for store in stores:
                for item in store.items:
                    print(f"{index + 1} - {item.item}")
                item_index = input("Enter the item to delete: ")
                store.items.pop(item_index - 1)

        elif choice == "q":
            break
    
    except:
        print("Sorry, invalid input. Please enter another choice.")