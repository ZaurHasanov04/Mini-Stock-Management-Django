# Generated by Django 4.1.2 on 2022-11-21 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Stock", "0003_alter_stock_active_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stock",
            name="active_number",
            field=models.IntegerField(),
        ),
    ]
