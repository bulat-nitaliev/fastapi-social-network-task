from fastapi import APIRouter,Depends, HTTPException, status
from typing import List
from src.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select, update, delete
from src.auth.models import post
from src.routers.schemas import PostCreate
from fastapi_users import FastAPIUsers
from src.auth.models import User
from src.auth.manager import get_user_manager
from src.auth.base_config import auth_backend


fastapi_users = FastAPIUsers[User, int](get_user_manager,[auth_backend],)

current_user = fastapi_users.current_user()

post_router = APIRouter(prefix='/posts',tags=['posts'])


@post_router.get('/',response_model=List[PostCreate])
async def get_all_post(session: AsyncSession = Depends(get_async_session)):
    query = select(post)
    result = await session.execute(query)
    return result.all()
    

@post_router.post('/')
async def add_post(new_post: PostCreate, 
                   session: AsyncSession = Depends(get_async_session),
                   user: User=Depends(current_user)):
    stmt = insert(post).values(user_id=user.id,**new_post.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status': 'success'}


@post_router.put('/')
async def update_post( 
    post_id:int, 
    update_post: PostCreate, 
    session:AsyncSession=Depends(get_async_session),
    user: User=Depends(current_user)):
    query = update(post).where(post.c.id == post_id).values(user_id=user.id,**update_post.dict())
    result = await session.execute(query)
    await session.commit()
    return {'status':'success'}


@post_router.delete('/')
async def delete_post_id(post_id:int, session:AsyncSession = Depends(get_async_session)):
    post_del = delete(post).where(post.c.id==post_id)
    await session.execute(post_del)
    await session.commit()
    return f'delete post id={post_id}'

@post_router.put('/lickes/{post_id}')
async def post_lickes(post_id:int,
                      user:User=Depends(current_user), 
                      session:AsyncSession = Depends(get_async_session)):
    query = select(post).where(post.c.id==post_id)
    result = await session.execute(query)
    if result.fetchall(): # проверяем наличие поста
        query = select(post).where(post.c.id==post_id).filter(post.c.user_id==user.id)
        result = await session.execute(query)
        
        if result.fetchall():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="You cannot like your post")
        else:
            query = update(post).where(post.c.id==post_id).filter(post.c.user_id!=user.id).values(likes_count=post.c.likes_count + 1)
            await session.execute(query)
            await session.commit()
            return {'status':'success'}
    else:
        return {'error':'post not found'}
    
@post_router.put('/dislickes/{post_id}')
async def post_dislickes(post_id:int,
                      user:User=Depends(current_user), 
                      session:AsyncSession = Depends(get_async_session)):
    query = select(post).where(post.c.id==post_id)
    result = await session.execute(query)
    if result.fetchall(): # проверяем наличие поста
        query = select(post).where(post.c.id==post_id).filter(post.c.user_id==user.id)
        result = await session.execute(query)
        
        if result.fetchall():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="You cannot dislike your post")
        else:
            query = update(post).where(post.c.id==post_id).filter(post.c.user_id!=user.id).values(dislikes_count=post.c.dislikes_count+1)
            await session.execute(query)
            await session.commit()
            return {'status':'success'}
    else:
        return {'error':'post not found'}
   