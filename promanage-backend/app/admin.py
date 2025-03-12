from fastapi_admin.app import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider

async def setup_admin(app):
    admin_app.ini(
        app,
        providers=[
            UsernamePasswordProvider(
                login_logo_url="https://images.icon-icons.com/3257/PNG/64/login_circle_icon_206018.png",
                admin_mode=AdminUser,
            )
        ],
    )