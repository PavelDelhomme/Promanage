from django.urls import path
from .views import CVEntryListView, CVEntryDetailView, CVEntryCreateView

urlpatterns = [
    path('', CVEntryListView.as_view(), name='cventry_list'),
    path('<int:pk>/', CVEntryDetailView.as_view(), name='cventry_detail'),
    path('new/', CVEntryCreateView.as_view(), name='cventry_create'),
]