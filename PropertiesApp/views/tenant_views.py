from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy

from PropertiesApp.models.tenant_model import Tenant
from PropertiesApp.forms.tenant_forms import (
    TenantCreateForm,
    TenantListForm,
    TenantDetailForm,
    TenantDeleteForm,
    TenantUpdateForm,
)


class TenantCreateView(CreateView):
    model = Tenant
    form_class = TenantCreateForm
    template_name = "PropertiesApp/user_input/f_create_tenant.html"
    success_url = reverse_lazy("list-tenant")


class TenantListView(ListView):
    model = Tenant
    form_class = TenantListForm
    context_object_name = "tenants"
    template_name = "PropertiesApp/list_tenant.html"


class TenantDetailView(DetailView):
    model = Tenant
    form_class = TenantDetailForm
    context_object_name = "tenant"
    template_name = "PropertiesApp/detail_tenant.html"


class TenantUpdateView(UpdateView):
    model = Tenant
    form_class = TenantUpdateForm
    template_name = "PropertiesApp/user_input/f_update_tenant.html"
    success_url = reverse_lazy("list-tenant")


class TenantDeleteView(DeleteView):
    model = Tenant
    form_class = TenantDeleteForm
    template_name = "PropertiesApp/user_input/f_delete_tenant.html"
    success_url = reverse_lazy("list-tenant")
