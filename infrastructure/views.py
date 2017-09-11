from django.shortcuts import render
from .models import Infrastructure

def index(request):
    infrastructure = Infrastructure.objects.all()
    context = {'infrastructure': infrastructure}
    return render(request, 'infrastructure/index.html', context)