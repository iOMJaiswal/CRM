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
    

# ! General  
class Immigration(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=100)
    document_number = models.CharField(max_length=200)
    issue_date = models.DateField()
    expired_date = models.DateField()
    eligible_review_date = models.DateField()
    document_file = models.FileField(upload_to="media/employee_immigration_document", null=True)
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return (f"{self.document_type}  ,  {self.document_number}")    
    
class Contact(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    relation = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return (f"{self.relation}  ,  {self.name}")
    
class Qualification(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    university = models.CharField(max_length=100)
    education_level = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    language = models.CharField(max_length=100)
    professional_skills = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return (f"{self.university}  ,  {self.education_level}")
    
class WorkExperience(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    post = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return (f"{self.company}  ,  {self.post}")

class BankAccount(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    account_title = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    bank_code = models.CharField(max_length=100)
    bank_branch = models.CharField(max_length=100)

    def __str__(self):
        return (f"{self.account_title}  ,  {self.account_number}")
    


# ! Set Salary

class BasicSalary(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month_year = models.DateField()
    payslip_type = models.CharField(max_length=100)
    basic_salary = models.CharField(max_length=100)
    
    def __str__(self):
        return (f"{self.payslip_type}")
    
class Allowances(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month_year = models.DateField()
    allowance_type = models.CharField(max_length=100)
    allowance_title = models.CharField(max_length=100)
    allowance_amount = models.CharField(max_length=100)
    
    def __str__(self):
        return (f"{self.allowance_title}")

class Commissions(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month_year = models.DateField()
    commission_title = models.CharField(max_length=100)
    commission_amount = models.CharField(max_length=100)
    
    def __str__(self):
        return (f"{self.commission_title}")

class Loans(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month_year = models.DateField()
    loan_option = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    number_of_installment = models.CharField(max_length=100)
    reason = models.TextField()
    
    def __str__(self):
        return (f"{self.loan_option}  ,  {self.title}")
    
    
class StatutoryDeductions(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month_year = models.DateField()
    deduction_option = models.CharField(max_length=100)
    deduction_title = models.CharField(max_length=100)
    deduction_amount = models.CharField(max_length=100)
    
    def __str__(self):
        return (f"{self.deduction_option}  ,  {self.deduction_title}")
    
    
class OtherPayments(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month_year = models.DateField()
    title = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    
    def __str__(self):
        return (f"{self.title}")
    
class Overtime(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month_year = models.DateField()
    title = models.CharField(max_length=100)
    number_of_days = models.CharField(max_length=100)
    total_hours = models.CharField(max_length=100)
    rate = models.CharField(max_length=100)
    
    def __str__(self):
        return (f"{self.title}")

class SalaryPension(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pension_type = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    
    def __str__(self):
        return (f"{self.pension_type}")
        
    

    

