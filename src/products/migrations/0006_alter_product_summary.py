# Generated by Django 4.1 on 2022-08-10 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_product_featured"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product", name="summary", field=models.TextField(blank=True),
        ),
    ]