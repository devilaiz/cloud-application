"""rename password to password hash

Revision ID: 1d72f41e427b
Revises: fea6b9f64c7b
Create Date: 2026-11-02 17:16:42.473630

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d72f41e427b'
down_revision: Union[str, Sequence[str], None] = 'fea6b9f64c7b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "users",
        "password",
        new_column_name="password_hash",
        existing_type=sa.String(length=255),
        existing_nullable=False
    )

def downgrade() -> None:
    op.alter_column(
        "users",
        "password_hash",
        new_column_name="password",
        existing_type=sa.String(length=255),
        existing_nullable=False
    )
