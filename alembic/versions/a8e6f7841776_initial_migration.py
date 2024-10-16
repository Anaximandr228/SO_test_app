"""Initial migration

Revision ID: a8e6f7841776
Revises: 
Create Date: 2024-10-15 14:04:23.492812

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'a8e6f7841776'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_type',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=100), nullable=False),
                    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'),
                              nullable=True),
                    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
                    sa.Column('time_deleted', sa.DateTime(timezone=True), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('product',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'),
                              nullable=True),
                    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
                    sa.Column('time_deleted', sa.DateTime(timezone=True), nullable=True),
                    sa.Column('name', sa.String(length=100), nullable=False),
                    sa.Column('product_type_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['product_type_id'], ['product_type.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    op.drop_table('product_type')
    # ### end Alembic commands ###
