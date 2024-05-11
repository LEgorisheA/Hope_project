from django.shortcuts import render


def index(request):
    return render(request, 'city_hall/lk.html')
