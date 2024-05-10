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
    

class Award(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    award_type = models.CharField(max_length=100)
    gift = models.CharField(max_length=100)
    cash = models.CharField(max_length=100)
    award_information = models.TextField()
    award_date = models.DateField(default=datetime.date.today)
    award_photo = models.FileField(upload_to="media/award_photo", null=True)


class Travel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    arrangement_type = models.CharField(max_length=100)
    purpose_of_visit = models.CharField(max_length=100)
    plcae_of_visit = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    expected_budget = models.CharField(max_length=100)
    actual_budget = models.CharField(max_length=100)
    travel_mode = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    
    
class Transfer(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    from_department = models.CharField(max_length=100)
    to_department = models.CharField(max_length=100)
    transfer_date = models.DateField(default=datetime.date.today)
    description = models.TextField(default=None)
    
    
class Resignation(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    notice_date = models.DateField(default=datetime.date.today)
    resignation_date = models.DateField(default=datetime.date.today)
    description = models.TextField(default=None)
    
    
class Complaint(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    complaint_from = models.CharField(max_length=100)
    complaint_against = models.CharField(max_length=100)
    complaint_title = models.CharField(max_length=100)
    description = models.TextField()
    complaint_date = models.DateField(default=datetime.date.today)
    
    
class Warning(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    warning_to = models.CharField(max_length=100)
    warning_type = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    warning_date = models.DateField(default=datetime.date.today)
    status = models.CharField(max_length=100)
    

class Termination(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    termination_to = models.CharField(max_length=100)
    termination_type = models.CharField(max_length=100)
    description = models.TextField()
    termination_date = models.DateField(default=datetime.date.today)
    notice_date = models.DateField(default=datetime.date.today)
    
    
    
    
    

    
    
    
