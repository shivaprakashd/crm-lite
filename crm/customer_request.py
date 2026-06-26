from pydantic import BaseModel


class CustomerRequest(BaseModel):
    customer_id: int
    name: str
    city: str
    email: str | None = None