from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import BaseModel

# Create your models here.

class User(AbstractUser, BaseModel):
    pass
