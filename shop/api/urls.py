from django.urls import path, re_path
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [

    path('login/', obtain_jwt_token),

    path('mycategories/', views.CategoryListAPIView.as_view()),
    path('categories/<int:category_id>/', views.CategoryDetailAPIView.as_view()),

    path('products/', views.product_list),
    path('products/<int:product_id>/', views.product_detail),


    # path('products/', views.product_list),
    # path('products/<int:product_id>/', views.product_detail),
]