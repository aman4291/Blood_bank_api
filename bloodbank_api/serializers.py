from rest_framework.serializers import SerializerMethodField, ModelSerializer, ValidationError
from bloodbank.models import DonorInfo, Stock


from datetime import date


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


class StockCreateSerializer(ModelSerializer):

    def validate(self, attrs):

        if attrs["blood_group"] != attrs["donated_by"].blood_group:
            raise ValidationError(
                "Stock blood group does not match Donor blood group")

        return super().validate(attrs)

    class Meta:
        fields = '__all__'
        model = Stock


class StockSerializer(ModelSerializer):

    donated_by = SerializerMethodField()
    donor_age = SerializerMethodField()

    def get_donated_by(self, obj):
        return obj.donated_by.name

    def get_donor_age(self, obj):
        return calculate_age(obj.donated_by.dob)

    class Meta:
        fields = '__all__'
        model = Stock


class DonorInfoSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = DonorInfo
