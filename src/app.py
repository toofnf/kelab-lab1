from fastapi import FastAPI, Depends, Response, status
from src.settings import config
from src.core.engine import get_session, engine
from src.core.models import User, Base
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager
from logger import logger

@asynccontextmanager
async def lifespan(application: FastAPI):
    Base.metadata.create_all(engine)
    get_session()
    yield


app = FastAPI(
    title=config.SERVICE_NAME,
    description=config.DESCRIPTION,
    docs_url=None if config.ENV == 'prd' else '/docs',
    redoc_url=None if config.ENV == 'prd' else '/redoc',
    version=config.VERSION,
    lifespan=lifespan
)


@app.post("/users/create")
def insert_user(login: str, session: Session = Depends(get_session)):
    user = User(login=login)
    session.add(user)
    session.commit()
    return Response(status_code=status.HTTP_201_CREATED)


@app.get("/users/{user_id}")
def read_user(user_id: int, session: Session = Depends(get_session)):
    result = session.query(User).filter(User.user_id == user_id)
    return result.one_or_none()


@app.get("/users")
def list_all_users(session: Session = Depends(get_session)):
    result = session.query(User).all()
    logger.info(result)
    return result
