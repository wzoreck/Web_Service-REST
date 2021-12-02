from rest_framework import viewsets
from rest.api import serializers
from rest.models import Data

class DataViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DataSerializer
    queryset = Data.objects.all()
    