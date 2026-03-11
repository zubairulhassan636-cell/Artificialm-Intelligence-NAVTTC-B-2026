import bankcore
import accounts

def main():
    print("Welcome To ABC Bank")
    while True:
        print("1. Create Account")
        print("2. Login account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Check Balance ")
        print("6. Exit")
        
        choice = int(input("Enter choice :"))
        
        if choice == 1:
            name = input("Enter name : ")
            password = input("Enter password :")
            bankcore.create_account(name, password)
        elif choice == 2:
            customer_id = input("Enter customer_id :")
            password = input("Enter password :")
            bankcore.login(customer_id, password)
        elif choice == 3:
            customer_id = input("Enter customer_id :")
            amount = float(input("Enter amount to deposit :"))
            accounts.deposit(customer_id, amount)
        elif choice == 4:
            customer_id = input("Enter customer_id :")
            amount = float(input("Enter amount to withdraw :"))
            accounts.withdraw(customer_id, amount)
        elif choice == 5:
            customer_id = input("Enter customer_id :")
            accounts.check_balance(customer_id)
        elif choice == 6:
            print("Thank you for using ABC Bank")
        else:
            print("Invalid choice")

main()
            
            