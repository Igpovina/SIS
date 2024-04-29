from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('courses', views.CourseView.as_view(), name='courses'),
]