from django.shortcuts import render, redirect
from django.views import View
from django.urls import redirect

def home_view(request):
    return redirect(reverse('main:home'))
