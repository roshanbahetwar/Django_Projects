from django.db import models

# Create your models here.
class EpopDetailsModels(models.Model):
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=30)
    pan = models.CharField(max_length=25)
    email = models.EmailField()
    mobile = models.BigIntegerField()