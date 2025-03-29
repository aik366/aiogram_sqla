from app.database.models import async_session
from app.database.models import User
from sqlalchemy import select, update, delete, desc


async def set_user(tg_id, full_name):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        
        if not user:
            new_user = User(
                tg_id=tg_id,
                full_name=full_name,
            )
            session.add(new_user)
            await session.commit()


async def select_user():
    async with async_session() as session:
        result = await session.execute(select(User).order_by(desc(User.tg_id)))
        return {str(i): (row.User.tg_id, row.User.full_name) for i, row in enumerate(result.all(), 1)}


async def delete_user(tg_id):
    async with async_session() as session:
        await session.execute(delete(User).where(User.tg_id == tg_id))
        await session.commit()


if __name__ == '__main__':
    import asyncio

    asyncio.run(select_user())
