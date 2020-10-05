from desarrollos.models import Leads
from rest_framework import viewsets
from .serializers import LeadSerializer

#Lead Viewset
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Leads.objects.all()
    serializer_class = LeadSerializer