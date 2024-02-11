from django.db import models

# Create your models here.
class MensModel(models.Model):
    cloth_category = models.CharField(max_length=25)
    cloth_price = models.FloatField()
    cloth_qty = models.IntegerField()

class WomenModel(models.Model):
    cloth_category = models.CharField(max_length=25)
    cloth_price = models.FloatField()
    cloth_qty = models.IntegerField()

class KidesModel(models.Model):
    cloth_category = models.CharField(max_length=25)
    cloth_price = models.FloatField()
    cloth_qty = models.IntegerField()