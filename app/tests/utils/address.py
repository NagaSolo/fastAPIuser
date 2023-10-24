from typing import Optional

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.address import AddressCreate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string, random_number, random_state


def create_random_address(db: Session, *, user_id: Optional[int] = None) -> models.Address:
    if user_id is None:
        user = create_random_user(db)
        user_id = user.id
    line = random_lower_string()
    postcode = random_number()
    city = random_lower_string()
    state = random_state()
    address_in = AddressCreate(
        line=line, 
        postcode=postcode, 
        city=city, state=state, id=id)
    return crud.address.create_with_owner(db=db, obj_in=address_in, user_id=user_id)
