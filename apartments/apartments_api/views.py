from .models import ApartmentModel
from rest_framework import viewsets, generics, pagination
from .serializers import ApartmentSerializer
from django.db.models import F, Max, Min
from rest_framework.response import Response
from rest_framework.views import APIView


class CustomNumberPagination(pagination.PageNumberPagination):

    def get_paginated_response(self, data):

        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': 
                self.page.paginator.count // self.page_size + 1
                if self.page.paginator.count % self.page_size != 0 
                else self.page.paginator.count // self.page_size,
            'results': data,
        })

class ApartmentViewSet(viewsets.ModelViewSet):

    serializer_class = ApartmentSerializer
    pagination_class = CustomNumberPagination

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

        if not_first_and_last_floor:
            if 'true' in not_first_and_last_floor:
            	queryset = queryset.exclude(apartment_floor=1)
            	queryset = queryset.exclude(apartment_floor=F('building_floors'))

        if apartments_year:
            queryset = queryset.filter(year_of_construction__in=apartments_year)
        if number_of_rooms:
        	queryset = queryset.filter(number_of_rooms__in=number_of_rooms)
     	
        return queryset


class InitDataView(APIView):

    def get(self, request, format=None):

        max_price = ApartmentModel.objects.aggregate(Max('apartment_price'))
        min_price = ApartmentModel.objects.aggregate(Min('apartment_price'))

        number_of_rooms = ApartmentModel.objects.values_list('number_of_rooms', flat=True)
        years_of_construction = ApartmentModel.objects.values_list('year_of_construction', flat=True)

        max_floor = ApartmentModel.objects.aggregate(Max('apartment_floor'))
        min_floor = ApartmentModel.objects.aggregate(Min('apartment_floor'))

        return Response({
            **max_price,
            **min_price,
            'number_of_rooms': set(number_of_rooms),
            'years_of_construction': set(years_of_construction),
            **max_floor,
            **min_floor,
        })
