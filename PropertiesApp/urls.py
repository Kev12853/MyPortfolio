from django.urls import path

from PropertiesApp.views import dwelling_views, lease_views, tenant_views

urlpatterns = [

    path('create_tenant.html', tenant_views.TenantCreateView.as_view(), name='create-tenant'),
    path('list_tenant.html', tenant_views.TenantListView.as_view(), name='list-tenant'),
    path('detail_tenant/<int:pk>/', tenant_views.TenantDetailView.as_view(), name='detail-tenant'),
    path('update_tenant/<int:pk>/', tenant_views.TenantUpdateView.as_view(), name='update-tenant'),
    path('delete_tenant/<int:pk>/', tenant_views.TenantDeleteView.as_view(), name='delete-tenant'),

    path('create_dwelling.html', dwelling_views.DwellingCreateView.as_view(), name='create-dwelling'),
    path('list_dwelling.html', dwelling_views.DwellingListView.as_view(), name='list-dwelling'),
    path('detail_dwelling/<int:pk>/', dwelling_views.DwellingDetailView.as_view(), name='detail-dwelling'),
    path('update_dwelling/<int:pk>/', dwelling_views.DwellingUpdateView.as_view(), name='update-dwelling'),
    path('delete_dwelling/<int:pk>/', dwelling_views.DwellingDeleteView.as_view(), name='delete-dwelling'),

    path('create_lease.html', lease_views.CreateNewLease.as_view(), name='create-lease'),
    path('list_lease.html', lease_views.LeaseListView.as_view(), name='list-lease'),
    path('detail_lease/<int:pk>/', lease_views.LeaseDetailView.as_view(), name='detail-lease'),
    path('update_lease/<int:pk>/', lease_views.LeaseUpdateView.as_view(), name='update-lease'),
    path('delete_lease/<int:pk>/', lease_views.LeaseDeleteView.as_view(), name='delete-lease'),


]
