"""empty message

Revision ID: 0482a4678a12
Revises: 6242e1772895
Create Date: 2021-07-01 16:28:38.218420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0482a4678a12'
down_revision = '6242e1772895'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.Column('games', sa.Text(), nullable=True),
    sa.Column('goals', sa.Integer(), nullable=True),
    sa.Column('assist', sa.Integer(), nullable=True),
    sa.Column('xG', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['player_id'], ['players.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('players', 'value',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('players', 'value',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_table('stats')
    # ### end Alembic commands ###
