from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Project, Task, Bug
from .forms import ProjectForm, TaskForm, BugForm

class ProjectListView(ListView):
    model = Project
    template_name = 'project_management/project_list.html'
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_management/project_detail.html'

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project_management/project_form.html'

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project_management/project_form.html'

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'project_management/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')


class TaskListView(ListView):
    model = Task
    template_name = 'project_management/task_list.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'project_management/task_detail.html'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'project_management/task_form.html'

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'project_management/task_form.html'

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'project_management/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

class BugListView(ListView):
    model = Bug
    template_name = 'project_management/bug_list.html'
    context_object_name = 'bugs'

class BugDetailView(DetailView):
    model = Bug
    template_name = 'project_management/bug_detail.html'


class BugCreateView(LoginRequiredMixin, CreateView):
    model = Bug
    form_class = BugForm
    template_name = 'project_management/bug_form.html'

class BugUpdateView(LoginRequiredMixin, UpdateView):
    model = Bug
    form_class = BugForm
    template_name = 'project_management/bug_form.html'

class BugDeleteView(LoginRequiredMixin, UpdateView):
    model = Bug
    template_name = 'project_management/bug_confirm_delete.html'
    success_url = reverse_lazy('project_list')