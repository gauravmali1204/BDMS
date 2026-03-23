from django.contrib import admin
from .models import order, orderItem
# Register your models here.

class orderItemInline(admin.TabularInline):
    model = orderItem
    extra = 1

@admin.register(order)
class orderAdmin(admin.ModelAdmin):
    list_display = ('id','custmer','status','total_amount','created_at')
    inlines = [orderItemInline]