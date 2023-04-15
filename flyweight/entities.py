import uuid
import pydantic
import datetime

class Place(pydantic.BaseModel):
    country: str
    city: str
    street: str
    map_url: str | None = None

class Spot(pydantic.BaseModel):
    place: Place
    date: datetime.datetime
    is_active: bool = True
