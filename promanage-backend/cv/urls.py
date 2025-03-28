from django.urls import path
from .views import (
    CVListView, 
    CVDetailView, 
    CVCreateView,
    CVDeleteView,
    CVEntryCreateView, 
    CVEntryUpdateView,
    CVEntryDeleteView,
)

from .pdf import generate_cv_pdf

urlpatterns = [
    path('', CVListView.as_view(), name='cv_list'),
    path('new/', CVCreateView.as_view(), name='cv_create'),
    path('<int:pk>/', CVDetailView.as_view(), name='cv_detail'),
    path('<int:pk>/delete/', CVDeleteView.as_view(), name='cv_delete'),
    path('<int:pk>/pdf/', generate_cv_pdf, name='cv_pdf'),
    path('<int:cv_id>/entries/new/', CVEntryCreateView.as_view(), name='cventry_create'),
    path('entries/<int:pk>/edit/', CVEntryUpdateView.as_view(), name='cventry_update'),
    path('entries/<int:pk>/delete/', CVEntryDeleteView.as_view(), name='cventry_delete'),
]