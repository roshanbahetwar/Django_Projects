from django.db import models

# Create your models here.
class LaptopModel(models.Model):
    mname = models.CharField(max_length=25)
    mprice = models.IntegerField()
    mqty = models.IntegerField()


class MobileModel(models.Model):
    mname = models.CharField(max_length=25)
    mprice = models.IntegerField()
    mqty = models.IntegerField()

class TvModel(models.Model):
    mname = models.CharField(max_length=25)
    mprice = models.IntegerField()
    mqty = models.IntegerField()