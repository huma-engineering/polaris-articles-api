"""empty message

Revision ID: b68beb8b8d96
Revises: 67ebb1e3851f
Create Date: 2018-03-23 12:58:06.305720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b68beb8b8d96'
down_revision = '67ebb1e3851f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('link', sa.Column('url', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('link', 'url')
    # ### end Alembic commands ###
