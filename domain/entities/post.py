from enum import Enum
from pydantic import BaseModel, Field

class PostStatus(str, Enum):
    PUBLISHED = 'publicado'
    DRAFT = 'rascunho'

class PostDto(BaseModel):
    title: str
    content: str

class Post(PostDto):
    status: PostStatus = Field(default=PostStatus.DRAFT)