#import path
from django.urls import re_path

#import views
from . import views

urlpatterns = [
    re_path(r'/?$', views.alumno_detail),
    re_path(r'<int:pk>/?$', views.alumno_detail),
]