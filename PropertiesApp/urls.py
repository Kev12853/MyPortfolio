from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from PropertiesApp.views import dwelling_views, lease_views, tenant_views

urlpatterns_tenants = [
    path(
        "create_tenant.html",
        tenant_views.TenantCreateView.as_view(),
        name="createTenant",
    ),
    path(
        "tenants.html",
        tenant_views.QuickAddTenantView.as_view(),
        name="list-tenants",
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
    # path(
    #     "list_tenant.html", tenant_views.TenantListView.as_view(), name="list-tenants"
    # ),
    path(
        "tenant_list.html",
        tenant_views.QuickAddTenantView.as_view(),
        name="alist-tenant",
    ),
    path(
        "detail_tenant/<int:pk>/",
        tenant_views.TenantDetailView.as_view(),
        name="detail-tenant",
    ),
    path(
        "update_tenant/<int:pk>/",
        tenant_views.TenantUpdateView,
        name="update-tenant",
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
    path(
        "create_lease.html", lease_views.CreateNewLease.as_view(), name="create-lease"
    ),
    path("list_lease.html", lease_views.LeaseListView.as_view(), name="list-lease"),
    path(
        "detail_lease/<int:pk>/",
        lease_views.LeaseDetailView.as_view(),
        name="detail-lease",
    ),
    path(
        "update_lease/<int:pk>/",
        lease_views.LeaseUpdateView.as_view(),
        name="update-lease",
    ),
    path(
        "delete_lease/<int:pk>/",
        lease_views.LeaseDeleteView.as_view(),
        name="delete-lease",
    ),
]

urlpatterns_dwellings = [
    path("students", dwelling_views.HomePageView.as_view(), name="studenthome"),
    path("get_student_list", dwelling_views.get_student_list, name="get_student_list"),
    path("add_student", dwelling_views.add_student, name="add_student"),
    path(
        "add_student_submit",
        dwelling_views.add_student_submit,
        name="add_student_submit",
    ),
    path(
        "add_student_cancel",
        dwelling_views.add_student_cancel,
        name="add_student_cancel",
    ),
    path(
        "<int:student_pk>/delete_student",
        dwelling_views.delete_student,
        name="delete_student",
    ),
    path(
        "<int:student_pk>/edit_student",
        dwelling_views.edit_student,
        name="edit_student",
    ),
    path(
        "<int:student_pk>/edit_student_submit",
        dwelling_views.edit_student_submit,
        name="edit_student_submit",
    ),
    # ==========================
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

urlpatterns_media = [static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)]

urlpatterns = (
    urlpatterns_tenants
    + urlpatterns_leases
    + urlpatterns_dwellings
)
# Serve media files in development
if settings.DEBUG:  # Ensure this only runs in development mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
