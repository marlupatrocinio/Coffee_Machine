isMachineOn = True
machineMilk= 1000
machineCoffee = 1000
machineWater = 1000
total = 0

def espresso(machineMilk, machineCoffee, machineWater):
    if machineMilk >= 50 and machineCoffee >= 18 and machineWater >= 50:
        print("Here is your espresso ☕️. Enjoy!")
        machineMilk -= 50
        machineCoffee -= 18
        machineWater -= 50
        return machineMilk, machineCoffee, machineWater
    else:
        print("Sorry there is not enough ingredients.")
        return machineMilk, machineCoffee, machineWater
def latte(machineMilk, machineCoffee, machineWater):
    if machineMilk >= 200 and machineCoffee >= 24 and machineWater >= 50:
        print("Here is your latte ☕️. Enjoy!")
        machineMilk -= 200
        machineCoffee -= 24
        machineWater -= 50
        return machineMilk, machineCoffee, machineWater
    else:
        print("Sorry there is not enough ingredients.")
        return machineMilk, machineCoffee, machineWater
def cappuccino(machineMilk, machineCoffee, machineWater):
    if machineMilk >= 100 and machineCoffee >= 24 and machineWater >= 50:
        print("Here is your cappuccino ☕️. Enjoy!")
        machineMilk -= 100
        machineCoffee -= 24
        machineWater -= 50
        return machineMilk, machineCoffee, machineWater
    else:
        print("Sorry there is not enough ingredients.")
        return machineMilk, machineCoffee, machineWater
    
def coinCalculate():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total

def priceCheck(total, userChoice):
    if userChoice == "espresso":
        if total >= 1.50:
            change = total - 1.50
            print(f"Here is ${round(change, 2)} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False
    elif userChoice == "latte":
        if total >= 2.50:
            change = total - 2.50
            print(f"Here is ${round(change, 2)} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False
    elif userChoice == "cappuccino":
        if total >= 3.00:
            change = total - 3.00
            print(f"Here is ${round(change, 2)} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

while isMachineOn:
    userChoice = input ("What would you like? (espresso/latte/cappuccino): \n")
    if userChoice == "espresso":
        total  = coinCalculate()
        priceCheck(total, userChoice)
        if priceCheck(total, userChoice) == True:
            machineMilk, machineCoffee, machineWater = espresso(machineMilk, machineCoffee, machineWater)
    elif userChoice == "latte":
        total = coinCalculate()
        priceCheck(total, userChoice)
        if priceCheck(total, userChoice) == True:
            machineMilk, machineCoffee, machineWater = latte(machineMilk, machineCoffee, machineWater)

    elif userChoice == "cappuccino":
        total = coinCalculate()
        priceCheck(total, userChoice)
        if priceCheck(total, userChoice) == True:
            machineMilk, machineCoffee, machineWater = cappuccino(machineMilk, machineCoffee, machineWater)

    elif userChoice == "report":
        print(f"Water: {machineWater}ml")
        print(f"Milk: {machineMilk}ml")
        print(f"Coffee: {machineCoffee}g")