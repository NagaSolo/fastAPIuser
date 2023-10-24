from .crud_address import address
from .crud_user import user

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.address import Address
# from app.schemas.address import AddressCreate, AddressUpdate

# address = CRUDBase[Address, AddressCreate, AddressUpdate](Address)
