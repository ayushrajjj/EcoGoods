from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('contact/<int:pk>/', views.contact_seller, name='contact_seller'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('orders/', views.user_orders, name='user_orders'),
]
