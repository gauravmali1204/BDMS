from django.db import models
from orders.models import order
# Create your models here.

class Invoice(models.Model):
    order = models.OneToOneField(order,on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=30,unique=True)
    gst_percent = models.DecimalField(max_digits=5,decimal_places=2,default=18)
    gst_amount = models.DecimalField(max_digits=10,decimal_places=2)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.invoice_number
    

class payment(models.Model):
    PAYMENT_MODE = (
        ('CASH','cash'),
        ('CARD','card'),
        ('UPI','upi'),
        ('BANK','bank transfer'),
    )


    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE,related_name='payments')
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    payment_mode = models.CharField(max_length=20,choices=PAYMENT_MODE)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.invoice.invoice_number}-{self.amount}"
    