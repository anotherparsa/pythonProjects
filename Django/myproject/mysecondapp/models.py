from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=25)
    password = models.CharField(max_length=32)
    