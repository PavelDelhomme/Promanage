from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from .base import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(Text)
    status = Column(Enum('draft', 'published', 'archived'))
    category = Column(String(50))
    start_date = Column(DateTime)
    end_date = Column(DateTime)