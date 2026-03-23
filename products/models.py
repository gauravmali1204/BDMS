from django.db import models

# Create your models here.
class products(models.Model):
    PRODUCT_TYPE = (
        ('PRODUCT','product'),
        ('SERVICE','service'),
    )

    name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100,choices=PRODUCT_TYPE)
    stock_unit = models.CharField(max_length=50,unique=True)  
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.product_type == 'SERVICE':
            self.stock = None
        return super().save(*args,**kwargs)
