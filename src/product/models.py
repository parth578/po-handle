from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import BaseModel
from django.utils.translation import gettext_lazy as _

class product(BaseModel):
     
    product_name = models.CharField(_("Name"), max_length=20)
    product_price = models.FloatField()
    product_descreption = models.CharField(_("Name"),max_length=500)
    is_ban = models.BooleanField(_("Name"),max_length=20)
    # hazmat_type = models.


# Create your models here.
