import os

print("=== SIMPLE ATM ===")

balance = 1000

while True:
    print("\n1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")

    try:
        choice = int(input("Enter choice: "))

        match choice:
            case 1:
                os.system("cls")
                print("=== SIMPLE ATM ===\n\n")
                print("Balance:", balance)

            case 2:

                os.system("cls")

                while True:
                    
                    print("=== SIMPLE ATM ===\n\n")

                    print("Current balance: ", balance)

                    amount = int(input("\nEnter amount to withdraw: "))

                    if amount <= 0:
                        os.system("cls")
                        print("\nInvalid amount!\n  ")

                    elif amount > balance:
                        os.system("cls")

                        print("Not enough balance! Enter a smaller amount.\n\n")

                    else:
                        balance = balance - amount

                        os.system("cls")

                        print("Withdraw successful!")
                        print("New balance:", balance)

                        print("\n\n=== SIMPLE ATM ===\n")

                        break

            case 3:
                os.system("cls")
                print("Thank you!")
                break

            case _:
                os.system("cls")
                print("=== SIMPLE ATM ===\n\n")
                print("Invalid option!")

    except:
        os.system("cls")
        print("Invalid input! Please enter numbers only.")