from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy

from PropertiesApp.business_logic import test1
from PropertiesApp.models.tenant_model import Tenant
from PropertiesApp.forms.tenant_forms import (
    QuickAddTenant_Form,
    TenantCreateForm,
    TenantListForm,
    TenantDetailForm,
    TenantDeleteForm,
    TenantUpdateForm,

)


def TestView(request):
    return render(request, "PropertiesApp/test.html")


def tenantHomeView(request):
    return render(request, 'PropertiesApp/tenant_home.html')


def tenantsList(request):
    tenants = Tenant.objects.all()
    context = {'tenants': tenants}
    return render(request, "PropertiesApp/tenant_list.html", context)


class QuickAddTenantView(CreateView):
    model = Tenant
    form_class = QuickAddTenant_Form
    template_name = "PropertiesApp/tenant_list.html"
    success_url = reverse_lazy("alist-tenant")

    def post(self, request, *args, **kwargs):
        form = QuickAddTenant_Form(request.POST)
        if form.is_valid():
            tenant = form.save()
            context={'tenant': tenant}
            return render(request, 'PropertiesApp/tenant_list.html#add-tenant', context)

        context = {"form": form, "tenants": Tenant.objects.all()}
        return render(request, "PropertiesApp/tenant_list.html", context)

    def get(self, request, *args, **kwargs):
        form = QuickAddTenant_Form()
        context = {"form": form, "tenants": Tenant.objects.all()}
        return render(request, "PropertiesApp/tenant_list.html", context)


class TenantListView(ListView):
    model = Tenant
    form_class = TenantListForm
    context_object_name = "tenants"
    template_name = "PropertiesApp/list_tenant.html"

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
    success_url = reverse_lazy("alist-tenant")

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         usecase = test1.test()
    #         # You can call methods on the usecase object here


class TenantDeleteView(DeleteView):
    model = Tenant
    form_class = TenantDeleteForm
    template_name = "PropertiesApp/user_input/f_delete_tenant.html"
    success_url = reverse_lazy("alist-tenant")
