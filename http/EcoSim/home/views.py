from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    msg = "Welcome To Page"
    return render(request, 'home/index.html', {'message': msg})

# Create your views here.
