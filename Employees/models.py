from django.db import models
from uuid import uuid4
import datetime
from Company.models import Company

class Employee(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    staff_id = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    office_shift = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    attendance_type = models.CharField(max_length=100)
    date = models.DateField(default=datetime.date.today)
    image = models.FileField(upload_to="media/employee_image", null=True)

    def __str__(self):
        return (f"{self.first_name},    {self.last_name},   {self.staff_id}")
