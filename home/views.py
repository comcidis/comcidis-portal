from django.shortcuts import render

def index(request):
    """Portal overview

    :req: request
    :returns: render page

    """
    return render(request, 'index.html')
