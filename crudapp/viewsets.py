from rest_framework import viewsets
from .  models import student
from . import serializers

class StudViewset(viewsets.ModelViewSet):
    queryset =student.object.all()
    serializer_class = serializers.StudSerializer
