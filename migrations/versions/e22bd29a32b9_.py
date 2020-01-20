"""empty message

Revision ID: e22bd29a32b9
Revises: 6158de006cad
Create Date: 2020-01-20 10:43:24.517485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e22bd29a32b9'
down_revision = '6158de006cad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('menu_item', sa.Column('category', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('menu_item', 'category')
    # ### end Alembic commands ###
