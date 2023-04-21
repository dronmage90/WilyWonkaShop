from django.urls import path, re_path
from . import views

urlpatterns = [
    path('companies/', views.company_list),
    path('companies/<int:company_id>/', views.company_detail),
    path('companies/<int:company_id>/vacancies/', views.products_detail),
    path('vacancies/', views.products_list),
    path('vacancies/<int:vacancy_id>/', views.product_one)
]
