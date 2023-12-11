from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import BaseModel
from product.models import Product
from django.utils.translation import gettext_lazy as _

from vendor.models import Vendor

# Create your models here.


class PurchaseOrder(BaseModel):
    order_number = models.CharField(_("Order Number"), max_length=255)
    date = models.DateTimeField(_("Date"))
    vendor = models.ForeignKey(Vendor, related_name="vendors", on_delete=models.SET_NULL, null=True)
    vendor_name = models.CharField(_("Vendor Name"), max_length=255)
    igst = models.FloatField(_("IGST"), default=0.0)
    sgst = models.FloatField(_("SGST"), default=0.0)
    total_discount_percentage = models.FloatField(_("Percentage"), default=0.0)
    total_discount_price = models.FloatField(_("Price"), default=0.0)
    total_price = models.FloatField(_("Price"), default=0.0)


class PurchaseOrderProduct(BaseModel):
    purchase_order = models.ForeignKey(
        PurchaseOrder, on_delete=models.SET_NULL, related_name="purchase_orders", null=True
    )
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, related_name="products", null=True
    )
    purchase_order_number = models.CharField(_("Purchase Order Number"), max_length=255)
    product_name = models.CharField(_("Product Name"), max_length=255)
    quantity = models.PositiveIntegerField(_("Quantity"))
    discount_percentage = models.FloatField(_("Percentage"), default=0.0)
    discount_price = models.FloatField(_("Price"), default=0.0)
    total_product_price = models.FloatField(_("Price"), default=0.0)
