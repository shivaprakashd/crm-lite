from crm.customer import Customer
from crm.customer_request import CustomerRequest
from crm.customer_repository import (
    load_customers,
    save_customers,
    find_customer_by_id
)


class DuplicateCustomerException(Exception):
    """Raised when attempting to create a customer with a duplicate ID"""
    pass


def create_customer(customer_request: CustomerRequest) -> Customer:
    """
    Create a new customer after checking for duplicates.
    
    Args:
        customer_request: Object with customer_id, name, city, and optional email
        
    Returns:
        Customer: The created customer object
        
    Raises:
        DuplicateCustomerException: If a customer with the same ID already exists
    """
    customers = load_customers()
    
    existing_customer = find_customer_by_id(
        customers,
        customer_request.customer_id
    )
    
    if existing_customer is not None:
        raise DuplicateCustomerException(
            f"Customer with ID {customer_request.customer_id} already exists"
        )
    
    customer = Customer(
        customer_request.customer_id,
        customer_request.name,
        customer_request.city,
        customer_request.email
    )
    
    customers.append(customer)
    save_customers(customers)
    
    return customer
