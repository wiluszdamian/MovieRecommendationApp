from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def user(request):
    return render(request, 'user.html')

def browse(request):
    return render(request, 'browse.html')