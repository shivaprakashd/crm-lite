import json

customers = [
    {
        "customer_id": 1001,
        "name": "Ravi Kumar",
        "mobile": "9876543210"
    },
    {
        "customer_id": 1002,
        "name": "Shivaprakash",
        "mobile": "9999999999"
    }
]

print(type(customers))

with open("customers.json", "w") as file:
    json.dump(customers, file, indent=4)

print("Customers saved")