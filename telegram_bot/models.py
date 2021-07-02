from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True, blank=False)
    last_name = models.CharField(max_length=50, null=True, blank=False)
    phone_number = models.IntegerField()
    username = models.CharField(max_length=20, null=True, blank=False)
    language_code = models.CharField(max_length=8, null=True, blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, null=True)

class Product(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)




