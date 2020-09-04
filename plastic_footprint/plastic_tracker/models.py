from django.db import models

# Create your models here.

class Customer(models.Model):
    fullname = models.CharField(max_length=100)
    monthly_balance = models.FloatField()

class Product(models.Model):
    product_id = models.IntegerField()
    name = models.CharField(max_length=100)
    plastic_weight = models.FloatField()