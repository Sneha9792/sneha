from .viewsets import StudViewset
from rest_framework import routers

router = routers.DefaultRouter()
routers.register('Student', StudViewset)
