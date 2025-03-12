from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import cv as schemas
from ...models import CVEntry
from ...db.session import get_db
from core.security import verify_token

router = APIRouter()

@router.post("/cv/", response_model=schemas.CVEntry)
async def create_cv_entry(
    entry: schemas.CVEntryCreate,
    db: Session = Depends(get_db),
    token: dict = Depends(verify_token)
):
    if not token.get("is_admin"):
        raise HTTPException(status_code=403, detail="Accès refusé")
    db_entry = CVEntry(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

@router.get("/cv/", response_model=List[schemas.CVEntry])
def read_cv_entries(
    skip: int = 0,
    limit: int = 100,
    entry_type: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(CVEntry)
    if entry_type:
        query = query.filter(CVEntry.entry_type == entry_type)
    return query.offset(skip).limit(limit).all()