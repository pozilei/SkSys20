from django.db import models

# Create your models here.
class Todo(models.Model):
    description = models.CharField(max_length=160)    
    due = models.CharField(max_length=80)
    accomplished = models.IntegerField()

    def __str__(self):
        return self.description