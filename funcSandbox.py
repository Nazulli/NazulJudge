print("Let's try a math function. Ever play WoW?")

def auctionHouseHelper():
    nameOfItem = "NONE"
    priceOfItem = 0
    desiredAmount = 0
    
    print("What's a short name for the item you want to buy?")
    nameOfItem = input("Item name: ")
    print("What's the gold price of the item?")
    priceOfItem = int(input("Price: "))
    print("How many do you want?")
    desiredAmount = int(input("Desired amount: "))
    
    
    while desiredAmount >= 0:
        currentCost = desiredAmount * priceOfItem
        desiredAmount - 1
        print(f'User wants {desiredAmount} more. This currently costs {currentCost}')
        
    
    
auctionHouseHelper()