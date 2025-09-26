from django.db import models

class Book(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'مبتدئ'),
        ('intermediate', 'متوسط'),
        ('advanced', 'متقدم'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to="library/files/")
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)

    def __str__(self):
        return self.title
