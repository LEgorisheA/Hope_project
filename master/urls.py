from django.urls import path

from master.views import index

app_name = "master"

urlpatterns = [
    path('', index, name='index'),

]