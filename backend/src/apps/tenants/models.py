from django_tenants.models import TenantMixin, DomainMixin
from django.db import models

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    plan = models.CharField(max_length=20, default='trial')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    auto_create_schema = True

    def __str__(self):
        return self.name

class Domain(DomainMixin):
    pass

class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Client, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True
