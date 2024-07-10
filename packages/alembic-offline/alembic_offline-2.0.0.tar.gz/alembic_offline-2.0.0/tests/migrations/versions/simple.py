"""Test migration."""
from alembic import op

revision = 'simple'
down_revision = '1'
some_attribute = 'some-value'


def upgrade():
    """Upgrade."""
    op.drop_column('account', 'id')


def downgrade():
    """Downgrade."""
    pass
