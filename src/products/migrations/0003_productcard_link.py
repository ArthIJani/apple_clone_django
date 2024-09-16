# Generated by Django 5.1.1 on 2024-09-15 04:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_productcard"),
    ]

    operations = [
        migrations.AddField(
            model_name="productcard",
            name="link",
            field=models.URLField(
                blank=True,
                help_text="URL for the product page",
                null=True,
                validators=[django.core.validators.URLValidator()],
            ),
        ),
    ]
