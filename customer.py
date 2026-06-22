from dataclasses import dataclass

@dataclass
class Customer:

    customer_id: int
    name: str
    city: str

    def display(self):
        print(  
            f"ID: {self.customer_id}, "
            f"Name: {self.name}, "
            f"City: {self.city}"
        )

    @staticmethod
    def from_dict(data: dict) -> "Customer":
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