from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_buyer = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


class tbl_register(models.Model):
    name=models.CharField(max_length=50,null=True)
    email=models.EmailField(primary_key=True)
    mobile=models.CharField(max_length=20,null=True)
    password=models.CharField(max_length=200,null=True)
    Pincode=models.CharField(max_length=20,null=True)
    city=models.CharField(max_length=50,null=True)
    address=models.TextField(null=True)
    picture=models.ImageField(upload_to='static/userpic/')
