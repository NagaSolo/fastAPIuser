from typing import Optional

from pydantic import ConfigDict, BaseModel


# Shared properties
class AddressBase(BaseModel):
    line: Optional[str] = None
    postcode: Optional[int] = None
    city: Optional[str] = None
    state: Optional[str] = None


# Properties to receive on address creation
class AddressCreate(AddressBase):
    line: str
    postcode: int
    city: str
    state: str


# Properties to receive on address update
class AddressUpdate(AddressBase):
    line: str
    postcode: int
    city: str
    state: str


# Properties shared by models stored in DB
class AddressInDBBase(AddressBase):
    id: Optional[int] = None
    user_id: int
    model_config = ConfigDict(from_attributes=True)


# Properties to return to client
class AddressResponse(AddressInDBBase):
    pass


# Properties properties stored in DB
class AddressInDB(AddressInDBBase):
    pass
