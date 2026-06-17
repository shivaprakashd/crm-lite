import json

from customer import Customer


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

customers = load_customers()

display_customers(customers)



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

