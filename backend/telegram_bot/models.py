from django.db import models

# Create your models here.
class User(models.Model):

    def __init__(self):
        return self.name

    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    phone_number = models.IntegerField()
    username = models.CharField(max_length=20, null=True)
    language_code = models.CharField(max_length=8, null=True, blank=True)

    is_admin = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    