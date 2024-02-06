from django.db import models

# Create your models here.
class SilverDetailsModels(models.Model):
    product = models.CharField(max_length=20)
    price = models.IntegerField()
    qty = models.IntegerField()
    date = models.DateField()
