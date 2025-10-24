"""
URL configuration for my_dds_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('all_lists/', AllListsView.as_view(), name='all_lists'),

    path('status/add/', TransactionStatusCreateView.as_view(), name='transaction_status_create'),
    path('status/<int:pk>/edit/', TransactionStatusUpdateView.as_view(), name='transaction_status_update'),
    path('status/<int:pk>/delete/', TransactionStatusDeleteView.as_view(), name='transaction_status_delete'),

    path('type/add/', TransactionTypeCreateView.as_view(), name='transaction_type_create'),
    path('type/<int:pk>/edit/', TransactionTypeUpdateView.as_view(), name='transaction_type_update'),
    path('type/<int:pk>/delete/', TransactionTypeDeleteView.as_view(), name='transaction_type_delete'),

    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    path('subcategory/add/', SubcategoryCreateView.as_view(), name='subcategory_create'),
    path('subcategory/<int:pk>/edit/', SubcategoryUpdateView.as_view(), name='subcategory_update'),
    path('subcategory/<int:pk>/delete/', SubcategoryDeleteView.as_view(), name='subcategory_delete'),

    path('transaction/create/', TransactionCreateUpdateView.as_view(), name='transaction_create'),
    path('transaction/update/<int:pk>/', TransactionCreateUpdateView.as_view(), name='transaction_update'),
    path('transaction/<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction_delete'),

    path('ajax/load_categories/', load_categories, name='ajax_load_categories'),
    path('ajax/load_subcategories/', load_subcategories, name='ajax_load_subcategories'),

    path('', TransactionListView.as_view(), name='transaction_list'),
]
