from django.urls import path, re_path
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [

    path('login/', obtain_jwt_token),

    path('mycategories/', views.CategoryListAPIView.as_view()),
    path('categories/<int:category_id>/', views.CategoryDetailAPIView.as_view()),

    path('products/', views.product_list),
    path('products/<int:product_id>/', views.product_detail),
    path('products/rest/', views.product_list_rest),
    path('products/home/', views.product_list_home),
    path('products/bycateg/<int:category_id>/', views.product_by_category),
    path('products/do/', views.do_product),
    # path('products/', views.product_list),
    # path('products/<int:product_id>/', views.product_detail),
]