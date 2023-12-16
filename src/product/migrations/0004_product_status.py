# Generated by Django 4.2.8 on 2023-12-16 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0003_alter_product_created_at_alter_product_descreption_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="status",
            field=models.CharField(
                choices=[("active", "Active"), ("inactive", "Inactive")],
                default="active",
                max_length=10,
                verbose_name="Status",
            ),
        ),
    ]
