from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# import your Base and models
from database import Base
import models  # make sure this imports your User model

# Alembic Config object
config = context.config

# Setup Python logging from the config file
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Tell Alembic about the SQLAlchemy models' metadata
target_metadata = Base.metadata

# Offline migrations
def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# Online migrations
def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

# Run offline or online based on context
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
