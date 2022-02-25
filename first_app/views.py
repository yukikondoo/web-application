from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dic = {'insert_me' : 'Hello I am from views.py'}
    return render(request, 'first_app/index.html', context=my_dic)

