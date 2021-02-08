stores = []

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = []

    def __str__(self):
        return "Store: % s Address: % s" % (self.name, self.address)  

print("Enter 1 to add a store.")
print("Enter 2 to add item to a store.")
print("Enter 3 to view your shopping list.")
print("Enter q to quit.")

while True:

    choice = input("Enter your choice:  ")
    if choice == "1":
        store_name = input("Enter store name: ")
        store_address = input("Enter store address: ")
        store = Store(store_name, store_address)
        stores.append(store)
    
    elif choice == "2":
        for index, value in enumerate(stores):
            print (index + 1, value) 
        store_choice = input("Enter which store you would like to add your items to: ")
        items = input("Enter the item:  ")
        price = input("Enter the price: ")
        quantity = input("Enter the quantity: ")
        store = stores[store_choice] 
        store.items.append(items)

    elif choice == "3": 
        print(stores)