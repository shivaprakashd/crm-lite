from fastapi import FastAPI, HTTPException, status
from crm.customer_request import CustomerRequest
from crm.customer_repository import load_customers, find_customer_by_id
from crm.customer_service import create_customer, DuplicateCustomerException

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
    try:
        customer = create_customer(customer_request)
        return customer
    except DuplicateCustomerException:
        raise HTTPException(
            status_code=409,
            detail="Customer already exists"
        )