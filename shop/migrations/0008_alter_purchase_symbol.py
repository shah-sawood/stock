# Generated by Django 4.1 on 2022-09-23 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0007_alter_purchase_symbol"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchase",
            name="symbol",
            field=models.CharField(max_length=7, unique=True),
        ),
    ]
