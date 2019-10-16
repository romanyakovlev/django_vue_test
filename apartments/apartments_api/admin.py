from django.contrib import admin
from .models import ApartmentModel

class ApartmentAdmin(admin.ModelAdmin):
	pass

admin.site.register(ApartmentModel, ApartmentAdmin)
