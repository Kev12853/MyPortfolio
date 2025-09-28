from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from PropertiesApp.forms.lease_forms import LeaseCreateForm, LeaseDeleteForm, LeaseListForm
from PropertiesApp.models.lease_model import Lease


class CreateNewLease(CreateView):
    model = Lease
    form_class = LeaseCreateForm
    template_name = "PropertiesApp/user_input/f_create_lease.html"
    success_url = reverse_lazy("list-lease")


class LeaseListView(ListView):
    model = Lease
    form_class = LeaseListForm
    context_object_name = "leases"
    template_name = "PropertiesApp/list_lease.html"


class LeaseDetailView(DetailView):
    model = Lease
    form_class = LeaseListForm
    context_object_name = "lease"
    template_name = "PropertiesApp/detail_lease.html"


class LeaseUpdateView(UpdateView):
    model = Lease
    form_class = LeaseListForm
    template_name = "PropertiesApp/user_input/f_update_lease.html"
    success_url = reverse_lazy("list-lease")


class LeaseDeleteView(DeleteView):
    model = Lease
    form_class = LeaseDeleteForm
    template_name = "PropertiesApp/user_input/f_delete_lease.html"
    success_url = reverse_lazy("list-lease")
