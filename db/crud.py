"""
Orders db CRUD operations
"""
from sqlalchemy.orm import Session

from . import models


def get_order(db: Session, tracking_number: str):
    """
    Fetch order info given tracking number
    """
    return db.query(models.Order).filter(models.Order.tracking_number == tracking_number).one_or_none()


def get_article(db: Session, sku: str):
    """
    Fetch article info given sku
    """
    return db.query(models.Article).filter(models.Article.sku == sku).one_or_none()
