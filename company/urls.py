from django.urls import path

from company.views import index

app_name = "company"

urlpatterns = [
    path('', index, name='index'),

]