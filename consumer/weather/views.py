from django.shortcuts import render, redirect
from django.views import View
import requests
import json

class Index(View):
    template_name = 'weather/index.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)
        
        #GET ALL API
        data_request = requests.get(url='http://127.0.0.1:8080/data/') # URL GET API

        self.context = {
            'data': data_request.json(),
        }

        self.renderizar = render(self.request, self.template_name, self.context)

    def get(self, *args, **kwargs):
        return self.renderizar


class Edit(View):
    template_name = 'weather/edit.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)
        
        self.pk = self.kwargs.get('pk')
        
        # GET API
        data = requests.get(url=f'http://127.0.0.1:8080/data/{self.pk}/')
        
        self.context = {
            'data': data.json(),
        }

        self.renderizar = render(self.request, self.template_name, self.context)

    def get(self, *args, **kwargs):
        return self.renderizar

    def post(self, *args, **kwargs):
        temperature = self.request.POST.get('temperature').replace(',', '.')
        humidity = self.request.POST.get('humidity').replace(',', '.')
        luminosity = self.request.POST.get('luminosity').replace(',', '.')
        date = self.request.POST.get('date')
        time = self.request.POST.get('time')
        
        load = {
            'temperature': float(temperature),
            'humidity': float(humidity),
            'luminosity': float(luminosity),
            'date': str(date),
            'time': str(time),
        }
        
        # PUT API
        r = requests.put(url=f'http://127.0.0.1:8080/data/{self.pk}/', json=load)
        
        return redirect('weather:index')

class Delete(View):
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)
        
        pk = self.kwargs.get('pk')
        
        # GET API
        requests.delete(url=f'http://127.0.0.1:8080/data/{pk}/')

    def get(self, *args, **kwargs):
        return redirect('weather:index')