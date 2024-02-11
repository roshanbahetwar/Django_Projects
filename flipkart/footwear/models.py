from django.db import models

# Create your models here.

class ShoesModel(models.Model):
    shoes_type = models.CharField(max_length=20)
    shoes_price = models.FloatField()
    shoes_qty = models.IntegerField()

class SportsModel(models.Model):
    sports_shoes_type = models.CharField(max_length=20)
    sports_shoes_price = models.FloatField()
    sports_shoes_qty = models.IntegerField()

class SlipperModel(models.Model):
    slipper_type = models.CharField(max_length=20)
    slipper_price = models.FloatField()
    slipper_qty = models.IntegerField()