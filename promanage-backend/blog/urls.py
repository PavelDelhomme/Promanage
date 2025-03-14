from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostCreateView

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpost_list'),
    path('<int:pk>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('new/', BlogPostCreateView.as_view(), name='blogpost_create'),
]
