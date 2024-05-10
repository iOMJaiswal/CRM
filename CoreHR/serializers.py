from rest_framework import serializers
from CoreHR.models import *


class PromotionSerializer(serializers.ModelSerializer):
    company_details = serializers.SerializerMethodField()
    employee_details = serializers.SerializerMethodField()
    
    class Meta:
        model = Promotion
        fields = '__all__'
    
    def get_company_details(self, obj):
        return {'company_name' : obj.company.company_name}
    
    def get_employee_details(self, obj):
        return {'employee_name' : f"{obj.employee.first_name} {obj.employee.last_name}"}
    
    
class AwardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Award
        fields = '__all__'
        
        
class TravelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Travel
        fields = '__all__'
    
    
class TransferSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transfer
        fields = '__all__'
        
        
class ResignationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Resignation
        fields = '__all__'
        

class ComplaintSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Complaint
        fields = '__all__'  
        
    
class WarningSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Warning
        fields = '__all__'
        

class TerminationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Termination
        fields = '__all__'
        
        