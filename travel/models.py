from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    desc = models.CharField(max_length=2000)
    img = models.ImageField(upload_to='pics')
    