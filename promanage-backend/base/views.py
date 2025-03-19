from django.conf import settings
import os
from django.views.generic import TemplateView
from blog.models import BlogPost

class HomeView(TemplateView):
    template_name = 'base/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Accueil - ProManage'
        context['recent_posts'] = BlogPost.objects.filter(is_public=True).order_by('-created_at')[:5]
        return context