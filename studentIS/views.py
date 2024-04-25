from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Q

from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, UpdateView, DeleteView

from .models import Student, Course, Classes

# Create your views here.
class StudentView(ListView):
    model = Student
    template_name = 'index.html'
    context_object_name = 'students'
    
class CourseView(ListView):
    model = Course
    template_name = 'courses.html'
    context_object_name = 'courses'

class ClassesView(ListView):
    model = Classes
    template_name = 'classes.html'
    context_object_name = 'classes'