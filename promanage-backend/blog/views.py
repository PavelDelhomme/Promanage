from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BlogPost

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blogpost_list.html'
    context_object_name = 'blog_posts'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return BlogPost.objects.all()
        return BlogPost.objects.filter(is_public=True)

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blogpost_detail.html'

class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blogpost_form.html'
    success_url = reverse_lazy('blogpost_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogPostUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blogpost_form.html'
    success_url = reverse_lazy('blogpost_list')


class BlogPostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/blogpost_confirm_delete.html'
    success_url = reverse_lazy('blogpost_list')

def share_on_linkedin(request, pk):
    post = BlogPost.objects.get(pk=pk)
    # Logique pour partager sur LinkedIn (à implémenter)
    return redirect('blogpost_detail', pk=pk)