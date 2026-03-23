from django.contrib import admin
from .models import custmer
# Register your models here.

@admin.register(custmer)
class custmerAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','is_active')
    search_fields = ('name','email')