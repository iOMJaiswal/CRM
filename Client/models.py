from django.db import models
from uuid import uuid4
import datetime
from Company.models import Company

class Client(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    client_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    fax = models.CharField(max_length=100, default=None)
    website = models.TextField(default=None)
    industry = models.ForeignKey(Company, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    about = models.TextField(default=None)

    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    attached_contract = models.FileField(
        upload_to="media/client_contract", null=True)
    attached_other = models.FileField(
        upload_to="media/client_other", null=True)

    def __str__(self):
        return self.client_name