from django.db import models

# Create your models here.

class Customer(models.Model):
    fullname = models.CharField(max_length=100)
    monthly_balance = models.FloatField()