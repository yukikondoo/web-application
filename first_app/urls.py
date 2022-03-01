from django.urls import path

from . import views
from first_app import views

# TEMPLATE TAGGING
app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('formpage/', views.form_name_view, name='form_name'),
    path('adminsignup/', views.signup_name_view, name='signup_name'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='user_logout'),
    path('login/', views.user_login, name='user_login'),
    path('special/', views.special, name='special'),
    

]