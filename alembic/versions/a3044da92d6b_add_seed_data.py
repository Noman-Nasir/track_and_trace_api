"""Add seed data

Revision ID: a3044da92d6b
Revises: 66cd75022ac5
Create Date: 2024-07-13 10:59:18.908613

"""
from typing import Sequence, Union

from alembic import op

from db.models import Article, OrderArticles, Order

# revision identifiers, used by Alembic.
revision: str = 'a3044da92d6b'
down_revision: Union[str, None] = '66cd75022ac5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.bulk_insert(
        Article.__table__,
        [
            dict(sku="LP123", name="Laptop", price="800"),
            dict(sku="MO456", name="Mouse", price="25"),
            dict(sku="MT789", name="Monitor", price="200"),
            dict(sku="KB012", name="Keyboard", price="50"),
            dict(sku="LP345", name="Laptop", price="900"),
            dict(sku="HP678", name="Headphones", price="100"),
            dict(sku="SP901", name="Smartphone", price="500"),
            dict(sku="CH234", name="Charger", price="20"),
        ]
    )

    op.bulk_insert(
        Order.__table__,
        [
            dict(tracking_number="TN12345678", carrier="DHL", sender_address="Street 1, 10115 Berlin, Germany",
                 receiver_address="Street 10, 75001 Paris, France", status="in-transit"),
            dict(tracking_number="TN12345679", carrier="UPS", sender_address="Street 2, 20144 Hamburg, Germany",
                 receiver_address="Street 20, 1000 Brussels, Belgium", status="inbound-scan"),
            dict(tracking_number="TN12345680", carrier="DPD", sender_address="Street 3, 80331 Munich, Germany",
                 receiver_address="Street 5, 28013 Madrid, Spain", status="delivery"),
            dict(tracking_number="TN12345681", carrier="FedEx", sender_address="Street 4, 50667 Cologne, Germany",
                 receiver_address="Street 9, 1016 Amsterdam, Netherlands", status="transit"),
            dict(tracking_number="TN12345682", carrier="GLS", sender_address="Street 5, 70173 Stuttgart, Germany",
                 receiver_address="Street 15, 1050 Copenhagen, Denmark", status="scanned"),
        ]
    )

    op.bulk_insert(
        OrderArticles.__table__,
        [
            dict(tracking_number="TN12345678", article_sku="LP123", article_quantity=1),
            dict(tracking_number="TN12345678", article_sku="MO456", article_quantity=1),
            dict(tracking_number="TN12345679", article_sku="MT789", article_quantity=2),
            dict(tracking_number="TN12345680", article_sku="KB012", article_quantity=1),
            dict(tracking_number="TN12345680", article_sku="MO456", article_quantity=1),
            dict(tracking_number="TN12345681", article_sku="LP345", article_quantity=1),
            dict(tracking_number="TN12345681", article_sku="HP678", article_quantity=1),
            dict(tracking_number="TN12345682", article_sku="SP901", article_quantity=1),
            dict(tracking_number="TN12345682", article_sku="CH234", article_quantity=1),
        ]
    )


def downgrade() -> None:
    op.execute("DELETE FROM articles")
    op.execute("DELETE FROM orders")
    # order_articles entries will be removed as we have set ondelete to CASCADE
