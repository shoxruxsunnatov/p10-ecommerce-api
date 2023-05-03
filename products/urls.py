from django.urls import path

from products import views

urlpatterns = [
    path("", views.ProductListCreateView.as_view(), name="products_list"),
    path("<int:pk>/", views.ProductDetailView.as_view(), name='product_detail')
]
