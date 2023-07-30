from fastapi import FastAPI, status, Depends
from fastapi_users import FastAPIUsers
import os
import sys
from sqlalchemy.ext.asyncio import AsyncSession

sys.path.append(os.path.join(sys.path[0], 'src'))
from src.auth.models import User
from src.auth.manager import get_user_manager
from src.auth.base_config import auth_backend
from src.auth.schemas import UserCreate, UserRead
from src.routers.post_router import post_router
from src.routers.user_router import user_router
from src.database import get_async_session

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI(title= 'test_task')

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend, requires_verification=True),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(post_router)
app.include_router(user_router)


