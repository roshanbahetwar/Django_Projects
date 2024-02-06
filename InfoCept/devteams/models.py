from django.db import models

# Create your models here.
class TeamsModelDetails(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    salary = models.IntegerField()
    city = models.CharField(max_length=25)
