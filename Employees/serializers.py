from rest_framework import serializers
from Employees.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    company_details = serializers.SerializerMethodField()
    
    class Meta:
        model = Employee
        fields = '__all__'
        
    def get_company_details(self, obj):
        return {'company_name' : obj.company.company_name}