# Generated by Django 4.1 on 2022-09-23 07:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_portfolio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="portfolio",
            name="cash",
            field=models.PositiveIntegerField(
                default=10000, validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
    ]
