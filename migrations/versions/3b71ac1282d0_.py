"""empty message

Revision ID: 3b71ac1282d0
Revises: 264d806b2387
Create Date: 2021-04-08 22:33:22.017656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b71ac1282d0'
down_revision = '264d806b2387'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('name', sa.String(length=50), nullable=True))
    op.drop_constraint('roles_title_key', 'roles', type_='unique')
    op.create_unique_constraint(None, 'roles', ['name'])
    op.drop_column('roles', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('title', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'roles', type_='unique')
    op.create_unique_constraint('roles_title_key', 'roles', ['title'])
    op.drop_column('roles', 'name')
    # ### end Alembic commands ###
