from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import BaseModel
from django.utils.translation import gettext_lazy as _



class Product(BaseModel):

    def img_directory_path(instance, filename):
        return "product-image/{0}/{1}".format(instance.name, filename)

    REGULAR = "R"
    HAZMAT = "H"

    HAZAMAT_CHOISES = (
        (REGULAR, "Regular"),
        (HAZMAT, "Hazmat"),
    )

    ACTIVE = "active"
    INACTIVE = "inactive"

    STATUS_CHOICES = (
        (ACTIVE, "Active"),
        (INACTIVE, "Inactive"),
    )    

    name = models.CharField(_("Product Name"), max_length=255)
    price = models.FloatField(_("Price"), default=0.0)
    descreption = models.TextField(
        _("descreption"), null=True, blank=True
    )
    is_ban = models.BooleanField(default=False)
    hazmat_type = models.CharField(_("Hazamt Type"), max_length=255, choices=HAZAMAT_CHOISES, default=REGULAR)
    image = models.ImageField(_("Image"), upload_to=img_directory_path, null=True, blank=True)
    status = models.CharField(_('Status'), max_length=10, choices=STATUS_CHOICES, default=ACTIVE)

    def save(self, *args, **kwargs):
        if not self.status:
            self.status = self.ACTIVE
        super().save(*args, **kwargs)    
