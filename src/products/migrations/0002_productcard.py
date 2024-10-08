# Generated by Django 5.1.1 on 2024-09-15 04:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductCard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        help_text="Product image", upload_to="product_images/"
                    ),
                ),
                (
                    "alt_text",
                    models.CharField(
                        help_text="Alternative text for the image", max_length=100
                    ),
                ),
                (
                    "has_free_engraving",
                    models.BooleanField(
                        default=False,
                        help_text="Whether the product offers free engraving",
                    ),
                ),
                ("name", models.CharField(help_text="Product name", max_length=100)),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Product price",
                        max_digits=8,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "order",
                    models.IntegerField(
                        default=0,
                        help_text="Order in which the product should appear (lower numbers first)",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Card",
                "verbose_name_plural": "Product Cards",
                "ordering": ["order", "name"],
            },
        ),
    ]
