#Cheap fish ($4.10 each): Shark, Flounder, Cod, Gurnet, Hoki, and Goldfish.
#Deluxe Fish ($7.20 each): Snapper, Pink Salmon, Tuna, Smoked Marlin, Pufferfish, Blobfish.
#If Frozen - discount $1.05 per fish item
#If Delivery - plus $5.00 to total cost, ask name, address, amnd phone no.
#If Pick up - ask name and phone no.
#MAX 7 fish per type, e.g. 7 cod and 7 flounder is acceptable. display nice error if invalid entry.
#At end of order, display names of fish (with price), total cost (display delivery cost), customer name, if cooked or frozen, if chips (plus price), and if for delivery (address and phonoe no.)


cheap_fish = [
    ["Shark","Flounder","Cod","Gurnet","Hoki","Goldfish"],
    [4.10, 4.10, 4.10, 4.10, 4.10, 4.10],
]

deluxe_fish = [
    ["Snapper","Pink Salmon","Tuna","Smoked Marlin","Pufferfish","Blobfish"],
    [7.20, 7.20, 7.20, 7.20, 7.20, 7.20]
]



index_for_name = 0
index_for_price = 1
invalid_entry = "Please select a valid option"


def fish_catagory_function():
    while True:
        try:
            divider_function()
            print_array_function(["Deluxe","Cheaper"])
            divider_function()
            fish_catagory = int(input("Would you like a deluxe or a cheaper fish? "))
        except ValueError:
            print(invalid_entry)
            continue
        
        match fish_catagory:
            case 1:
                fish_order_function(deluxe_fish)
            case 2:
                fish_order_function(cheap_fish)
            case _:
                print(invalid_entry)


def input_checking_function(prompt: str, array: list):
    while True:
        try:
            input_index = int(input(prompt))
        except ValueError:
            print(invalid_entry)
            continue

        if input_index not in range(len(array) + 1):
            print(invalid_entry)
        else:
            return input_index

def fish_order_function(fish_array: list):
    divider_function()
    print_array_function(fish_array[index_for_name])
    divider_function()
    fish_index = input_checking_function("What fish woukld you like? ", fish_array[index_for_name])
    fish_amount = input_checking_function("How many of this fish would you like? ", range(7))
    
    item_price = (fish_array[index_for_price][fish_index - 1]) * fish_amount

    price_string = "%.2f" % item_price
    print("Your choice: " + fish_array[index_for_name][fish_index - 1] + " x" + str(fish_amount) + ", Price: $" + price_string)


def print_array_function(items: list):
    for index in range(len(items)):
        print(f"{index + 1}) {items[index]}")


def divider_function():
    print(20 * "-")

if __name__ == "__main__":
    fish_catagory_function()