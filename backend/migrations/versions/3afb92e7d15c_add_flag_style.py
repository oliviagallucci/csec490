"""add flag style

Revision ID: 53d97f1cad27
Revises: 06d1c613adde
Create Date: 2024-04-04 21:20:57.085080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3afb92e7d15c'
down_revision = '06d1c613adde'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('flags', schema=None) as batch_op:
        batch_op.add_column(sa.Column('style', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():

    with op.batch_alter_table('flags', schema=None) as batch_op:
        batch_op.drop_column('style')

    # ### end Alembic commands ###
