from django.http import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("<em>My Second App</em>")
    my_dict = {"insert_me" : "Hello, I am from views.py - I am the index page!",
               "title" : "Index Page"}
    return render(request, 'AppTwo/index.html', context=my_dict)


def help(request):
    my_dict = {"help_me" : "Hello, I am also from views.py - but I am the help page!",
               "title": "Help Page"}
    return render(request, 'AppTwo/index.html', context=my_dict)


