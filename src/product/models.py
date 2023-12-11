from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import BaseModel
from django.utils.translation import gettext_lazy as _



class Product(BaseModel):
    REGULAR = "R"
    HAZMAT = "H"

    HAZAMAT_CHOISES = (
        (REGULAR, "Regular"),
        (HAZMAT, "Hazmat"),
    )

    name = models.CharField(_("Product Name"), max_length=255)
    price = models.FloatField(_("Price"), default=0.0)
    descreption = models.CharField(
        _("descreption"), max_length=255, null=True, blank=True
    )
    is_ban = models.BooleanField(default=False)
    hazmat_type = models.CharField(_("Hazamt Type"), max_length=255, choices=HAZAMAT_CHOISES, default=REGULAR)


