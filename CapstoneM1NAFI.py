# CAPSTONE MODUL 1 MUHAMMAD NAFI ADZIQ KELAS DATA SCIENCE
# TEMA = PENJUALAN DI TOKO ROTI TRADITIONAL

itemName = ["Bread", "SpicyBread", "SweetBread"]
itemQty = [10,15,20]
itemPrice = [5,10,10]
itemOriginialProducer = ['france', 'england', 'china']
itemFlavour = ['plain', 'spicy', 'sweet']
itemID = ['fraplabread', 'engspispicy', 'chiswesweet']
itemSold = [0,0,0]




# All Function
def instructionList():

    print("\n===== Store Prompt =====")
    print("1. Every Items List\n2. Item Addition\n3. Item Removal\n4. Update Item\n5. Buy An Item\n6. Exit Program")

def ItemsList():

    print("\nindex\t| item name\t| items stock\t| item price\t| item producer\t| item flavour\t| item ID\t| Item Sold".title())
    for i in range(len(itemName)):
        print("{}\t| {:<10}\t| {:<10}\t| ${:<10}\t| {:<10}\t| {:<10}\t| {:<10}\t| {}".
              format((i), itemName[i], itemQty[i],itemPrice[i], itemOriginialProducer[i], itemFlavour[i], itemID[i], itemSold[i]))

def ItemsListAddition():

    while True:
        newItemName = input("\ninput new item name: ".title())
        newItemFlavour = input("input new item flavour: ".title())
        newItemOriginalProducer = input("input new item producer: ".title())
        newItemQty = int(input("input new item qty (numbers): ".title()))
        newItemPrice = int(input("input new item price (numbers): ".title()))
        newItemId = newItemOriginalProducer[:3] + newItemFlavour[:3] + newItemName[:5]
        newItemSold = 0
        
        if newItemId in itemID :
            print("\n\t\t\tDuplicate detected, item not added please retry.")
            break

        itemName.append(newItemName)
        itemQty.append(newItemQty)
        itemPrice.append(newItemPrice)
        itemOriginialProducer.append(newItemOriginalProducer)
        itemFlavour.append(newItemFlavour)
        itemID.append(newItemId)
        itemSold.append(newItemSold)
        break
        
def itemRemoval():

    itemDeletion = int(input("\nPlease choose an index for fruit removal: "))
    del itemName[itemDeletion]
    del itemQty[itemDeletion]
    del itemPrice[itemDeletion]
    del itemOriginialProducer[itemDeletion]
    del itemFlavour[itemDeletion]
    del itemID[itemDeletion]
    del itemSold[itemDeletion]
    print("\n\t\t\t\tdata successfully removed.")

def itemUpdate():

    while True:
       
        itemUpdateInput = int(input("\nchoose an index that needs to be updated: "))
        itemUpdateInputChoose = input("Update All or Update Specific? (all/Specific) ")

        if itemUpdateInputChoose == "specific":

            itemUpdateInputSpesificCase = input("what would you like to update (name/qty/price/producer/flavour): ".lower())

            if itemUpdateInputSpesificCase == "name":

                itemUpdateName = input("Updated version of name: ")
                itemName[itemUpdateInput] = itemUpdateName
                itemUpdateID = itemID[itemUpdateInput][:6] + itemUpdateName [:5]
                itemID[itemUpdateInput] = itemUpdateID.lower()
                updateFinishing = input("update finished?(yes/no):  ")

            elif itemUpdateInputSpesificCase == "qty":

                itemUpdateQty = input("updated version of qty: ")
                itemQty[itemUpdateInput] = itemUpdateQty
                updateFinishing = input("update finished?(yes/no):  ")

            elif itemUpdateInputSpesificCase == "price":

                itemUpdatePrice = input("updated version of price: $")
                itemPrice[itemUpdateInput] = itemUpdatePrice
                updateFinishing = input("update finished?(yes/no):  ")

            elif itemUpdateInputSpesificCase == "producer":

                itemUpdateProducer = input("Updated Item Producer: ")
                itemOriginialProducer[itemUpdateInput] = itemUpdateProducer
                itemUpdateID = itemUpdateProducer [:3] + itemID[itemUpdateInput][4:]
                itemID[itemUpdateInput] = itemUpdateID.lower()
                updateFinishing = input("update finished?(yes/no):  ")

            elif itemUpdateInputSpesificCase == "flavour":

                itemUpdateFlavour = input("Updated Item Flavour: ")
                itemFlavour[itemUpdateInput] = itemUpdateFlavour
                itemUpdateID = itemID[itemUpdateInput][:3] + itemUpdateFlavour[:3] + itemID[itemUpdateInput][6:]
                itemID[itemUpdateInput] = itemUpdateID.lower()
                updateFinishing = input("update finished?(yes/no):  ")

            else:

                print("unknow input")

        elif itemUpdateInputChoose== "all":

            itemUpdateName = input("Updated version of name: ")
            itemName[itemUpdateInput] = itemUpdateName
            itemUpdateQty = input("updated version of qty: ")
            itemQty[itemUpdateInput] = itemUpdateQty
            itemUpdatePrice = input("updated version of price: $")
            itemPrice[itemUpdateInput] = itemUpdatePrice
            itemUpdateProducer = input("Updated Item Producer: ")
            itemOriginialProducer[itemUpdateInput] = itemUpdateProducer
            itemUpdateFlavour = input("Updated Item Flavour: ")
            itemFlavour[itemUpdateInput] = itemUpdateFlavour
            updateFinishing = input("update finished?(yes/no):  ")
            itemUpdateID = itemUpdateProducer[:3] + itemUpdateFlavour[:3] + itemUpdateName[:5]
            itemID[itemUpdateInput] = itemUpdateID
       
        if updateFinishing == "yes":
            break
        print("data successfully updated")

