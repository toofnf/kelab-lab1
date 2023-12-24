import sqlalchemy as sa

from src.core.metadata import DeclarativeBase


class Base(DeclarativeBase):
    __abstract__ = True

    def __repr__(self) -> str:
        columns = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        return f'<{self.__tablename__}: ' f'{", ".join(map(lambda x: f"{x[0]}={x[1]}", columns.items()))}>'


class User(Base):
    __tablename__ = 'users'

    user_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    login = sa.Column(sa.String, unique=True, nullable=False)
