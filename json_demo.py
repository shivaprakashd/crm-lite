import json

customer = {
    "customer_id": 1001,
    "name": "Ravi Kumar",
    "mobile": "9876543210",
    "village": "Thiruvannamalai"
}

with open("customer.json", "w") as file:
    json.dump(customer, file, indent=4)

print("Customer saved")