from django.urls import path, re_path
from . import views

urlpatterns = [
    path('companies/', views.company_list),
    path('companies/home', views.company_list_home),
    path('companies/rest', views.company_list_rest),
    path('companies/<int:company_id>/', views.company_detail),
    path('companies/<int:company_id>/products/', views.products_detail),
    path('products/', views.products_list),
    path('products/<int:product_id>/', views.product_one),
    path('products/home', views.products_list_home),
    path('products/rest', views.products_list_rest)
]
