"""Initial migration

Revision ID: 416b05e0d8ee
Revises: 
Create Date: 2022-10-27 18:10:11.061010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '416b05e0d8ee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('clients', sa.Column('ciudad', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('clients', 'ciudad')
    # ### end Alembic commands ###
