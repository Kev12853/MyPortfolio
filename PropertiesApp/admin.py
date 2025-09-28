from django.contrib import admin
from .models.tenant_model import Tenant
from .models.dwelling_model import Dwelling
from .models.lease_model import Lease

admin.site.register(Tenant)
admin.site.register(Dwelling)
admin.site.register(Lease)