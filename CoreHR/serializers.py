from rest_framework import serializers
from CoreHR.models import *


class PromotionSerializer(serializers.ModelSerializer):
    company_details = serializers.SerializerMethodField()
    employee_details = serializers.SerializerMethodField()
    
    def get_company_details(self, obj):
        return {'company_name' : obj.company.company_name}
    
    def get_employee_details(self, obj):
        return {'employee_name' : f"{obj.employee.first_name} {obj.employee.last_name}"}
    
    class Meta:
        model = Promotion
        fields = '__all__'
    
    
class AwardSerializer(serializers.ModelSerializer):
    
    company_details = serializers.SerializerMethodField()
    employee_details = serializers.SerializerMethodField()
    
    def get_company_details(self, obj):
        return {'company_name' : obj.company.company_name}
    
    def get_employee_details(self, obj):
        return {'employee_name' : f"{obj.employee.first_name} {obj.employee.last_name}"}
    
    class Meta:
        model = Award
        fields = '__all__'
        
        
class TravelSerializer(serializers.ModelSerializer):
    
    company_details = serializers.SerializerMethodField()
    employee_details = serializers.SerializerMethodField()
    
    def get_company_details(self, obj):
        return {'company_name' : obj.company.company_name}
    
    def get_employee_details(self, obj):
        return {'employee_name' : f"{obj.employee.first_name} {obj.employee.last_name}"}
    
    class Meta:
        model = Travel
        fields = '__all__'
    
    
class TransferSerializer(serializers.ModelSerializer):
    
    company_details = serializers.SerializerMethodField()
    employee_details = serializers.SerializerMethodField()
    
    def get_company_details(self, obj):
        return {'company_name' : obj.company.company_name}
    
    def get_employee_details(self, obj):
        return {'employee_name' : f"{obj.employee.first_name} {obj.employee.last_name}"}
    class Meta:
        model = Transfer
        fields = '__all__'
        
        
class ResignationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Resignation
        fields = '__all__'
        

class ComplaintSerializer(serializers.ModelSerializer):
    
    company_details = serializers.SerializerMethodField()
    employee_details = serializers.SerializerMethodField()
    
    def get_company_details(self, obj):
        return {'company_name' : obj.company.company_name}
    
    def get_employee_details(self, obj):
        return {'employee_name' : f"{obj.employee.first_name} {obj.employee.last_name}"}
    
    class Meta:
        model = Complaint
        fields = '__all__'  
        
    
class WarningSerializer(serializers.ModelSerializer):
    
    company_details = serializers.SerializerMethodField()
    employee_details = serializers.SerializerMethodField()
    
    def get_company_details(self, obj):
        return {'company_name' : obj.company.company_name}
    
    def get_employee_details(self, obj):
        return {'employee_name' : f"{obj.employee.first_name} {obj.employee.last_name}"}
    class Meta:
        model = Warning
        fields = '__all__'
        

class TerminationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Termination
        fields = '__all__'
        
        