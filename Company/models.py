from django.db import models
from uuid import uuid4
import datetime

class Company(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    company_name = models.CharField(max_length=100)
    company_type = models.CharField(max_length=100)
    treading_name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    website = models.TextField(default=None)
    location = models.CharField(max_length=100)
    tax_number = models.CharField(max_length=100)
    company_logo = models.FileField(upload_to="media/company_logo", null=True)
    created_on = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.company_name