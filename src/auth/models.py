from sqlalchemy import Table, Column, Integer, String, ForeignKey, TIMESTAMP, Boolean, Text
from datetime import datetime
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.orm import DeclarativeBase
from src.database import metadata



user= Table(
    'user',
    metadata,
    Column('id',Integer, primary_key=True),
    Column('email',String,nullable=False),
    Column('username',String,nullable=False),
    Column('hashed_password', String, nullable=False),
    Column('registered_at', TIMESTAMP, default=datetime.utcnow),
    Column('is_active',Boolean, default=True, nullable=False),
    Column('is_superuser',Boolean, default=False, nullable=False),
    Column('is_verified',Boolean, default=False, nullable=False)
)

post = Table(
    'post',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String, nullable=False),
    Column('content', Text, nullable=False),
    Column('likes_count', Integer),
    Column('dislikes_count', Integer),
    Column('date_creation', TIMESTAMP, default=datetime),
    Column('user_id', Integer, ForeignKey(user.c.id))
)



class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[int], Base):
    id= Column(Integer, primary_key=True)
    email= Column(String,nullable=False)
    username= Column(String,nullable=False)
    registered_at= Column( TIMESTAMP, default=datetime.utcnow)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)

