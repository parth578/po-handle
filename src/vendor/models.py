from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import BaseModel
from django.utils.translation import gettext_lazy as _
from user.models import User
from product.models import Product

# Create your models here.


class Vendor(BaseModel):
    user = models.ForeignKey(User, related_name="vendors", on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ForeignKey(User, related_name="staffs", on_delete=models.CASCADE, null=True, blank=True)
    gst_number = models.CharField(_("Number"), max_length=255)
    address_line_1 = models.CharField(_("Address line 1"), max_length=255)
    address_line_2 = models.CharField(
        _("Address line 2"), max_length=255, null=True, blank=True
    )
    address_line_3 = models.CharField(
        _("Address line 3"), max_length=255, null=True, blank=True
    )
    city = models.CharField(_("City"), max_length=255)
    state = models.CharField(_("State"), max_length=255)
    zip_code = models.IntegerField(_("Zip Code"))
    country = models.CharField(_("Country"), max_length=255)


class VendorProduct(BaseModel):
    product = models.ForeignKey(
        Product, related_name="vendor_products", on_delete=models.SET_NULL, null=True
    )
    vendor = models.ForeignKey(
        Vendor, related_name="vendor", on_delete=models.SET_NULL, null=True
    )
