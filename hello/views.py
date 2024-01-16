from django.http import HttpResponse 
from django.shortcuts import render

def index(request):
    return render(request, "hello/index.html")

def brian(request): 
    return HttpResponse("Hello Brian!")

def greeting(request, name): 
    return render(request, "hello/greeting.html", {
        "name": name.capitalize()
    })