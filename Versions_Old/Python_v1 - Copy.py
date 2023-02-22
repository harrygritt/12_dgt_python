#Cheap fish ($4.10 each): Shark, Flounder, Cod, Gurnet, Hoki, and Goldfish.
#Deluxe Fish ($7.20 each): Snapper, Pink Salmon, Tuna, Smoked Marlin, Pufferfish, Blobfish.
#If Frozen - discount $1.05 per fish item
#If Delivery - plus $5.00 to total cost, ask name, address, amnd phone no.
#If Pick up - ask name and phone no.
#MAX 7 fish per type, e.g. 7 cod and 7 flounder is acceptable. display nice error if invalid entry.
#At end of order, display names of fish (with price), total cost (display delivery cost), customer name, if cooked or frozen, if chips (plus price), and if for delivery (address and phonoe no.)



cheap_fish = [
    ["Shark","Flounder","Cod","Gurnet","Hoki","Goldfish"],
    [4.10],
]

deluxe_fish = [
    ["Snapper","Pink Salmon","Tuna","Smoked Marlin","Pufferfish","Blobfish"],
    [7.20]
]

index_for_name = 0
index_for_price = 1


def fish_order_function():
    fish_name = int(input("What fish?"))
    if fish_name > len(cheap_fish[index_for_name]):
        print("Invalid entry")
        fish_order_function()
    print("Fish 1: " + str(fish_name))
    print("Fish 1 Name: " + cheap_fish[index_for_name][fish_name - 1] + ", Fish 1 Price: $" + str(cheap_fish[index_for_price][fish_name - 1]))


fish_order_function()