from django.db import models
from tenants.models import TenantAwareModel

class Contact(TenantAwareModel):
    CONTACT_TYPE_CHOICES = [
        ('lead', 'Lead'),
        ('customer', 'Customer'),
        ('partner', 'Partner'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=200, blank=True)
    contact_type = models.CharField(max_length=20, choices=CONTACT_TYPE_CHOICES, default='lead')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
