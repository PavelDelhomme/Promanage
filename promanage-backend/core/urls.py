# core/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('project_management.urls')),
    path('blog/', include('blog.urls')),
    path('cv/', include('cv.urls')),
]
