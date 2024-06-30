# Money counter for Mars: Terraformed
import os

teraforming_rate = 20
# Material counters
bank = 0
income = 0
titan, metal, plants, energy, heat = 0, 0, 0, 0, 0
titan_income, metal_income, plants_income, energy_income, heat_income = 0, 0, 0, 0, 0

print("Welcome to Mars: Terraformed!")
# Ask the user for the pregame stats
income = int(input("How much credit income did you get from pregame? "))
bank = int(input("How much money did you get from pregame? "))
metal_income = int(input("How much metal income did you get from pregame? "))
metal = int(input("How much metal did you get from pregame? "))
titan_income = int(input("How much titan income did you get from pregame? "))
titan = int(input("How much titan did you get from pregame? "))
plants_income = int(input("How much plants income did you get from pregame? "))
plants = int(input("How much plants did you get from pregame? "))
energy_income = int(input("How much energy income did you get from pregame? "))
energy = int(input("How much energy did you get from pregame? "))
heat_income = int(input("How much heat income did you get from pregame? "))
heat = int(input("How much heat did you get from pregame? "))
teraforming_rate += int(input("How much terraforming rate did you get from pregame? "))
# Clear the screen
os.system('clear')

# Main game loop
while True:
    print(f"Current income: {income + teraforming_rate}")
    print(f"Current bank: {bank}")
    # Ask the user what they want to do
    print("What would you like to do?")
    print("1. Increase terraforming rate")
    print("2. Withdraw money from bank")
    print("3. Deposit money into bank")
    print("4. Increase income")
    print("5. Next Generation")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        teraforming_rate += 1;
    elif choice == 2:
        amount = int(input(f"How much would you like to withdraw(current balance: {bank})? "))
        if amount <= bank:
            bank -= amount
        else:
            print("You do not have enough money in the bank!")
    elif choice == 3:
        amount = int(input(f"How much would you like to deposit? "))
        bank += amount
    elif choice == 4:
        income += int(input(f"How much would you like to increase your income? "))
    elif choice == 5:
        bank += (income + teraforming_rate)
        os.system('clear')
        continue