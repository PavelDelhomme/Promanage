from pydantic import BaseModel
from datetime import date
from typing import Optional

class CVEntryBase(BaseModel):
    entry_type: str
    title: str
    description: Optional[str] = None
    company: Optional[str] = None
    start_date: date
    end_date: Optional[date] = None
    skills: Optional[str] = None
    url: Optional[str] = None

class CVEntryCreate(CVEntryBase):
    pass

class CVEntry(CVEntryBase):
    id: int

    class Config:
        orm_mode = True