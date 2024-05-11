from django.shortcuts import render


def index(request):
    return render(request, 'user/welcome.html')


def user_account(request):
    return render(request, 'user/lk.html')
