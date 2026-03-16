branch_id = 2057

user_info = []

def generate_customer_id():
    user_number = len(user_info) + 1
    return f"{branch_id}-{user_number}"

def create_account(name, password):
    customer_id = generate_customer_id()
    user = [customer_id, name, password]
    user_info.append(user)
    print("Account created. Your ID:", customer_id)

def login(customer_id, password):
    for user in user_info:
        if user[0] == customer_id and user[2] == password:
            print("Login successful")
            return True

    print("Invalid Login")
    return False