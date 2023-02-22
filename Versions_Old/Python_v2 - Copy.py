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


def fish_catagory_function ():
    fish_catagory = int(input("Would you like a deluxe or a cheaper fish?"))
    if fish_catagory > 2 and fish_catagory < 0:
        pass



def fish_order_function():
    while True:
        try:
            fish_index = int(input("What fish would you like?"))
        except ValueError:
            print("Please select a valid fish")
            continue

        if fish_index in range(len(cheap_fish[index_for_name])-1):
            print("Please select a valid fish")
        else:
            break

    print("Fish 1: " + str(fish_index))
    print("Fish 1 Name: " + cheap_fish[index_for_name][fish_index - 1] + ", Fish 1 Price: $" + str(cheap_fish[index_for_price][fish_index - 1]))


fish_order_function()