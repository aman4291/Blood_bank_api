from rest_framework import serializers
from bloodbank.models import DonorInfo, Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Stock


class DonorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = DonorInfo
