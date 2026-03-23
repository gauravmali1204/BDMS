from django.contrib import admin
from .models import products
# Register your models here.
@admin.register(products)
class productAdmin(admin.ModelAdmin):
    list_display = ('name','product_type','price','stock','is_active')
    search_fields = ('name','stock_unit')
    list_filter = ('product_type','is_active')
