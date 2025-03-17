from django.db import models
from django.contrib.auth.models import User
from project_management.models import Project

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True, related_name='blog_posts')
    tags = models.CharField(max_length=200, blank=True)
    cover_image = models.ImageField(upload_to='blog_covers/', null=True, blank=True)
    
    def __str__(self):
        return self.title
