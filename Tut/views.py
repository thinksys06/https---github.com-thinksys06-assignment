# this is Tutorial website .

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'Index.html')

def contact(request):
    return render(request, 'Contact_us.html')

def about(request):
    return render(request, 'About.html')

def classes(request):
    return render(request, 'Index.html')