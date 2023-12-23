from django.urls import path
from user.views import (
BaseHomeTemplateView,
) 


urlpatterns = [
    path("base-templateview/", BaseHomeTemplateView.as_view(), name="base_tempalteview"),
]
