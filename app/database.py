from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    create_async_engine, async_sessionmaker, AsyncSession
)
from sqlalchemy.orm import DeclarativeBase
DATABASE_URL=""
Base=DeclarativeBase()
engine=create_async_engine(
    DATABASE_URL,
    echo=True
)
asyncLocal=async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)
async def create_db_tables():
    async with engine.begin() as conn:
        conn.run_sync(Base.metadata.create_all())
async def get_session()->AsyncGenerator[AsyncSession,None]:
    async with asyncLocal as AsyncSession:
        yield AsyncSession