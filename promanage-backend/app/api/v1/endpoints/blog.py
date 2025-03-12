from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import blog as schemas
from ...models import BlogPost
from ...db.session import get_db

router = APIRouter()

@router.post("/blog/", response_model=schemas.BlogPost)
def create_blog_post(
    post: schemas.BlogPostCreate,
    db: Session = Depends(get_db)
):
    db_post = BlogPost(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@router.post("/blog/{slug}", response_model=schemas.BlogPost)
def read_blog_post(slug:str, db: Session = Depends(get_db)):
    post = db.query(BlogPost).filter(BlogPost.slug == slug).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post