from fastapi import FastAPI, HTTPException, status
from crm.customer_request import CustomerRequest
from crm.customer import Customer

from crm.customer_repository import (
    load_customers,
    find_customer_by_id,
    save_customers
)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to CRM Lite API!"}

@app.get("/customers")
def get_customers():

    customers = load_customers()

    return customers

@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):

    customers = load_customers()

    customer = find_customer_by_id(
        customers,
        customer_id
    )

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer

@app.post("/customers", status_code=status.HTTP_201_CREATED)
def add_customer(customer_request: CustomerRequest):

    customers = load_customers()

    existing_customer = find_customer_by_id(
        customers,
        customer_request.customer_id
    )

    if existing_customer is not None:
        raise HTTPException(
            status_code=409,
            detail="Customer already exists"
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