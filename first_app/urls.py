from django.urls import path

from . import views
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formpage/', views.form_name_view, name='form_name'),
]