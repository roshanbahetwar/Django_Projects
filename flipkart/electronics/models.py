from django.db import models

# Create your models here.
class LaptopModel(models.Model):

    model_name = models.CharField(max_length=25)
    model_price = models.FloatField()
    model_qty = models.IntegerField()


class MobileModel(models.Model):
    model_name = models.CharField(max_length=25)
    model_price = models.FloatField()
    model_qty = models.IntegerField()


class TvModel(models.Model):
    model_name = models.CharField(max_length=25)
    model_price = models.FloatField()
    model_qty = models.IntegerField()