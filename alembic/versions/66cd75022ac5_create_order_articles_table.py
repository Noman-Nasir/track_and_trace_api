"""create order_articles table

Revision ID: 66cd75022ac5
Revises: 1f31cf7d2511
Create Date: 2024-07-13 10:59:09.776653

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '66cd75022ac5'
down_revision: Union[str, None] = '1f31cf7d2511'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "order_articles",
        sa.Column(
            "tracking_number",
            sa.String,
            sa.ForeignKey("orders.tracking_number", ondelete='CASCADE'),
            primary_key=True
        ),
        sa.Column(
            "article_sku",
            sa.String,
            sa.ForeignKey("articles.sku", ondelete='CASCADE'),
            primary_key=True
        ),
        sa.Column(
            "article_quantity",
            sa.Integer,
            nullable=False
        )
    )


def downgrade() -> None:
    op.drop_table("orders")
