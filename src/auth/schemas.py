from fastapi_users import schemas
from typing import Optional
from pydantic.version import VERSION as PYDANTIC_VERSION
from pydantic import BaseModel, ConfigDict

PYDANTIC_V2 = PYDANTIC_VERSION.startswith("2.")

class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    email: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

   
    if PYDANTIC_V2:  # pragma: no cover
        model_config = ConfigDict(from_attributes=True)  # type: ignore
    else:  # pragma: no cover

        class Config:
            orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

class Token(BaseModel):
    access_token: str
    token_type: str