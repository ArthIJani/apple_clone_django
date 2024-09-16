from django.contrib import admin
from .models import NewProductCard, ProductCard

@admin.register(NewProductCard)
class NewProductCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'created_at', 'updated_at')
    search_fields = ('title', 'subtitle', 'description')


@admin.register(ProductCard)
class ProductCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'formatted_price', 'has_free_engraving', 'order', 'link')
    list_filter = ('has_free_engraving',)
    search_fields = ('name',)