from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.item import Item
from app.crud.item import get_item, create_item
from app.db.session import get_db


router = APIRouter()


@router.post("/items/", response_model=Item)
def create_new_item(item: Item, db: Session = Depends(get_db)):
    db_item = get_item(db, item_id=item.id)
    if db_item:
        raise HTTPException(status_code=400, detail="Item already exists")
    return create_item(db=db, item=item)
