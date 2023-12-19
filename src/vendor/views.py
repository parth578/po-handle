from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from base.views import (
    BaseCreateView,
    BaseDetailView,
    BaseListView,
    BaseUpdateView,
    BaseView,
)
from vendor.forms import VendorCreateForm, VendorUpdateForm
# from django_datatables_too.mixins import DataTableMixin

from vendor.models import Vendor
from django.template.loader import get_template
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


class VendorListView(BaseListView):
    model = Vendor
    template_name = "vendor/list_vendor.html"


class VendorCreateView(SuccessMessageMixin, BaseCreateView):
    model = Vendor
    form_class = VendorCreateForm
    success_message = "You have registered Successfully!!"
    template_name = "vendor/create_vendor.html"
    success_url = reverse_lazy("vendor:list_vendor")

    def form_invalid(self, form):
        response = super().form_invalid(form)
        print("Registration error:", form.errors)
        return response


class VendorDataTablesAjaxPagination(DataTableMixin, BaseView):
    model = Vendor
    pass


class VendorUpdateView(SuccessMessageMixin, BaseUpdateView):
    model = Vendor
    form_class = VendorUpdateForm
    success_message = "Vendor details Updated Successfully!!"
    template_name = "vendor/update_vendor.html"
    success_url = reverse_lazy("vendor:list_vendor")


class VendorDetailView(BaseDetailView):
    model = Vendor
    template_name = "vendor/vendor_detail.html"
    context_object_name = "vendor"


class VendorDeleteAjaxView(BaseView):
    def post(self, request):
        vendor_id = self.request.POST.get("id")
        Vendor.objects.filter(id=vendor_id).delete()
        return JsonResponse({"message": "Vendor Details Deleted Successfully."})
