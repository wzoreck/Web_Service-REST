from django.shortcuts import render
from django.views import View
import requests

class Index(View):
    template_name = 'weather/index.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)
        
        data_request = requests.get(url='http://127.0.0.1:8080/data/') # URL GET API
        print(data_request.json())

        self.context = {
            'data': data_request.json(),
        }

        self.renderizar = render(self.request, self.template_name, self.context)

    def get(self, *args, **kwargs):
        return self.renderizar
