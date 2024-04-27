from django.db import models
from uuid import uuid4
import datetime
from Company.models import Company
from Employees.models import Employee

class Promotion(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    promotion_date = models.DateField(default=datetime.date.today)
    description = models.TextField(default=None)

    def __str__(self):
        return self.title
