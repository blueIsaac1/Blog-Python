from typing import TypeVar
from pydantic import BaseModel
from domain.entities.post import Post, PostStatus

dataT = TypeVar("DataT")

class PostTortoiseAdapter(BaseModel):
    model : dataT # type: ignore

    async def list(self):
        return await self.model.filter(status = PostStatus.PUBLISHED)
    
    async def create(self, post: Post):
        return await self.model.create(**post.dict())
    
    async def get(self, post_id: int):
        return await self.model.get(id=post_id)
    
    async def publish(self, post_id: int):
        post = await self.get(post_id)
        post.status = PostStatus.PUBLISHED
        await post.save()