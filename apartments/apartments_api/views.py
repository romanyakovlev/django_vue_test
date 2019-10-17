from .models import ApartmentModel
from rest_framework import viewsets
from .serializers import ApartmentSerializer


class ApartmentViewSet(viewsets.ModelViewSet):

    queryset = ApartmentModel.objects.all()
    serializer_class = ApartmentSerializer