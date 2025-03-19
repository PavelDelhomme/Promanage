# core/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include("base.urls")),
    path('admin/', admin.site.urls),
    path('projects/', include("project_management.urls")),
    path('blog/', include("blog.urls")),
    path('cv/', include("cv.urls")),
    path('tasks/', include("tasks.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)