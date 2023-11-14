#import path
from django.urls import path,re_path

#import views
from . import views

urlpatterns = [
    re_path(r'/?$', views.profesor_detail, name="profesor_detail"),
    re_path(r'<int:pk>/?$', views.profesor_detail, name="profesor_detail_id"),
]