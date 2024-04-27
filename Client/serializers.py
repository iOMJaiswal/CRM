from rest_framework import serializers
from Client.models import Client

class ClientSerializer(serializers.ModelSerializer):
    
    company_details = serializers.SerializerMethodField()
    
    class Meta:
        model = Client
        fields = '__all__'
        
        
    def get_company_details(self, obj):
        return {'company_name' : obj.industry.company_name}