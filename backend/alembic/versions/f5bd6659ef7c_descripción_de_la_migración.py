"""Descripción de la migración

Revision ID: f5bd6659ef7c
Revises: 697ff790d380
Create Date: 2024-10-30 14:10:27.418706

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f5bd6659ef7c'
down_revision: Union[str, None] = '697ff790d380'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
