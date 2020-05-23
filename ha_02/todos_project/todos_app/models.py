from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    uni = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Todo(models.Model):
    description = models.CharField(max_length=160)    
    due = models.CharField(max_length=80)
    accomplished = models.IntegerField()

    def __str__(self):
        return self.description

