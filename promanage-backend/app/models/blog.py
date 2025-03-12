from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Text
from sqlalchemy.sql import func
from .base import Base

class BlogPost(Base):
    __tablename__ = "blog_posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    content = Column(Text)
    slug = Column(String(200), unique=True) # Pour les URLs SEO
    is_published = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())
    project_id = Column(Integer, ForeignKey('projects.id'))