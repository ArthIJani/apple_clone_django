from django.db import models
from django.core.validators import URLValidator, MinValueValidator

class NewProductCard(models.Model):
    title = models.CharField(max_length=100, help_text="Text for the h3 tag (e.g., 'GET READY')")
    subtitle = models.CharField(max_length=200, help_text="Text for the h2 tag")
    description = models.TextField(help_text="Text for the p tag")
    link_url = models.CharField(max_length=200, validators=[URLValidator()], help_text="URL for the card link (e.g., '/iphone-pre-order')")
    background_image = models.ImageField(upload_to='card_backgrounds/', help_text="Background image for the card")
    order = models.IntegerField(default=0, help_text="Order in which the card should appear (lower numbers first)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "New-Products Card"
        verbose_name_plural = "New-Product Cards"
        ordering = ['order', '-created_at']  # Order by 'order' field, then by creation date


class ProductCard(models.Model):
    image = models.ImageField(upload_to='product_images/', help_text="Product image")
    alt_text = models.CharField(max_length=100, help_text="Alternative text for the image")
    has_free_engraving = models.BooleanField(default=False, help_text="Whether the product offers free engraving")
    name = models.CharField(max_length=100, help_text="Product name")
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)], help_text="Product price")
    order = models.IntegerField(default=0, help_text="Order in which the product should appear (lower numbers first)")
    link = models.URLField(
        max_length=200, 
        validators=[URLValidator()], 
        help_text="URL for the product page",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Product Card"
        verbose_name_plural = "Product Cards"

    @property
    def formatted_price(self):
        return f"${self.price:.2f}"