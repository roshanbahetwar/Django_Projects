from django.db import models

# Create your models here.
class DevDetailsModels(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    city = models.CharField(max_length=25)
    email = models.EmailField()
    join_date = models.DateField()