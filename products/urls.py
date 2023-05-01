from django.urls import path

from products import views

app_name = 'products'

urlpatterns = [
    path('', views.get_products_list, name='products'),
    path('product/<int:pk>/', views.get_product_detail, name='product_detail'),
    path('category/<int:pk>/', views.get_products_list_by_category, name='category'),
    path('categories/', views.categories, name='create_category')
]