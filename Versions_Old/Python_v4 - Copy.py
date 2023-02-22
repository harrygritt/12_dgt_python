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
invalid_entry = ("Please select a valid option")


def fish_catagory_function ():
    while True:
        try:
            print(20 * "-" + "\n 1) Deluxe \n 2) Cheaper")
            fish_catagory = int(input("Would you like a deluxe or a cheaper fish?"))
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


def fish_order_function(fish_array : list):
    while True:
        try:
            fish_index = int(input("What fish would you like?"))
        except ValueError:
            print(invalid_entry)
            continue

        if fish_index not in range(len(fish_array[index_for_name])):
            print(invalid_entry)
        else:
            break

    print("Fish 1: " + str(fish_index))
    print("Fish 1 Name: " + fish_array[index_for_name][fish_index - 1] + ", Fish 1 Price: $" + str(fish_array[index_for_price][fish_index - 1]))


fish_catagory_function()