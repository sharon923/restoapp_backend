from django.db import models

# Create your models here.
class RestoModel(models.Model):
    name= models.CharField(default='',max_length=100)
    image= models.CharField(default='', max_length=500)
    description= models.CharField(default='',max_length=500)
    price= models.CharField(default='',max_length=100)
    rating= models.CharField(default='',max_length=100)
    available= models.CharField(default='',max_length=100)
    
