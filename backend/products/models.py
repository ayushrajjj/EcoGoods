from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='product_photos/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    is_sold = models.BooleanField(default=False)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Pending')
