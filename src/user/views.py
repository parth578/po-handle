from django.shortcuts import render
from base.views import BaseTemplateView
from django.views.generic import TemplateView
# Create your views here.
class BaseHomeTemplateView(TemplateView):
    template_name = "base.html"
