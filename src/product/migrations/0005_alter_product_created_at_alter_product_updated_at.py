# Generated by Django 4.2.8 on 2023-12-16 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0004_product_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]