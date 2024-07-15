"""create orders table

Revision ID: 1f31cf7d2511
Revises: e8834e10f6ef
Create Date: 2024-07-13 10:59:03.018529

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '1f31cf7d2511'
down_revision: Union[str, None] = 'e8834e10f6ef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "orders",
        sa.Column("tracking_number", sa.String, nullable=False, unique=True, index=True, primary_key=True),
        sa.Column("carrier", sa.String, nullable=False),
        sa.Column("sender_address", sa.String, nullable=False),
        sa.Column("receiver_address", sa.String, nullable=False),
        sa.Column("status", sa.String, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("orders")
