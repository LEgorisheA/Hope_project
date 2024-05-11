from django.urls import path

from user.views import user_account

app_name = "user"

urlpatterns = [
    path('', user_account, name='index'),
]