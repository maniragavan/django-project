from django.db import models

# Create your models here.

class Destination(models.Model):     
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    price = models.IntegerField()
    Duration = models.IntegerField()
    offer = models.BooleanField(default=False)