import pydantic

class Address(pydantic.BaseModel):
    country: str
    city: str
    street: str

class User(pydantic.BaseModel):
    first_name: str
    last_name: str
    age: int

class UserWithHome(User):
    address: Address

