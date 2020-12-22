from django.shortcuts import render
from django.http.request import HttpRequest
# Create your views here.


def homepage(request):
    return render(request, 'accounts/main.html')