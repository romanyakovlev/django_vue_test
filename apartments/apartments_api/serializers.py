from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import ApartmentModel
from rest_framework.views import APIView
from rest_framework.response import Response


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentModel
        fields = [
        	'apartment_price', 'number_of_rooms', 'apartment_floor', 
        	'year_of_construction', 'apartment_adress', 'id', 'building_floors'
        ]


