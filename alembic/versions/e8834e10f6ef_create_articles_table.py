"""create articles table

Revision ID: e8834e10f6ef
Revises: 
Create Date: 2024-07-13 10:58:54.182948

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'e8834e10f6ef'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "articles",
        sa.Column("sku", sa.String, primary_key=True, nullable=False, unique=True, index=True),
        sa.Column("name", sa.String, index=True),
        sa.Column("price", sa.Float, nullable=False)
    )


def downgrade() -> None:
    op.drop_table("articles")
