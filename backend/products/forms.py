from django import forms
from .models import Product, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'photo', 'price', 'description', 'category']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product']
