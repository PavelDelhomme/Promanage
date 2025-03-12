from sqlalchemy import Column, Integer, String, Enum, Date, Text, JSON
from datetime import date
from .base import Base


class CVEntry(Base):
    __tablename__ = "cv_entries"

    id = Column(Integer, primary_key=True)
    entry_type = Column(Enum("experience", "education", "skill", "certification"))
    title = Column(String(100))
    description = Column(Text)
    organization = Column(String(100))  # Entreprise/École
    location = Column(String(100)) # Localisation
    start_date = Column(Date)
    end_date = Column(Date)
    skills = Column(Text) # JSON: {"backend": ["Python", "Java"], ...}
    languages = Column(JSON) # {"Anglais": "B2", "Russe": "A2"}
    interests = Column(Text) # 'Lecture, Sport, Musique"
    technical_skills = Column(JSON) # {"DevOps": ["Docker", "Nginx"], ...}
    certifications = Column(Text)
    url = Column(String(200))
    is_public = Column(Boolean, default=False)