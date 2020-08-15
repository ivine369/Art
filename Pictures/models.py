from django.db import models

# Create your models here.
#category model
class Category(models.Model):
    name = models.CharField(max_length=200,unique=True)
   
#picture model
class Picture(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='pictures/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200,default=True)
    url = models.CharField(max_length=200,default=True)
     