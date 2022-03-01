from cmath import log
from os import access
import profile
from django.shortcuts import render, redirect
from first_app.models import Topic, Webpage, AccesRecord
from . import forms
from django.forms import ModelForm
from first_app.forms import UserForm, UserProfileInfoForm

#login
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    webpage_list = AccesRecord.objects.order_by('date')
    date_dict = {'access_records' : webpage_list}   
    return render(request, 'first_app/index.html', context=date_dict)

#log in
@login_required
def special(request):
    return render(request, 'first_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'first_app/index.html')


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

    
def signup_name_view(request):
    form = forms.NewUserForm()

    if request.method =='POST':
        form = forms.NewUserForm(request.POST)

        if form.is_valid():
            # DO SOMETHHING CODE
            form.save(commit=True)
            return index(request)
        else:
            print('Error')

    return render(request, 'first_app/signup_page.html', {'form' : form})

def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'first_app/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return render(request, 'first_app/index.html', {})
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        
        else:
            print("Someone tried to login and failed")
            print("Username : {} and password {}".format(username, password))
            return HttpResponse("invalid login details suppliec")
    
    else:
        return render(request, 'first_app/login.html', {})