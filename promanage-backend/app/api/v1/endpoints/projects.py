from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.project import Project
from app.db.session import get_db

router = APIRouter()

@router.post("/projects/", response_model=ProjectOut)
async def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_project = Project(**project.dict(), owner_id=current_user.id)
    db.add(db_project)
    db.commit()
    return db_project

