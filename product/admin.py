from django.contrib import admin

from .models import Category, Order, Product

admin.site.register(Category)
admin.site.register(Order)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
