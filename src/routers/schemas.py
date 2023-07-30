from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PostCreate(BaseModel):
    title: str
    content: str
    date_creation: Optional[datetime] 
    # likes_count: int
    # dislikes_count: int

# class PostShow(BaseModel):
#     todos: list(PostCreate)
#     # id: int
#     # user_id: int
#     # title: str
#     # content: str
#     # date_creation: Optional[datetime]
#     # likes_count: Optional[int] = 0
#     # dislikes_count: Optional[int] = 0

#     class Config:
#         schema_extra = {
#             'example': {
#                 'todos':[{
#                     "id": 0,
#                     "user_id": 0,
#                     "title": "string",
#                     "content": "string",
#                     "date_creation": "2023-07-23T22:17:35.158Z",
#                     "likes_count": 0,
#                     "dislikes_count": 0
#                     },{
#                     "id": 0,
#                     "user_id": 0,
#                     "title": "string",
#                     "content": "string",
#                     "date_creation": "2023-07-23T22:17:35.158Z",
#                     "likes_count": 0,
#                     "dislikes_count": 0
#                     }
#                 ]
#             }



#         }