def itemBuy():

    itemCart = []
    cartQty = []
    cartPrice = []
    totalCartPrice = []
    totalPrice = 0
    totalAllPrice = 0
    revenue = 0
        
    def itemCartList():
        print("\nItem Cart:")
        print("Item Name\t| Item Qty\t| Item Price\t| Total Item Price")
        for i in range(len(itemCart)):
            print("{:<10}\t| {:<10}\t| ${:<10}\t| ${}".format(itemCart[i], cartQty[i], cartPrice[i], totalCartPrice[i]))

    while True:

        
        buyIndex = int(input("\nInput Item Index: "))
        buyQty = int(input("Qty: "))
        finishShopping = input("Finish Shopping(yes/no): ")

        if buyQty > int(itemQty[buyIndex]):

            print("not enough quantity, {} only {} left".format(itemName[buyIndex], itemQty[buyIndex]))

        else:

            totalPrice = buyQty*itemPrice[buyIndex]
            itemCart.append(itemName[buyIndex])
            cartQty.append(itemQty[buyIndex])
            cartPrice.append(itemPrice[buyIndex])
            totalCartPrice.append(totalPrice)
            totalAllPrice += totalPrice
            itemQty[buyIndex] -= buyQty
            itemSold[buyIndex] += buyQty

            itemCartList()

        if "yes" in finishShopping:

            while True:
                print("\nPlease pay the following amount: ${}".format(totalAllPrice))
                money = int(input("Please Input Payment Amount: "))
                if money < totalAllPrice:
                    print("\nBalance Is Not Accepted: Not Enough Payment Amount.")
                if money > totalAllPrice:
                    change = money - totalAllPrice
                    revenue += money - change
                    print("\nThank You For Shopping With Us, Your Change is ${}.".format(change))
                    print('Store Revenue for This Purchase: +${}'.format(revenue))
                    break
                elif money == totalAllPrice:
                    revenue += money
                    print("\nPayment Accepted With No Change Left, Thank You For Shopping With Us.")
                    print('Store Revenue for This Purchase: +${}'.format(revenue))
                    break
            break

# Running Code
while True:
    instructionList()
    try:  
        promptInput = int(input("choose prompt according to numbers: "))

        if promptInput == 6:

            print("\nExiting Program...")
            break

        elif promptInput == 1:

            ItemsList()

        elif promptInput == 2:

            ItemsList()
            ItemsListAddition()
            ItemsList()

        elif promptInput == 3:

            ItemsList()
            itemRemoval()
            ItemsList()

        elif promptInput == 4:

            ItemsList()
            itemUpdate()
            ItemsList()

        elif promptInput == 5:

            ItemsList()
            itemBuy()


        else:

            print("\nERROR >>: wrong option, please choose accordingly(1-5)")

    except ValueError:

        print("\n\t\t\tInput error, please input accordingly.".title())

    except IndexError:

        print("\n\t\t\tInvalid index choice, index input is not recognized or too high.")

    

