from rest_framework import routers
from .api import LeadViewSet, DesarrolloViewSet

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'Leads')
router.register('api/desarrollo', DesarrolloViewSet, 'Desarrollo')

urlpatterns = router.urls