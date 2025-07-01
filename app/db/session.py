from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_async_engine(str(settings.DATABASE_URL), echo=True)
async_sessionmaker = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_async_db():
    async with async_sessionmaker() as session:
        yield session
