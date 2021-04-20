from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def brian(request):
    return HttpResponse("<h1 style=\"color:blue\">Hello, brian!</h1>")

def david(request):
    return HttpResponse("Hello, David")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })