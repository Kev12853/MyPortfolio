from urllib import response
from django.shortcuts import render, get_object_or_404
from django_htmx.http import trigger_client_event
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy

from PropertiesApp.business_logic import test1
from PropertiesApp.models.tenant_model import Tenant
from PropertiesApp.forms.tenant_forms import (
    Tenant_Form,
    TenantCreateForm,
    TenantListForm,
    TenantDetailForm,
    TenantDeleteForm,
    
)

def createTenant(request):
    form = Tenant_Form(request.POST)
    if form.is_valid():
        tenant = form.save()


# def TestView(request):
#     return render(request, "PropertiesApp/edit_tenant_inline.html")


def tenantHomeView(request):
    return render(request, "PropertiesApp/tenant_home.html")


def tenantsList(request):
    tenants = Tenant.objects.all()
    context = {"tenants": tenants}
    return render(request, "PropertiesApp/tenants.html", context)


class QuickAddTenantView(CreateView):
    form_class = Tenant_Form
    template_name = "tenants/add-tenant-modal.html"
    success_url = reverse_lazy("list-tenants")

    def form_valid(self, form):
        # Set the user before saving the form if you have logged in users
        # tenant = form.save(commit=False)
        # tenant.user = self.request.user

        tenant = form.save()
        # Prepare response for htmx
        context = {"tenant": tenant}
        response = render(self.request, "tenants/tenant_row.html", context)
        response["HX-Trigger"] = "tenant-added"
        return response

    def get(self, request, *args, **kwargs):
        form = Tenant_Form()
        context = {"form": form, "tenants": Tenant.objects.all()}
        return render(request, "PropertiesApp/tenants.html", context)


def TenantUpdateView(request, pk):
    # get the tenant from db
    tenant = get_object_or_404(Tenant, pk=pk)
    # Initialize the form with the tenant instance
    form = Tenant_Form(request.POST or None, instance=tenant)

    if request.method == "POST":
        if form.is_valid():
            tenant = form.save()
            return render(
                request,
                "tenants/tenant_row.html",
                {
                    "form": Tenant_Form(instance=tenant),
                    "tenant": tenant,
                },
            )

        # Handle invalid form scenario
        return render(
            request,
            "tenants/edit-tenant-modal.html",
            {
                "form": form,
                "tenant": tenant,
            },
        )

    # For GET request
    return render(
        request,
        "tenants/edit_tenant_inline.html",
        {
            "form": form,
            "tenant": tenant,
        },
    )

def display_tenant(request, pk):
    tenant = get_object_or_404(Tenant, pk=pk)
    return render(request, "tenants/tenant_row.html", {"tenant": tenant})

class TenantListView(ListView):
    model = Tenant
    form_class = TenantListForm
    context_object_name = "tenants"
    template_name = "PropertiesApp/list_tenant.html"


class TenantCreateView(CreateView):
    model = Tenant
    form_class = TenantCreateForm
    template_name = "PropertiesApp/f_create_tenant.html"
    # success_url = reverse_lazy("tenant-list")


class TenantDetailView(DetailView):
    model = Tenant
    form_class = TenantDetailForm
    context_object_name = "tenant"
    template_name = "PropertiesApp/detail_tenant.html"


class TenantDeleteView(DeleteView):
    model = Tenant
    form_class = TenantDeleteForm
    template_name = "PropertiesApp/f_delete_tenant.html"
    success_url = reverse_lazy("list-tenants")
