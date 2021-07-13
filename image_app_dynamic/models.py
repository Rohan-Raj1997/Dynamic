from os import name
from django.db import models

# Create your models here.
class Image(models.Model):
    Caption=models.CharField(max_length=50)
    Image=models.ImageField(upload_to='new/%y')
    State_Name=models.CharField(max_length=50)
    City_Name=models.CharField(max_length=50)
    Famous_Food=models.CharField(max_length=50)
    Famous_River=models.CharField(max_length=50)
    Population=models.PositiveIntegerField()


    def __str__(self):
        return self.Caption