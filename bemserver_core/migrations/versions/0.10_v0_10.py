"""v0.10

Revision ID: 0.10
Revises: 0.8
Create Date: 2023-02-28 10:24:26.825352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0.10"
down_revision = "0.8"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("ener_cons_ts_by_building", "wh_conversion_factor")
    op.drop_column("ener_cons_ts_by_site", "wh_conversion_factor")
    op.alter_column(
        "timeseries", "unit_symbol", existing_type=sa.VARCHAR(length=20), nullable=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "timeseries", "unit_symbol", existing_type=sa.VARCHAR(length=20), nullable=True
    )
    op.add_column(
        "ener_cons_ts_by_site",
        sa.Column(
            "wh_conversion_factor",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.add_column(
        "ener_cons_ts_by_building",
        sa.Column(
            "wh_conversion_factor", sa.INTEGER(), autoincrement=False, nullable=False
        ),
    )
    # ### end Alembic commands ###
