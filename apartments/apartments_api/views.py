from .models import ApartmentModel
from rest_framework import viewsets, generics
from .serializers import ApartmentSerializer
from django.db.models import F


class ApartmentViewSet(viewsets.ModelViewSet):

    serializer_class = ApartmentSerializer

    def get_queryset(self):

        queryset = ApartmentModel.objects.all()

        low_price = self.request.query_params.get('low_price', None)
        high_price = self.request.query_params.get('high_price', None)

        apartments_year = self.request.query_params.getlist('years', None)
        number_of_rooms = self.request.query_params.getlist('rooms', None)

        low_floor = self.request.query_params.get('low_floor', None)
        high_floor = self.request.query_params.get('high_floor', None)
        not_first_and_last_floor = self.request.query_params.get('toggle', None)
       
        if low_price and high_price:
            queryset = queryset.filter(apartment_price__range=(low_price, high_price))
        if low_floor and high_floor:
            queryset = queryset.filter(apartment_floor__range=(low_floor, high_floor))

        if 'true' in not_first_and_last_floor:
        	queryset = queryset.exclude(apartment_floor=1)
        	queryset = queryset.exclude(apartment_floor=F('building_floors'))

        if apartments_year:
            queryset = queryset.filter(year_of_construction__in=apartments_year)
        if number_of_rooms:
        	queryset = queryset.filter(number_of_rooms__in=number_of_rooms)
     	
        return queryset


