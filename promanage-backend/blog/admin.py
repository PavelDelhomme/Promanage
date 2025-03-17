from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_public', 'project')
    list_filter = ('is_public', 'author', 'project')
    search_fields = ('title', 'content')
