from django.db import models

# Create your models here.
class CopperDetailsModels(models.Model):
    product = models.CharField(max_length=25)
    price = models.IntegerField()
    qty = models.IntegerField()
    date = models.DateField()
