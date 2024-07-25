from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login page if user is not authenticated
    products = Product.objects.filter(is_sold=False)
    return render(request, 'index.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        if request.user == product.seller:
            if 'delete' in request.POST:
                product.delete()
                return redirect('index')
            elif 'update' in request.POST:
                form = ProductForm(request.POST, request.FILES, instance=product)
                if form.is_valid():
                    form.save()
                    return redirect('product_detail', pk=pk)
        else:
            # Handle contacting logic here if needed
            pass
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'product_detail.html', {'product': product, 'form': form})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def contact_seller(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        # Handle contacting logic here
        pass
    return render(request, 'contact_seller.html', {'product': product})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to the index view
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after signup
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def user_orders(request):
    orders = Order.objects.filter(buyer=request.user)
    return render(request, 'user_orders.html', {'orders': orders})

@login_required
def profile_view(request):
    return render(request, 'profile.html')

def logout_view(request):
    logout(request)
    return redirect('login')
