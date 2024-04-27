from rest_framework import serializers
from Promotion.models import Promotion


class PromotionSerializer(serializers.ModelSerializer):
    company_details = serializers.SerializerMethodField()
    employee_details = serializers.SerializerMethodField()
    
    class Meta:
        model = Promotion
        fields = '__all__'
    
    # def create(self, validated_data):
        
    
    
    def get_company_details(self, obj):
        return {'company_name' : obj.company.company_name}
    
    def get_employee_details(self, obj):
        return {'employee_name' : f"{obj.employee.first_name} {obj.employee.last_name}"}