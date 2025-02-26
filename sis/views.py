from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.shortcuts import redirect

def home(request):
    """
    Redirects to home page
    """
    return redirect('home/')
