# Generated by Django 4.1.2 on 2022-11-27 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Sale", "0002_remove_sale_sale_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="sale",
            name="prev_sale_number",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="sale",
            name="contract_type",
            field=models.CharField(
                choices=[("M", "Mebel"), ("T", "Texnika"), ("S", "Stol")],
                default="Mebel",
                max_length=1,
            ),
        ),
    ]