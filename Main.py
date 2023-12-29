isMachineOn = True #command to control the while loop
machineMilk= 1000 #quantity of milk in the machine
machineCoffee = 1000 #quantity of coffee in the machine
machineWater = 1000 #quantity of water in the machine
total = 0 #total amount of money inserted by the user

def espresso(machineMilk, machineCoffee, machineWater): #function to make espresso
    if machineMilk >= 50 and machineCoffee >= 18 and machineWater >= 50: #check if there is enough ingredients in the machine
        print("Here is your espresso ☕️. Enjoy!")
        machineMilk -= 50
        machineCoffee -= 18
        machineWater -= 50
        return machineMilk, machineCoffee, machineWater #return the new values of the ingredients in the machine
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
        return machineMilk, machineCoffee, machineWater #do i need this line of code?
    
def coinCalculate(): #function to calculate the total amount of money inserted by the user
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01) #calculate the total amount of money inserted by the user
    return total

def priceCheck(total, userChoice): #function to check if the user has inserted enough money
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
        
##all functions are set up. Now the program starts the user interaction
##cann the necessary functions

while isMachineOn:
    userChoice = input ("What would you like? (espresso/latte/cappuccino): \n")
    if userChoice == "espresso":
        total  = coinCalculate()
        priceCheck(total, userChoice)
        if priceCheck(total, userChoice) == True:
            machineMilk, machineCoffee, machineWater = espresso(machineMilk, machineCoffee, machineWater) #update the values of the ingredients in the machine using the return values of the function
        total = 0 #do i need this line of code?
    elif userChoice == "latte":
        total = coinCalculate()
        priceCheck(total, userChoice)
        if priceCheck(total, userChoice) == True:
            machineMilk, machineCoffee, machineWater = latte(machineMilk, machineCoffee, machineWater) #update the values of the ingredients in the machine using the return values of the function
        total = 0
    elif userChoice == "cappuccino":
        total = coinCalculate()
        priceCheck(total, userChoice)
        if priceCheck(total, userChoice) == True:
            machineMilk, machineCoffee, machineWater = cappuccino(machineMilk, machineCoffee, machineWater) #update the values of the ingredients in the machine using the return values of the function
        total = 0
    elif userChoice == "report":
        print(f"Water: {machineWater}ml")
        print(f"Milk: {machineMilk}ml")
        print(f"Coffee: {machineCoffee}g")
    elif userChoice == "off":
        isMachineOn = False #end the application
    else:
        print("Please, enter a valid input.")