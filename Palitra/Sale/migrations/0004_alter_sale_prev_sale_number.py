# Generated by Django 4.1.2 on 2022-11-27 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Sale", "0003_sale_prev_sale_number_alter_sale_contract_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sale",
            name="prev_sale_number",
            field=models.IntegerField(default=0),
        ),
    ]