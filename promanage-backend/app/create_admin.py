from sqlalchemy.orm import Session
from core.security import get_password_hash
from db.session import get_db
from models.user import AdminUser

def create_admin():
    db: Session = next(get_db())
    admin = AdminUser(
        username="admin",
        password=get_password_hash("motdepasseadmin"),
        is_superuser=True
    )
    db.add(admin)
    db.commit()
    print("Admin crée avec succès")

if __name__ == "__main__":
    create_admin()