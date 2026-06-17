class Customer:

    def __init__(self, customer_id, name, city):
        self.customer_id = customer_id
        self.name = name
        self.city = city

    def display(self):
        print(
            f"ID: {self.customer_id}, "
            f"Name: {self.name}, "
            f"City: {self.city}"
        )

    @staticmethod
    def from_dict(data):
        return Customer(
            data["customer_id"],
            data["name"],
            data["city"]
        )
    
    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "city": self.city
    }