from pydantic import BaseModel
from datetime import datetime

class BlogPostBase(BaseModel):
    title: str
    content: str
    slug: str
    is_published: bool = False
    project_id: Optional[int] = None

class BlogPostCreate(BlogPostBase):
    pass

class BlogPost(BlogPostBase):
    id: int
    created_at = datetime
    updated_at = datetime

    class Config:
        orm_mode = True