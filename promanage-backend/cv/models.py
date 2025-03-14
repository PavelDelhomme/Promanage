from django.db import models


class CVEntry(models.Model):
    ENTRY_TYPE_CHOICES = [
        ('EXPERIENCE', 'Expérience professionnelle'),
        ('EDUCATION', 'Formation'),
        ('SKILL', 'Compétence'),
        ('CERTIFICATE', 'Certificat'),
    ]
    
    entry_type = models.CharField(max_length=20, choices=ENTRY_TYPE_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_public = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.get_entry_type_display()} : {self.title}"