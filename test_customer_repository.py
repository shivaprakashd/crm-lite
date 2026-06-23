from crm.customer import Customer
from crm.customer_repository import find_customer_by_id


def test_find_existing_customer():

    customers = [
        Customer(1, "Shiv", "Bangalore"),
        Customer(2, "Ravi", "Mysore")
    ]

    customer = find_customer_by_id(
        customers,
        2
    )

    assert customer is not None
    assert customer.name == "Ravi"

def test_find_missing_customer():
    customers = [
        Customer(1, "Shiv", "Bangalore"),
        Customer(2, "Ravi", "Mysore")
    ]

    customer = find_customer_by_id(
        customers,
        99
    )

    assert customer is None

def test_find_first_customer():
    customers = [
        Customer(1, "Shiv", "Bangalore"),
        Customer(2, "Ravi", "Mysore")
    ]

    customer = find_customer_by_id(
        customers,
        1
    )

    assert customer is not None
    assert customer.name == "Shiv"

def test_customer_email():
    customer = Customer(1, "Shiv", "Bangalore", email="shivaprakashd@gmail.com")
    assert customer.email == "shivaprakashd@gmail.com"

def test_from_dict_without_email():
    data = {
        "customer_id": 1,
        "name": "Shiv",
        "city": "Bangalore"
    }

    customer = Customer.from_dict(data)

    assert customer.customer_id == 1
    assert customer.name == "Shiv"
    assert customer.city == "Bangalore"
    assert customer.email is None

# test_find_first_customer()
# test_find_existing_customer()
# test_find_missing_customer()

# print("All tests passed")