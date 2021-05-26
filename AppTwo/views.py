from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import AccessRecord,Topic,Webpage

# Create your views here.

def index(request):
    #return HttpResponse("<em>My Second App</em>")
    all_pages = Webpage.objects.all()
    web_title = "Site Name"
    all_accesses = AccessRecord.objects.all()
    acc_title = "Date Accessed"
    all_topics = Topic.objects.all()
    top_title = "Topics"
    #print(all_entries)
    return render(request, "AppTwo/index.html", {"web_title" : web_title, "all_pages": all_pages, 
                                                 "acc_title": acc_title, "all_accesses": all_accesses, 
                                                 "top_title": top_title, "all_topics": all_topics })
    #my_dict = {"insert_me" : "Hello, I am from views.py - I am the index page!",
    # "title" : "Index Page"}
   # return render(request, 'AppTwo/index.html', context=my_dict)


def help(request):
    my_dict = {"help_me" : "Hello, I am also from views.py - but I am the help page!",
               "title": "Help Page"}
    return render(request, 'AppTwo/index.html', context=my_dict)

