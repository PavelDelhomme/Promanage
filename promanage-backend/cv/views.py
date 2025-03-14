from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CVEntry

class CVEntryListView(ListView):
    model = CVEntry
    template_name = 'cv/cventry_list.html'
    context_object_name = 'cv_entries'

class CVEntryDetailView(DetailView):
    model = CVEntry
    template_name = 'cv/cventry_detail.html'

class CVEntryCreateView(LoginRequiredMixin, CreateView):
    model = CVEntry
    template_name = 'cv/cventry_form.html'
    fields = ['entry_type', 'title', 'description', 'start_date', 'end_date', 'is_public']

class CVEntryUpdateView(LoginRequiredMixin, UpdateView):
    model = CVEntry
    template_name = 'cv/cventry_form.html'
    fields = ['entry_type', 'title', 'description', 'start_date', 'end_date', 'is_public']

class CVEntryDeleteView(LoginRequiredMixin, DeleteView):
    model = CVEntry
    template_name = 'cv/cventry_confirm_delete.html'
    success_url = '/cv_entries/'