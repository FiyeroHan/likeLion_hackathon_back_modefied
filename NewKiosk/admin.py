from django.contrib import admin
from .models import Category, Product, Order, Product_Order, Receipt

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Product_Order)
admin.site.register(Receipt)