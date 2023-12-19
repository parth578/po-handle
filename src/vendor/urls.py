from django.urls import path

from vendor.views import (
    VendorListView,
    VendorCreateView,
    VendorDataTablesAjaxPagination,
    VendorUpdateView,
    VendorDetailView,
    VendorDeleteAjaxView,
)


app_name = "vendor"

urlpatterns = [
    path("", VendorListView.as_view(), name="list_vendor"),
    path("reg/", VendorCreateView.as_view(), name="registration_vendor"),
    path(
        "product-list-ajax/",
        VendorDataTablesAjaxPagination.as_view(),
        name="vendor_list_ajax",
    ),
    path("<str:pk>/update/", VendorUpdateView.as_view(), name="update_vendor"),
    path("product/<int:pk>/", VendorDetailView.as_view(), name="vendor_detail"),
    path("product-delete-ajax/", VendorDeleteAjaxView.as_view(), name="delete_product"),
]
