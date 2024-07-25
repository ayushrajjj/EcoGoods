from django.urls import path
from .views import index, product_detail, contact_seller, login_view, signup_view, user_orders, profile_view, logout_view

urlpatterns = [
    path('', index, name='index'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('contact/<int:pk>/', contact_seller, name='contact_seller'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('orders/', user_orders, name='user_orders'),
    path('profile/', profile_view, name='profile'),  # Ensure profile URL is included
    path('logout/', logout_view, name='logout'),
]
