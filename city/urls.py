from django.urls import path

from city.views import index

app_name = "city"

urlpatterns = [
    path('', index, name='index'),

]