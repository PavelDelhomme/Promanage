from django.db import models
from django.contrib.auth.models import User

class CurriculumVitae(models.Model):
    title = models.CharField("Titre du CV", max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField("Public", default=False)
    pdf_file = models.FileField(upload_to='cvs/', null=True, blank=True)

    def __str__(self):
        return self.title

class CVEntry(models.Model):
    ENTRY_TYPE_CHOICES = [
        ('EXPERIENCE', 'Expérience'),
        ('FORMATION', 'Formation'),
        ('COMPETENCE', 'Compétence'),
        ('LANGUE', 'Langue'),
        ('PROJET', 'Projet'),
    ]
    
    cv = models.ForeignKey(CurriculumVitae, on_delete=models.CASCADE, related_name='entries', null=True, blank=True)
    entry_type = models.CharField("Type", max_length=20, choices=ENTRY_TYPE_CHOICES)
    title = models.CharField("Titre", max_length=200)
    description = models.TextField("Description")
    start_date = models.DateField("Date début", null=True, blank=True)
    end_date = models.DateField("Date fin", null=True, blank=True)
    order = models.IntegerField("Ordre", default=0)

    class Meta:
        ordering = ['order', '-start_date']
        verbose_name = "Entrée de CV"
        verbose_name_plural = "Entrées de CV"

    def __str__(self):
        return f"{self.get_entry_type_display()} : {self.title}"
