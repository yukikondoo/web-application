from os import access
from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccesRecord
from . import forms

# Create your views here.

def index(request):
    webpage_list = AccesRecord.objects.order_by('date')
    date_dict = {'access_records' : webpage_list}   
    return render(request, 'first_app/index.html', context=date_dict)

def form_name_view(request):
    form = forms.FormName()

    if request.method =='POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # DO SOMETHHING CODE
            print("VALIDATION SUCCESS!")
            print("NAME : " + form.cleaned_data['name'])
            print("EMAIL : " + form.cleaned_data['email'])
            print("TEXT : " + form.cleaned_data['text'])


    return render(request, 'first_app/form_page.html', {'form' : form})

    
