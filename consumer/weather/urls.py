from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('edit/', views.Edit.as_view(), name='edit'),
]