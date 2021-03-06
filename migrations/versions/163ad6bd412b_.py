"""empty message

Revision ID: 163ad6bd412b
Revises: 80eb5aeeccda
Create Date: 2021-07-15 21:50:03.219184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '163ad6bd412b'
down_revision = '80eb5aeeccda'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('avaliation', sa.Integer(), nullable=True),
    sa.Column('car_id', sa.Integer(), nullable=False),
    sa.Column('lessee_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['car_id'], ['car.id'], ),
    sa.ForeignKeyConstraint(['lessee_id'], ['user_lessee.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('record_locator', sa.Column('user_lesse_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'record_locator', type_='foreignkey')
    op.create_foreign_key('record_locator_user_lesse_id_fkey', 'record_locator', 'user_lesse', ['user_lesse_id'], ['id'])
    op.alter_column('record_locator', 'comment',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
    op.drop_column('record_locator', 'user_lessee_id')
    op.drop_constraint(None, 'car', type_='unique')
    op.create_table('record_lesse',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('comment', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('avaliation', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('car_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('lesse_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['car_id'], ['car.id'], name='record_lesse_car_id_fkey'),
    sa.ForeignKeyConstraint(['lesse_id'], ['user_lesse.id'], name='record_lesse_lesse_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='record_lesse_pkey')
    )
    op.create_table('user_lesse',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=55), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=55), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('city', sa.VARCHAR(length=55), autoincrement=False, nullable=False),
    sa.Column('state', sa.VARCHAR(length=2), autoincrement=False, nullable=False),
    sa.Column('cnh', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('cpf_encrypt', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('password_hash', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_lesse_pkey'),
    sa.UniqueConstraint('cpf_encrypt', name='user_lesse_cpf_encrypt_key'),
    sa.UniqueConstraint('email', name='user_lesse_email_key')
    )
    op.drop_table('record_lessee')
    op.drop_table('user_lessee')
    # ### end Alembic commands ###
