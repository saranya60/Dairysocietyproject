from django.db import models

# Create your models here.
class productdb(models.Model):
    Product = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=1000, null=True, blank=True)
    Price = models.FloatField(null=True, blank=True)
    Image = models.ImageField(upload_to="Product", null=True, blank=True)

class salesdb(models.Model):
    Date = models.DateField(auto_now=True)
    Product = models.CharField(max_length=100, null=True, blank=True)
    Price = models.FloatField(null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Total = models.FloatField(null=True, blank=True)
    Customer = models.CharField(max_length=100, null=True, blank=True)
class customerdb(models.Model):
    Customer = models.CharField(max_length=100, null=True, blank=True)
    Place = models.CharField(max_length=1000, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
class billdb(models.Model):
    Date = models.DateField(auto_now=True)
    Customer = models.CharField(max_length=100, null=True, blank=True)
    Total = models.FloatField(null=True, blank=True)

class pricechart(models.Model):
    fat = models.FloatField(null=True, blank=True)
    snf = models.FloatField(null=True, blank=True)
    rate = models.FloatField(null=True, blank=True)

class milkdb(models.Model):
    Date = models.DateField(auto_now=True)
    Farmer = models.CharField(max_length=1000, null=True, blank=True)
    Milk = models.FloatField(null=True, blank=True)
    FAT = models.FloatField(null=True, blank=True)
    SNF = models.FloatField(null=True, blank=True)
    Rate = models.FloatField(null=True, blank=True)
    Totalrate = models.FloatField(null=True, blank=True)

class invoicedb(models.Model):
    Date = models.DateField(auto_now=True)
    Total = models.FloatField(null=True, blank=True)

