# Import modules
from operator import inv
import time
import sys
import os

# Variables
start_options = [
    "Start Order", "Order Details", "Finish Order", "Cancel Order"
]

details_menu = [
    "For Delivery (+$5)", "For Pick-up", "Frozen (-$1.05 per fish)", "Cooked", "Return to Main Menu"
]

cheap_fish = [
    ["Shark", "Flounder", "Cod", "Gurnet", "Hoki", "Goldfish"],
    [4.10, 4.10, 4.10, 4.10, 4.10, 4.10],
    [7, 7, 7, 7, 7, 7]
]

deluxe_fish = [
    ["Snapper", "Pink Salmon", "Tuna", "Smoked Marlin", "Pufferfish", "Blobfish"],
    [7.20, 7.20, 7.20, 7.20, 7.20, 7.20],
    [7, 7, 7, 7, 7, 7]
]

sides = [
    ["Scoop of Chips"],
    [1.00],
    [84]
]

user_details = [
    "Delivery/Pick-Up", "Cooked/Frozen", "Name", "Number", "Address"
]

user_order = [
    [],
    []
]

yes = {"Y", "YES", "YE", "YEP", "SURE", "YEAH", "YO"}
no = {"N", "NO", "NAH", "NOT", "NAY"}

INDEX_FOR_NAME = 0
INDEX_FOR_PRICE = 1
INDEX_FOR_QUANTITY = 2
INVALID_MENU_ENTRY = "Please select a valid menu option"
PRINTING_WIDTH = 50


# Main menu function
def start_menu():
    # Clear screen
    clear()
    print("Welcome to Freddy's Fast Fish")

    # Print menu
    divider()
    print_array(start_options)
    divider()

    # Ask for menu option
    menu_index = input_checking("Please select an option: ", start_options)
    match menu_index:
        case 1:
            # Call item catagory function
            catagory_input()
        case 2:
            # Call order details function
            order_details()
        case 3:
            # Ask name and number of user
            customer_name = input("What is your name?: ")
            customer_number = input("What is your phone number?: ")

            # Store variables in details list
            user_details[2] = customer_name
            user_details[3] = customer_number

            # Call reciept function
            print_reciept()
        case 4:
            print("Cancelling Order\nPlease come again")

            # Block process for 2 seconds so user can see statement
            time.sleep(2)

            # Closing program
            sys.exit()
        case _:
            # Tell user to input valid entry and re-ask input
            print(INVALID_MENU_ENTRY)


# Item catagory menu function
def catagory_input():
    clear()

    # Tell program user is not yet ordering a side
    ordering_sides = 0
    while True:
        # Show menu and warn user if input is invalid
        try:
            # Print menu
            divider()
            print_array(["Deluxe", "Cheaper", "Sides", "Return to Main Menu"])
            divider()

            # Ask user for menu option
            item_catagory = int(input("Please select a catagory: "))
        except ValueError:
            print(INVALID_MENU_ENTRY)
            continue

        match item_catagory:
            case 1:
                # Call function based on input above with relative menu
                item_order(deluxe_fish)
            case 2:
                item_order(cheap_fish)
            case 3:
                # Tell program that user is ordering a side (for error message)
                ordering_sides = 1
                item_order(sides)
                # Reset variable
                ordering_sides = 0
            case 4:
                start_menu()
            case _:
                print(INVALID_MENU_ENTRY)


# Error checking function
def input_checking(prompt: str, array: list, start_index: int = 1, type = "none"):

    # Loop while input is invalid
    while True:
        try:
            input_index = int(input(prompt))
        except ValueError:
            print(INVALID_MENU_ENTRY, "by entering a valid number")
            continue
        
        # Check if option is in chosen list/menu, if not, display error message and loop
        if input_index not in range(start_index, len(array) + 1):
            if type == "quantity" and ordering_sides = 0:
                print("Please input an integer between 1 and 7")
            if type == "quantity" and ordering_sides = 1:
                print("Please input an integer between 1 and 84")
            else:
                print(INVALID_MENU_ENTRY)
        else:
            return input_index


# Users details function
def order_details():
    while True:
        # Clear screen and print menu
        clear()
        divider()
        print_array(details_menu)
        divider()

        # Ask user for details
        details_index = input_checking(
            "Please select an option: ", details_menu)
        match details_index:
            case 1:
                # Tell user what they input
                print("For Delivery, + $5.00")

                # Ask for user's address
                customer_address = input("What is your address?: ")

                # Store that order is "For Delivery" in details list
                user_details[0] = "For Delivery"

                # Store variables in details list
                user_details[4] = customer_address

                # Block process for 2 seconds so user can see statement
                time.sleep(2)
            case 2:
                print("For Pick up")
                user_details[0] = "For Pick-Up"
                time.sleep(2)
            case 3:
                print("Frozen, - $1.05 per fish")
                user_details[1] = "Frozen"
                time.sleep(2)
            case 4:
                print("Cooked")
                user_details[1] = "Cooked"
                time.sleep(2)
            case 5:
                # Call main menu
                start_menu()
            case _:
                print(INVALID_MENU_ENTRY)


