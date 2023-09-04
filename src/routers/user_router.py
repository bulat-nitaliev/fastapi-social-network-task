from fastapi import APIRouter, Depends, HTTPException, status,Response
from typing import List, Optional, Any, Union
from src.auth.schemas import UserRead, Token
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from sqlalchemy import insert, select, update, delete
from src.auth.models import user, User
from fastapi.security import OAuth2PasswordRequestForm
from src.auth.manager import get_user_manager
from fastapi_users import BaseUserManager
from datetime import timedelta
from fastapi_users.jwt import generate_jwt, SecretType, JWT_ALGORITHM


user_router = APIRouter(prefix='/users',tags=['users'])


# @user_router.post("/", status_code=200)
# def singin_access_token(
#     form_data: OAuth2PasswordRequestForm = Depends(), user_tools: BaseUserManager= Depends()
# ) -> Any:
#     """
#     Providing access token OAuth2.
#     """
#     user = user_tools.authenticate(form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#         )
#     access_token_expires = timedelta(minutes=30)
#     access_token = generate_jwt(data={"sub": user.email},secret=SecretType,lifetime_seconds=access_token_expires,algorithm=J)
#     return {"access_token": access_token, "token_type": "cookie"}

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