"""empty message

Revision ID: 8502091fc2e2
Revises: 9e57ed7ea56c
Create Date: 2021-04-08 22:32:31.951347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8502091fc2e2'
down_revision = '9e57ed7ea56c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('government_members', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    op.add_column('governments', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    op.add_column('members', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    op.add_column('parties', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    op.add_column('permissions', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    op.add_column('roles', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('roles', 'deleted_at')
    op.drop_column('permissions', 'deleted_at')
    op.drop_column('parties', 'deleted_at')
    op.drop_column('members', 'deleted_at')
    op.drop_column('governments', 'deleted_at')
    op.drop_column('government_members', 'deleted_at')
    # ### end Alembic commands ###