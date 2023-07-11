from django.db import models

# Create your models here.
class ActressDetailsModels(models.Model):
    a_name = models.CharField(max_length=25)
    a_age = models.IntegerField()
    a_salary = models.IntegerField()
    a_city = models.CharField(max_length=25)