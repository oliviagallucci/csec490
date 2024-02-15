"""init

Revision ID: 05871efbe099
Revises: 
Create Date: 2024-02-06 15:52:28.790326

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "05871efbe099"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "organizations",
        sa.Column("uuid", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("slug", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_table(
        "users",
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=True),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("first_name", sa.String(), nullable=True),
        sa.Column("last_name", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("username"),
    )
    op.create_table(
        "classes",
        sa.Column("uuid", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("slug", sa.String(), nullable=True),
        sa.Column("visible", sa.Boolean(), nullable=True),
        sa.Column("organization_id", sa.UUID(), nullable=True),
        sa.ForeignKeyConstraint(
            ["organization_id"],
            ["organizations.uuid"],
        ),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_table(
        "lessons",
        sa.Column("uuid", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("visible", sa.Boolean(), nullable=True),
        sa.Column("config", sa.String(), nullable=True),
        sa.Column("class_id", sa.UUID(), nullable=True),
        sa.ForeignKeyConstraint(
            ["class_id"],
            ["classes.uuid"],
        ),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_table(
        "flags",
        sa.Column("uuid", sa.UUID(), nullable=False),
        sa.Column("type", sa.String(), nullable=True),
        sa.Column("config", sa.String(), nullable=True),
        sa.Column("points", sa.Integer(), nullable=True),
        sa.Column("lesson_id", sa.UUID(), nullable=True),
        sa.ForeignKeyConstraint(
            ["lesson_id"],
            ["lessons.uuid"],
        ),
        sa.PrimaryKeyConstraint("uuid"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("flags")
    op.drop_table("lessons")
    op.drop_table("classes")
    op.drop_table("users")
    op.drop_table("organizations")
    # ### end Alembic commands ###
