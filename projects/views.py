from django.shortcuts import render

from .models import Job


def home(request):
    jobs = Job.objects
    return render(request, 'portfolio/home.html', {'jobs': jobs})


def contacts(request):
    return render(request, 'portfolio/contacts.html')

