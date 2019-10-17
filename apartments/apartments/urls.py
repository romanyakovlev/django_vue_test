from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apartments_api import views

router = routers.DefaultRouter()
router.register(r'apartments', views.ApartmentViewSet)


urlpatterns = [
	path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