# Function that orders items
def item_order(item_array: list):
    clear()

    # Print menu
    divider()
    print_array_multi([item_array[INDEX_FOR_NAME],
                      format_price(item_array[INDEX_FOR_PRICE])])
    divider()

    # Get index of item from user input based on item array, and store it
    item_index = input_checking(
        "What item would you like? ", item_array[INDEX_FOR_NAME])
    item_name = item_array[INDEX_FOR_NAME][item_index - 1]

    # Check number of chosen item and calculate the amount the user can order
    item_remaining = (item_array[INDEX_FOR_QUANTITY][item_index - 1]) - \
        array_quantity_counter(item_name, user_order[INDEX_FOR_NAME])
    item_amount = input_checking(
        "How many of this item would you like? ", range(item_remaining), 0, "quantity")

    # Get price from array and format as string
    item_price = (item_array[INDEX_FOR_PRICE][item_index - 1])
    price_string = "%.2f" % (item_price * item_amount)

    # Print ordered item and price
    print("Your choice: " + item_name + " x" + str(item_amount) + ", Price: $"
          + price_string)

    # Put ordered item in user's order array
    for each in range(item_amount):
        user_order[INDEX_FOR_NAME].append(item_name)
        user_order[INDEX_FOR_PRICE].append(item_price)


# Counting quantity of item in list function
def array_quantity_counter(key, array: list):
    # Store base quantity
    quantity = 0

    # Loop through each item in the list, if the item is the same as the key then increase quantity
    for item in array:
        if item == key:
            quantity += 1
    return quantity


def price_count_array():
    # Store a base number to start counting on (0 if pickup, 5 if delivery)
    price_change = 0
    if user_details[0] == "For Delivery":
        price_change = 5

    # Loop through each item in the second array
    for item_index in range(len(user_order[INDEX_FOR_PRICE])):
        # Add the price
        price_change += user_order[INDEX_FOR_PRICE][item_index]
   
        # If frozen -$1.05 from each fish ordered
        if user_details[1] == "Frozen" and user_order[INDEX_FOR_NAME][item_index] not in sides[INDEX_FOR_NAME]:
            price_change -= 1.05

    # Format/round price
    total_price = "%.2f" % (price_change)

    # Print total price
    print("Total:" + " " * 37 + "[$" + total_price + "]")


# Format single level list function
def print_array(items: list):

    # For every index for the item in the list
    for index in range(len(items)):

        # Print index and item
        print(f"{index + 1}) {items[index]}")


# Format multi-level list function
def print_array_multi(items: list):
    # For every index fro the first item in list
    for index in range(len(items[0])):

        # Store the index and the first item
        print_item = f"{index + 1}) {items[0][index]}"

        # Store the second item
        print_second_item = f"[{str(items[1][index])}]"

        # Space out according to printing width
        print_spacing = PRINTING_WIDTH - \
            (len(print_item) + len(print_second_item))

        # Print item with correct spacing
        print(print_item + (" " * print_spacing) + print_second_item)


# Format price printing function
def format_price(array: list):
    # Create copy of array so original is unaffected
    formatted_array = array.copy()

    # For each index in the array
    for item_index in range(len(formatted_array)):

        # Add the dollar sign and format the price to 2 decimal places
        formatted_array[item_index] = "$" + \
            ("%.2f" % (formatted_array[item_index]))
    return formatted_array


# Printing reciept function
def print_reciept():
    clear()
    # Make copy of user details
    user_details_copy = user_details.copy()

    # Check if copy has specified detail in it, if not take user back to input for the detail
    if user_details_copy[0] == "Delivery/Pick-Up":
        print("Please input whether your order is for delivery or pick-up")

        # Block process for 2 seconds so user can see statement
        time.sleep(2)
        order_details()

    if user_details_copy[1] == "Cooked/Frozen":
        print("Please input whether your order is to be cooked or frozen")
        time.sleep(2)
        order_details()

    # Check if user has inputed their address for delivery, if not, don't print address
    if user_details_copy[4] == "Address":
        user_details_copy.pop(4)

    print("Your Reciept:")
    divider()

    # Create a new array to store new order (temporary)
    user_order_temp = [
        [],
        []
    ]

    # Loop through the user order
    for each in user_order[INDEX_FOR_NAME]:
        # Check if this item in the order is already in the new array
        is_in = False
        for alread_item in user_order_temp[INDEX_FOR_NAME]:
            if each in alread_item:
                is_in = True
                break
        if is_in:
            continue

        # Get the amount of item using the quantity function
        quantity = array_quantity_counter(each, user_order[INDEX_FOR_NAME])

        # In the new array append the name + "x3" to name index and then append price * quantity to price index
        user_order_temp[INDEX_FOR_NAME].append(each + " x " + str(quantity))
        user_order_temp[INDEX_FOR_PRICE].append(
            user_order[INDEX_FOR_PRICE][user_order[INDEX_FOR_NAME].index(each)] * quantity)

    # Print multiple array
    print_array_multi([user_order_temp[INDEX_FOR_NAME],
                      format_price(user_order_temp[INDEX_FOR_PRICE])])
    price_count_array()
    divider()
    print("Order Details:")
    divider()
    print_array(user_details_copy)
    divider()

    # Ask if order is correct
    while True:
        confirm_order = input("Would you like to continue?: ").upper()
        if confirm_order in yes:
            print("\nThank you for ordering at Freddy's Fast Fish")

            # Block process for 3 seconds and close program
            time.sleep(3)
            sys.exit()
        elif confirm_order in no:
            # Take user back to start menu
            start_menu()
        else:
            print(INVALID_MENU_ENTRY)


# Printing divider function
def divider():
    # Printing divider
    print(PRINTING_WIDTH * "-")


# Clearing sreen function
def clear():
    # Clearing screen
    os.system("cls")


    start_menu()