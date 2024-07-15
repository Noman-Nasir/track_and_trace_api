"""
SQLAlchemy models
"""
from typing import List

from sqlalchemy import Column, ForeignKey, String, Float
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .database import Base


class OrderArticles(Base):
    """
    Many-to-Many association object for articles and orders
    """
    __tablename__ = "order_articles"
    tracking_number: Mapped[int] = mapped_column(ForeignKey("orders.tracking_number"), primary_key=True)
    article_sku: Mapped[int] = mapped_column(ForeignKey("articles.sku"), primary_key=True)
    article_quantity: Mapped[int]
    article: Mapped["Article"] = relationship(back_populates="orders")
    order: Mapped["Order"] = relationship(back_populates="order_articles")


class Article(Base):
    """
    articles table object
    """
    __tablename__ = "articles"

    sku = Column(String, primary_key=True, nullable=False, unique=True, index=True)
    name = Column(String, index=True)
    price = Column(Float, nullable=False)
    orders: Mapped[List["OrderArticles"]] = relationship(back_populates="article")


class Order(Base):
    """
    orders table object
    """
    __tablename__ = "orders"

    tracking_number = Column(String, nullable=False, unique=True, index=True, primary_key=True)
    carrier = Column(String, nullable=False)
    sender_address = Column(String, nullable=False)
    receiver_address = Column(String, nullable=False)
    status = Column(String, nullable=False)
    order_articles: Mapped[List["OrderArticles"]] = relationship(back_populates="order")
