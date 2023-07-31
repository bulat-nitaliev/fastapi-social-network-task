from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
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

@user_router.get('/{user_id}',response_model=List[UserRead])
async def get_user(user_id:int,session:AsyncSession=Depends(get_async_session)):
    query = select(user).where(user.c.id==user_id)
    result = await session.execute(query)
    value = result.fetchall()
    if value:
        return value
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="User not found")

@user_router.delete('/{user_id}')
async def delete_user(user_id:int,session:AsyncSession=Depends(get_async_session)):
    del_user = delete(user).where(user.c.id==user_id)
    await session.execute(del_user)
    await session.commit()
    return f'the user by ID = {user_id} has been deleted'