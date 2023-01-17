"""v0.8

Revision ID: 0.8
Revises: 0.6
Create Date: 2023-01-17 16:16:33.472422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0.8"
down_revision = "0.6"
branch_labels = None
depends_on = None


event_categories_table = sa.sql.table(
    "event_categs",
    sa.sql.column("id", sa.Integer),
    sa.sql.column("name", sa.String),
    sa.sql.column("description", sa.String),
)


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "st_check_outliers_by_campaigns",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("campaign_id", sa.Integer(), nullable=False),
        sa.Column("is_enabled", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ["campaign_id"],
            ["campaigns.id"],
            name=op.f("fk_st_check_outliers_by_campaigns_campaign_id_campaigns"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_st_check_outliers_by_campaigns")),
        sa.UniqueConstraint(
            "campaign_id", name=op.f("uq_st_check_outliers_by_campaigns_campaign_id")
        ),
    )
    # ### end Alembic commands ###

    op.bulk_insert(
        event_categories_table,
        [
            {"name": "No data outliers"},
        ],
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("st_check_outliers_by_campaigns")
    # ### end Alembic commands ###

    op.execute(
        event_categories_table.delete().where(
            event_categories_table.c.name == op.inline_literal("No data outliers")
        )
    )
