from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project, Task, Bug

class ProjectListView(ListView):
    model = Project
    template_name = 'project_management/project_list.html'
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_management/project_detail.html'

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'project_management/project_form.html'
    fields = ['title', 'description', 'category', 'start_date', 'end_date', 'is_public']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'project_management/project_form.html'
    fields = ['title', 'description', 'category', 'status', 'start_date', 'end_date', 'is_public']

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'project_management/project_confirm_delete.html'
    success_url = '/projects/'


class TaskListView(ListView):
    model = Task
    template_name = 'project_management/task_list.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'project_management/task_detail.html'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'project_management/task_form.html'
    fields = ['title', 'description', 'status', 'due_date']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'project_management/task_form.html'
    fields = ['title', 'description', 'status', 'due_date']

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'project_management/task_confirm_delete.html'
    success_url = 'projects/'

class BugListView(ListView):
    model = Bug
    template_name = 'project_management/bug_list.html'
    context_object_name = 'bugs'

class BugDetailView(DetailView):
    model = Bug
    template_name = 'project_management/bug_detail.html'

class BugCreateView(LoginRequiredMixin, CreateView):
    model = Bug
    template_name = 'project_management/bug_form.html'
    fields = ['title', 'description', 'status', 'priority']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)*

class BugUpdateView(LoginRequiredMixin, UpdateView):
    model = Bug
    template_name = 'project_management/bug_form.html'
    fields = ['title', 'description', 'status', 'priority']

class BugDeleteView(LoginRequiredMixin, UpdateView):
    model = Bug
    template_name = 'project_management/bug_confirm_delete.html'
    success_url = 'projects/'