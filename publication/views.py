from django.shortcuts import render
from .models import Publication


def index(request):
    publications = Publication.objects.all()
    context = {'publications': publications}
    return render(request, 'publication/index.html', context)
