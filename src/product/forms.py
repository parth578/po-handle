from django import forms
from product.models import Product
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self,  *args, **kwargs):
        super(ProductCreateForm, self).__init__(*args, **kwargs)

        self.fields["hazmat_type"].widget.attrs["class"] = "select2-data-array form-control select2-list"
        self.fields['descreption'].widget.attrs = {'class': 'form-control','rows': 4}
        self.fields['status'].widget = forms.HiddenInput()
        # self.fields['status'].initial = Product.ACTIVE

        # # Use crispy forms to enhance rendering
        # self.helper = FormHelper(self)
        # self.helper.form_method = 'post'
        # self.helper.add_input(Submit('submit', 'Save'))        


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self,  *args, **kwargs):
        super(ProductUpdateForm, self).__init__(*args, **kwargs)

        self.fields["hazmat_type"].widget.attrs["class"] = "select2-data-array form-control select2-list"
        self.fields['descreption'].widget.attrs = {'class': 'form-control','rows': 4}
