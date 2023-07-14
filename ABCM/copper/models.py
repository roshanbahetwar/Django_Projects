from django.db import models

# Create your models here.
class CopperDetailsModels(models.Model):
    prd_reg_no = models.IntegerField()
    prd_name = models.CharField(max_length=25)
    prd_qty = models.IntegerField()
    prd_price = models.IntegerField()
