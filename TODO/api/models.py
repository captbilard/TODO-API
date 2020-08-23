from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=500)
    completed = models.BooleanField(null=True)
    url = models.CharField(max_length=500, null=True)
    order = models.IntegerField(null=True)

    def __str__(self):
        return self.title