from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.AddressResponse])
def read_addresses(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve addresses.
    """
    if crud.user.is_superuser(current_user):
        addresses = crud.address.get_multi(db, skip=skip, limit=limit)
    else:
        addresses = crud.address.get_multi_by_owner(
            db=db, user_id=current_user.id, skip=skip, limit=limit
        )
    print(addresses)
    return addresses


@router.post("/", response_model=schemas.AddressResponse)
def create_address(
    *,
    db: Session = Depends(deps.get_db),
    address_in: schemas.AddressCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new addresses.
    """
    address = crud.address.create_with_owner(db=db, obj_in=address_in, user_id=current_user.id)
    return address


@router.put("/{id}", response_model=schemas.AddressResponse)
def update_address(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    address_in: schemas.AddressUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an address.
    """
    address = crud.address.get(db=db, id=id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    if not crud.user.is_superuser(current_user) and (address.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    address = crud.address.update(db=db, db_obj=address, obj_in=address_in)
    return address


@router.get("/{id}", response_model=schemas.AddressResponse)
def read_address(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get address by ID.
    """
    address = crud.address.get(db=db, id=id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    if not crud.user.is_superuser(current_user) and (address.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return address


@router.delete("/{id}", response_model=schemas.AddressResponse)
def delete_address(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an address.
    """
    address = crud.address.get(db=db, id=id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    if not crud.user.is_superuser(current_user) and (address.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    address = crud.address.remove(db=db, id=id)
    return address
