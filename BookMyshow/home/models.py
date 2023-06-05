from django.db import models

# Create your models here.
class HomeDetailsModels(models.Model):
    name = models.CharField(max_length=25)
    movie = models.CharField(max_length=30)
    price = models.IntegerField()
    date = models.DateField()
    email = models.EmailField()
    mobile = models.BigIntegerField()