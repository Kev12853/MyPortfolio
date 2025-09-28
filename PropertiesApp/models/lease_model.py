from django.db import models

from PropertiesApp.models.dwelling_model import Dwelling
from PropertiesApp.models.tenant_model import Tenant

class Lease(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    dwelling = models.ForeignKey(Dwelling, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Lease for {self.tenant} at {self.dwelling}"