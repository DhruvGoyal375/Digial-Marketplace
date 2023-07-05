"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name="index"),
    path('product/<int:id>', views.detail,name='detail'),
    path('success/', views.payment_success_view,name='success'),
    path('failed/', views.payment_failed_view, name='failed'),
    path('api/checkout-session/<int:id>/', views.create_checkout_session,name='api_checkout_session'),
    path('createproduct/', views.create_product, name='createproduct'),
    path('editproduct/<int:id>', views.product_edit, name='editproduct'),
    path('delete/<int:id>', views.product_delete, name='delete'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='myapp/logout.html'), name='logout'),
    path('invalid/', views.invalid, name='invalid'),
    path('purchases/', views.my_purchases, name='purchases'),
    path('sales/', views.sales, name='sales'),
    
]
