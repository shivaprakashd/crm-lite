import json

from customer import Customer

from customer_repository import (
    load_customers,
    save_customers
)

def display_menu():

    print("\nCRM Lite")
    print("========")
    print("1. Display Customers")
    print("2. Add Customer")
    print("3. Save Customers")
    print("4. Exit")

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

        save_customers(customers)

    elif choice == "4":

        print("Goodbye")
        break

    else:

        print("Invalid choice")