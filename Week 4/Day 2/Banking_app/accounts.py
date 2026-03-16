account_balance = []

def deposit(customer_id, amount):

    for acc in account_balance:
        if acc[0] == customer_id:
            acc[1] += amount
            print("Deposit Successful")
            return

    account_balance.append([customer_id, amount])
    print("Deposit Successful")


def withdraw(customer_id, amount):

    for acc in account_balance:
        if acc[0] == customer_id:

            if acc[1] >= amount:
                acc[1] -= amount
                print("Withdrawal successful")
            else:
                print("Insufficient amount")

            return

    print("Account not found")


def check_balance(customer_id):

    for acc in account_balance:
        if acc[0] == customer_id:
            return acc[1]

    return 0
            