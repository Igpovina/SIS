from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Q

from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, UpdateView, DeleteView

from django.contrib.auth import login, get_user_model, authenticate

from .models import User, Course, Classes
from .forms import RegisterForm


# Create your views here.
def login_user(request):
    if request.method == 'POST':
        my_form = AuthenticationForm(request, data=request.POST)
        if my_form.is_valid():
            data = my_form.cleaned_data
            user = data['username']
            pwd = data['password']
            
            user_auth = authenticate(username = user, password = pwd)
            
            if user_auth:
                login(request, user_auth)
                response = f'Welcome Dr. {user}'
                return redirect('login')
            else:
                response = 'User name or password are invalid'
                return render(request, 'index.html', {'response':response, 'my_form':my_form})
            
        response = 'User name or password are invalid'
        return render(request, 'index.html', {'response':response, 'my_form':my_form})
    else:
        my_form = AuthenticationForm()
        return render(request, 'index.html', {'my_form':my_form})


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()  # save the user
        return super().form_valid(form)

class StudentView(ListView):
    model = User
    template_name = 'index.html'
    context_object_name = 'users'
    
class CourseView(ListView):
    model = Course
    template_name = 'courses.html'
    context_object_name = 'courses'

class ClassesView(ListView):
    model = Classes
    template_name = 'classes.html'
    context_object_name = 'classes'