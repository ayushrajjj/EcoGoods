# products/admin.py

from django.contrib import admin
from .models import Category, Product, Order

# Register the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

# Register the Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'seller', 'is_sold')
    search_fields = ('name', 'description', 'category__name', 'seller__username')
    list_filter = ('is_sold', 'category', 'seller')
    ordering = ('-id',)

# Register the Order model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'buyer', 'status')
    search_fields = ('product__name', 'buyer__username', 'status')
    list_filter = ('status',)
    ordering = ('-id',)
