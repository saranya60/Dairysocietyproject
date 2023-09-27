from django.db import models

# Create your models here.
class employeedb(models.Model):
    Empname = models.CharField(max_length=100, null=True, blank=True)
    Designation = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=1000, null=True, blank=True)
    Dateofbirth = models.CharField(max_length=1000, null=True, blank=True)
    Gender = models.CharField(max_length=10, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Salary = models.IntegerField(null=True, blank=True)
    Image = models.ImageField(upload_to="employee", null=True, blank=True)

class postdb(models.Model):
    Designation = models.CharField(max_length=100, null=True, blank=True)

class farmerdb(models.Model):
    Cardno = models.CharField(max_length=100, null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=1000, null=True, blank=True)
    Dateofbirth = models.CharField(max_length=1000, null=True, blank=True)
    Gender = models.CharField(max_length=10, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="employee", null=True, blank=True)
class attendancedb(models.Model):
    Date = models.DateField(auto_now=True)
    Empname = models.CharField(max_length=100, null=True, blank=True)
    Attendance = models.CharField(max_length=10, null=True, blank=True)

class registerdb(models.Model):
    Username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    Password = models.CharField(max_length=50, null=True, blank=True)
class imagedb(models.Model):
    Image = models.ImageField(upload_to="image", null=True, blank=True)
class cartdb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Productname = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Totalprice = models.IntegerField(null=True, blank=True)
    Price = models.FloatField(null=True, blank=True)
class orderdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Address = models.TextField(max_length=100, null=True, blank=True)
    Pin = models.IntegerField(null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Subtotal = models.IntegerField(null=True, blank=True)
    Date = models.DateField(auto_now=True)
    Status = models.CharField(max_length=20,default='pending')

class messagedb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Message = models.TextField(max_length=100, null=True, blank=True)
    Date = models.DateField(auto_now=True)