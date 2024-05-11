from django.urls import path

from city_hall.views import index

app_name = "city_hall"

urlpatterns = [
    path('', index, name='index'),

]