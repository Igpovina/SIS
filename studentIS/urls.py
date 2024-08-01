from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('register', views.student_register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('courses', views.CourseView.as_view(), name='courses'),
]