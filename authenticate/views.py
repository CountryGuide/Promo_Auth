import os

from django.shortcuts import render


def home(request):
    return render(request, os.path.join('authenticate', 'home.html'), {})
