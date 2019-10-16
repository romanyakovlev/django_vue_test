
from django.db import models

class ApartmentModel(models.Model):

    apartment_price = models.PositiveIntegerField(default=0)
    number_of_rooms = models.PositiveIntegerField(default=1)
    apartment_floor = models.PositiveIntegerField(default=1)
    year_of_construction = models.PositiveIntegerField(default=2019)
    apartment_adress = models.CharField(max_length=200, blank=False)

