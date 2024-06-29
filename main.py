# Money counter for Mars: Terraformed
import os

income = 0
bank = 0
teraforming_rate = 20

print("Welcome to Mars: Terraformed!")
income = int(input("How much income do you have from pregame? "))
bank = int(input("How much money did you get from pregame? "))
os.system('clear')
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