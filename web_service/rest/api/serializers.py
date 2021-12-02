from rest_framework import serializers
from rest.models import Data


class DataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Data
        fields = '__all__'
        