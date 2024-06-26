"""vm_lesson_data

Revision ID: 9a65d8370129
Revises: 06d1c613adde
Create Date: 2024-04-04 20:40:22.453194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a65d8370129'
down_revision = '06d1c613adde'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lesson_vms',
    sa.Column('uuid', sa.UUID(), nullable=False),
    sa.Column('lesson_id', sa.UUID(), nullable=True),
    sa.Column('vm_id', sa.UUID(), nullable=True),
    sa.Column('user', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['lesson_id'], ['lessons.uuid'], ),
    sa.ForeignKeyConstraint(['user'], ['users.username'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    with op.batch_alter_table('flags', schema=None) as batch_op:
        batch_op.add_column(sa.Column('style', sa.String(), nullable=True))
        batch_op.drop_column('type')

    with op.batch_alter_table('lessons', schema=None) as batch_op:
        batch_op.add_column(sa.Column('vm_image', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('vm_flavor', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lessons', schema=None) as batch_op:
        batch_op.drop_column('vm_flavor')
        batch_op.drop_column('vm_image')

    with op.batch_alter_table('flags', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.drop_column('style')

    op.drop_table('lesson_vms')
    # ### end Alembic commands ###
