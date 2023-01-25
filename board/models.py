from django.db import models
from datetime import date

# Create your models here.
class Todo(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    deadline = models.DateField()