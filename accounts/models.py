from django.db import models
from django.contrib.auth.models import AbstractUser,User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, related_name = 'profile', on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'profile/', default = 'profile/default.png')


    def __str__(self) -> str:
        return self.user.username