from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy import exc

from app.crud.base import CRUDBase
from app.models.address import Address
from app.schemas.address import AddressCreate, AddressUpdate


class CRUDAddress(CRUDBase[Address, AddressCreate, AddressUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: AddressCreate, user_id: int
    ) -> Address:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)
        try:
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            return db_obj
        except exc.SQLAlchemyError as e:
            print(f"ERROR is: {e}")

    def get_multi_by_owner(
        self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[Address]:
        return (
            db.query(self.model)
            .filter(Address.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


address = CRUDAddress(Address)
