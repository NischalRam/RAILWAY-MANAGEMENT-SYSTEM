from django.db import models

# Create your models here.

class booking(models.Model):

    customer = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=10)
    goingfrom = models.CharField(max_length=200)
    to = models.CharField(max_length=200)
    date = models.DateField()

class newuser(models.Model):

    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    username  = models.CharField(max_length=100)
    password  = models.CharField(max_length=100)
    email    = models.EmailField(max_length=100)
    

    
