"""
URL configuration for Quotation project.

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

from quot_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.index,name='index'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('home', views.userlogin, name='home'),

    path('home_page', views.home_page, name='home_page'),

    path('uom', views.uom, name='uom'),
    path('uom_list', views.uom_list, name='uom_list'),

    path('company', views.company, name='company'),
    path('company_list', views.company_list, name='company_list'),
    path('company/delete/<int:id>/', views.delete_company, name='delete_company'),
    path('company/edit/<int:pk>', views.edit_company, name='edit_company'),

    path('customer', views.customer, name='customer'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/edit/<int:pk>', views.edit_customer, name='edit_customer'),
    path('customer/delete/<int:customer_id>/', views.delete_customer, name='delete_customer'),

    path('item', views.item, name='item'),
    path('item_list', views.item_list, name='item_list'),
    path('item/edit/<int:pk>', views.edit_item, name='edit_item'),
    path('item/delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('fetch_item_data/', views.fetch_item_data, name='fetch_item_data'),
    path('fetch_item_names/', views.fetch_item_names, name='fetch_item_names'),

    path('successPage',views.successPage,name='successPage'),
    path('customer_name', views.customer_name, name='customer_name'),
    path('fetch_customer_data/', views.fetch_customer_data, name='fetch_customer_data'),

    path('quotation',views.quotation,name='quotation'),
    path('save_purchase_details/', views.save_purchase_details, name='save_purchase_details'),
    path('receipt/<int:quot_Number>/', views.receipt_view, name='receipt_view'),

    path('Quotation_list', views.Quotation_list, name='Quotation_list'),
    path('quotation/delete/<int:id>/', views.delete_quotation, name='delete_quotation'),
    path('edit_quotation/<int:pk>/', views.edit_Quotation, name='edit_quotation'),

    path('receipt/<int:id>/', views.receipt_view, name='receipt1'),










]
