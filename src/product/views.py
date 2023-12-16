from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from base.views import BaseCreateView, BaseDetailView, BaseListView, BaseUpdateView, BaseView
from product.forms import ProductCreateForm, ProductUpdateForm
from django_datatables_too.mixins import DataTableMixin

from product.models import Product
from django.template.loader import get_template
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.



class ProductListView(BaseListView):
    model = Product
    template_name = "product/list_product.html"

class ProductCreateView(SuccessMessageMixin, BaseCreateView):
    model = Product
    form_class = ProductCreateForm
    success_message = "Product Created Successfully!!"
    template_name = "product/create_product.html"
    success_url = reverse_lazy("product:list_product")    

    def form_invalid(self, form):
        response = super().form_invalid(form)
        print("Create Product error:", form.errors)
        return response
        


class ProductDataTablesAjaxPagination(DataTableMixin, BaseView):
    model = Product

    def get_queryset(self):
        qs = Product.objects.all()
        return qs.order_by("-id")

    def _get_actions(self, obj):
        """Get action buttons w/links."""
        update_url = reverse("product:update_product", kwargs={"pk": obj.id})
        delete_url = reverse("product:delete_product")
        return f'<div class="row"><center><a href="{update_url}" title="Edit"><i class="ft-edit font-medium-3 mr-2"></i></a>  <label data-title="{obj.name}" title="Delete" data-url="{delete_url}" data-id="{obj.id}" id="delete_btn" class="danger p-0 ajax-delete-btn"><i class="ft-trash font-medium-3"></i></label></center></div>'


    def _get_product_image(self, obj):
        t = get_template("product/get_product_image.html")
        return t.render(
            {
                "height": 30,
                "img_url": obj.image,
                "obj": obj,

            }
        )    
    
    def _get_status(self, obj):
        t = get_template("product/get_product_status.html")
        return t.render(
            {"product": obj, "request": self.request}
    )

    def filter_queryset(self, qs):
        """Return the list of items for this view."""
        # If a search term, filter the query
        if self.search:
            return qs.filter(
                Q(name__icontains=self.search) |
                Q(name__icontains=self.search) 
                
            )
        return qs        
    
    def prepare_results(self, products):
        return [
            {
                # 'no' : index,
                'id': product.id,
                'name': product.name,
                'product_image': self._get_product_image(product),
                'price': product.price,
                'status': self._get_status(product),
                'actions': self._get_actions(product),
            }
            for product in products
        ]    
    
    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        return JsonResponse(context_data)    
    

class ProductUpdateView(SuccessMessageMixin, BaseUpdateView):
    model = Product
    form_class = ProductUpdateForm
    success_message = "Product Updated Successfully!!"
    template_name = "product/update_product.html"
    success_url = reverse_lazy("product:list_product")  

class ProductDetailView(BaseDetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'

class ProductDeleteAjaxView(BaseView):
    def post(self, request):
        product_id = self.request.POST.get("id")
        Product.objects.filter(id=product_id).delete()
        return JsonResponse({"message": "Product Deleted Successfully."})      