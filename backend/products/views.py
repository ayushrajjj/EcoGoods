from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order
from .forms import ProductForm, OrderForm

def index(request):
    products = Product.objects.filter(is_sold=False)
    return render(request, 'index.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def contact_seller(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        # Handle contacting logic here
        pass
    return render(request, 'contact_seller.html', {'product': product})

def login_view(request):
    if request.method == 'POST':
        # Handle login logic
        pass
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        # Handle signup logic
        pass
    return render(request, 'signup.html')

def user_orders(request):
    orders = Order.objects.filter(buyer=request.user)
    return render(request, 'user_orders.html', {'orders': orders})
