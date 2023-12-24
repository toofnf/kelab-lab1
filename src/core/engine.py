from contextlib import contextmanager
from typing import Any, Iterator

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from src.settings import config

engine = sa.create_engine(
    config.database_uri,
    pool_pre_ping=True,
    connect_args={
        'keepalives': 1,
        'keepalives_idle': 30,
        'keepalives_interval': 10,
        'keepalives_count': 5,
    },
    echo=True
)

product_session = sessionmaker(bind=engine)


@contextmanager
def create_session() -> Iterator[Any]:
    new_session = product_session()
    try:
        yield new_session
        new_session.commit()
    except Exception:
        new_session.rollback()
        raise
    finally:
        new_session.close()


def get_session() -> Any:
    with create_session() as session:
        yield session
