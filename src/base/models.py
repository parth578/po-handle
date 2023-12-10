from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=False, null=True)
    updated_at = models.DateTimeField(auto_now_add=False, null=True)

    class Meta:
        abstract = True
