APP_VERSION = "1.1"

import json

from crm.customer import Customer

from crm.customer_repository import (
    load_customers,
    save_customers,
    find_customer_by_id
)

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def display_menu() -> None:

    print("\nCRM Lite")
    print("========")
    print("1. Display Customers")
    print("2. Add Customer")
    print("3. Search Customer")
    print("4. Save Customers")
    print("5. Update Customers")
    print("6. Delete Customers")
    print("7. Exit")

def display_customers(customers: list[Customer]) -> None:

    print("\nCustomer List")
    print("-------------")

    for customer in customers:
        customer.display()
        
def add_customer(customers: list[Customer]) -> None:

    customer_id = int(input("Enter Customer ID: "))

    existing_customer = find_customer_by_id(
        customers,
        customer_id
    )

    if existing_customer is not None:

        print("Customer ID already exists")
        return
    
    name = input("Enter Name: ")
    city = input("Enter City: ")
    email = input("Enter Email (optional): ").strip() or None

    customer = Customer(
        customer_id,
        name,
        city
    )

    customers.append(customer)

    print("Customer added")

def get_customer_id(prompt: str) -> int:
    while True:
        try:
            return(int(input(prompt)))
        except ValueError:
            print("Invalid input. Please enter a valid customer ID.")

def search_customer(customers: list[Customer]) -> None:
    
    customer_id = get_customer_id("Enter Customer ID to search: ")
    
    customer = find_customer_by_id(
        customers,
        customer_id
    )

    if customer is None:

        print("Customer not found")
        logging.warning(f"Customer with ID {customer_id} not found in the system.")

    else:

        customer.display()    

def update_customer(customers: list[Customer]) -> None:

    customer_id = get_customer_id("Enter Customer ID to update: ")

    customer = find_customer_by_id(
        customers,
        customer_id
    )

    if customer is None:

        print("Customer not found")

    else:

        name = input("Enter new Name: ")
        city = input("Enter new City: ")
        email = input("Enter new Email (optional): ").strip() or None

        customer.name = name
        customer.city = city
        customer.email = email

        print(f"Customer {customer.customer_id} updated")

def delete_customer(customers: list[Customer]) -> None:

    customer_id = get_customer_id("Enter Customer ID to delete: ")

    customer = find_customer_by_id(
        customers,
        customer_id
    )

    if customer is None:

        print("Customer not found")

    else:
    
        customers.remove(customer)
        print(f"Customer {customer.name} deleted")
        logging.info(f"Customer {customer.name} is now deleted")

customers = load_customers()

while True:

    display_menu()

    choice = input("\nEnter choice: ")

    if choice == "1":

        display_customers(customers)

    elif choice == "2":

        add_customer(customers)

    elif choice == "3":

        search_customer(customers)
    
    elif choice == "4":

        save_customers(customers)

    elif choice == "5":

        update_customer(customers)

    elif choice == "6":

        delete_customer(customers)

    elif choice == "7":

        print("Goodbye")
        break

    else:

        print("Invalid choice")