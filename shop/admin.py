from django.contrib import admin
from .models import Product, Cart, CheckOut, Category,OderTracking


#OderTracking
admin.site.register(OderTracking)



# Product admin class
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['Product_name', 'Product_Description']
    list_filter = ['Product_Update', 'UnitPrice', 'category', 'available']
    prepopulated_fields = {'Product_slug': ('Product_name',)}


admin.site.register(Product, ProductAdmin)


# Category Admin
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('Category_Name',)}


admin.site.register(Category, CategoryAdmin)


# Product admin class
class CartAdmin(admin.ModelAdmin):
    search_fields = ['Product_Code', ]


admin.site.register(Cart, CartAdmin)


# Checkout admin class
class CheckoutAdmin(admin.ModelAdmin):
    search_fields = ['user', 'Country', ]
    list_filter = ['user', 'Country', 'Payment_Method', 'City']


admin.site.register(CheckOut, CheckoutAdmin)
