from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me':"hello i am from views.py !"}
    return render(request,'app2/index.html',context=my_dict)
