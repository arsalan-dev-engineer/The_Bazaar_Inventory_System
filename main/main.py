from prettytable import PrettyTable
import random

bazaar_ms = PrettyTable()
bazaar_ms.field_names = ["Item ID", "Item Name", "Cost (Per Unit)", "Item Quantity", "Total Cost"]


print("\n----------Welcome to Bazaar----------\n")

def view_bazaar():
    print()
    print(bazaar_ms)

    
def search_bazaar():
    pass


def add_item():
    print()
    item_name = input("Enter item name: ")
    item_cost = float(input("Enter item cost (per unit): "))
    item_quantity = int(input("Enter quantity: "))
    total_cost = item_cost + item_quantity
    gen = random.randint(0000000, 999999)
    item_id = item_name[0:2].upper() + str(gen)
    
    
    bazaar_ms.add_row([f"{item_id}", f"{item_name}", f"{item_cost}", f"{item_quantity}", f"{total_cost}"])
    

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
