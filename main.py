from prettytable import PrettyTable
import random

bazaar_ms = PrettyTable()
bazaar_ms = PrettyTable(["Item ID", "Item Name", "Cost (Per Unit)", "Item Quantity", "Total Cost"])
#bazaar_ms.add_autoindex("Item Index")
bazaar_ms_search = PrettyTable(["Item ID", "Item Name", "Cost (Per Unit)", "Item Quantity", "Total Cost"])

print("\n----------Welcome to Bazaar----------\n")

def view_bazaar():
    print()
    print(bazaar_ms)

    
def search_bazaar():
    print()
    search = input("Search for item: ")
    for i in bazaar_ms.rows:
        if search in i:
            bazaar_ms_search.add_row(i)
        else:
            print("Item does not exist")
    
    print(bazaar_ms_search)
    bazaar_ms_search.clear_rows()


def add_item():
    print()
    try:
        item_name = input("Enter item name: ")
        item_cost = float(input("Enter item cost (per unit): "))
        item_quantity = int(input("Enter quantity: "))
        total_cost = item_cost + item_quantity
        gen = random.randint(0000000, 999999)
        item_id = item_name[0:2].upper() + str(gen)
        bazaar_ms.add_row([f"{item_id}", f"{item_name}", f"{item_cost:.2f}", f"{item_quantity}", f"{total_cost:.2f}"])
    
    except ValueError:
        print("Incorrect Entry, returning to menu")
    
def remove_item():
    pass

     
while True:
    try:
        menu = int(input("Select options:\n" +
                         "1. View Bazaar\n" +
                         "2. Search Bazaar\n" +
                         "3. Add Item\n" +
                         "4. Remove Item\n" +
                         "5. Exit Bazaar\n"))
    
        if menu == 1:
            view_bazaar()
        elif menu == 2:
            search_bazaar()
        elif menu == 3:
            add_item()
        elif menu == 4:
            remove_item()
        elif menu == 5:
            print("Goodbye")
            break
        else:
            print("Try again!\n")

    except ValueError:
        print("Try again!\n")
