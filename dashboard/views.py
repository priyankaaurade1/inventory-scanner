from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def user_profile(request):
    return render(request, 'users-profile.html')