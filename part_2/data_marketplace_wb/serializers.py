from rest_framework import serializers
from .models import data_wb_card


class data_wb_serializer(serializers.ModelSerializer):
    class Meta:
        model = data_wb_card
        fields = ("article", "brand", "name")
