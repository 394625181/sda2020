from django.urls import path

from . import views

app_name = 'Finance'
urlpatterns = [
    path('', views.index, name='index'),

]