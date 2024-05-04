from rest_framework import serializers
from Employees.models import *

class EmployeeSerializer(serializers.ModelSerializer):
    company_details = serializers.SerializerMethodField()
    
    class Meta:
        model = Employee
        fields = '__all__'
        
    def get_company_details(self, obj):
        return {'company_name' : obj.company.company_name}
    
    
class ImmigrationSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Immigration
        fields = '__all__'
        
    
class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = '__all__'
        

class QualificationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Qualification
        fields = '__all__'
        
        
class WorkExperienceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WorkExperience
        fields = '__all__'
        
class BankAccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BankAccount
        fields = '__all__'
        
class BasicSalarySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BasicSalary
        fields = '__all__'
        
class AllowancesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Allowances
        fields = '__all__'
        
class CommissionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Commissions
        fields = '__all__'
        
class LoansSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Loans
        fields = '__all__'

class StatutoryDeductionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StatutoryDeductions
        fields = '__all__'
        
class OtherPaymentsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OtherPayments
        fields = '__all__'

class OvertimeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Overtime
        fields = '__all__'

class SalaryPensionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SalaryPension
        fields = '__all__'
        


        