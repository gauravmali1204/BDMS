from django.contrib import admin
from.models import Invoice,payment
# Register your models here.

class paymentinline(admin.TabularInline):
    model = payment
    extra = 1

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number','order','total_amount','created_at')
    inlines = [paymentinline]