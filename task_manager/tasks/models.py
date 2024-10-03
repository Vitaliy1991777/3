from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('added', 'Добавлена'),
        ('in_progress', 'В работе'),
        ('completed', 'Выполнена'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='added')

    def __str__(self):
        return self.name
