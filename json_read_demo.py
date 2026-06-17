import json

with open("customer.json", "r") as file:
    customer = json.load(file)

print(customer)

print(customer["name"])

print(customer["village"])