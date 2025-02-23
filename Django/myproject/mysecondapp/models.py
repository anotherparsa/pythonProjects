from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=25)
    password = models.CharField(max_length=32)
    age = models.IntegerField(default=-1)
    rule = models.CharField (max_length=50, default="user")
    suspended = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.username}"
    