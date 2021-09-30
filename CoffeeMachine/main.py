from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO 1 : Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def orderFunc():
    order = input("What would you like? (espresso/latte/cappuccino):")
    if order == "espresso" or order == "latte" or order == "cappuccino":
        return order
    elif order == "report":
        resource()
        orderFunc()
    elif order == "off":  # TODO 2: Turn off the Coffee Machine by entering “off” to the prompt
        return "off"
    else:
        print("Sorry, Try Again.")
        orderFunc()


def resource():  # TODO 3: Print report of resources
    print('\nReport:')
    print(
        f'{resources["water"]} ml of water,\n{resources["milk"]} ml of milk, \n{resources["coffee"]} grams of coffee.\n ')


# TODO 4: Check if rescources are sufficiant
def checkResourceAvaliable(order):
    currentResourceList = [float(resources["water"]), float(resources["coffee"]), float(resources["milk"])]
    orderResorceList = [float(MENU[order]["ingredients"]["water"]), float(MENU[order]["ingredients"]["coffee"]),float(MENU[order]["ingredients"]["milk"])]
    for i in range(3):
        if currentResourceList[i] < orderResorceList[i]:
            print("soz, no beannnnz")
            return False
    print("Resources Avaliabubble")
    return True


# TODO 5: Proscess coins

# TODO 6:Check transaction successful?

# TODO 7: Make Coffee

def moneyCalc(order):
    purchaseDone = False
    while not purchaseDone:
        price = MENU[order]["cost"]
        quartNum = float(input('how many quarters?')) * 0.25
        dimeNum = float(input('how many dimes?')) * 0.1
        nickNum = float(input('how many nickles?')) * 0.05
        penNum = float(input('how many pennies?')) * 0.01
        totalCoins = quartNum + dimeNum + nickNum + penNum
        if totalCoins == price:
            print('Bang on Brotendo')
            purchaseDone = True
        elif totalCoins > price:
            print(f'your change is ${totalCoins - price}')
            purchaseDone = True
        elif totalCoins < price:
            print("you need to put in more money!")

machineon = True
while machineon:
    order = orderFunc()
    if order == "off":
        print("goodnight")
        machineon = False
    elif checkResourceAvaliable(order):
        print('\nTime to insert some coins!')  # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
        moneyCalc(order)
        resources['water'] -= MENU[order]["ingredients"]['water']
        resources['milk'] -= MENU[order]["ingredients"]['milk']
        resources['coffee'] -= MENU[order]["ingredients"]['coffee']
        resource()
    else:
        print('sorry we are out of resources, maybe try another drink')
