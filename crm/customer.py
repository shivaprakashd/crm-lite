from dataclasses import dataclass

@dataclass
class Customer:
    customer_id: int
    name: str
    city: str
    email: str | None = None
        
    def display(self):
        print(  
            f"ID: {self.customer_id}, "
            f"Name: {self.name}, "
            f"City: {self.city}"
            f"Email: {self.email if self.email else 'N/A'}"
        )

    @staticmethod
    def from_dict(data: dict) -> 'Customer':
        return Customer(
            data["customer_id"],
            data["name"],
            data["city"],
            data.get("email")
        )
    
    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "city": self.city,
            "email": self.email
        }