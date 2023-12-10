from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import BaseModel
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractUser, BaseModel):
    ADMIN = "admin"
    MANAGER = "manager"
    STAFF = "staff"
    VENDOR = "vendor"

    USER_ROLE = (
        (ADMIN, "Admin"),
        (MANAGER, "Manager"),
        (STAFF, "Staff"),
        (VENDOR, "Vendor"),
    )

    full_name = models.CharField(_("Name"), max_length=20)
    profile_photo = models.ImageField(_("Image"), upload_to="user-profile")
    role = models.CharField(_("Role"), choices=USER_ROLE, max_length=20)
    phone_number = models.CharField(_("Name"), max_length=20, null=True, blank=True)
    email = models.EmailField(_("Email"), unique=True)
