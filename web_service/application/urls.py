from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest.api import viewsets as dataviewsets


route = routers.DefaultRouter()
route.register(r'data', dataviewsets.DataViewSet, basename="Data")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
