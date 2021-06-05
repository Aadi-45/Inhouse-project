from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    address = models.TextField(null=True)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username
    

