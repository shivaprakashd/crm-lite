import json

from customer import Customer

def display_menu():

    print("\nCRM Lite")
    print("========")
    print("1. Display Customers")
    print("2. Add Customer")
    print("3. Exit")

def load_customers():

    with open("customers.json", "r") as file:
        response = json.load(file)

    customer_dicts = response["customers"]

    customers = []

    for customer_data in customer_dicts:
        customer = Customer.from_dict(customer_data)
        customers.append(customer)

    return customers

def display_customers(customers):

    print("\nCustomer List")
    print("-------------")

    for customer in customers:
        customer.display()

def add_customer(customers):

    customer_id = int(input("Enter Customer ID: "))
    name = input("Enter Name: ")
    city = input("Enter City: ")

    customer = Customer(
        customer_id,
        name,
        city
    )

    customers.append(customer)

    print("Customer added")

customers = load_customers()

while True:

    display_menu()

    choice = input("\nEnter choice: ")

    if choice == "1":

        display_customers(customers)

    elif choice == "2":

        add_customer(customers)

    elif choice == "3":

        print("Goodbye")
        break

    else:

        print("Invalid choice")



# import json

# # customers = [
# #     {
# #         "customer_id": 1001,
# #         "name": "Ravi Kumar",
# #         "mobile": "9876543210"
# #     },
# #     {
# #         "customer_id": 1002,
# #         "name": "Shivaprakash",
# #         "mobile": "9999999999"
# #     }
# # ]


# def save_customers():
#     with open("customers.json", "w") as file:
#         json.dump(customers, file, indent=4)


# # save_customers()

# # print("Customers saved")

# def load_customers():
#     with open("customers.json", "r") as file:
#         return json.load(file)


# customers = load_customers()

# for customer in customers:
#     print(customer["customer_id"])
#     print(customer["name"])
#     print(customer["mobile"])
#     print("-----")

# print(type(customers))
# print(type(customers[0]))

# new_customer = {
#     "customer_id": 1003,
#     "name": "Anitha",
#     "mobile": "8888888888"
# }

# customers.append(new_customer)

# save_customers()

# print("New customer added and saved")

