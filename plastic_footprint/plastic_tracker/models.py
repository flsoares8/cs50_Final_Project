from django.db import models

# Create your models here.

class Customer(models.Model):
    fullname = models.CharField(max_length=100)
    id_number = models.IntegerField(blank = True)
    monthly_balance = models.FloatField(default = 2.0)
    
class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    plastic_weight = models.FloatField()