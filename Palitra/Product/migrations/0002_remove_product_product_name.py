# Generated by Django 4.1.2 on 2022-11-09 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Product", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="product_name",
        ),
    ]
