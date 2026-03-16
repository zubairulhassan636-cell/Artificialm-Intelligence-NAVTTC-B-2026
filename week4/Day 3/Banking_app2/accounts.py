balance_record = {}

def check_balance(customer_id):
    balance =  balance_record.get(customer_id,0)
    print("Current Balance is :", balance)
    return balance
def deposit(customer_id, amount):
    if customer_id not in balance_record:
        balance_record[customer_id] = 0
        balance_record[customer_id]+=amount
        print("Deposit Successfull")
        print("New Balance is :", balance_record[customer_id])
def withdraw(customer_id, amount):
    balance = balance_record.get(customer_id, 0)
    if balance>=amount:
        balance_record[customer_id]-=amount
        print("Withdrawal Successfull")
        print("Remaining Balance", balance_record.get[customer_id])
    else:
        print("Insufficient Balance")