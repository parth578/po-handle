from django import forms
from vendor.models import Vendor

class VendorCreateForm(forms.ModelForm):
    
    class Meta:
        model = Vendor
        fields = "__all__"

    def __init__(self,  *args, **kwargs):
        super(VendorCreateForm, self).__init__(*args, **kwargs)
        pass

class VendorUpdateForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = "__all__"

    def __init__(self,  *args, **kwargs):
        super(VendorUpdateForm, self).__init__(*args, **kwargs)
        pass
