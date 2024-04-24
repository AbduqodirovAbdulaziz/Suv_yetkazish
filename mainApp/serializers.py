from rest_framework import serializers
from .models import *


class SuvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suv
        fields = '__all__'

        def validate_litr(self, litr):
            if litr > 19:
                raise serializers.ValidationError("Bunday katta litrlarda suv sotilmaydi")
            return litr


class MijozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adminlik
        fields = '__all__'

        def validate_yosh(self, yosh):
            if yosh < 19:
                raise serializers.ValidationError("Yoshingiz mos kelmaydi")
            return yosh


class HaydovchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Haydovchi
        fields = '__all__'


class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = '__all__'
