from django.shortcuts import render
from django.views import View
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

def tenantHomeView(request):
    return render(request, 'PropertiesApp/tenant_home.html')


def tenantsList(request):
    tenants = Tenant.objects.all()
    context = {'tenants': tenants}
    return render(request, "PropertiesApp/tenant_list.html", context)


""" class TenantHomeView(CreateView):
    model = Tenant
    template_name = "PropertiesApp/tenant_home.html"
    form_class = TenantCreateForm
    success_url = reverse_lazy("tenant_home")  # Adjust the URL name as needed

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tenants"] = Tenant.objects.all()  # Include all tenants in the context
        return context

    def post(self, request):
        form = TenantCreateForm(request.POST)
        if form.is_valid():
            tenant = form.save()
            context = {'tenant': tenant}
            return render(request,'tenant_home.html#tenant-item', context)  # Redirect to the index view after saving

        context = {'form': form}  # Include the form in the context for error display
        return render(request, "tenant_home.html", context)


    def form_valid(self, form):
        tenant = form.save()
        return super().form_valid(form)  # Redirects to success_url after saving

""" 

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
