from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,'polls/layout.html')

def create(request):
    return render(request, 'polls/create.html')

def first(request):
    return render(request, 'polls/first.html')