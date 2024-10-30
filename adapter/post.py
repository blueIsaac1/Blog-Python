from typing import Typevar
from pydantic import BaseModel
from domain.entities.post import Post

dataT = Typevar("DataT")

class PostTortoiseAdapter(BaseModel):
    model : dataT # type: ignore

    async def list(self):
        return await self.model.all()
    
    async def create(self, post: Post):
        return await self.model.create(**post.dict())
    
    async def get(self, post_id: int):
        return await self.model.get(id=post_id)