from django.db import models
from custmers.models import custmer
from products.models import products
from django.contrib.auth.models import User
# Create your models here.

class order(models.Model):
    STATUS_CHOICES =(
        ('PENDING','pending'),
        ('COMPLETED','completed'),
        ('CANCELLED','cancelled'),
    )

    custmer = models.ForeignKey(custmer,on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='PENDING')
    total_amount = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"order #{self.id}"
    
class orderItem(models.Model):
    order = models.ForeignKey(order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(products,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def get_total(self):
        return self.quantity * self.price