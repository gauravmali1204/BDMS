from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class profile(models.Model):
    ROLE_CHOICES = (
        ('ADMIN','admin'),
        ('MANAGER','manager'),
        ('STAFF','staff'),

    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=20,choices=ROLE_CHOICES)
    
    