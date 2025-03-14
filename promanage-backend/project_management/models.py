# project_management/models.py

from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('PERSONAL', 'Personnel'),
        ('PROFESSIONAL', 'Professionnel'),
        ('FREELANCE', 'Freelance'),
    ]
    STATUS_CHOICES = [
        ('PLANNING', 'En planification'),
        ('ONGOING', 'En cours'),
        ('COMPLETED', 'Terminé'),
        ('ON_HOLD', 'En pause'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PLANNING')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_public = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('TODO', 'À faire'),
        ('IN_PROGRESS', 'En cours'),
        ('DONE', 'Terminé')
    ])
    due_date = models.DateField()
    
    def __str__(self):
        return f"{self.title} - {self.project.title}"

class Bug(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='bugs')
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('OPEN', 'Ouvert'),
        ('IN_PROGRESS', 'En cours'),
        ('RESOLVED', 'Résolu'),
        ('CLOSED', 'Fermé')
    ])
    priority = models.CharField(max_length=20, choices=[
        ('LOW', 'Basse'),
        ('MEDIUM', 'Moyenne'),
        ('HIGH', 'Haute'),
        ('CRITICAL', 'Critique')
    ])
    
    def __str__(self):
        return f"{self.title} - {self.project.title}"
