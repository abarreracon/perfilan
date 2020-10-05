from desarrollos.models import Leads, Desarrollo
from rest_framework import viewsets
from .serializers import LeadSerializer, DesarrolloSerializer

#Lead Viewset
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Leads.objects.all()
    serializer_class = LeadSerializer

#Desarrollo viewset
class DesarrolloViewSet(viewsets.ModelViewSet):
    queryset = Desarrollo.objects.all()
    serializer_class = DesarrolloSerializer