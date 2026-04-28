from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    SUBJECT_CHOICES = [
        ('Hindi', 'Hindi'),
        ('English', 'English'),
        ('Math', 'Math'),
        ('Science', 'Science'),
    ]

    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title