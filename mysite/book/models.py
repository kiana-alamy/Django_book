from django.db import models

# Create your models here.

class book(models.Model):
    title= models.CharField(max_length=100)
    auther= models.CharField(max_length=150)
    date= models.DateField
    pagese= models.IntegerField
    template= models.ImageField