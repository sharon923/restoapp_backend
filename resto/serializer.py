from rest_framework import serializers
from resto.models import RestoModel

class RestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestoModel
        fields = (
            'name',
            'image',
            'description',
            'price',
            'rating',
            'available'
        )