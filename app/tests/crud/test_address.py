from sqlalchemy.orm import Session

from app import crud
from app.schemas.address import AddressCreate, AddressUpdate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string, random_number, random_state


def test_create_address(db: Session) -> None:
    line = random_lower_string()
    postcode = random_number()
    city = random_lower_string()
    state = random_state()
    address_in = AddressCreate(line=line, postcode=postcode, city=city, state=state)
    user = create_random_user(db)
    address = crud.address.create_with_owner(db=db, obj_in=address_in, user_id=user.id)
    assert address.line == line
    assert address.postcode == postcode
    assert address.city == city
    assert address.state == state
    assert address.user_id == user.id


def test_get_address(db: Session) -> None:
    line = random_lower_string()
    postcode = random_number()
    city = random_lower_string()
    state = random_state()
    address_in = AddressCreate(line=line, postcode=postcode, city=city, state=state)
    user = create_random_user(db)
    address = crud.address.create_with_owner(db=db, obj_in=address_in, user_id=user.id)
    stored_item = crud.address.get(db=db, id=address.id)
    assert stored_item
    assert address.line == line
    assert address.postcode == postcode
    assert address.city == city
    assert address.state == state
    assert address.user_id == user.id


def test_update_item(db: Session) -> None:
    line = random_lower_string()
    postcode = random_number()
    city = random_lower_string()
    state = random_state()
    address_in = AddressCreate(line=line, postcode=postcode, city=city, state=state)
    user = create_random_user(db)
    address = crud.address.create_with_owner(db=db, obj_in=address_in, user_id=user.id)
    line2 = random_lower_string()
    postcode2 = random_number()
    city2 = random_lower_string()
    state2 = random_state()
    address_update = AddressUpdate(line=line2, postcode=postcode2, city=city2, state=state2)
    address2 = crud.address.update(db=db, db_obj=address, obj_in=address_update)
    assert address.id == address2.id
    assert address.line == line2
    assert address.postcode == postcode2
    assert address.city == city2
    assert address.state == state2
    assert address.user_id == user.id


def test_delete_item(db: Session) -> None:
    line = random_lower_string()
    postcode = random_number()
    city = random_lower_string()
    state = random_state()
    address_in = AddressCreate(line=line, postcode=postcode, city=city, state=state)
    user = create_random_user(db)
    address = crud.address.create_with_owner(db=db, obj_in=address_in, user_id=user.id)
    address2 = crud.address.remove(db=db, id=address.id)
    address3 = crud.address.get(db=db, id=address.id)
    assert address3 is None
    assert address2.id == address.id
    assert address2.line == line
    assert address2.postcode == postcode
    assert address2.city == city
    assert address2.state == state
    assert address2.user_id == user.id
