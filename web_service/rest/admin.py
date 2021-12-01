from .models import *
from django.contrib import admin


class DataAdmin(admin.ModelAdmin):
    list_display = ('id', 'temperature', 'humidity', 'luminosity', 'date', 'time')
    list_display_links = ('id',)


admin.site.register(Data, DataAdmin)