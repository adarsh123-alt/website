from django.db import models
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=12)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    date=models.DateField()
