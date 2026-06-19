import json

from customer import Customer


def load_customers():

    with open("customers.json", "r") as file:
        response = json.load(file)

    customer_dicts = response["customers"]

    customers = []

    for customer_data in customer_dicts:

        customer = Customer.from_dict(
            customer_data
        )

        customers.append(customer)

    return customers


def save_customers(customers):

    customer_dicts = []

    for customer in customers:

        customer_dicts.append(
            customer.to_dict()
        )

    response = {
        "customers": customer_dicts
    }

    with open("customers.json", "w") as file:

        json.dump(
            response,
            file,
            indent=4
        )

    print("Customers saved successfully")