"""sluggify

Revision ID: 0e2bb800b3c5
Revises: 3afb92e7d15c
Create Date: 2024-04-04 22:12:20.019748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e2bb800b3c5'
down_revision = '3afb92e7d15c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    
    with op.batch_alter_table('permissions', schema=None) as batch_op:
        batch_op.drop_constraint('permissions_class_id_fkey', type_='foreignkey')
        
    with op.batch_alter_table('flags', schema=None) as batch_op:
        batch_op.drop_constraint('flags_lesson_id_fkey', type_='foreignkey')
        batch_op.drop_column('type')
       
    with op.batch_alter_table('lessons', schema=None) as batch_op:
        batch_op.drop_constraint('lessons_class_id_fkey', type_='foreignkey')
        batch_op.drop_column('uuid')
        
    with op.batch_alter_table('classes', schema=None) as batch_op:
        batch_op.alter_column('slug',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.drop_column('uuid')
        batch_op.create_primary_key('pk_classes', ['slug'])
        
    with op.batch_alter_table('lessons', schema=None) as batch_op:
        batch_op.add_column(sa.Column('slug', sa.String(), nullable=False))
        batch_op.alter_column('class_id',
               existing_type=sa.UUID(),
               type_=sa.String(),
               nullable=False)
        batch_op.create_foreign_key(None, 'classes', ['class_id'], ['slug'])
        batch_op.create_primary_key('pk_lessons', ['slug', 'class_id'])
        
    with op.batch_alter_table('flags', schema=None) as batch_op:
        batch_op.add_column(sa.Column('class_id', sa.String(), nullable=False))
        batch_op.alter_column('lesson_id',
               existing_type=sa.UUID(),
               type_=sa.String(),
               nullable=False)
        batch_op.create_foreign_key('fk_flag_lesson', 'lessons', ['class_id', 'lesson_id'], ['class_id', 'slug'])
        
    with op.batch_alter_table('permissions', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('class_id',
               existing_type=sa.UUID(),
               type_=sa.String(),
               nullable=False)
        batch_op.create_foreign_key(None, 'classes', ['class_id'], ['slug'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('permissions', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('permissions_class_id_fkey', 'classes', ['class_id'], ['uuid'])
        batch_op.alter_column('class_id',
               existing_type=sa.String(),
               type_=sa.UUID(),
               nullable=True)
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(),
               nullable=True)

    with op.batch_alter_table('lessons', schema=None) as batch_op:
        batch_op.add_column(sa.Column('uuid', sa.UUID(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('lessons_class_id_fkey', 'classes', ['class_id'], ['uuid'])
        batch_op.alter_column('class_id',
               existing_type=sa.String(),
               type_=sa.UUID(),
               nullable=True)
        batch_op.drop_column('slug')

    with op.batch_alter_table('flags', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.drop_constraint('fk_flag_lesson', type_='foreignkey')
        batch_op.create_foreign_key('flags_lesson_id_fkey', 'lessons', ['lesson_id'], ['uuid'])
        batch_op.alter_column('lesson_id',
               existing_type=sa.String(),
               type_=sa.UUID(),
               nullable=True)
        batch_op.drop_column('class_id')

    with op.batch_alter_table('classes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('uuid', sa.UUID(), autoincrement=False, nullable=False))
        batch_op.alter_column('slug',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###
