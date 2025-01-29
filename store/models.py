from django.db import models

from users.models import User


class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Drop(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    sortno = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('bulk', 'Bulk'),
    )
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    design = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, null=True)
    drop = models.ForeignKey(Drop, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier_name = models.CharField(max_length=120)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.courier_name


from django.db import models
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

# class Invoice(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     date_created = models.DateTimeField(default=timezone.now)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#
#     def __str__(self):
#         return f'Invoice {self.id} for {self.client.name}'