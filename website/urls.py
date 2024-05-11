"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from user.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('user/', include('user.urls', namespace='user')),
    path('company/', include('company.urls', namespace='company')),
    path('prefecture/', include('prefecture.urls', namespace='prefecture')),
    path('master/', include('master.urls', namespace='master')),
    path('city/', include('city.urls', namespace='city')),
    path('city_hall/', include('city_hall', namespace='city_hall')),

]
