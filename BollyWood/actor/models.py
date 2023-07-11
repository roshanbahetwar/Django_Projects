from django.db import models

# Create your models here.
class ActorDetailsModel(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    salary = models.IntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=25)