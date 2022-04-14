from django.db import models


# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    due_on = models.DateTimeField(blank=True, null=True)
    owner = models.CharField(max_length=250, blank=True, null=True)
    mark = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'