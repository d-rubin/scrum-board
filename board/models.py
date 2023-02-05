from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from datetime import date
from django.core.exceptions import ValidationError
from django.db.models import ManyToManyField


class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=250)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_todo_set')
    assignees = ManyToManyField(User, related_name='assigned_users')
    created_at = models.DateField(default=date.today)
    due_date = models.DateField()
    # priority = models.IntegerField(default=2,)
    # status = models.IntegerField(default=1, min_value=1, max_value=5)
