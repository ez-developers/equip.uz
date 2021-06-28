from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    phone_number = models.IntegerField(max_length=12)
    username = models.CharField(max_length=20, null=True)

