from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def new(request):
    return render(request, 'main/new.html')

def data(request):
    return HttpResponse("<h1>Это третья страница моего проекта на Django</h1>"
                        "<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnjd6vnBoSHCYGHXqOLqKH_jC8malDYgRiLhAqHqfzbw&s=10' alt='logo'>")

def test(request):
    return HttpResponse("<h1>Это тестовая страница моего проекта на Django</h1>")

# Create your views here.
