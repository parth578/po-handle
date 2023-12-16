from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    RedirectView,
    TemplateView,
    UpdateView,
    View,
)
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin



# -----------------------------------------------------------------------------
# Generic Views
# -----------------------------------------------------------------------------
class BaseView(SuccessMessageMixin, LoginRequiredMixin, View):
    """View with LoginRequiredMixin and PermissionRequiredMixin."""

    pass


class BaseRedirectView(SuccessMessageMixin, LoginRequiredMixin, RedirectView):
    """
    Return the URL redirect to. Keyword arguments from the URL pattern
    match generating the redirect request are provided as kwargs to this
    method.
    """

    pass


class BaseLoginRequiredView(SuccessMessageMixin, LoginRequiredMixin, View):
    """View with LoginRequiredMixin."""

    pass


class BaseTemplateView(SuccessMessageMixin, LoginRequiredMixin, TemplateView):
    """TemplateView CBV with LoginRequiredMixin and PermissionRequiredMixin."""

    pass


class BaseFormView(SuccessMessageMixin, LoginRequiredMixin, FormView):
    """FormView CBV with LoginRequiredMixin and PermissionRequiredMixin."""

    pass


class BaseListView(
    LoginRequiredMixin,
    ListView,
):
    """ListView CBV with LoginRequiredMixin and PermissionRequiredMixin."""

    pass


class BaseDetailView(SuccessMessageMixin, LoginRequiredMixin, DetailView):
    """DetailView CBV with LoginRequiredMixin and PermissionRequiredMixin."""

    pass


class BaseCreateView(
    LoginRequiredMixin,
    CreateView,
):
    pass


class BaseUpdateView(
    LoginRequiredMixin,
    UpdateView,
):
    pass


class BaseDeleteView(
    LoginRequiredMixin,
    DeleteView,
):
    """CBV to delete a model record - both Ajax and POST requests."""

    pass
