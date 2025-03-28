from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CurriculumVitae, CVEntry
from .forms import CVEntryForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

class CVListView(ListView):
    model = CurriculumVitae
    template_name = 'cv/cv_list.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return CurriculumVitae.objects.filter(user=self.request.user)
        return CurriculumVitae.objects.filter(is_public=True)

class CVDetailView(DetailView):
    model = CurriculumVitae
    template_name = 'cv/cv_detail.html'

class CVCreateView(LoginRequiredMixin, CreateView):
    model = CurriculumVitae
    template_name = 'cv/cv_form.html'
    fields = ['title', 'is_public']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('cv_detail', kwargs={'pk': self.kwargs['cv_id']})

class CVEntryCreateView(LoginRequiredMixin, CreateView):
    model = CVEntry
    form_class = CVEntryForm  # Utilisez le formulaire modifié
    template_name = 'cv/cventry_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {'cv': self.kwargs['cv_id']}
        return kwargs

    def form_valid(self, form):
        form.instance.cv = CurriculumVitae.objects.get(pk=self.kwargs['cv_id'])
        return super().form_valid(form)

class CVDeleteView(LoginRequiredMixin, DeleteView):
    model = CurriculumVitae
    template_name = 'cv/cv_confirm_delete.html'
    success_url = reverse_lazy('cv_list')

class CVEntryDeleteView(LoginRequiredMixin, DeleteView):
    model = CVEntry
    template_name = 'cv/cventry_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('cv_detail', kwargs={'pk': self.object.cv.id})


class CVEntryUpdateView(LoginRequiredMixin, UpdateView):
    model = CVEntry
    template_name = 'cv/cventry_form.html'
    fields = ['entry_type', 'title', 'description', 'start_date', 'end_date', 'order']

def generate_cv_pdf(request, pk):
    cv = CurriculumVitae.objects.get(pk=pk)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{cv.title}.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    # Configuration du PDF
    width, height = letter
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, height - 100, cv.title)

    y_position = height - 130
    for entry in cv.entries.all().order_by('order'):
        p.setFont("Helvetica-Bold", 12)
        p.drawString(100, y_position, entry.title)
        p.setFont("Helvetica", 10)
        y_position -= 20
        p.drawString(120, y_position, entry.description)
        y_position -= 30

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
