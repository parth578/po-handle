from django.urls import path

from product.views import (
    ProductCreateView,
    ProductDataTablesAjaxPagination,
    ProductDeleteAjaxView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
)



app_name = "product"

urlpatterns = [
    path("", ProductListView.as_view(), name="list_product"),
    path("add/", ProductCreateView.as_view(), name="add_product"),
    path("product-list-ajax/",
        ProductDataTablesAjaxPagination.as_view(), name='product_list_ajax'),   
     path("<str:pk>/update/",
          ProductUpdateView.as_view(), name="update_product"),
     path("product-delete-ajax/", ProductDeleteAjaxView.as_view(), name="delete_product"),
     path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),



]
