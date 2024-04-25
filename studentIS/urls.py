from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.StudentView.as_view(), name='students'),
    path('courses', views.CourseView.as_view(), name='courses'),
]