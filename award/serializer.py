from rest_framework import serializers
from .models import Rating

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('user', 'post', 'review')