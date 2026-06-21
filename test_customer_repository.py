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

test_find_first_customer()
test_find_existing_customer()
test_find_missing_customer()

print("All tests passed")