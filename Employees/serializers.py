from rest_framework import serializers
from Employees.models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
    

# ! General      
class ImmigrationSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Immigration
        fields = '__all__'
        
    
class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = '__all__'
        
class SocialProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SocialProfile
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
     
     


# ! Set Salary    
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
        


        