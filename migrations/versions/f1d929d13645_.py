"""empty message

Revision ID: f1d929d13645
Revises: de425892fb00
Create Date: 2021-07-13 09:22:26.179226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1d929d13645'
down_revision = 'de425892fb00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_lesse', 'cpf_encrypt',
               existing_type=sa.VARCHAR(length=14),
               type_=sa.String(length=255),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_lesse', 'cpf_encrypt',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=14),
               existing_nullable=False)
    # ### end Alembic commands ###