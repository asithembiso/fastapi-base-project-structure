from sqlalchemy.orm import Session
from app.models.item import Item as ItemModel
from app.schemas.item import Item as ItemSchema


def get_item(db: Session, item_id: int):
    return db.query(ItemModel).filter(ItemModel.id == item_id).first()


def create_item(db: Session, item: ItemSchema):
    db_item = ItemModel(id=item.id, name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
