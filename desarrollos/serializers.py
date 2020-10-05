from rest_framework import serializers
from desarrollos.models import Desarrollo, Leads

#Lead Serializer
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = '__all__'

#Desarrollo Serializer
class DesarrolloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desarrollo
        fields = '__all__'