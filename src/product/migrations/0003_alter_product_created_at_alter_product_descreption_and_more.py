# Generated by Django 4.2.8 on 2023-12-16 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 12, 16, 11, 15, 16, 47057, tzinfo=datetime.timezone.utc
                )
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="product",
            name="descreption",
            field=models.TextField(blank=True, null=True, verbose_name="descreption"),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 12, 16, 11, 15, 32, 875295, tzinfo=datetime.timezone.utc
                )
            ),
            preserve_default=False,
        ),
    ]