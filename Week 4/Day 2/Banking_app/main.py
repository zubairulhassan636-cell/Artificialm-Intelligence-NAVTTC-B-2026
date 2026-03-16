import bankcore
import accounts


def banking_menu(customer_id):

    while True:

        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw money")
        print("4. Logout0")

        choice = int(input("Enter choice: "))

        if choice == 1:
            balance = accounts.check_balance(customer_id)
            print("Your Balance is:", balance)

        elif choice == 2:
            amount = int(input("Enter amount to deposit: "))
            accounts.deposit(customer_id, amount)

        elif choice == 3:
            amount = int(input("Enter amount to withdraw: "))
            accounts.withdraw(customer_id, amount)
        elif choice == 4:
            print("Logged out successfully")
            break

        else:
            print("Invalid Option")


def main_menu():

    while True:

        print("\nWelcome to the ABC Bank")
        print("1. Create an account")
        print("2. Login to the Account")
        print("3. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:

            name = input("Enter your name: ")
            password = input("Create password: ")

            bankcore.create_account(name, password)

        elif choice == 2:

            customer_id = input("Enter customer_id: ")
            password = input("Enter password: ")

            if bankcore.login(customer_id, password):
                banking_menu(customer_id)

        elif choice == 3:
            print("Thank you for using ABC Bank")
            break

        else:
            print("Invalid option")


main_menu()