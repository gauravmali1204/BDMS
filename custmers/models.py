from django.db import models

# Create your models here.
class custmer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=10)
    gst_number=models.CharField(max_length=20,blank=True,null=True)
    address=models.TextField(blank=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name