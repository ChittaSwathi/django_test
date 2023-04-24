from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cat_name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'cat_id']

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
