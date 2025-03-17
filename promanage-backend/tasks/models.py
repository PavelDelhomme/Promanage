from django.db import models
from project_management.models import Project

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
