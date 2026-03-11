branch_id = 2057
user_info = {}

def generate_customer_id():
    user_number = len(user_info)+1
    return f"{branch_id}-{user_number}"
def create_account(name,password):
    customer_id = generate_customer_id()
    print(customer_id)
    user_info[customer_id] = {
        "name" : name,
        "password" : password}
    print("Account created successfully")
    
def login(customer_id, password):
    if customer_id in user_info:
        if user_info[customer_id]["password"] == password:
            print("Login successfull")
        else:
            print("Invalid password")