from django.contrib.auth.models import AbstractUser 

# Create your models here.
from django.db import models

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(verbose_name='Admin Status', default=False)
