from django.shortcuts import render
from .models import Infrastructure

def index(request):
    infrastructure = Infrastructure.objects.all()
    context = {'mobile_title_page': 'Infraestrutura',
               'infrastructure': infrastructure}
    return render(request, 'infrastructure/index.html', context)