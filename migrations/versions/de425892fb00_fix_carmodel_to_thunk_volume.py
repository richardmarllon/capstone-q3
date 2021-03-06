"""fix: carmodel to thunk_volume

Revision ID: de425892fb00
Revises: e2174250b5d9
Create Date: 2021-07-12 16:35:04.468946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de425892fb00'
down_revision = 'e2174250b5d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('car', sa.Column('thunk_volume', sa.Integer(), nullable=True))
    op.drop_column('car', 'trunk_volume')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('car', sa.Column('trunk_volume', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('car', 'thunk_volume')
    # ### end Alembic commands ###
