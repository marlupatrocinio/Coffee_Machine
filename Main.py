isMachineOn = True
machineMilk= 1000
machineCoffee = 1000
machineWater = 1000

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

while isMachineOn:
    userChoice = input ("What would you like? (espresso/latte/cappuccino): \n")
    if userChoice == "espresso":
        machineMilk, machineCoffee, machineWater = espresso(machineMilk, machineCoffee, machineWater)
    elif userChoice == "latte":
        machineMilk, machineCoffee, machineWater = latte(machineMilk, machineCoffee, machineWater)
    elif userChoice == "cappuccino":
        machineMilk, machineCoffee, machineWater = cappuccino(machineMilk, machineCoffee, machineWater)
    elif userChoice == "report":
        print(f"Water: {machineWater}ml")
        print(f"Milk: {machineMilk}ml")
        print(f"Coffee: {machineCoffee}g")