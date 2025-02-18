from fastapi import FastAPI
from config import config
from database import Base, engine
from app.db import get_async_session, get_user_db
from app.users import get_user_manager
from app.schemas import UserCreate
import contextlib
import asyncio

app = FastAPI(debug=config.DEBUG)

get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)

async def create_first_superuser():
    try:
        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    user = await user_db.get_by_email(config.FIRST_SUPERUSER_EMAIL)
                    if not user:
                        await user_manager.create(
                            UserCreate(
                                email=config.FIRST_SUPERUSER_EMAIL,
                                password=config.FIRST_SUPERUSER_PASSWORD,
                                is_superuser=True
                            )
                        )
                        print(f"First superuser created: {config.FIRST_SUPERUSER_EMAIL}")
    except Exception as e:
        print(f"Error creating first superuser: {str(e)}")

@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)
    await create_first_superuser()

@app.get("/")
async def root():
    return {"message": "Welcome to ProManage Backend"}

@app.get("/health")
async def health_check():
    return {"status": "OK"}
