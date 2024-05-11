from django.urls import path

from prefecture.views import index

app_name = "prefecture"

urlpatterns = [
    path('', index, name='index'),

]