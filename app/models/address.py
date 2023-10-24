from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Address(Base):
    id = Column(Integer, primary_key=True, index=True)
    line = Column(Integer, index=True)
    postcode = Column(Integer, index=True)
    city = Column(String, index=True)
    state = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="addresses")
