from django.db import models
from uuid import uuid4
import datetime

class Company(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    company_name = models.CharField(max_length=100)
    company_type = models.CharField(max_length=100)
    treading_name = models.CharField(max_length=100)
    gst_number = models.CharField(max_length=100)
    pancard_number = models.CharField(max_length=100)
    
    # Address
    line_1 = models.CharField(max_length=100)
    line_2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    
    
    admin_name = models.CharField(max_length=100)
    admin_designation = models.CharField(max_length=100)
    admin_phone_number = models.CharField(max_length=100)
    admin_email = models.CharField(max_length=100)
    website = models.TextField(default=None, null=True)
    tan_number = models.CharField(max_length=100)
    company_logo = models.FileField(upload_to="media/company_logo", null=True)
    currency = models.CharField(max_length=100)
    signature_of_admin = models.FileField(upload_to="media/signature", null=True)
    created_on = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.company_name