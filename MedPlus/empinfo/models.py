from django.db import models

# Create your models here.
class EmpDetailsModels(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
