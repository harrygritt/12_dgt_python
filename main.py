#Cheap fish ($4.10 each): Shark, Flounder, Cod, Gurnet, Hoki, and Goldfish.
#Deluxe Fish ($7.20 each): Snapper, Pink Salmon, Tuna, Smoked Marlin, Pufferfish, Blobfish.
#If Frozen - discount $1.05 per fish item
#If Delivery - plus $5.00 to total cost, ask name, address, and phone no.
#If Pick up - ask name and phone no.
#MAX 7 fish per type, e.g. 7 cod and 7 flounder is acceptable. display nice error if invalid entry.
#At end of order, display names of fish (with price), total cost (display delivery cost), customer name, if cooked or frozen, if chips (plus price), and if for delivery (address and phonoe no.)


import time
import sys

start_options = [
    "Start Order","Order Details","Finish Order"
]

cheap_fish = [
    ["Shark","Flounder","Cod","Gurnet","Hoki","Goldfish"],
    [4.10, 4.10, 4.10, 4.10, 4.10, 4.10],
]

deluxe_fish = [
    ["Snapper","Pink Salmon","Tuna","Smoked Marlin","Pufferfish","Blobfish"],
    [7.20, 7.20, 7.20, 7.20, 7.20, 7.20]
]

sides = [
    ["Scoop of Chips"],
    [1.00]
]

user_order = [
    [],
    []
]

yes = {"Y", "YES", "YE", "YEP", "SURE", "YEAH"}
no = {"N", "NO", "NAH", "NOT", "NAY"}

index_for_name = 0
index_for_price = 1
invalid_entry = "Please select a valid option"
printing_width = 50


def start_menu():
    print("Welcome to Freddy's Fast Fish")
    divider()
    print_array(start_options)
    divider()
    menu_index = input_checking("Please selct an option: ", start_options)
    match menu_index:
            case 1:
                catagory_input()
            case 2:
                order_details()
            case 3:
                print_reciept()
            case _:
                print(invalid_entry)


def catagory_input():
    while True:
        try:
            divider()
            print_array(["Deluxe", "Cheaper", "Sides", "Return to Main Menu"])
            divider()
            fish_catagory = int(input("Would you like a deluxe or a cheaper fish? "))
        except ValueError:
            print(invalid_entry)
            continue
        
        match fish_catagory:
            case 1:
                fish_order(deluxe_fish)
            case 2:
                fish_order(cheap_fish)
            case 3:
                fish_order(sides)
            case 4:
                start_menu()
            case _:
                print(invalid_entry)


def input_checking(prompt: str, array: list, start_index: int = 1):
    while True:
        try:
            input_index = int(input(prompt))
        except ValueError:
            print(invalid_entry)
            continue

        if input_index not in range(start_index, len(array) + 1):
            print(invalid_entry)
        else:
            return input_index


def name_and_number():
    user_name = input("What is your name?: ")
    user_number = input("What is your phone number?: ")


#Prototype atm!!!
def order_details():
    while True:
        delivery_option = input("Would you like your order delivered?: ").upper()
        if delivery_option in yes:
            print("wants delivered")
            print("For delivery")
            print("gimme name address and number + $5 surcharge")
            break
        elif delivery_option in no:
            print("doesnt want delivered")
            print("gimme name and number")
            break
        else:
            print(invalid_entry)
    
    while True:
        frozen_option = input("Would you like your order frozen?: ").upper()
        if frozen_option in yes:
            print("Order is frozen, you get a $1.05 discount per fish")
            start_menu()
        elif frozen_option in no:
            print("Order is to be cooked")
            start_menu()
        else:
            print(invalid_entry)


#Function that orders fish
def fish_order(fish_array: list):
    #Print menu
    divider()
    print_array_multi([fish_array[index_for_name], format_price(fish_array[index_for_price])])
    divider()

    #Get index of fish from user input based on fish array, and store it
    fish_index = input_checking("What item would you like? ", fish_array[index_for_name])
    fish_name = fish_array[index_for_name][fish_index - 1]
    
    #Check number of chosen fish and calculate the amount the user can order
    fish_remaining = 7 - array_quantity_counter(fish_name, user_order[index_for_name])
    fish_amount = input_checking("How many of this item would you like? ", range(fish_remaining), 0)

    #Get price from array and format as string
    item_price = (fish_array[index_for_price][fish_index - 1]) 
    price_string = "%.2f" % (item_price * fish_amount)

    #Print ordered fish and price
    print("Your choice: " + fish_name + " x" + str(fish_amount) + ", Price: $"
         + price_string)

    #Put ordered fish in user's order array
    for each in range(fish_amount):
        user_order[index_for_name].append(fish_name)
        user_order[index_for_price].append(item_price)

    
def array_quantity_counter(key, array: list):
    quantity = 0
    for item in array:
        if item == key:
            quantity += 1
    return quantity


def print_array(items: list):
    for index in range(len(items)):
        print(f"{index + 1}) {items[index]}")


def print_array_multi(items: list):
    for index in range(len(items[0])):
        print_item = f"{index + 1}) {items[0][index]}"
        print_second_item = f"[{str(items[1][index])}]"
        print_spacing = printing_width - (len(print_item) + len(print_second_item))
        print(print_item + (" " * print_spacing) + print_second_item)


def format_price(array: list):
    formatted_array = array.copy()
    for item_index in range(len(formatted_array)):
        formatted_array[item_index] =  "$" + ("%.2f" % (formatted_array[item_index]))
    return formatted_array


def print_reciept():
    divider()
    print("Your Reciept:")
    divider()

    #Create a new array to store new order (temp)
    user_order_temp = [
        [],
        []
    ]

    #Loop through the user order
    for each in user_order[index_for_name]:
        #Check if this item in the order is already in the new array
        is_in = False
        for alread_item in user_order_temp[index_for_name]:
            if each in alread_item:
                is_in = True
                break
        if is_in:
            continue
    
        #Get the amount of item using the quantity function
        quantity = array_quantity_counter(each, user_order[index_for_name])

        #In the new array append the name + "x3" to name index and then append price * quantity to price index
        user_order_temp[index_for_name].append(each + " x " + str(quantity))
        user_order_temp[index_for_price].append(user_order[index_for_price][user_order[index_for_name].index(each)] * quantity)

    # Print multiple array
    print_array_multi([user_order_temp[index_for_name], format_price(user_order_temp[index_for_price])])
    divider()

    #Ask if order is correct
    while True:
        confirm_order = input("Would you like to continue?: ").upper()
        if confirm_order in yes:
            print("\nThank you for ordering at Freddy's Fast Fish")
            time.sleep(3)
            sys.exit()
        elif confirm_order in no:
            #Take user back to start menu 
            start_menu()
        else:
            print(invalid_entry)


def divider():
    print(printing_width * "-")


if __name__ == "__main__":
    start_menu()
    print("max is the best")