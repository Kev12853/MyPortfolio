from django.urls import path
from PropertiesApp.views import tenant_views, lease_views, dwelling_views

urlpatterns_tenants = [
    # path(
    #     "edit_tenant_inline.html",
    #     tenant_views.TestView,
    #     name="test",
    # ),
    path(
        "create_tenant/",
        tenant_views.QuickAddTenantView.as_view(),
        name="createTenant",
    ),
    path(
        "list_tenant.html",
        tenant_views.TenantListView.as_view(),
        name="list-tenant",
    ),
    path(
        "tenants.html",
        tenant_views.QuickAddTenantView.as_view(),
        name="list-tenants",
    ),
    path(
        "detail_tenant/<int:pk>/",
        tenant_views.TenantDetailView.as_view(),
        name="detail-tenant",
    ),
    path(
        "edit_tenant/<int:pk>/",
        tenant_views.TenantUpdateView,
        name="editTenant",
    ),
    path(
        "display_tenant/<int:pk>/",
        tenant_views.display_tenant,
        name="displayTenant",
    ),
    path(
        "delete_tenant/<int:pk>/",
        tenant_views.TenantDeleteView.as_view(),
        name="delete-tenant",
    ),
    path(
        "tenant_home",
        tenant_views.tenantHomeView,
        name="tenant-home",
    ),
]

urlpatterns_leases = [
    
    # ===========================
    path(
        "dwellings.html",
        dwelling_views.DwellingHomeView.as_view(),
        name="dwellings",
    ),
    path(
        "create_dwelling.html",
        dwelling_views.DwellingCreateView.as_view(),
        name="create-dwelling",
    ),
    path(
        "list_dwelling.html",
        dwelling_views.DwellingListView.as_view(),
        name="list-dwelling",
    ),
    path(
        "detail_dwelling/<int:pk>/",
        dwelling_views.DwellingDetailView.as_view(),
        name="detail-dwelling",
    ),
    path(
        "update_dwelling/<int:pk>/",
        dwelling_views.DwellingUpdateView.as_view(),
        name="update-dwelling",
    ),
    path(
        "delete_dwelling/<int:pk>/",
        dwelling_views.DwellingDeleteView.as_view(),
        name="delete-dwelling",
    ),
]

urlpatterns = urlpatterns_tenants + urlpatterns_leases + urlpatterns_dwellings
