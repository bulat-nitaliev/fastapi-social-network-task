from fastapi import APIRouter, Depends
from typing import List
from src.auth.schemas import UserRead
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from sqlalchemy import insert, select, update, delete
from src.auth.models import user



user_router = APIRouter(prefix='/users',tags=['users'])


@user_router.get('/',response_model=List[UserRead])
async def get_all_users(session:AsyncSession=Depends(get_async_session)):
    query = select(user)
    result = await session.execute(query)
    return result.all()

@user_router.get('/{user_id}',response_model=UserRead)
async def get_user(user_id:int,session:AsyncSession=Depends(get_async_session)):
    query = select(user).where(user.c.id==user_id)
    result = await session.execute(query)
    return result.all()